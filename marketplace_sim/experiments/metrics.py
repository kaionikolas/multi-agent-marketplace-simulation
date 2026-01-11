# experiments/metrics.py

from typing import List, Dict
from collections import defaultdict


def compute_price_per_round(transactions: List[Dict]) -> Dict[int, float]:
    prices = defaultdict(list)

    for tx in transactions:
        prices[tx["round"]].append(tx["price"])

    avg_price = {
        round_id: sum(values) / len(values)
        for round_id, values in prices.items()
    }

    return avg_price


def compute_volume_per_round(transactions: List[Dict]) -> Dict[int, int]:
    volume = defaultdict(int)

    for tx in transactions:
        volume[tx["round"]] += tx["quantity"]

    return dict(volume)


def compute_final_wealth(agents: Dict[str, any]) -> Dict[str, float]:
    wealth = {}

    for agent_id, agent in agents.items():
        wealth[agent_id] = agent.cash + agent.inventory

    return wealth
