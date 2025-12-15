import numpy as np

from parameters import *
from experiments import variance_experiment, kde_distributions
from plots import plot_variance, plot_kde

if __name__ == "__main__":

    # variance experiment
    rho_values = np.linspace(-0.9, 0.9, 19)
    empirical, analytical = variance_experiment(
        rho_values,
        N_paths=25000,
        S0_1=S0_1, S0_2=S0_2,
        mu1=mu1, mu2=mu2,
        sigma1=sigma1, sigma2=sigma2,
        w1=w1, w2=w2,
        T=T,
        N_steps=N_steps,
        rng=rng,
    )
    plot_variance(rho_values, empirical, analytical)

    # KDE distributions
    rho_list = [-0.8, 0.0, 0.8]
    results = kde_distributions(
        rho_list,
        N_paths_hist=25000,
        S0_1=S0_1, S0_2=S0_2,
        mu1=mu1, mu2=mu2,
        sigma1=sigma1, sigma2=sigma2,
        w1=w1, w2=w2,
        T=T,
        N_steps=N_steps,
        rng=rng,
    )
    plot_kde(results, rho_list)
