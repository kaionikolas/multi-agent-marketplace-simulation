# Multi-Agent Marketplace Simulation

## Overview

This project implements a **fully autonomous multi-agent marketplace simulation** in Python, where heterogeneous agents interact to buy and sell a single good over multiple rounds. Through decentralized decision-making, agent memory, and adaptive pricing strategies, the system exhibits **emergent economic behaviors** such as price formation, trade volume dynamics, and wealth redistribution.

The project was developed as a technical challenge for the **AI Engineer position at CloudWalk** and follows the *Global Guidelines for AI Challenges*, with emphasis on clarity, autonomy, observability, and reproducibility.

---

## Key Features

- 10–15 autonomous agents with distinct **roles**, **risk profiles**, and **strategies**
- Explicit **agent memory** for storing past interactions and transactions
- Centralized market mechanism for **price discovery and transaction matching**
- Complete **transaction ledger** for auditability and metrics
- End-to-end **market simulation** with measurable outcomes
- Metrics and plots illustrating emergent market dynamics

---

## Design Rationale

The system models a **single-good marketplace with centralized order matching**. This design choice intentionally minimizes unnecessary infrastructure complexity while preserving core economic dynamics such as negotiation, competition, and price adaptation.

By keeping the market mechanism simple, the project focuses on:
- Agent autonomy and heterogeneity  
- Memory-driven adaptive behavior  
- Clear observability of decisions and outcomes  
- Full reproducibility and ease of evaluation  

This balance allows evaluators to clearly assess agent reasoning and system behavior without being obscured by excessive engineering overhead.

---

## Architecture

The project is modular and organized as follows:

```text
marketplace_sim/
├── agents/ # Buyer, Seller, and Hybrid agents
├── memory/ # Agent memory implementation
├── market/ # Market orchestration and order matching
├── ledger/ # Transaction ledger and logging
├── simulation/ # End-to-end simulation runner
├── experiments/ # Metrics computation and plotting
├── logs/ # Execution logs

---

### Component Responsibilities

- **agents/**  
  Defines autonomous agents with role-specific decision logic and risk-aware pricing strategies.

- **memory/**  
  Stores historical interactions and trades, enabling agents to adapt behavior over time.

- **market/**  
  Coordinates each simulation round, collects bids and asks, matches trades, and updates prices.

- **ledger/**  
  Records all transactions and interactions, ensuring traceability and auditability.

- **simulation/**  
  Orchestrates the full simulation lifecycle.

- **experiments/**  
  Computes metrics and generates plots for analysis and evaluation.

---

## Agent Behavior & Autonomy

Each agent is characterized by:

- **Role**: Buyer, Seller, or Hybrid  
- **Risk Profile**: Low, Medium, or High  
- **Strategy**: Price aggressiveness conditioned on risk and recent market outcomes  

Agents operate autonomously:
- They decide whether to buy, sell, or abstain each round
- They adapt bid/ask prices based on memory and market signals
- No hard-coded coordination or scripted outcomes exist

Emergent behavior arises naturally from repeated interactions and local decision-making.

---

## How to Run

### Requirements

- Python 3.9+
- matplotlib

## Install dependencies:

```md
```bash
pip install matplotlib

### Run the Simulation

From the project root directory:

```md
```bash
python -m simulation.run_simulation

This command:

- Initializes agents and the market

- Runs the simulation for a fixed number of rounds

- Prints round-by-round summaries

- Generates market metrics and plots

---

## Observability & Evaluation

The system is designed to be easily inspectable and evaluator-friendly:

- Console logs show the evolution of prices and trade volume per round

- A complete transaction ledger records all interactions

- Metrics and plots expose emergent market behavior

- Modular code structure enables fast inspection and debugging

---

## Reproducibility

- No paid APIs or external services are required

- Minimal dependencies

- Deterministic execution structure (can be extended with random seeds)

- Fully runnable on local machines and cloud environments (e.g. Google Colab)

---

## References & Inspiration

- Generative Agents: Interactive Simulacra of Human Behavior

- Agent Laboratory — Framework for Autonomous Agent Research
