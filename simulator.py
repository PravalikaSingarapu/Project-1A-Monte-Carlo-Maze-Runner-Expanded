import numpy as np
from engine.rng import generate_correlated_normals, generate_antithetic_normals

def simulate_gbm(S0, mu, sigma, corr, T, steps, n_paths, use_antithetic=False):

    dt = T / steps
    n_assets = len(S0)

    if use_antithetic:
        Z = generate_antithetic_normals(corr, n_paths, n_assets)
        n_paths = Z.shape[0]
    else:
        Z = generate_correlated_normals(corr, n_paths, n_assets)

    paths = np.zeros((n_paths, steps + 1, n_assets))
    paths[:, 0, :] = S0

    for t in range(1, steps + 1):
        drift = (mu - 0.5 * sigma ** 2) * dt
        diffusion = sigma * np.sqrt(dt) * Z

        paths[:, t, :] = paths[:, t - 1, :] * np.exp(drift + diffusion)

    return paths

