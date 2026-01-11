# agents/seller.py

from typing import Dict, Any
from agents.base import BaseAgent


class SellerAgent(BaseAgent):
    """
    Seller agent that generates ask orders.
    """

    def generate_order(self, market_state: Dict[str, Any]) -> Dict[str, Any]:
        if self.inventory <= 0:
            return {}

        last_price = market_state.get("last_price", self.price_expectation)

        # Risk-based aggressiveness
        if self.risk_profile == "low":
            ask_price = last_price * 1.05
        elif self.risk_profile == "high":
            ask_price = last_price * 0.95
        else:
            ask_price = last_price

        order = {
            "agent_id": self.agent_id,
            "type": "sell",
            "price": round(ask_price, 2),
            "quantity": 1,
        }

        return order
