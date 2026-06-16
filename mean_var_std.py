
import numpy as np
def calculate(list):
    if len(list) != 9:
        raise ValueError( "List must contain nine numbers.")
    
    array_dict = np.array(list).reshape(3, 3)
    
    calculations = {
        'mean': [array_dict.mean(axis=0).tolist(), array_dict.mean(axis=1).tolist(), array_dict.mean().tolist()],
        'variance': [array_dict.var(axis=0).tolist(), array_dict.var(axis=1).tolist(), array_dict.var().tolist()],
        'standard deviation': [array_dict.std(axis=0).tolist(), array_dict.std(axis=1).tolist(), array_dict.std().tolist()],
        'max': [array_dict.max(axis=0).tolist(), array_dict.max(axis=1).tolist(), array_dict.max().tolist()],
        'min': [array_dict.min(axis=0).tolist(), array_dict.min(axis=1).tolist(), array_dict.min().tolist()],
        'sum': [array_dict.sum(axis=0).tolist(), array_dict.sum(axis=1).tolist(), array_dict.sum().tolist()]
    }
    return calculations
