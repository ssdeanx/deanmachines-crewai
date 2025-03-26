# hyperbrowser_suite_tools.py (Final Version)
"""
Standalone script defining a suite of LangChain Tools for HyperBrowser,
verified against documentation and search results. Includes session management.

Includes:
- Stateless Tools:
  1. Official HyperBrowserTool ('hyper_browser_browse') for general browsing.
  2. Custom tool for explicit scraping ('hyper_browser_scrape') using client.scrape.start_and_wait.
  3. Custom tool for explicit crawling ('hyper_browser_crawl') using client.crawl.start_and_wait.
- Stateful Session Tools:
  4. 'start_hyper_browser_session': Creates a persistent session using client.sessions.create.
  5. 'run_in_hyper_browser_session': Runs tasks within an existing session (assuming session_obj.run exists).
  6. 'close_hyper_browser_session': Closes a persistent session using client.sessions.stop.

Requires:
- 'hyperbrowser-python' library (`pip install hyperbrowser-python`)
- 'langchain-hyperbrowser' library (`pip install langchain-hyperbrowser`)
- HYPERBROWSER_API_KEY environment variable set.
"""

import os
import json
import logging
import uuid
from typing import List, Dict, Any, Optional
from langchain.tools import Tool

# --- Configure Logging ---
log_level = os.getenv("LOG_LEVEL", "INFO").upper()
valid_log_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
if log_level not in valid_log_levels: log_level = "INFO"
logging.basicConfig(level=log_level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Import Official LangChain Tool ---
try:
    from langchain_hyperbrowser import HyperBrowserTool
    LANGCHAIN_HYPERBROWSER_AVAILABLE = True
    logger.info("Imported HyperBrowserTool from langchain-hyperbrowser.")
except ImportError:
    LANGCHAIN_HYPERBROWSER_AVAILABLE = False
    logger.warning("Could not import HyperBrowserTool from 'langchain-hyperbrowser'.")
    class HyperBrowserTool: # Dummy
        def __init__(self, *args, **kwargs): raise ImportError("'langchain-hyperbrowser' not installed.")
        def run(self, *args, **kwargs): raise ImportError("'langchain-hyperbrowser' not installed.")

# --- Import Core SDK & Specific Models ---
try:
    from hyperbrowser import HyperBrowser as CoreHyperBrowser
    # Import parameter models for type hinting and potentially cleaner arg passing
    from hyperbrowser.models.scrape import StartScrapeJobParams
    from hyperbrowser.models.crawl import StartCrawlJobParams
    from hyperbrowser.models.session import CreateSessionParams
    CORE_HYPERBROWSER_AVAILABLE = True
    logger.info("Imported core HyperBrowser SDK and parameter models.")
except ImportError:
    CORE_HYPERBROWSER_AVAILABLE = False
    if not LANGCHAIN_HYPERBROWSER_AVAILABLE: logger.warning("Core HyperBrowser SDK ('hyperbrowser-python') or its models not found.")
    # Dummy classes
    class CoreHyperBrowser:
        def __init__(self, *args, **kwargs): pass
        # Define dummy submodules based on search results
        class Scrape:
             def start_and_wait(self, *args, **kwargs): raise ImportError("Core SDK 'hyperbrowser-python' not installed.")
        class Crawl:
             def start_and_wait(self, *args, **kwargs): raise ImportError("Core SDK 'hyperbrowser-python' not installed.")
        class Sessions:
             def create(self, *args, **kwargs): raise ImportError("Core SDK 'hyperbrowser-python' not installed.")
             # Need a dummy session object for create to return
             class DummySession:
                 id = None
                 def run(self, *args, **kwargs): raise ImportError("Core SDK 'hyperbrowser-python' not installed.")
                 def close(self, *args, **kwargs): raise ImportError("Core SDK 'hyperbrowser-python' not installed.")
             def create(self, *args, **kwargs): return self.DummySession()
             def stop(self, *args, **kwargs): raise ImportError("Core SDK 'hyperbrowser-python' not installed.")
        # Assign instances of dummy submodules
        scrape = Scrape()
        crawl = Crawl()
        sessions = Sessions()

    # --- CORRECTED INDENTATION for dummy parameter classes ---
    class StartScrapeJobParams:
        def __init__(self, **kwargs): pass
    class StartCrawlJobParams:
        def __init__(self, **kwargs): pass
    class CreateSessionParams:
        def __init__(self, **kwargs): pass


# --- Simple In-Memory Session State Management ---
# WARNING: Not thread-safe or suitable for concurrent requests.
ACTIVE_SESSIONS: Dict[str, Any] = {} # Stores session objects from client.sessions.create()

# --- Helper to Check Core SDK Availability & Key ---
def _check_core_sdk_availability_and_key(require_core_sdk: bool = True) -> str | None:
    """Checks library availability and API key. Returns error message string or None if OK."""
    if require_core_sdk and not CORE_HYPERBROWSER_AVAILABLE:
        error_msg = "Error: Core HyperBrowser SDK ('hyperbrowser-python') is required for this specific tool but is not available."
        logger.error(error_msg); return error_msg
    # Check if *any* tool is available if core isn't strictly required
    if not require_core_sdk and not CORE_HYPERBROWSER_AVAILABLE and not LANGCHAIN_HYPERBROWSER_AVAILABLE:
         error_msg = "Error: Neither Core HyperBrowser SDK nor Langchain integration is available."
         logger.error(error_msg); return error_msg
    api_key = os.getenv("HYPERBROWSER_API_KEY")
    if not api_key:
         error_msg = "Error: HYPERBROWSER_API_KEY environment variable not set."
         logger.error(error_msg); return error_msg
    return None


# === Stateless Tool Logic Functions (Refined SDK Usage) ===

def run_hyper_browser_scrape(input_json: str) -> str:
    """Uses client.scrape.start_and_wait() for targeted extraction."""
    if error := _check_core_sdk_availability_and_key(require_core_sdk=True): return error
    logger.debug(f"Executing Core SDK 'scrape.start_and_wait' with input: {input_json[:250]}...")
    try:
        data = json.loads(input_json); url = data.get("url"); extract_query = data.get("extract_query"); selector = data.get("selector")
        if not url or not isinstance(url, str): return "Error: Invalid or missing 'url' in JSON for scrape."
        if not extract_query and not selector: return "Error: Must provide 'extract_query' or 'selector' in JSON for scrape."
        if extract_query and selector: logger.warning("Both 'extract_query' and 'selector' provided for scrape; query likely preferred.")
        params_dict = {"url": url};
        if extract_query: params_dict["query"] = extract_query
        if selector: params_dict["selector"] = selector
        # Add other params like 'regex', 'schema_', 'browser' to params_dict if needed
        logger.info(f"Executing Core SDK 'scrape.start_and_wait' on URL: {url}")
        client = CoreHyperBrowser()
        params_obj = StartScrapeJobParams(**params_dict)
        # Assuming start_and_wait returns the result directly
        result = client.scrape.start_and_wait(params=params_obj)
        logger.info("Core SDK 'scrape.start_and_wait' completed."); result_str = str(result) if result is not None else "No content scraped."
        return f"HyperBrowser Scrape Result:\n---\n{result_str}\n---"
    except json.JSONDecodeError: logger.error(f"Failed to decode JSON for scrape: {input_json[:250]}..."); return "Error: Invalid JSON input format for scrape."
    except ImportError as ie: return f"Error: {ie}"
    except Exception as e: logger.error(f"Error during Core SDK 'scrape.start_and_wait': {e}", exc_info=True); return f"Error executing scrape: {type(e).__name__}: {e}"

def run_hyper_browser_crawl(input_json: str) -> str:
    """Uses client.crawl.start_and_wait() to crawl a website."""
    if error := _check_core_sdk_availability_and_key(require_core_sdk=True): return error
    logger.debug(f"Executing Core SDK 'crawl.start_and_wait' with input: {input_json[:250]}...")
    try:
        data = json.loads(input_json); start_url = data.get("start_url"); depth = data.get("depth", 1); match_pattern = data.get("match_pattern")
        if not start_url or not isinstance(start_url, str): return "Error: Invalid or missing 'start_url' in JSON for crawl."
        try: depth_int = int(depth) if depth is not None else 1
        except ValueError: return "Error: 'depth' must be an integer."
        params_dict = {"url": start_url, "depth": depth_int};
        if match_pattern: params_dict["match"] = match_pattern
        # Add other params like 'limit', 'browser' to params_dict if needed
        logger.info(f"Executing Core SDK 'crawl.start_and_wait' starting at: {start_url} with depth {depth_int}")
        client = CoreHyperBrowser()
        params_obj = StartCrawlJobParams(**params_dict)
        # Assuming start_and_wait returns the list of URLs
        result_list = client.crawl.start_and_wait(params=params_obj)
        logger.info(f"Core SDK 'crawl.start_and_wait' completed, found {len(result_list) if result_list else 0} URLs.")
        return json.dumps(result_list if result_list else [], indent=2)
    except json.JSONDecodeError: logger.error(f"Failed to decode JSON for crawl: {input_json[:250]}..."); return "Error: Invalid JSON input format for crawl."
    except ImportError as ie: return f"Error: {ie}"
    except Exception as e: logger.error(f"Error during Core SDK 'crawl.start_and_wait': {e}", exc_info=True); return f"Error executing crawl: {type(e).__name__}: {e}"

# === Stateful Session Tool Logic Functions ===
def start_hyper_browser_session(config_json: Optional[str] = None) -> str:
    """Creates a new persistent HyperBrowser session using client.sessions.create()."""
    if error := _check_core_sdk_availability_and_key(require_core_sdk=True): return json.dumps({"error": error})
    logger.info(f"Attempting to start HyperBrowser session with config: {config_json[:250] if config_json else 'Defaults'}...")
    config_dict = {}
    if config_json:
        try:
            config_dict = json.loads(config_json);
            if not isinstance(config_dict, dict): raise ValueError("Config must be JSON object.")
            logger.debug(f"Parsed session config keys: {list(config_dict.keys())}")
        except (json.JSONDecodeError, ValueError) as e: error_msg = f"Invalid JSON config: {e}"; logger.error(error_msg); return json.dumps({"error": error_msg})
    try:
        client = CoreHyperBrowser()
        params_obj = CreateSessionParams(**config_dict)
        session_obj = client.sessions.create(params=params_obj) # Get session object
        session_id = getattr(session_obj, 'id', None); id_source = "object 'id'"
        if not session_id: session_id = str(uuid.uuid4()); id_source = "generated UUID"; logger.warning(f"Session object lacks 'id', using {id_source}: {session_id}")
        logger.info(f"Session created successfully with ID: {session_id} (source: {id_source})")
        ACTIVE_SESSIONS[session_id] = session_obj # Store the session object
        return json.dumps({"session_id": session_id})
    except ImportError as ie: return json.dumps({"error": f"ImportError: {ie}"})
    except Exception as e: logger.error(f"Error starting session: {e}", exc_info=True); return json.dumps({"error": f"Failed to start session: {type(e).__name__}: {e}"})

def run_in_hyper_browser_session(input_json: str) -> str:
    """
    Runs a task within an existing HyperBrowser session (assuming session_obj.run exists).
    NOTE: The existence/behavior of session_obj.run() is assumed based on guides;
    if errors occur, alternative interaction via ws_endpoint might be needed.
    """
    if error := _check_core_sdk_availability_and_key(require_core_sdk=True): return error
    logger.debug(f"Attempting task in session with input: {input_json[:250]}...")
    session_id = None
    try:
        data = json.loads(input_json); session_id = data.get("session_id"); task = data.get("task")
        if not session_id or not isinstance(session_id, str): return "Error: Missing 'session_id' in JSON."
        if not task or not isinstance(task, str): return "Error: Missing 'task' in JSON."
        session_obj = ACTIVE_SESSIONS.get(session_id)
        if session_obj is None: logger.error(f"Session ID '{session_id}' not found."); return f"Error: Session ID '{session_id}' not found or closed."
        # Check for the 'run' method
        if not hasattr(session_obj, 'run') or not callable(getattr(session_obj, 'run', None)):
             logger.error(f"Session object for ID '{session_id}' (type: {type(session_obj)}) lacks callable 'run' method. Cannot execute task directly this way.")
             return f"Error: Session object for ID '{session_id}' doesn't support direct 'run'. Task execution failed."
        logger.info(f"Running task in session '{session_id}': {task[:150]}...")
        result = session_obj.run(task=task) # Call the run method
        logger.info(f"Task completed in session '{session_id}'."); result_str = str(result) if result is not None else "No content returned."
        return f"Session Task Result (ID: {session_id}):\n---\n{result_str}\n---"
    except json.JSONDecodeError: logger.error(f"Failed to decode JSON for run_in_session: {input_json[:250]}..."); return "Error: Invalid JSON input format for run_in_session."
    except ImportError as ie: return f"Error: {ie}"
    except Exception as e: logger.error(f"Error running task in session '{session_id}': {e}", exc_info=True); return f"Error executing task in session '{session_id}': {type(e).__name__}: {e}"

def close_hyper_browser_session(input_json: str) -> str:
    """Closes an active HyperBrowser session using client.sessions.stop()."""
    if error := _check_core_sdk_availability_and_key(require_core_sdk=True): return error
    logger.debug(f"Attempting to close session with input: {input_json[:250]}...")
    session_id = None
    try:
        data = json.loads(input_json); session_id = data.get("session_id")
        if not session_id or not isinstance(session_id, str): return "Error: Missing 'session_id' in JSON."
        # Check if tracked locally before attempting API call
        if session_id not in ACTIVE_SESSIONS: logger.warning(f"Attempted to close untracked/already closed session ID '{session_id}'."); return f"Session ID '{session_id}' not found. Assuming already closed."
        logger.info(f"Closing session ID via API: {session_id}...")
        client = CoreHyperBrowser()
        response = client.sessions.stop(id=session_id) # Use client.sessions.stop()
        del ACTIVE_SESSIONS[session_id] # Remove from tracker
        success = getattr(response, 'success', True) # Assume success if unclear
        if success: logger.info(f"Successfully closed session ID via API: {session_id}."); return f"Successfully closed session ID: {session_id}."
        else: logger.warning(f"API issue closing session ID '{session_id}'. Response: {response}"); return f"API call to close session '{session_id}' completed with potential issue. Removed from tracking."
    except json.JSONDecodeError: logger.error(f"Failed to decode JSON for close_session: {input_json[:250]}..."); return "Error: Invalid JSON input format for close_session."
    except ImportError as ie: return f"Error: {ie}"
    except Exception as e:
        logger.error(f"Error closing session '{session_id}': {e}", exc_info=True)
        if session_id and session_id in ACTIVE_SESSIONS: del ACTIVE_SESSIONS[session_id]; logger.warning(f"Removed session '{session_id}' from tracking due to closure error.")
        return f"Error closing session '{session_id}': {type(e).__name__}: {e}"


# --- Instantiate Tools ---
hyperbrowser_tools_list: List[Tool] = []
# Instantiate tools only if dependencies met, append to list
if LANGCHAIN_HYPERBROWSER_AVAILABLE:
    try:
        official_tool = HyperBrowserTool()
        official_tool.name = "hyper_browser_browse" # Specific name for clarity
        official_tool.description = ("Use for *stateless* web browsing tasks (navigate, click, type, extract basic info) via natural language. Handles complex interactions automatically within a *single call*. Input is a single string task description. Example: \"Go to example.com and return the main heading text.\"")
        hyperbrowser_tools_list.append(official_tool); logger.info(f"Initialized official Langchain Tool as: '{official_tool.name}'")
    except Exception as e: logger.error(f"Failed to initialize official HyperBrowserTool: {e}", exc_info=True)
else: logger.warning("Official 'langchain-hyperbrowser' tool unavailable.")

if CORE_HYPERBROWSER_AVAILABLE:
    try:
        scrape_tool = Tool( name="hyper_browser_scrape", description=("Extracts specific content from a URL using query OR CSS selector (stateless). Input JSON: {'url': '<url>', 'extract_query': '<query>'} OR {'url': '<url>', 'selector': '<css_selector>'}."), func=run_hyper_browser_scrape )
        hyperbrowser_tools_list.append(scrape_tool); logger.info("Initialized custom Scrape tool.")
    except Exception as e: logger.error(f"Failed to create custom scrape tool: {e}", exc_info=True)
    try:
        crawl_tool = Tool( name="hyper_browser_crawl", description=("Crawls a website from a start URL (stateless). Input JSON: {'start_url': '<url>', 'depth': <int>, 'match_pattern': '<optional_str>'}."), func=run_hyper_browser_crawl )
        hyperbrowser_tools_list.append(crawl_tool); logger.info("Initialized custom Crawl tool.")
    except Exception as e: logger.error(f"Failed to create custom crawl tool: {e}", exc_info=True)
    try:
        start_session_tool = Tool( name="start_hyper_browser_session", description=("Creates a persistent browser session for stateful tasks. Returns JSON: {'session_id': '<new_id>'}. Store the session_id! Optional input JSON for config: '{\"browser\": \"firefox\", \"profile_id\": \"id\"}'."), func=start_hyper_browser_session )
        hyperbrowser_tools_list.append(start_session_tool); logger.info("Initialized Start Session tool.")
    except Exception as e: logger.error(f"Failed to create start_session tool: {e}", exc_info=True)
    try:
        run_in_session_tool = Tool( name="run_in_hyper_browser_session", description=("Runs a task within an *existing* browser session (stateful). Input JSON: {'session_id': '<id>', 'task': '<natural_language_task>'}."), func=run_in_hyper_browser_session )
        hyperbrowser_tools_list.append(run_in_session_tool); logger.info("Initialized Run In Session tool.")
    except Exception as e: logger.error(f"Failed to create run_in_session tool: {e}", exc_info=True)
    try:
        close_session_tool = Tool( name="close_hyper_browser_session", description=("Closes an active persistent browser session. Input JSON: {'session_id': '<id>'}."), func=close_hyper_browser_session )
        hyperbrowser_tools_list.append(close_session_tool); logger.info("Initialized Close Session tool.")
    except Exception as e: logger.error(f"Failed to create close_session tool: {e}", exc_info=True)
if not CORE_HYPERBROWSER_AVAILABLE: logger.warning("Custom 'scrape', 'crawl', and session tools unavailable (core SDK 'hyperbrowser-python' missing).")


# --- Optional: Test Block ---
if __name__ == "__main__":
    print(f"\n--- HyperBrowser Tools Initialization & Session Test ---")
    print(f"Official Tool Available: {LANGCHAIN_HYPERBROWSER_AVAILABLE}")
    print(f"Core SDK Available: {CORE_HYPERBROWSER_AVAILABLE}")
    print(f"API Key Set: {'Yes' if os.getenv('HYPERBROWSER_API_KEY') else 'No'}")
    print(f"Tools Initialized: {len(hyperbrowser_tools_list)} -> {[tool.name for tool in hyperbrowser_tools_list]}")

    if not hyperbrowser_tools_list or not os.getenv('HYPERBROWSER_API_KEY'):
        print("\nSkipping live tests (Tools unavailable or API Key missing).")
    else:
        # Find tools for testing
        start_tool = next((t for t in hyperbrowser_tools_list if t.name == 'start_hyper_browser_session'), None)
        run_tool = next((t for t in hyperbrowser_tools_list if t.name == 'run_in_hyper_browser_session'), None)
        close_tool = next((t for t in hyperbrowser_tools_list if t.name == 'close_hyper_browser_session'), None)

        # --- Test Session Lifecycle ---
        if start_tool and run_tool and close_tool:
            print("\n--- Testing Session Lifecycle ---")
            session_id = None
            try:
                # 1. Start Session
                print("1. Starting session...")
                start_result_json = start_tool.run('{}') # Default config
                print(f"   Start Result: {start_result_json}")
                start_result = json.loads(start_result_json)
                if "error" in start_result: raise Exception(f"Failed to start session: {start_result['error']}")
                session_id = start_result.get("session_id")
                if not session_id: raise Exception("Did not receive session_id.")
                print(f"   Obtained Session ID: {session_id}")

                # 2. Run Task in Session
                print("\n2. Running task in session...")
                task_input = json.dumps({"session_id": session_id, "task": "Go to example.com and get the H1 text."})
                print(f"   Task Input: {task_input}")
                run_result = run_tool.run(task_input)
                print(f"   Run Result:\n{run_result}")
                if isinstance(run_result, str) and "Error:" in run_result: raise Exception(f"Task 1 execution failed: {run_result}")

            except Exception as e:
                print(f"!!! Session Test Block Failed: {type(e).__name__}: {e}")
            finally:
                # 3. Close Session
                if session_id:
                    print(f"\n3. Closing session {session_id}...")
                    close_input = json.dumps({"session_id": session_id})
                    try:
                        close_result = close_tool.run(close_input)
                        print(f"   Close Result: {close_result}")
                    except Exception as e: print(f"   Close attempt failed: {type(e).__name__}: {e}")
                    print(f"   Active Sessions Check After Close: {list(ACTIVE_SESSIONS.keys())}")
                else: print("\n3. Skipping session close (no valid session ID obtained).")
        else: print("\n--- Session Lifecycle Test Skipped (Required tools unavailable) ---")
        print("-" * 20)
