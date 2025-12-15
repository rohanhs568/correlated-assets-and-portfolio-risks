import numpy as np
from simulator import simulate_correlated_gbm
from portfolio import portfolio_return, analytical_variance

def variance_experiment(
    rho_values,
    N_paths,
    S0_1, S0_2,
    mu1, mu2,
    sigma1, sigma2,
    w1, w2,
    T,
    N_steps,
    rng
):
    empirical = []
    analytical = []

    for rho in rho_values:
        S1, S2 = simulate_correlated_gbm(
            S0_1, S0_2,
            mu1, mu2,
            sigma1, sigma2,
            rho,
            T,
            N_steps,
            N_paths,
            rng
        )

        Rp = portfolio_return(S1, S2, w1, w2)
        empirical.append(np.var(Rp, ddof=1))
        analytical.append(analytical_variance(rho, w1, w2, sigma1, sigma2, T))

    return np.array(empirical), np.array(analytical)


def kde_distributions(
    rho_list,
    N_paths_hist,
    S0_1, S0_2,
    mu1, mu2,
    sigma1, sigma2,
    w1, w2,
    T,
    N_steps,
    rng
):
    results = {}

    for rho in rho_list:
        S1, S2 = simulate_correlated_gbm(
            S0_1, S0_2,
            mu1, mu2,
            sigma1, sigma2,
            rho,
            T,
            N_steps,
            N_paths_hist,
            rng
        )
        Rp = portfolio_return(S1, S2, w1, w2)
        results[rho] = Rp

    return results

