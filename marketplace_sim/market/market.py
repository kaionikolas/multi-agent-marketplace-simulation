# market/market.py

from typing import List, Dict, Any
from market.orderbook import OrderBook
from ledger.ledger import TransactionLedger


class Market:
    """
    Market orchestrates agent interactions and trade execution.
    """

    def __init__(self, agents: List[Any]):
        self.agents = {agent.agent_id: agent for agent in agents}
        self.orderbook = OrderBook()
        self.ledger = TransactionLedger()

        self.last_price: float = 1.0
        self.round: int = 0

    def run_round(self) -> None:
        """
        Run a single market round.
        """
        self.round += 1

        market_state = {
            "last_price": self.last_price,
            "round": self.round,
        }

        orders = []
        for agent in self.agents.values():
            order = agent.generate_order(market_state)
            if order:
                orders.append(order)

        self.orderbook.add_orders(orders)
        trades = self.orderbook.match_orders()

        for trade in trades:
            self._execute_trade(trade)

        self.orderbook.clear()

    def _execute_trade(self, trade: Dict[str, Any]) -> None:
        """
        Execute a trade and update agents and ledger.
        """
        buyer = self.agents[trade["buyer_id"]]
        seller = self.agents[trade["seller_id"]]

        price = trade["price"]
        quantity = trade["quantity"]

        # Update balances
        buyer.cash -= price * quantity
        buyer.inventory += quantity

        seller.cash += price * quantity
        seller.inventory -= quantity

        # Update last market price
        self.last_price = price

        # Record transaction
        self.ledger.record(
            buyer_id=buyer.agent_id,
            seller_id=seller.agent_id,
            price=price,
            quantity=quantity,
            round_id=self.round,
        )

        # Notify agents
        buyer.update_after_trade(trade)
        seller.update_after_trade(trade)
