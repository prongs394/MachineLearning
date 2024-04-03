import numpy as np

def cost_function( x, y, theta0, theta1 ):
    """Compute the squared error cost function

    Inputs:
    x        vector of length m containing x values
    y        vector of length m containing y values
    theta_0  (scalar) intercept parameter
    theta_1  (scalar) slope parameter

    Returns:
    cost     (scalar) the cost
    """

    cost = 0.0

    ##################################################
    # TODO: write code here to compute cost correctly
    p = theta0 + x*theta1
    cost = np.sum(0.5*(p-y)**2)
    print(type(cost))



    ##################################################

    return cost


def gradient(x, y, theta_0, theta_1):
    """Compute the partial derivative of the squared error cost function

    Inputs:
    x          vector of length m containing x values
    y          vector of length m containing y values
    theta_0    (scalar) intercept parameter
    theta_1    (scalar) slope parameter

    Returns:
    d_theta_0  (scalar) Partial derivative of cost function wrt theta_0
    d_theta_1  (scalar) Partial derivative of cost function wrt theta_1
    """
    d_theta_0, d_theta_1 = 0, 0
    ##################################################
    # TODO: write code here to compute partial derivatives correctly
    d_theta_0 = np.sum(theta_0 + theta_1*x - y)
    d_theta_1 = np.sum(x*(theta_0 + theta_1*x - y))
    ##################################################

    return d_theta_0, d_theta_1 # return is a tuple

def explicit_answer(x, y):
    """Compute the explicit values of theta1 and theta2

    Inputs:
    x          vector of length m containing x values
    y          vector of length m containing y values

    Returns:
    theta_0  (scalar) intercept of line
    theta_1  (scalar) slope of line
    """
    theta1 = np.sum((x - np.mean(x)) * (y - np.mean(y))) / np.sum(np.power(x - np.mean(x), 2))
    theta0 = np.mean(y) - theta1 * np.mean(x)
    print("explicit: ",theta0, "   ", theta1)




    ##################################################
    # TODO: write code here to compute explicit values of theta_0 and theta_1
    ##################################################