import pandas as pd
df=pd.read_csv("Telco Customer Churn data.zip")
print(df)
print(df.info())
#Internet type
print(df["Internet Type"])
df["Internet Type"]=df["Internet Type"].fillna("Missing value")
print(df["Internet Type"].head(45))
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df["Internet Type encoded"]=le.fit_transform(df["Internet Type"])
print(df["Internet Type encoded"])
print(df.info())
#Offer
print(df["Offer"])
df["Offer"]=df["Offer"].fillna("Missing value")
print(df["Offer"])
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df["Offer encoded"]=le.fit_transform(df["Offer"]) 
print(df["Offer encoded"])
print(df.info())
#Churn Category
print(df["Churn Category"])
df["Churn Category"]=df["Churn Category"].fillna("Missing value")
print(df["Churn Category"])
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df["Churn Category encoded"]=le.fit_transform(df["Churn Category"])
print(df["Churn Category encoded"])
print(df.info())
#Churn Reason
print(df["Churn Reason"])
df["Churn Reason"]=df["Churn Reason"].fillna("Missing value")
print(df["Churn Reason"])
from sklearn.preprocessing import LabelEncoder
le= LabelEncoder()
df["Churn Reason encoded"]=le.fit_transform(df["Churn Reason"])
print(df["Churn Reason encoded"])
print(df.info())







#Object to int
from sklearn.preprocessing import LabelEncoder
encoders={}
cat_cols = df.select_dtypes(include="object").columns
for col in cat_cols:
    le=LabelEncoder()
    df[col]=le.fit_transform(df[col].astype(str))
    encoders[col]=le
print("Label encoding done successfully")
print(df.info())

df.to_csv("Cleaned churn data")