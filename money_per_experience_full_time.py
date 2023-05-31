import pandas as pd
import matplotlib.pyplot as plt

from filtered_data_set import filtered_data

filtered_data = filtered_data()

# Define the desired order of experience levels
experience_order = ['EN', 'MI', 'SE', 'EX']

# Group the data by year, experience level, and calculate the average salary
grouped_data = filtered_data.groupby(['work_year', 'experience_level'])['salary_in_usd'].mean().unstack()

# Reorder the columns based on the desired experience level order
grouped_data = grouped_data[experience_order]

# Create the bar graph
grouped_data.plot(kind='bar')

# Set the labels and title
plt.xlabel('Year')
plt.ylabel('Average Salary')
plt.title('Full Time Salaries by Experience Level for Each Year')

# Display the graph
plt.show()