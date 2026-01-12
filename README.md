# Project-1A-Monte-Carlo-Maze-Runner-Expanded
Creating a Monte Carlo simulation engine for risk analysis. Implement correlated random number generation, path-dependent calculations, and convergence analysis. Build variance reduction techniques, scenario aggregation, and risk metric dashb# Monte Carlo Maze Runner: Expanded Risk Engine

## Overview
This project is a **production-grade Monte Carlo simulation engine** for multi-asset financial risk analysis.  
It supports:

- Correlated random number generation
- Multi-scenario simulations:
  - Base
  - Crash
  - Boom
  - High Volatility
  - Stagflation
- Variance reduction techniques (antithetic)
- Convergence analysis and performance benchmarking
- Portfolio risk metrics (VaR / CVaR)
- 3D stochastic visualization (random walks)
- Dockerized deployment for reproducibility

---

## Project Structure

mc_risk_engine/
├── engine/ # Core simulation modules
│ ├── init.py
│ ├── simulator.py # GBM simulation functions
│ ├── rng.py # Correlated and antithetic RNG
│ └── scenario_loader.py # Scenario JSON loader
├── scenarios/ # JSON files defining simulation scenarios
│ ├── base.json
│ ├── crash.json
│ ├── boom.json
│ ├── high_vol.json
│ └── stagflation.json
├── benchmarks/ # Performance and convergence scripts
│ └── performance.py
├── visualization/ # 3D random walk visualization
│ └── random_walk_3d.py
├── Dockerfile # Containerized deployment
├── requirements.txt # Python dependencies
├── main.py # Entry point for multi-scenario simulations
└── README.md # Project documentation


---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/PravalikaSingarapu/Project-1A-Monte-Carlo-Maze-Runner-Expanded.git
cd mc_risk_engine

2.Install Python dependencies
pip install -r requirements.txt


Running the Project
1. Run all scenarios (main engine)
python main.py
Output: VaR, CVaR, mean, and standard deviation for each scenario.

2. Run performance benchmark
python benchmarks/performance.py
Output: Speed vs accuracy table for different path sizes.

3. Run 3D random walk visualization
python visualization/random_walk_3d.py
Output: Interactive 3D plot of stochastic random walks.

4. Run using Docker
docker build -t mc-risk-engine .
docker run mc-risk-engine
Output: Container runs main.py automatically with all scenarios.


Key Features

Multi-Scenario Simulation: Base, Crash, Boom, High Volatility, Stagflation

Variance Reduction: Antithetic paths to reduce Monte Carlo noise

Convergence & Performance Tracking: Benchmark speed vs accuracy trade-offs

3D Visualization: Random walk demonstration of stochastic paths

Production Ready: Fully containerized for reproducibility



Author

Pravalika Singarapu – Internship Project at Zetheta Private Limited




References

Monte Carlo Methods in Finance

Geometric Brownian Motion (GBM)

Antithetic Variance Reduction Techniques

