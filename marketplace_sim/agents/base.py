# agents/base.py

from abc import ABC, abstractmethod
from typing import Dict, Any
from memory.memory import AgentMemory


class BaseAgent(ABC):
    """
    Abstract base class for all agents in the marketplace.
    """

    def __init__(
        self,
        agent_id: str,
        cash: float,
        inventory: int,
        risk_profile: str
    ):
        self.agent_id = agent_id
        self.cash = cash
        self.inventory = inventory
        self.risk_profile = risk_profile
        self.memory = AgentMemory()

        # Adaptive belief about market price
        self.price_expectation: float = 1.0

    @abstractmethod
    def generate_order(self, market_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a buy or sell order based on the current market state.
        """
        pass

    def update_after_trade(self, trade: Dict[str, Any]) -> None:
        """
        Update internal state after a trade is executed.
        """
        self.memory.store(trade)
        self._update_price_expectation(trade["price"])

    def _update_price_expectation(self, trade_price: float) -> None:
        """
        Simple adaptive rule for updating expected price.
        """
        alpha = 0.2  # learning rate
        self.price_expectation = (
            alpha * trade_price + (1 - alpha) * self.price_expectation
        )
