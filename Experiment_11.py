import pandas as pd 
series=pd.Series([10,20,30,40,50])
print(series)

# creating series with custom indexes:
series1=pd.Series([10,20,30,40,50],index=["a","b","c","d","e"])
print(series1)

# creating dataframes using dictionary:
data={"name":["Alice","Bob","Charlie"],"Age":[12,12,13]}
df=pd.DataFrame(data)
print(df)
# selecting columns:
print(df["name"])
print(df["Age"])
print(df["name","Age"])
# selecting rows using iloc and loc
print(df.iloc[0]) # first row by position
print(df.loc[0])  # row with index 0