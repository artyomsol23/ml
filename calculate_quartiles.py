import numpy as np
from typing import List, Dict, Union


def calculate_quartiles(data: list[float]):
    if not data:
        raise ValueError("Входной список данных пуст")

    data_array = np.array(data)
    
    q1 = float(np.percentile(data_array, 25))
    q2 = float(np.percentile(data_array, 50))
    q3 = float(np.percentile(data_array, 75))
    
    return {'Q1': q1, 'Q2': q2, 'Q3': q3}
