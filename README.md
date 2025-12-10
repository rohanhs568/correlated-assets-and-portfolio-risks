# Correlated Portfolio Risk

A simulation study of how correlation affects diversification and portfolio risk in a two-asset geometric Brownian motion model. The project combines analytical results with Monte Carlo experiments to demonstrate how the variance of portfolio log-returns depends on the correlation parameter $\rho$.

---

## Motivation

Diversification is a central idea in quantitative finance, but its effectiveness depends on how strongly assets move together. In the Black-Scholes setting each asset follows a geometric Brownian motion, and the correlation between the Brownian drivers determines how their log-returns co-move.

For a two-asset portfolio with weights $w_1$ and $w_2$, volatilities $\sigma_1$ and $\sigma_2$, and correlation $\rho$, the variance of the portfolio log-return over $[0,T]$ is

$$ \text{Var}(R_p) = w_1^2 \sigma_1^2 T + w_2^2 \sigma_2^2 T + 2 w_1 w_2 \rho \sigma_1 \sigma_2 T. $$

This expression shows a linear relationship between portfolio risk and correlation.  
The aim of this project is to verify this behaviour numerically, explore the distribution of portfolio outcomes, and illustrate how diversification strength changes with $\rho$.

---

## Project overview

### 1. Modelling and simulation
- Define a two-asset geometric Brownian motion with correlation parameter $\rho$  
- Construct correlated Gaussian increments using a Cholesky factorisation  
- Simulate batches of joint price paths over $[0,T]$

### 2. Empirical vs analytical risk
- Compute portfolio log-returns for each simulated path  
- Estimate the variance for a grid of correlation values  
- Compare empirical variances with the analytical formula  
- Plot variance as a function of $\rho$ to confirm the predicted linear dependence

### 3. Distributional effects of correlation
- Simulate large samples of portfolio outcomes for selected $\rho$ values  
- Plot histograms and kernel density estimates  
- Observe how the distribution narrows for negative correlation and widens for positive correlation  
- Provide a direct visual illustration of diversification effects

---

## Repository structure


src/ <br />
parameters.py # model and simulation parameters <br />
simulator.py # correlated GBM simulator <br />
portfolio.py # portfolio utilities and analytical variance <br />
experiments.py # variance and KDE experiments <br />
plots.py # plotting functions <br />
main.py # reproduce all results <br />

notebooks/ <br />
correlated_portfolio_risk.ipynb <br />

figures/ <br />
variance_vs_rho.png <br />
kde_distributions.png <br />

README.md <br />
.gitignore <br />


---

## Results

### Portfolio variance vs correlation
Monte Carlo estimates match the analytical curve closely. Portfolio variance increases as $\rho$ becomes larger, reflecting weaker diversification when the assets move more closely together.

### Distribution of portfolio outcomes
Kernel density estimates highlight the change in dispersion:

- $\rho < 0$ produces narrow, stable distributions  
- $\rho = 0$ produces intermediate spread  
- $\rho > 0$ produces wider, more volatile distributions  

The mean remains similar across scenarios; the change in risk is captured by the change in variance.

---

## Conclusion

This project shows how correlation drives portfolio risk in the two-asset Black-Scholes setting. The analytical variance depends linearly on $\rho$, and simulation results confirm this relationship. The distributional analysis provides a more intuitive view: negative correlation stabilises the portfolio, while positive correlation amplifies fluctuations.

Natural extensions include multi-asset portfolios, time-varying or stochastic correlations, heavier-tailed return models, or alternative risk measures such as Value-at-Risk or Expected Shortfall. The simulation framework here forms a base for more advanced portfolio and risk analysis used in industry.


