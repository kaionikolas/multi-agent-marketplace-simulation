# agents/hybrid.py

from typing import Dict, Any
from agents.base import BaseAgent


class HybridAgent(BaseAgent):
    """
    Hybrid agent that can both buy and sell depending on its state.
    """

    def generate_order(self, market_state: Dict[str, Any]) -> Dict[str, Any]:
        last_price = market_state.get("last_price", self.price_expectation)

        # Decide role dynamically
        if self.inventory > 0 and self.cash < last_price:
            action = "sell"
        elif self.cash > last_price:
            action = "buy"
        else:
            return {}

        if action == "buy":
            bid_price = last_price * (1.0 if self.risk_profile == "medium" else 1.05)
            bid_price = min(bid_price, self.cash)

            return {
                "agent_id": self.agent_id,
                "type": "buy",
                "price": round(bid_price, 2),
                "quantity": 1,
            }

        else:
            ask_price = last_price * (1.0 if self.risk_profile == "medium" else 0.95)

            return {
                "agent_id": self.agent_id,
                "type": "sell",
                "price": round(ask_price, 2),
                "quantity": 1,
            }
