import pandas as pd
import re
import matplotlib.pyplot as plt
from adjustText import adjust_text

from filtered_data_set import filtered_data

filtered_data = filtered_data()

# Calculate the average salary for each year and job title
avg_salary = filtered_data.groupby(['work_year', 'job_title'])['salary_in_usd'].mean().unstack()

# Calculate the salary increase per year for each job title
salary_increase = avg_salary.diff()

# Remove the first row (NaN values) as there's no previous year to compare with
salary_increase = salary_increase.iloc[1:]

# Filter out the points with a salary increase of 0
salary_increase_nonzero = salary_increase.replace(0, float('nan')).dropna(how='all')

# Sort the salary increase dataframe by index (year)
salary_increase_nonzero.sort_index(inplace=True)

# Create a scatter plot for each job title and get the corresponding color
scatter_plots = []
labels = []
for i, job_title in enumerate(salary_increase_nonzero.columns):
    scatter = plt.scatter(salary_increase_nonzero.index, salary_increase_nonzero[job_title], label=job_title)
    scatter_plots.append(scatter)
    # Add labels on each point with the associated numbers, colored to match the job dots
    for j, value in enumerate(salary_increase_nonzero[job_title]):
        label = plt.text(salary_increase_nonzero.index[j], value, f'{value:.0f}',
                         color=plt.rcParams['axes.prop_cycle'].by_key()['color'][i])
        labels.append(label)

# Set the labels and title
plt.xlabel('Year', fontsize=14)
plt.ylabel('Salary Increase (USD)', fontsize=14)
plt.title('Salary Increase per Year by Job Title', fontsize=16)

# Set the X-axis ticks to one year intervals
plt.xticks(range(min(salary_increase_nonzero.index), max(salary_increase_nonzero.index) + 1, 1), fontsize=10)

# Adjust the positions of labels to avoid overlaps
adjust_text(labels)

# Create a legend with scatter plots
plt.legend(scatter_plots, [scatter.get_label() for scatter in scatter_plots])

# Display the chart
plt.show()
