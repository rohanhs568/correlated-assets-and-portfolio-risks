import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

def plot_variance(rho_values, empirical, analytical):
    plt.figure(figsize=(6,4))
    plt.plot(rho_values, analytical, linewidth=2, label="analytical")
    plt.plot(rho_values, empirical, "o", label="empirical")
    plt.xlabel(r"$\rho$")
    plt.ylabel("Variance of portfolio log-return")
    plt.title("Portfolio variance vs correlation")
    plt.legend()
    plt.grid(alpha=0.2)
    plt.tight_layout()
    plt.show()


def plot_kde(results, rho_list):
    colors = {
        -0.8: "#1f77b4",
        0.0:  "#2ca02c",
        0.8:  "#d62728",
    }

    all_vals = np.concatenate([results[rho] for rho in rho_list])
    xmin, xmax = np.percentile(all_vals, [0.2, 99.8])
    xgrid = np.linspace(xmin, xmax, 500)

    fig, axes = plt.subplots(1, 3, figsize=(15, 4), sharex=True, sharey=True)

    for ax, rho in zip(axes, rho_list):
        kde = gaussian_kde(results[rho])
        yvals = kde(xgrid)
        ax.plot(xgrid, yvals, color=colors[rho], linewidth=2)
        ax.fill_between(xgrid, yvals, color=colors[rho], alpha=0.15)
        ax.set_title(f"$\\rho = {rho}$", fontsize=12)
        ax.set_xlabel("Portfolio log-return", fontsize=10)

    axes[0].set_ylabel("Density", fontsize=10)
    plt.tight_layout()
    plt.show()

