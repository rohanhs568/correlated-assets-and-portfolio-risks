import numpy as np

def portfolio_return(S1, S2, w1, w2):
    """
    compute portfolio log-return at time T
    """
    R1 = np.log(S1[:, -1] / S1[:, 0])
    R2 = np.log(S2[:, -1] / S2[:, 0])
    return w1 * R1 + w2 * R2


def analytical_variance(rho, w1, w2, sigma1, sigma2, T):
    """
    analytical variance of portfolio log-return as a function of rho
    """
    return (
        w1**2 * sigma1**2 * T
        + w2**2 * sigma2**2 * T
        + 2 * w1 * w2 * rho * sigma1 * sigma2 * T
    )

