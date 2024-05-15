import pandas as pd

data=pd.read_csv("./titanic_new.csv")
data.head()
data=data.loc[:, data.columns !='Unnamed: 0']
data["Age"]=data["Age"].fillna(data["Age"].mean())
data.to_csv('./titanic_new.csv',index=False)