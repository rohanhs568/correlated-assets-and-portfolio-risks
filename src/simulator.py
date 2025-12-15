import numpy as np

def simulate_correlated_gbm(
    S0_1, S0_2,
    mu1, mu2,
    sigma1, sigma2,
    rho,
    T,
    N_steps,
    N_paths,
    rng=None,
):
    """
    simulate two correlated geometric Brownian motions on [0, T]
    returns arrays S1, S2 of shape (N_paths, N_steps + 1)
    """
    if rng is None:
        rng = np.random.default_rng()

    dt = T / N_steps

    # avoid singular covariance at |rho|=1
    rho = float(np.clip(rho, -0.999999, 0.999999))

    Sigma = np.array([[1.0, rho],
                      [rho, 1.0]])

    try:
        L = np.linalg.cholesky(Sigma)
    except np.linalg.LinAlgError:
        raise ValueError(f"covariance matrix not positive definite for rho = {rho}")

    Z = rng.standard_normal(size=(N_paths, N_steps, 2))
    dW = Z @ L.T * np.sqrt(dt)

    S1 = np.empty((N_paths, N_steps + 1))
    S2 = np.empty((N_paths, N_steps + 1))
    S1[:, 0] = S0_1
    S2[:, 0] = S0_2

    drift1 = (mu1 - 0.5 * sigma1**2) * dt
    drift2 = (mu2 - 0.5 * sigma2**2) * dt

    for n in range(N_steps):
        S1[:, n+1] = S1[:, n] * np.exp(drift1 + sigma1 * dW[:, n, 0])
        S2[:, n+1] = S2[:, n] * np.exp(drift2 + sigma2 * dW[:, n, 1])

    return S1, S2

