import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    
    X = np.array(X)
    y = np.array(y)

    #the main issue in this code * is used for the element wise multiplication in which dimension should same of two matrix

    #but in @ , dot we have m * n style multiplication things 


    theta1 = X.T @ X
    theta1 = np.linalg.inv(theta1)

    theta2 = (X.T) @ y

    theta = theta1 @ theta2

    return theta.tolist()
    