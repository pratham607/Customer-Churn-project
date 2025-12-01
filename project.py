from sklearn.preprocessing import LabelEncoder
import pandas as pd
le = LabelEncoder() 
df = pd.read_csv("Telco Customer Churn data.zip")
#print(df["Offer"].tail(40))
df["offer_encoded"]=le.fit_transform(df["Offer"])
df["offer_encoded"]=df["offer_encoded"].fillna(df["offer_encoded"].median())
print(df["offer_encoded"])


#Internet type
print(df["Internet Type"])
df["InternetType_encoded"]=le.fit_transform(df["Internet Type"])
print(df["InternetType_encoded"])
df["InternetType_encoded"]=df["InternetType_encoded"].fillna(df["InternetType_encoded"].median())
print(df["InternetType_encoded"])

#Churn Category
print(df["Churn Category"])
df["ChurnCategory_encoded"]=le.fit_transform(df["Churn Category"])
print(df["ChurnCategory_encoded"])
df["ChurnCategory_encoded"]=df["ChurnCategory_encoded"].fillna(df["ChurnCategory_encoded"].median())
print(df["ChurnCategory_encoded"])

#Churn Reason
print(df["Churn Reason"])
df["ChurnReason_encoded"]=le.fit_transform(df["Churn Reason"])
print(df["ChurnReason_encoded"])
df["ChurnCategory_encoded"]=df["ChurnReason_encoded"].fillna(df["ChurnReason_encoded"].median())



df=df.drop(columns=["Offer","Internet Type","Churn Category","Churn Reason"])

# object to int 

from sklearn.preprocessing import LabelEncoder
encoders = {}
cat_cols = df.select_dtypes(include='object').columns
for col in cat_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    encoders[col] = le

#print("Label Encoding Done Successfully! ")
#df.head()


print(df.info())

df.to_csv("cleaned Telco Customer Churn data.zip")