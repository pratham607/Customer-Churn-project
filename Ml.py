"""import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error , r2_score
df=pd.read_csv("cleaned Telco Customer Churn data.zip")
#print(df)
X=df[["Customer ID","Gender","Age","Under 30","Senior Citizen","Married","Dependents","Number of Dependents","Country","State","City","Zip Code","Latitude",
      "Quarter","Referred a Friend","Number of Referrals","Tenure in Months","Phone Service","Avg Monthly Long Distance Charges",
      "Multiple Lines","Internet Service","Avg Monthly GB Download","Online Security","Online Backup","Device Protection Plan","Premium Tech Support",
      "Streaming TV","Unlimited Data","Contract","Paperless Billing","Payment Method","Monthly Charge","Total Charges","Total Refunds","Total Extra Data Charges",
      "Total Long Distance Charges","Total Revenue","Satisfaction Score","Churn Label","Churn Score","CLTV","offer_encoded","InternetType_encoded",
      "ChurnCategory_encoded","ChurnReason_encoded"]]
y=df["Customer Status"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=45)
model=LogisticRegression()
model.fit(X_train,y_train)
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
y_pred=model.fit(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision (weighted):", precision_score(y_test, y_pred, average='weighted'))
print("Recall (weighted):", recall_score(y_test, y_pred, average='weighted'))
print("F1 Score (weighted):", f1_score(y_test, y_pred, average='weighted'))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))"""
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# Load data
df = pd.read_csv("cleaned Telco Customer Churn data.zip")

# ------------------- FIX 1: Define X and y properly -------------------
X = df[["Gender","Age","Under 30","Senior Citizen","Married","Dependents","Number of Dependents","Country",
        "State","City","Zip Code","Latitude","Quarter","Referred a Friend","Number of Referrals",
        "Tenure in Months","Phone Service","Avg Monthly Long Distance Charges","Multiple Lines",
        "Internet Service","Avg Monthly GB Download","Online Security","Online Backup",
        "Device Protection Plan","Premium Tech Support","Streaming TV","Unlimited Data","Contract",
        "Paperless Billing","Payment Method","Monthly Charge","Total Charges","Total Refunds",
        "Total Extra Data Charges","Total Long Distance Charges","Total Revenue","Satisfaction Score",
        "Churn Score","CLTV","offer_encoded","InternetType_encoded",
        "ChurnCategory_encoded","ChurnReason_encoded"]]

# ❌ Removed "Customer ID" because it breaks ML (unique for each customer)
# ❌ Removed "Churn Label" because it leaks the target

y = df["Customer Status"]   # <-- target

# ------------------- FIX 2: Encode categorical columns automatically -------------------
X = pd.get_dummies(X, drop_first=True)

# ------------------- Split train/test -------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=45)

# ------------------- Train model -------------------
model = LogisticRegression(max_iter=2000)
model.fit(X_train, y_train)

# ------------------- Predict -------------------
y_pred = model.predict(X_test)

# ------------------- FIX 3: Use weighted avg (target is multiclass) -------------------
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision (weighted):", precision_score(y_test, y_pred, average='weighted'))
print("Recall (weighted):", recall_score(y_test, y_pred, average='weighted'))
print("F1 Score (weighted):", f1_score(y_test, y_pred, average='weighted'))

print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

