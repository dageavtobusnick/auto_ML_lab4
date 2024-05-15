import pandas as pd
from sklearn.preprocessing import OneHotEncoder

data=pd.read_csv("./titanic_new.csv")
data.head()
enc=OneHotEncoder(drop='if_binary')
data["Sex"]=pd.DataFrame(enc.fit_transform(data[["Sex"]]).toarray())[0]
data.to_csv('./titanic_new.csv',index=False)