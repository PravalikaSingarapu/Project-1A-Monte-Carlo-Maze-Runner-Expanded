import numpy as np
from engine.simulator import simulate_gbm
from engine.scenario_loader import load_scenario


def compute_var_cvar(values, alpha=0.95):
    sorted_vals = np.sort(values)
    index = int((1 - alpha) * len(sorted_vals))
    var = sorted_vals[index]
    cvar = sorted_vals[:index].mean() if index > 0 else var
    return var, cvar


def run_all_scenarios(n_paths=10000, variance_method="standard"):
    scenario_files = [
        "scenarios/base.json",
        "scenarios/crash.json",
        "scenarios/boom.json",
        "scenarios/high_vol.json",
        "scenarios/stagflation.json"
    ]

    print("\nMonte Carlo Risk Engine")
    print("========================")

    for file in scenario_files:
        scenario = load_scenario(file)

        mu = np.array(scenario["mu"])
        sigma = np.array(scenario["sigma"])
        corr = np.array(scenario["correlation"])
        T = scenario["T"]
        steps = scenario["steps"]

        S0 = np.array([100, 100])

        use_antithetic = (variance_method == "antithetic")

        print(f"\n--- Scenario: {scenario['name']} ---")

        paths = simulate_gbm(
            S0=S0,
            mu=mu,
            sigma=sigma,
            corr=corr,
            T=T,
            steps=steps,
            n_paths=n_paths,
            use_antithetic=use_antithetic
        )

        portfolio_values = paths[:, -1, :].sum(axis=1)

        var, cvar = compute_var_cvar(portfolio_values)

        print(f"Paths simulated : {len(portfolio_values)}")
        print(f"Mean value      : {portfolio_values.mean():.2f}")
        print(f"Std deviation   : {portfolio_values.std():.2f}")
        print(f"VaR (95%)       : {var:.2f}")
        print(f"CVaR (95%)      : {cvar:.2f}")


if __name__ == "__main__":
    run_all_scenarios(
        n_paths=20000,
        variance_method="antithetic"   # change to "standard" if needed
    )

