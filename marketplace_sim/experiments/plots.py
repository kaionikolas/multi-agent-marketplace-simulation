# experiments/plots.py

import matplotlib.pyplot as plt


def plot_price_evolution(price_per_round: dict):
    rounds = sorted(price_per_round.keys())
    prices = [price_per_round[r] for r in rounds]

    plt.figure()
    plt.plot(rounds, prices)
    plt.xlabel("Round")
    plt.ylabel("Average Price")
    plt.title("Price Evolution Over Time")
    plt.grid(True)
    plt.savefig("logs/price_evolution.png") 
    plt.show()


def plot_volume(volume_per_round: dict):
    rounds = sorted(volume_per_round.keys())
    volumes = [volume_per_round[r] for r in rounds]

    plt.figure()
    plt.bar(rounds, volumes)
    plt.xlabel("Round")
    plt.ylabel("Trade Volume")
    plt.title("Trade Volume Per Round")
    plt.grid(True)
    plt.savefig("logs/volume_per_round.png")
    plt.show()


def plot_wealth_distribution(wealth: dict):
    agents = list(wealth.keys())
    values = list(wealth.values())

    plt.figure()
    plt.bar(agents, values)
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Total Wealth")
    plt.title("Final Wealth Distribution")
    plt.tight_layout()
    plt.savefig("logs/wealth_distribution.png")
    plt.show()
