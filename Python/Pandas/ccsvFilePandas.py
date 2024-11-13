import pandas as pd

# csv = pd.read_csv(r'data.csv')
# print(csv)
# print(csv.to_string())


# max_rows
# The number of rows returned is defined in Pandas option settings.
# You can check your system's maximum rows with the "pd.options.display.max_rows" statement.
pd.options.display.max_rows=9999
csv = pd.read_csv(r'data.csv')
print(csv)