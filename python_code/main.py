import numpy as np
import pandas as pd

def example_fcn():

    print("Hello")

    print(np.sqrt(16))
    print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))

    return

def example_fcn_2(x):
    return x + 1

example_fcn()
