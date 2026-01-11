# agents/buyer.py

from typing import Dict, Any
from agents.base import BaseAgent


class BuyerAgent(BaseAgent):
    """
    Buyer agent that generates bid orders.
    """

    def generate_order(self, market_state: Dict[str, Any]) -> Dict[str, Any]:
        if self.cash <= 0:
            return {}

        last_price = market_state.get("last_price", self.price_expectation)

        # Risk-based aggressiveness
        if self.risk_profile == "low":
            bid_price = last_price * 0.95
        elif self.risk_profile == "high":
            bid_price = last_price * 1.05
        else:
            bid_price = last_price

        # Never bid more cash than available
        bid_price = min(bid_price, self.cash)

        order = {
            "agent_id": self.agent_id,
            "type": "buy",
            "price": round(bid_price, 2),
            "quantity": 1,
        }

        return order
