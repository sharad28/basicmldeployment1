import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn
from sklearn.datasets import load_boston
import 
boston = load_boston()
bos = pd.DataFrame(boston.data)
