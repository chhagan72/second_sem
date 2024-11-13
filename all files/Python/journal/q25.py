# Plot the following data on a line chart and customize the chart according to the belowgiven instructions:
# Month January February March April May Sales 510 350 475 580 600 Weekly Sales Report
# 1. Write a title for the chart “The Monthly Sales Report“
# 2. Write the appropriate titles of both the axes
# 3. Write code to Display legends
# 4. Display blue color for the line
# 5. Use the line style – dashed
# 6. Display diamond style markers on data points
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May']
sales = [510, 350, 475, 580, 600]

# Plot the data
plt.plot(months, sales, color='blue', linestyle='--', marker='D', markersize=8, label='Sales')

# Customize the chart
plt.title('The Monthly Sales Report')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()

# Display the chart
plt.show()
