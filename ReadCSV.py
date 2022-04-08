import pandas as pd

data = pd.read_csv('C:\\Users\\umayadav\\PycharmProjects\\TestDataPython.csv')
print (data.loc[:,['FirstName','LastName']])
# Use the multi-axes indexing funtion
print (data.loc[2:6,['FirstName','LastName']])
print(data[0:5]["Email"])  # read first 5 rows of column Email
print(data[0:5])  # read first 5 rows
print(data)  # print full data
