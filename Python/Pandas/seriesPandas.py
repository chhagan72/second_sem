import pandas as pd

# a=[1,2,3,4,5]
# b=pd.Series(a)
# print(b)

# Return the first value of the Series
# print(b[0])

# Create Labels
# a=[1,2,3,4,5]
# b=pd.Series(a, index=['A','B','C','D','E'])
# print(b)

# Return the value of "C"
# print(b['C'])

# Key/Value Objects as Series
# calories = {"day1": 420, "day2": 380, "day3": 390}
# b=pd.Series(calories)
# print(b)

# Create a Series using only data from "day1" and "day2"
# calories = {"day1": 420, "day2": 380, "day3": 390}
# b=pd.Series(calories, index=['day1','day2'])
# print(b)

# Create a DataFrame from two Series
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
a=pd.DataFrame(data)
print(a)
