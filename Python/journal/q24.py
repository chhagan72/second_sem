# 24 Create the following DataFrame Sales containing year wise sales figures for five
# salespersons in INR. Use the years as column labels, and salesperson names as row labels.
# 2018 2019 2020 2021
# Kapil 110 205 177 189 Kamini 130 165 175 190 Shikhar 115 206 157 179 Mohini 118 198
# 183 169
# 1. Create the DataFrame.
# 2. Display the row labels of Sales.
# 3. Display the column labels of Sales.
# 4. Display the data types of each column of Sales.
# 5. Display the dimensions, shape, size and values of Sales
import pandas as pd

# Create the DataFrame Sales
data = {
    '2018': [110, 130, 115, 118],
    '2019': [205, 165, 206, 198],
    '2020': [177, 175, 157, 183],
    '2021': [189, 190, 179, 169]
}
salespersons = ['Kapil', 'Kamini', 'Shikhar', 'Mohini']
sales = pd.DataFrame(data, index=salespersons)

# Display the row labels of Sales
print("Row labels of Sales:")
print(sales.index)

# Display the column labels of Sales
print("\nColumn labels of Sales:")
print(sales.columns)

# Display the data types of each column of Sales
print("\nData types of each column of Sales:")
print(sales.dtypes)

# Display the dimensions, shape, size, and values of Sales
print("\nDimensions of Sales:")
print(sales.ndim)
print("\nShape of Sales:")
print(sales.shape)
print("\nSize of Sales:")
print(sales.size)
print("\nValues of Sales:")
print(sales.values)

