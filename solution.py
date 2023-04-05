import pandas as pd
import numpy as np
import math

chat_id = 919511341

def solution(x: np.array) -> float:
    sum = 0.0
    for i in range(0, len(x)):
        if x[i] > 143:
            sum = sum + math.log((x[i]-143))
    sum = sum/len(x)
    return sum
