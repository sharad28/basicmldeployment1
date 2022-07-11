import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor
import joblib

class model:

    def load_boston_data(self):
        self.boston = load_boston()
        # bos = pd.DataFrame(boston.data)

        self.X = self.boston.data
        self.y = self.boston.target
        print(self.X.shape)
        """
        Based on feature importance we have selected important
        features as CRIM (0), NOX (4), RM(5), Age(6),DIS(7),
        PTratio(10), LSTA(12)
        """
        self.X_nw = self.X[:,[0,4,5,6,7,10,12]]
        print(self.X_nw.shape)
        print("Check for Null values")
        self.isnull_check()
        print("Check for Dublicate vales")
        self.check_dublicate()
        
    def split_data(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X_nw, self.y, test_size=0.33, random_state=42)

    def model_train(self):
        pass
    
    def isnull_check(self):
        print("Total # null values:",pd.DataFrame(self.X).isnull().sum().sum())
        print("--"*10)
    def check_dublicate(self):
        print("Total # dublicate values:",pd.DataFrame(self.X).duplicated().sum() )
        print("--"*10)

    def pipeline(self):
        self.pipe = make_pipeline(StandardScaler(), SVR(kernel='linear'))
        self.pipe.fit(self.X_train, self.y_train)
        # print("Test score of model : ",round(self.pipe.score(self.X_test, self.y_test),3))
        joblib.dump(self.pipe,'pipeline.pkl')

        # load = joblib.load('pipeline.pkl')
        # print("load model score:",load.score(self.X_test, self.y_test))

        

obj =model()
obj.load_boston_data()
obj.split_data()
obj.pipeline()
rf=RandomForestRegressor()
feature_imprt= dict(zip(obj.boston.feature_names,rf.fit(obj.X,obj.y).feature_importances_))

plt.bar(obj.boston.feature_names,rf.fit(obj.X,obj.y).feature_importances_)
plt.show()

