import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    x=np.asarray(x)
    k=x-np.mean(x);
    variance=float(np.sum(k**2)/(x.size-1))
    sd=float(np.sqrt(variance))
    return {"variance": variance, "standard_deviation":sd}
    pass