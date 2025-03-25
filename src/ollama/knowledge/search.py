from typing import Dict, List, Optional, Any
import logging
from pathlib import Path
from datetime import datetime
import json
from dataclasses import dataclass

logger = logging.getLogger(__name__)

@dataclass
class SearchResult:
    category: str
    entry_id: str
    title: str
    relevance: float
    content: Dict[str, Any]
    metadata: Dict[str, Any]

class KnowledgeSearch:
    def __init__(self, base_path: str = "./knowledge"):
        self.base_path = Path(base_path)
        self.index_path = self.base_path / "index"
        self.index_path.mkdir(exist_ok=True)
        self.latest_index = self._load_latest_index()

    def _load_latest_index(self) -> Dict:
        index_files = list(self.index_path.glob("index_*.json"))
        if not index_files:
            return {}
        latest = max(index_files, key=lambda x: x.stat().st_mtime)
        with open(latest) as f:
            return json.load(f)

    def refresh_index(self) -> None:
        """Update the search index"""
        new_index = {}
        for category in ["prompt-templates", "model-specific", "domain-knowledge"]:
            category_path = self.base_path / category
            if not category_path.exists():
                continue

            for file in category_path.glob("*.yaml"):
                try:
                    with open(file) as f:
                        content = f.read()
                        entry_id = file.stem
                        new_index[f"{category}/{entry_id}"] = {
                            "content": content,
                            "category": category,
                            "entry_id": entry_id,
                            "updated": datetime.fromtimestamp(
                                file.stat().st_mtime
                            ).isoformat()
                        }
                except Exception as e:
                    logger.error(f"Error indexing {file}: {str(e)}")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        index_file = self.index_path / f"index_{timestamp}.json"
        with open(index_file, "w") as f:
            json.dump(new_index, f, indent=2)
        self.latest_index = new_index

    def search(self,
              query: str,
              categories: Optional[List[str]] = None,
              limit: int = 10) -> List[SearchResult]:
        """Search the knowledge base"""
        results = []
        query = query.lower()

        for key, entry in self.latest_index.items():
            if categories and entry["category"] not in categories:
                continue

            content = entry["content"].lower()
            if query in content:
                # Simple relevance score based on word frequency
                relevance = content.count(query) / len(content.split())

                results.append(SearchResult(
                    category=entry["category"],
                    entry_id=entry["entry_id"],
                    title=entry.get("title", entry["entry_id"]),
                    relevance=relevance,
                    content=entry["content"],
                    metadata={"updated": entry["updated"]}
                ))

        # Sort by relevance and limit results
        results.sort(key=lambda x: x.relevance, reverse=True)
        return results[:limit]

    def get_related(self, entry_id: str, limit: int = 5) -> List[SearchResult]:
        """Find related knowledge entries"""
        if not entry_id in self.latest_index:
            return []

        entry = self.latest_index[entry_id]
        content_words = set(entry["content"].lower().split())
        results = []

        for other_id, other_entry in self.latest_index.items():
            if other_id == entry_id:
                continue

            other_words = set(other_entry["content"].lower().split())
            # Calculate similarity based on word overlap
            similarity = len(content_words & other_words) / len(content_words | other_words)

            if similarity > 0:
                results.append(SearchResult(
                    category=other_entry["category"],
                    entry_id=other_entry["entry_id"],
                    title=other_entry.get("title", other_entry["entry_id"]),
                    relevance=similarity,
                    content=other_entry["content"],
                    metadata={"updated": other_entry["updated"]}
                ))

        results.sort(key=lambda x: x.relevance, reverse=True)
        return results[:limit]

    def get_recent_updates(self, days: int = 7) -> List[Dict]:
        """Get recently updated entries"""
        cutoff = datetime.now().timestamp() - (days * 24 * 60 * 60)
        recent = []

        for entry in self.latest_index.values():
            updated = datetime.fromisoformat(entry["updated"]).timestamp()
            if updated > cutoff:
                recent.append({
                    "category": entry["category"],
                    "entry_id": entry["entry_id"],
                    "updated": entry["updated"]
                })

        recent.sort(key=lambda x: x["updated"], reverse=True)
        return recent
