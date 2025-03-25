"""
Knowledge Manager for CrewAI
This module provides knowledge management capabilities for AI agents,
including versioning, categorization, and efficient retrieval.
"""

import os
import json
import yaml
from typing import Dict, List, Any, Optional
from datetime import datetime
from pathlib import Path
import hashlib
from dataclasses import dataclass, asdict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class KnowledgeEntry:
    """Represents a single knowledge entry with metadata."""
    id: str
    content: str
    category: str
    tags: List[str]
    source: str
    created_at: str
    updated_at: str
    version: int
    confidence: float
    references: List[str]
    metadata: Dict[str, Any]

class KnowledgeManager:
    """
    Manages the storage, retrieval, and versioning of knowledge entries.
    Provides categorization and efficient search capabilities.
    """

    def __init__(self, base_path: str = "./knowledge"):
        """Initialize the knowledge manager."""
        self.base_path = Path(base_path)
        self._ensure_directory_structure()
        self.categories = self._load_categories()

    def _ensure_directory_structure(self):
        """Create necessary directory structure."""
        # Create main directories
        (self.base_path / "entries").mkdir(parents=True, exist_ok=True)
        (self.base_path / "categories").mkdir(exist_ok=True)
        (self.base_path / "indexes").mkdir(exist_ok=True)
        (self.base_path / "archive").mkdir(exist_ok=True)

        # Create category config if not exists
        categories_file = self.base_path / "categories.yaml"
        if not categories_file.exists():
            default_categories = {
                "general": {
                    "description": "General knowledge entries",
                    "tags": ["general", "misc"]
                },
                "domain": {
                    "description": "Domain-specific knowledge",
                    "tags": ["domain", "specialized"]
                },
                "process": {
                    "description": "Process-related knowledge",
                    "tags": ["process", "workflow"]
                },
                "technical": {
                    "description": "Technical documentation and references",
                    "tags": ["technical", "documentation"]
                }
            }
            with open(categories_file, 'w') as f:
                yaml.dump(default_categories, f)

    def _load_categories(self) -> Dict[str, Dict[str, Any]]:
        """Load category definitions."""
        categories_file = self.base_path / "categories.yaml"
        with open(categories_file, 'r') as f:
            return yaml.safe_load(f)

    def _generate_id(self, content: str, category: str) -> str:
        """Generate a unique ID for a knowledge entry."""
        timestamp = datetime.now().isoformat()
        content_hash = hashlib.md5(f"{content}{category}{timestamp}".encode()).hexdigest()
        return f"k-{content_hash[:8]}"

    def add_entry(self, content: str, category: str, tags: List[str],
                  source: str, confidence: float = 1.0,
                  references: List[str] = None,
                  metadata: Dict[str, Any] = None) -> str:
        """
        Add a new knowledge entry.

        Args:
            content: The knowledge content
            category: Category for classification
            tags: List of relevant tags
            source: Source of the knowledge
            confidence: Confidence score (0.0 to 1.0)
            references: List of related entry IDs
            metadata: Additional metadata

        Returns:
            The ID of the created entry
        """
        if category not in self.categories:
            raise ValueError(f"Invalid category: {category}")

        entry_id = self._generate_id(content, category)
        timestamp = datetime.now().isoformat()

        entry = KnowledgeEntry(
            id=entry_id,
            content=content,
            category=category,
            tags=tags,
            source=source,
            created_at=timestamp,
            updated_at=timestamp,
            version=1,
            confidence=max(0.0, min(1.0, confidence)),
            references=references or [],
            metadata=metadata or {}
        )

        # Save entry
        entry_path = self.base_path / "entries" / f"{entry_id}.json"
        with open(entry_path, 'w') as f:
            json.dump(asdict(entry), f, indent=2)

        # Update category index
        self._update_category_index(category, entry_id)

        # Update tag indexes
        for tag in tags:
            self._update_tag_index(tag, entry_id)

        logger.info(f"Added knowledge entry: {entry_id}")
        return entry_id

    def get_entry(self, entry_id: str) -> Optional[KnowledgeEntry]:
        """
        Retrieve a knowledge entry by ID.

        Args:
            entry_id: The entry ID

        Returns:
            The knowledge entry if found, None otherwise
        """
        entry_path = self.base_path / "entries" / f"{entry_id}.json"
        if not entry_path.exists():
            return None

        with open(entry_path, 'r') as f:
            data = json.load(f)
            return KnowledgeEntry(**data)

    def update_entry(self, entry_id: str, content: str = None,
                    tags: List[str] = None, metadata: Dict[str, Any] = None,
                    confidence: float = None) -> Optional[KnowledgeEntry]:
        """
        Update an existing knowledge entry.

        Args:
            entry_id: The entry ID
            content: New content (optional)
            tags: New tags (optional)
            metadata: New metadata (optional)
            confidence: New confidence score (optional)

        Returns:
            The updated entry if successful, None if entry not found
        """
        entry = self.get_entry(entry_id)
        if not entry:
            return None

        # Archive current version
        archive_path = self.base_path / "archive" / f"{entry_id}_v{entry.version}.json"
        with open(archive_path, 'w') as f:
            json.dump(asdict(entry), f, indent=2)

        # Update fields
        if content is not None:
            entry.content = content
        if tags is not None:
            entry.tags = tags
        if metadata is not None:
            entry.metadata.update(metadata)
        if confidence is not None:
            entry.confidence = max(0.0, min(1.0, confidence))

        entry.version += 1
        entry.updated_at = datetime.now().isoformat()

        # Save updated entry
        entry_path = self.base_path / "entries" / f"{entry_id}.json"
        with open(entry_path, 'w') as f:
            json.dump(asdict(entry), f, indent=2)

        logger.info(f"Updated knowledge entry: {entry_id} (v{entry.version})")
        return entry

    def search_entries(self, query: str = None, category: str = None,
                      tags: List[str] = None, min_confidence: float = 0.0,
                      limit: int = 10) -> List[KnowledgeEntry]:
        """
        Search knowledge entries based on various criteria.

        Args:
            query: Text to search for
            category: Filter by category
            tags: Filter by tags
            min_confidence: Minimum confidence score
            limit: Maximum number of results

        Returns:
            List of matching knowledge entries
        """
        results = []
        entries_dir = self.base_path / "entries"

        for entry_file in entries_dir.glob("*.json"):
            with open(entry_file, 'r') as f:
                data = json.load(f)
                entry = KnowledgeEntry(**data)

                # Apply filters
                if category and entry.category != category:
                    continue

                if tags and not all(tag in entry.tags for tag in tags):
                    continue

                if entry.confidence < min_confidence:
                    continue

                if query and query.lower() not in entry.content.lower():
                    continue

                results.append(entry)

                if len(results) >= limit:
                    break

        return results

    def _update_category_index(self, category: str, entry_id: str):
        """Update category index with new entry."""
        index_path = self.base_path / "indexes" / f"category_{category}.txt"
        with open(index_path, 'a') as f:
            f.write(f"{entry_id}\n")

    def _update_tag_index(self, tag: str, entry_id: str):
        """Update tag index with new entry."""
        index_path = self.base_path / "indexes" / f"tag_{tag}.txt"
        with open(index_path, 'a') as f:
            f.write(f"{entry_id}\n")

    def get_category_entries(self, category: str) -> List[KnowledgeEntry]:
        """Get all entries for a specific category."""
        if category not in self.categories:
            return []

        index_path = self.base_path / "indexes" / f"category_{category}.txt"
        if not index_path.exists():
            return []

        entries = []
        with open(index_path, 'r') as f:
            entry_ids = f.read().splitlines()
            for entry_id in entry_ids:
                entry = self.get_entry(entry_id)
                if entry:
                    entries.append(entry)

        return entries

    def get_tag_entries(self, tag: str) -> List[KnowledgeEntry]:
        """Get all entries with a specific tag."""
        index_path = self.base_path / "indexes" / f"tag_{tag}.txt"
        if not index_path.exists():
            return []

        entries = []
        with open(index_path, 'r') as f:
            entry_ids = f.read().splitlines()
            for entry_id in entry_ids:
                entry = self.get_entry(entry_id)
                if entry:
                    entries.append(entry)

        return entries
