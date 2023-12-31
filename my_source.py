# Contains code under test for pytest notebook

def add_func(a, b):
    return a + b


def prime(a, b):
    return a**b


def euclid(p, q):
    """Return the euclidean distance.
    Args:
        p (list): p vector
        q (list): q vector

    Returns:
        euclidean distance
    """
    dist = 0
    for p_i, q_i in zip(p, q):
        dist += (q_i - p_i) ** 2
    return dist ** 0.5


"""Contains code under test for solution_ci."""

def add_func(a, var_two):
    """
    Add two variables.

    Args
        a: first variable
        var_two: second variable

    """
    return a + var_two
