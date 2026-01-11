# simulation/run_simulation.py

import random

from agents.buyer import BuyerAgent
from agents.seller import SellerAgent
from agents.hybrid import HybridAgent
from market.market import Market


def create_agents():
    agents = []

    # Buyers
    for i in range(4):
        agents.append(
            BuyerAgent(
                agent_id=f"buyer_{i}",
                cash=100.0,
                inventory=0,
                risk_profile=random.choice(["low", "medium", "high"]),
            )
        )

    # Sellers
    for i in range(4):
        agents.append(
            SellerAgent(
                agent_id=f"seller_{i}",
                cash=0.0,
                inventory=10,
                risk_profile=random.choice(["low", "medium", "high"]),
            )
        )

    # Hybrids
    for i in range(3):
        agents.append(
            HybridAgent(
                agent_id=f"hybrid_{i}",
                cash=50.0,
                inventory=5,
                risk_profile=random.choice(["low", "medium", "high"]),
            )
        )

    return agents


def run_simulation(rounds: int = 50):
    agents = create_agents()
    market = Market(agents)

    print("Starting market simulation...")
    print(f"Agents: {len(agents)} | Rounds: {rounds}")
    print("-" * 40)

    for _ in range(rounds):
        market.run_round()
        print(
            f"Round {market.round:02d} | "
            f"Last price: {market.last_price:.2f} | "
            f"Total trades: {len(market.ledger.transactions)}"
        )

    print("-" * 40)
    print("Simulation finished.")

    return market


if __name__ == "__main__":
    market = run_simulation(rounds=50)

    from experiments.metrics import (
        compute_price_per_round,
        compute_volume_per_round,
        compute_final_wealth,
    )
    from experiments.plots import (
        plot_price_evolution,
        plot_volume,
        plot_wealth_distribution,
    )

    transactions = market.ledger.all_transactions()

    price_per_round = compute_price_per_round(transactions)
    volume_per_round = compute_volume_per_round(transactions)
    wealth = compute_final_wealth(market.agents)

    plot_price_evolution(price_per_round)
    plot_volume(volume_per_round)
    plot_wealth_distribution(wealth)

