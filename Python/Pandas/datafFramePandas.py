# What is a DataFrame

import pandas as pd

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# a=pd.DataFrame(data)
# print(a)

# Locate Row
# As you can see from the result above, the DataFrame is like a table with rows and columns.
# Pandas use the loc attribute to return one or more specified row(s)
# print(a.loc[0])

# Return row 0 and 2
# print(a.loc[[0,2]])

# Named Indexes
# With the index argument, you can name your own indexes.

# b=pd.DataFrame(data, index=['day1','day2','day3'])
# print(b)

# Locate Named Indexes
# Use the named index in the "loc" attribute to return the specified row(s)

# print(b.loc[['day1','day3']])

# Load Files Into a DataFrame
# If your data sets are stored in a file, Pandas can load them into a DataFrame.

c=pd.read_csv(r'C:\Users\Chhagan\Desktop\MCA SEM-II\Python\Pandas\data.csv')
print(c)

