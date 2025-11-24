import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

df=pd.read_csv("C:/Users/rahul/Downloads/Banking.csv")
print(df)

host="localhost"
port=3306
username="root"
password="root"
database="banking_domain"
engine=create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")
table_name="bank_details"
df.to_sql(table_name,engine,if_exists="replace",index=False)
print("data loaded successfully")
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.describe())
print(df["Estimated Income"].value_counts())
labels=["Low","Medium","High"]
bins=[0,100000,300000,float("inf")]
df["Income band"]=pd.cut(df["Estimated Income"],bins=bins,labels=labels,right=False)
print(df["Income band"])
print(df["Income band"].value_counts().plot(kind="bar"))
plt.show()

categorical_col=df[["Nationality","BRId","GenderId","IAId","Fee Structure","Occupation","Loyalty Classification",
                    "Estimated Income","Amount of Credit Cards","Income band","Properties Owned","Risk Weighting"]].columns
for col in categorical_col:
    print(f"Value Counts for {col}")
    print(df[col].value_counts())

for i ,y in enumerate(df[["Nationality","BRId","GenderId","IAId","Fee Structure","Occupation","Loyalty Classification",
                    "Estimated Income","Amount of Credit Cards","Income band","Properties Owned","Risk Weighting"]]):
    plt.figure(i)
    sns.countplot(data=df,x=y,hue="GenderId")
    plt.show()

# histplot of value count of different occupation
for col in categorical_col:
    if col=="Occupation":
        continue
    plt.figure(figsize=(8,4))
    sns.histplot(df[col])
    plt.title("Histogram of occupation count")
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.show()

#Numerical analysis
numerical_cols=df[["Estimated Income","Superannuation Savings","Credit Card Balance",
                   "Bank Loans","Bank Deposits","Checking Accounts","Saving Accounts","Foreign Currency Account","Business Lending"]]
for i ,col in enumerate(numerical_cols):
    plt.figure(figsize=(8,4))
    plt.subplot(4,3,i+1)
    sns.histplot(df[col],kde=True)
    plt.title(col)
    plt.show()
# heatmap
correlation_matrix=df.corr(numeric_only=True)
plt.figure(figsize=(12,12))
sns.heatmap(correlation_matrix,annot=True,cmap="crest",fmt=".2f")
plt.title("Correlation matrix")
plt.show()





