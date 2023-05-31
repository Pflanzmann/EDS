import pandas as pd
import re
import matplotlib.pyplot as plt

from filtered_data_set import filter_dataset

filtered_data = filter_dataset()

# Calculate the average salary for each year and job title
avg_salary = filtered_data.groupby(['work_year', 'job_title'])['salary_in_usd'].mean().unstack()

# Calculate the salary increase per year for each job title
salary_increase = avg_salary.pct_change() * 100

# Remove the first row (NaN values) as there's no previous year to compare with
salary_increase = salary_increase.iloc[1:]

# Add the year 2020 as a starting point with 0% salary increase
salary_increase.loc[2020] = 0

# Sort the salary increase dataframe by index (year)
salary_increase.sort_index(inplace=True)

# Plot the salary increase for each job title
for job_title in salary_increase.columns:
    plt.plot(salary_increase.index, salary_increase[job_title], label=job_title)

# Set the labels and title
plt.xlabel('Year')
plt.ylabel('Salary Increase (%)')
plt.title('Salary Increase per Year by Job Title')
plt.legend()

# Set the X-axis ticks to one year intervals
plt.xticks(range(min(salary_increase.index), max(salary_increase.index)+1, 1))

# Display the chart
plt.show()
