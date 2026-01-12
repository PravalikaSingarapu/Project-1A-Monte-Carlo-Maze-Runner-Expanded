import numpy as np

def var(portfolio_values, alpha=0.05):
    return np.percentile(portfolio_values, 100 * alpha)

def cvar(portfolio_values, alpha=0.05):
    var_threshold = var(portfolio_values, alpha)
    return portfolio_values[portfolio_values <= var_threshold].mean()

def control_variate_adjustment(simulated, control, control_expectation):
    beta = np.cov(simulated, control)[0,1] / np.var(control)
    adjusted = simulated - beta * (control - control_expectation)
    return adjusted

