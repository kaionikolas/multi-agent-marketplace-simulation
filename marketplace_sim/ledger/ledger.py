# ledger/ledger.py

from typing import List, Dict, Any
from datetime import datetime


class TransactionLedger:
    """
    Records all transactions executed in the market.
    """

    def __init__(self):
        self.transactions: List[Dict[str, Any]] = []

    def record(
        self,
        buyer_id: str,
        seller_id: str,
        price: float,
        quantity: int,
        round_id: int
    ) -> None:
        """
        Record a transaction in the ledger.
        """
        transaction = {
            "timestamp": datetime.utcnow().isoformat(),
            "buyer_id": buyer_id,
            "seller_id": seller_id,
            "price": price,
            "quantity": quantity,
            "round": round_id,
        }
        self.transactions.append(transaction)

    def all_transactions(self) -> List[Dict[str, Any]]:
        """
        Return all recorded transactions.
        """
        return list(self.transactions)
