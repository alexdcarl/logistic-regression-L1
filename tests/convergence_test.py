"""
Convergence tests
"""

import numpy as np
from logistic_regression_l1 import LogisticRegressionL1

def prob(X, betas):
    """
    Calculate probability given beta coefficient (sigmoid function)

    Params
    ------
    X : matrix of observations, not including bias
    betas : array of coefficients, includes bias

    Returns
    -------
    prob : array, probability for each observation
    """
    betas = betas * 1.
    X = np.insert(X, 0, 1., axis=1) * 1.
    power = X.dot(betas)

    return np.exp(power) / (1 + np.exp(power))

def create_random_observations(num_obs, num_feat, betas):
    """
    Create random observations, X, weights, and y (successes)

    Params
    ------
    num_obs : int
    num_feat : int (doesn't include bias)
    betas : list of beta coefficients, includes bias

    Returns
    -------
    matrix : 2d np array formatted as [X columns, m, y]
    """
    matrix = np.zeros((num_obs, num_feat + 2))

    for i in xrange(num_feat):
        matrix[:,i] = np.random.randint(0, 100, size=num_obs) * 1.0 / 100

    m = np.random.randint(500, 1000, size = num_obs)

    X = matrix[:, :-2]
    P = prob(X, np.array(betas))
    y = P * m

    matrix[:, -2] = m
    matrix[:, -1] = y

    return matrix

# Run test for 2 features, 100 observations
betas = [5., 0.3, 1.]

logitfitL1 = LogisticRegressionL1()
matrix = create_random_observations(100, 2, betas)
lambda_grid = np.exp(-1*np.linspace(1,17,200))
logitfitL1.fit(matrix, lambda_grid)

np.testing.assert_almost_equal(np.array(betas), logitfitL1.coef_, 2)
