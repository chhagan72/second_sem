import pandas as pd
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
data = pd.DataFrame(mydataset)
print(data)


print(pd.__version__)