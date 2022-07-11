import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
import joblib

class model:

    def load_boston_data(self):
        boston = load_boston()
        # bos = pd.DataFrame(boston.data)

        self.X = boston.data
        self.y = boston.target

        print("Check for Null values")
        self.isnull_check()
        print("Check for Dublicate vales")
        self.check_dublicate()
        
    def split_data(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y,
         test_size=0.33, random_state=42)

    def model_train(self):
        pass
    
    def isnull_check(self):
        print("Total # null values:",pd.DataFrame(self.X).isnull().sum().sum())
        print("--"*10)
    def check_dublicate(self):
        print("Total # dublicate values:",pd.DataFrame(self.X).duplicated().sum() )
        print("--"*10)

obj =model()
obj.load_boston_data()
obj.split_data()


