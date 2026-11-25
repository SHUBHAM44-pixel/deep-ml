import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    # Your code here
    #standarization
    mean_d = np.mean(data, axis = 0)
    std_d = np.std(data, axis = 0,ddof = 0)
    standardized_data = np.round((data - mean_d) / std_d , 4)

    #min max feature_scaling
    min_d = np.min(data,axis = 0)
    max_d  = np.max(data,axis = 0)

    normalized_data = np.round((data - min_d) / (max_d - min_d), 4)
    

    return standardized_data, normalized_data