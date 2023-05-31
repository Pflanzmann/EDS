import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('salaries.csv')

# Calculate the employment type counts
employment_type_counts = data['employment_type'].value_counts()

# Create the pie chart
plt.pie(employment_type_counts, labels=employment_type_counts.index, autopct='%1.1f%%')

# Set the title
plt.title('Employment Type Distribution')

# Display the chart
plt.show()
