import matplotlib.pyplot as plt

# Given data
overs = [5, 10, 15, 20]
runs = [45, 79, 145, 234]

# Calculate the run rate
run_rate = [runs[i] / overs[i] for i in range(len(overs))]

# Plotting the line chart
plt.plot(overs, run_rate, marker='o', linestyle='-')
plt.title('Run Rate in T20 Match')
plt.xlabel('Overs')
plt.ylabel('Run Rate')
plt.grid(True)
plt.show()
