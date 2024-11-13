import pandas as pd
from pandas.core.frame import DataFrame

# Creating a DataFrame from a dictionary
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['New York', 'Los Angeles', 'Chicago']
# }
# Create pandas dataframe using 2D list and perform following operations.
# i) Display first 5 rows.
# ii) Count missing values in column 2nd
# data = [
#     [1, 2, 3],
#     [4, None, 6],
#     [7, 8, None],
#     [10, 11, 12],
#     [13, None, 15],
#     [16, 17, 18],
#     [19, 20, 21]
# ]
# df = pd.DataFrame(data, columns=['A','B','C'])
# df1=df.head(5)
# print(df)
# print("\nFirst 5 rows of the DataFrame:")
# print(df1)

# print("missing value")
# ms_value = df['B'].isna().sum()
# ms_value1 = df['C'].isna().sum()
# print(ms_value)
# print(ms_value1)

# Displaying the DataFrame



# Create dataframe using three series having size 10. series are account number, name and balance.

# account_number = pd.Series([1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010])
# name = pd.Series(['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack'])
# balance = pd.Series([5000.75, 1500.00, 2345.50, 3200.00, 1234.80, 7500.10, 8600.30, 2100.00, 4750.25, 5600.55])

# df = pd.DataFrame({
#     'account_number': account_number,
#     'name':name,
#     'balance':balance
# })
# print(df)

# Given a dataFrame df in Pandas as below: [4]
# City MaxTemp MinTemp RainFall
# Delhi 40 32 24.1
# Bengaluru 31 25 36.2
# Chennai 35 27 40.8
# Mumbai 29 21 35.2
# Kolkata 39 23 41.8
# Write commands:
# i) to compute sum of every column of the dateFrame.
# ii) to compute mean of column rainFall.
# iii) to compute Median of the MaxTemp column.
# iv) to display all column names
# data = {
#     'City': ['Delhi', 'Bengaluru', 'Chennai', 'Mumbai', 'Kolkata'],
#     'MaxTemp': [40, 31, 35, 29, 39],
#     'MinTemp': [32, 25, 27, 21, 23],
#     'RainFall': [24.1, 36.2, 40.8, 35.2, 41.8]
# }
# df = pd.DataFrame(data)
# print(df)

# column_sums = df.sum(numeric_only=True)
# print("\nSum of every column:")
# print(column_sums)

# rainfall_mean = df['RainFall'].mean()
# print("\nMean of RainFall column:")
# print(rainfall_mean)

# maxtemp_median = df['MaxTemp'].median()
# print("\nMedian of MaxTemp column:")
# print(maxtemp_median)

# column_names = df.columns.tolist()
# print("\nColumn names:")
# print(column_names)

# Create the DataFrame
data = {
    'ID': [1001, 1002, 1003],
    'Name': ['Mohan', 'Sachin', 'Virat'],
    'HRA': [12000, 13000, 11000],
    'TA': [6000, 5000, 4000],
    'DA': [10000, 9000, 8000]
}

df = pd.DataFrame(data)

# i) Compute sum of each column
column_sums = df.sum()

# ii) Compute mean of each integer column
integer_columns_mean = df.select_dtypes(include='int64').mean()

# iii) Compute median of each integer column
integer_columns_median = df.select_dtypes(include='int64').median()

print("Sum of each column:")
print(column_sums)
print("\nMean of each integer column:")
print(integer_columns_mean)
print("\nMedian of each integer column:")
print(integer_columns_median)