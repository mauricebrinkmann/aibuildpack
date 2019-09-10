import pandas as pd
from sklearn.linear_model import LinearRegression

 
class Prediction:
  def __init__(self,aijson):  
        self.aijson = aijson
        # define data frame
        self.df = pd.DataFrame(data=self.aijson["data"])
        # define input and output for the model
        self.X = self.df[self.aijson["input"]].values
        self.y = self.df[self.aijson["target"]].values
        # do the simplest of all machine learning trainings
        self.reg = LinearRegression().fit(self.X, self.y)
        print("Model accuracy: %6.2f" % (self.reg.score(self.X, self.y)))
        
  def get_prediction(self,input):
    # generate new data - the data that we want to predict
    # (must be in the same format as the input data!!!)
    new_data = pd.DataFrame(input)
    # make prediction of new data
    target = self.reg.predict(new_data)
    return target
