import numpy as np
from scipy.optimize import fsolve

def explicit(f, y0, time_vect):
    """
    Euler's explicit method for solving ordinary differential equations (ODEs).

    Parameters:
        f: function
            The ordinary differential equation (ODE) to be solved. It should take two arguments:
            t: float
                The current time.
            y: numpy.ndarray
                The current state vector.
            It should return the derivative of y with respect to t.
        y0: numpy.ndarray
            The initial condition, representing the value of y at the initial time.
        time_vect: numpy.ndarray
            The time points at which the solution is desired.

    Returns:
        numpy.ndarray
            An array containing the solution at each time point.
    """
    d = len(y0)
    y = np.zeros((d, len(time_vect)))
    y[:, 0] = y0
    for i in range(1, len(time_vect)):
        dt = time_vect[i] - time_vect[i-1]
        y[:, i] = y[:, i-1] + dt * f(time_vect[i-1], y[:, i-1])
    return y

def implicit(f, y0, time_vect):
    """
    Euler's implicit method for solving ordinary differential equations (ODEs).

    Parameters:
        f: function
            The ordinary differential equation (ODE) to be solved. It should take two arguments:
            t: float
                The current time.
            y: numpy.ndarray
                The current state vector.
            It should return the derivative of y with respect to t.
        y0: numpy.ndarray
            The initial condition, representing the value of y at the initial time.
        time_vect: numpy.ndarray
            The time points at which the solution is desired.

    Returns:
        numpy.ndarray
            An array containing the solution at each time point.
    """
    d = len(y0)
    y = np.zeros((d, len(time_vect)))
    y[:, 0] = y0
    for i in range(1, len(time_vect)):
        dt = time_vect[i] - time_vect[i-1]
        y[:, i] = fsolve(lambda x: x - y[:, i-1] - dt * f(time_vect[i], x), y[:, i-1])
    return y

def mid_point(f, y0, time_vect):
    """
    Euler's midpoint method for solving ordinary differential equations (ODEs).

    Parameters:
        f: function
            The ordinary differential equation (ODE) to be solved. It should take two arguments:
            t: float
                The current time.
            y: numpy.ndarray
                The current state vector.
            It should return the derivative of y with respect to t.
        y0: numpy.ndarray
            The initial condition, representing the value of y at the initial time.
        time_vect: numpy.ndarray
            The time points at which the solution is desired.

    Returns:
        numpy.ndarray
            An array containing the solution at each time point.
    """
    d = len(y0)
    y = np.zeros((d, len(time_vect)))
    y[:, 0] = y0
    for i in range(1, len(time_vect)):
        dt = time_vect[i] - time_vect[i-1]
        y[:, i] = y[:, i-1] + dt * f(time_vect[i-1] + dt/2, y[:, i-1] + dt/2 * f(time_vect[i-1], y[:, i-1]))
    return y
