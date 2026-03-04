import numpy as np
import pandas as pd
from pathlib import Path
from scipy.stats import qmc
from scipy.stats import norm
from scipy.optimize import brentq

from tqdm import tqdm


def black_scholes_price(S0, K, T, r, sigma, option_type='call'):
    """Calculate Black-Scholes option prices for arrays of parameters."""

    T = np.maximum(T, 1e-6)
    sigma = np.maximum(sigma, 1e-6)
    
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == 'call':
        price = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)
        
    return price

def sample_params(n_samples):
    params_dict = {
        "S0": (0.4, 1.6),       # S0 (moneyness = S0/K)
        "taus": (0.2, 1.1),     # time to maturity
        "rs": (0.02, 0.1),      # risk-free rate
        "sigma": (0.01, 1.0)    # volatility
    }

    sampler = qmc.LatinHypercube(d=len(params_dict))
    sample_unit_cube = sampler.random(n=n_samples)

    l_bounds = [v[0] for v in params_dict.values()]
    r_bounds = [v[1] for v in params_dict.values()]
    samples = qmc.scale(sample_unit_cube, l_bounds, r_bounds)

    df_params = pd.DataFrame(samples, columns=params_dict.keys())
    return df_params

def generate_labels(n_samples):
    df_labels = sample_params(n_samples)
    chunk_size = 10000
    prices = []

    for i in tqdm(range(0, len(df_labels), chunk_size)):
        batch = df_labels.iloc[i : i + chunk_size]
        
        S0 = batch["S0"].values
        K = 1.0
        r = batch["rs"].values
        T = batch["taus"].values
        sigma = batch["sigma"].values
        
        p = black_scholes_price(S0, K, T, r, sigma, option_type="call")
        prices.extend(p)

    df_labels["price"] = prices
    
    Path("data").mkdir(exist_ok=True)
    df_labels.to_csv("data/synthetic_data-bs.csv", index=None)


if __name__ == "__main__":
    generate_labels(n_samples=100_000)