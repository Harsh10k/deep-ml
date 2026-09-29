import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    if len(arr.shape) == 1 and norm_type == "frobenius":
        raise ValueError()
    arr = arr.flatten()
    if norm_type == "l1":
        c = 0
        for i in arr:
            c += abs(i)
        return float(c)
    elif norm_type == "l2" or norm_type == "frobenius":
        c = 0
        for i in arr:
            c += i**2
        return float(np.sqrt(c))
    elif norm_type == "linf":
        m = abs(arr[0])
        for e in arr:
            if abs(e) > m:
                m = abs(e)
        return float(m)
    else:
        raise ValueError()


