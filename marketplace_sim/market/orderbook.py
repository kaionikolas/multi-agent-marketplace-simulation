# market/orderbook.py

from typing import List, Dict, Any


class OrderBook:
    """
    Simple centralized order book for matching buy and sell orders.
    """

    def __init__(self):
        self.buy_orders: List[Dict[str, Any]] = []
        self.sell_orders: List[Dict[str, Any]] = []

    def add_orders(self, orders: List[Dict[str, Any]]) -> None:
        """
        Separate buy and sell orders.
        """
        for order in orders:
            if not order:
                continue
            if order["type"] == "buy":
                self.buy_orders.append(order)
            elif order["type"] == "sell":
                self.sell_orders.append(order)

    def match_orders(self) -> List[Dict[str, Any]]:
        """
        Match buy and sell orders and return executed trades.
        """
        trades = []

        # Sort buyers by highest bid, sellers by lowest ask
        self.buy_orders.sort(key=lambda x: x["price"], reverse=True)
        self.sell_orders.sort(key=lambda x: x["price"])

        while self.buy_orders and self.sell_orders:
            buy = self.buy_orders[0]
            sell = self.sell_orders[0]

            if buy["price"] >= sell["price"]:
                trade_price = round((buy["price"] + sell["price"]) / 2, 2)

                trade = {
                    "buyer_id": buy["agent_id"],
                    "seller_id": sell["agent_id"],
                    "price": trade_price,
                    "quantity": 1,
                }
                trades.append(trade)

                self.buy_orders.pop(0)
                self.sell_orders.pop(0)
            else:
                break

        return trades

    def clear(self) -> None:
        """
        Clear all remaining orders.
        """
        self.buy_orders.clear()
        self.sell_orders.clear()
