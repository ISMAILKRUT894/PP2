def add(a, b):
    """Return the sum of a and b."""
    return a + b
def mean(values):
    """
    Calculate the arithmetic mean.

    Parameters
    ----------
    values : list of float
        List of numbers.

    Returns
    -------
    float
        The mean value.
    """
    return sum(values) / len(values)