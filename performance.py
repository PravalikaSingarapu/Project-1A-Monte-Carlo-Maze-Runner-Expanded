import time
import numpy as np
from engine.simulator import simulate_gbm
from engine.scenario_loader import load_scenario

def benchmark():
    scenario = load_scenario("scenarios/base.json")

    mu = np.array(scenario["mu"])
    sigma = np.array(scenario["sigma"])
    corr = np.array(scenario["correlation"])
    T = scenario["T"]
    steps = scenario["steps"]
    S0 = np.array([100, 100])

    path_sizes = [1000, 5000, 10000, 20000, 50000]

    print("\n=== Performance Benchmark (Speed vs Accuracy) ===")
    print(f"{'Paths':>10} | {'Time (s)':>10} | {'Mean':>10} | {'Std':>10}")
    print("-" * 50)

    for n_paths in path_sizes:
        start = time.perf_counter()

        paths = simulate_gbm(S0, mu, sigma, corr, T, steps, n_paths)
        portfolio_value = paths[:, -1, :].sum(axis=1)

        elapsed = time.perf_counter() - start

        mean_val = portfolio_value.mean()
        std_val = portfolio_value.std()

        print(f"{n_paths:>10} | {elapsed:>10.4f} | {mean_val:>10.2f} | {std_val:>10.2f}")

if __name__ == "__main__":
    benchmark()

