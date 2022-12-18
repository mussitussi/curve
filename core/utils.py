import numpy as np


NUMBER = (int, float, complex)


def min_generic(x, y):
    is_numbers = isinstance(x, NUMBER), isinstance(y, NUMBER)
    if is_numbers == (True, True):
        return min(x, y)
    elif is_numbers == (True, False):
        return np.min([np.repeat(x, len(y)), y], axis=0)
    elif is_numbers == (False, True):
        return np.min([np.repeat(y, len(x)), x], axis=0)
    else:
        assert len(x) == len(y)
        return np.min([x, y], axis=0)
