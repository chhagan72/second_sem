import pandas as pd



# Empty Cells
a = pd.read_csv(r'data.csv')
# print(a)

# b = a.dropna()
# print(b)
# print(b.to_string())


# If you want to change the original DataFrame, use the inplace = True argument

a.dropna(inplace=True)
print(a.to_string())



