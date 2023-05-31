import pandas as pd
import re
import matplotlib.pyplot as plt

from filtered_data_set import filtered_data

filtered_data = filtered_data()

# Calculate the average salary for each year and job title
avg_salary = filtered_data.groupby(['work_year', 'job_title'])['salary_in_usd'].mean().unstack()

# Calculate the salary increase per year for each job title
salary_increase = avg_salary.diff()

# Remove the first row (NaN values) as there's no previous year to compare with
salary_increase = salary_increase.iloc[1:]

# Add the year 2020 as a starting point with 0 salary increase
salary_increase.loc[2020] = 0

# Sort the salary increase dataframe by index (year)
salary_increase.sort_index(inplace=True)

# Get the years and job titles
years = salary_increase.index
job_titles = salary_increase.columns

# Set the width of each bar
bar_width = 0.35

# Set the position of each bar on the x-axis
bar_positions = range(len(years))

# Create the bar chart
for i, job_title in enumerate(job_titles):
    plt.bar(0 + (i * bar_width), salary_increase[job_title], bar_width, label=job_title)

# Set the labels and title
plt.xlabel('Year')
plt.ylabel('Salary Increase (USD)')
plt.title('Salary Increase per Year by Job Title')
plt.xticks(bar_positions, years)
plt.legend()

# Display the chart
plt.show()
