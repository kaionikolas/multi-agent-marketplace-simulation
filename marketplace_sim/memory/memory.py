# memory/memory.py

from typing import List, Dict, Any


class AgentMemory:
    """
    Simple memory system for agents.
    Stores past interactions and transactions and allows retrieval.
    """

    def __init__(self, max_size: int = 100):
        self.max_size = max_size
        self.events: List[Dict[str, Any]] = []

    def store(self, event: Dict[str, Any]) -> None:
        """
        Store an event in memory.
        If memory exceeds max size, remove the oldest event.
        """
        self.events.append(event)
        if len(self.events) > self.max_size:
            self.events.pop(0)

    def retrieve_recent(self, k: int = 5) -> List[Dict[str, Any]]:
        """
        Retrieve the last k events.
        """
        return self.events[-k:]

    def retrieve_all(self) -> List[Dict[str, Any]]:
        """
        Retrieve all stored events.
        """
        return list(self.events)
