#  Observe following data and plot data according to given instructions:
# Batsman 2017 2018 2019 2020 Virat Kohli 2501 1855 2203 1223 Steve Smith 2340 2250 2003
# 1153 Babar Azam 1750 2147 1896 1008 Rohit Sharma 1463 1985 1854 1638 Kane Williamson
# 1256 1785 1874 1974 Jos Butler 1125 1853 1769 1436
# 1. Create a bar chart to display data of Virat Kohli & Rohit Sharma.
# 2. Customize the chart in this manner
# 1. Use different widths
# 2. Use different colors to represent different years score
# 3. Display appropriate titles for axis and chart
# 4. Show legends
# 5. Create a bar chart to display data of Steve Smith, Kane Williamson & Jos Butler.
# Customize Chart as per your wish.
# 6. Display data of all players for the specific year. 
import matplotlib.pyplot as plt

# Data
batsmen = ['Virat Kohli', 'Steve Smith', 'Babar Azam', 'Rohit Sharma', 'Kane Williamson', 'Jos Butler']
years = ['2017', '2018', '2019', '2020']
scores = {
    'Virat Kohli': [2501, 1855, 2203, 1223],
    'Steve Smith': [2340, 2250, 2003, 1153],
    'Babar Azam': [1750, 2147, 1896, 1008],
    'Rohit Sharma': [1463, 1985, 1854, 1638],
    'Kane Williamson': [1256, 1785, 1874, 1974],
    'Jos Butler': [1125, 1853, 1769, 1436]
}

# Plot for Virat Kohli & Rohit Sharma
plt.figure(figsize=(10, 6))  # Set the figure size

for i, (batsman, color) in enumerate(zip(['Virat Kohli', 'Rohit Sharma'], ['blue', 'orange'])):
    plt.bar([x + i * 0.2 for x in range(len(years))], scores[batsman], width=0.2, color=color, label=batsman)

plt.title('Virat Kohli & Rohit Sharma - Yearly Scores')
plt.xlabel('Year')
plt.ylabel('Score')
plt.xticks(range(len(years)), years)
plt.legend()
plt.show()

# Plot for Steve Smith, Kane Williamson & Jos Butler
plt.figure(figsize=(10, 6))  # Set the figure size

for i, batsman in enumerate(['Steve Smith', 'Kane Williamson', 'Jos Butler']):
    plt.bar([x + i * 0.2 for x in range(len(years))], scores[batsman], width=0.2, label=batsman)

plt.title('Steve Smith, Kane Williamson & Jos Butler - Yearly Scores')
plt.xlabel('Year')
plt.ylabel('Score')
plt.xticks(range(len(years)), years)
plt.legend()
plt.show()

# Display data of all players for the specific year (e.g., 2019)
year = '2019'
plt.figure(figsize=(10, 6))  # Set the figure size

for batsman in batsmen:
    plt.bar(batsman, scores[batsman][years.index(year)], label=batsman)

plt.title(f'Yearly Scores of All Players in {year}')
plt.xlabel('Batsmen')
plt.ylabel('Score')
plt.legend()
plt.xticks(rotation=45)
plt.show()
