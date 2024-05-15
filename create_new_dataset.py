import pandas as pd

data=pd.read_csv("./titanic.csv")
data.head()
data=data[["Pclass","Sex","Age"]]
data.to_csv('./titanic_new.csv',index=False)