import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)


df = pd.read_csv("customers.csv")
df.head()


df.shape
df.dtypes
df.isnull().sum()

df.columns
df["customer_type"].value_counts()
df["customer_type"].value_counts().head(1)
df["customer_type"].value_counts().sort_values().head(1)

df["customer_type"].value_counts(normalize=True)*100

df["CustomerID"].duplicated().sum()
df.groupby("CustomerID")["customer_type"].nunique().gt(1).sum()

df.head()