import pandas as pd
from sklearn.linear_model import LinearRegression

 

# define data
d = {'input 1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
     'input 2': [0.8, 0.9, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0],
     'target': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}

 

df = pd.DataFrame(data=d)

 

# define input and output for the model
X = df[['input 1', 'input 2']].values
y = df['target'].values

 

# do the simplest of all machine learning trainings
reg = LinearRegression().fit(X, y)
reg.score(X, y)

 

# generate new data - the data that we want to predict
# (must be in the same format as the input data!!!)
new_data = pd.DataFrame({'input 1': [1, 2, 3], 
                         'input 2': [0.4, 0.5, 0.6]})

 

# make prediction of new data
prediction = reg.predict(new_data)
