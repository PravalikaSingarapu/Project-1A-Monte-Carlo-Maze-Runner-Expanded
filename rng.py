import numpy as np

def generate_correlated_normals(corr_matrix, n_paths, n_assets):
    L = np.linalg.cholesky(corr_matrix)
    Z = np.random.normal(size=(n_paths, n_assets))
    return Z @ L.T


def generate_antithetic_normals(corr_matrix, n_paths, n_assets):
    half = n_paths // 2
    Z = np.random.normal(size=(half, n_assets))
    Z_corr = Z @ np.linalg.cholesky(corr_matrix).T

    Z_full = np.vstack([Z_corr, -Z_corr])
    return Z_full

