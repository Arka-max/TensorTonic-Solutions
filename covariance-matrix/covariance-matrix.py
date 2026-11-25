import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    X=np.asarray(X)
    c=X-np.mean(X,axis=0)
    res=np.dot(c.T,c)/(X.shape[0]-1)
    return res
    pass