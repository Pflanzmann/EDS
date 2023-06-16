import pandas as pd
import re
import matplotlib.pyplot as plt

from filtered_data_set import filtered_data_with_others

# Read the CSV file
data = filtered_data_with_others()

# Calculate the job title percentages
job_title_counts = data['job_title'].value_counts()
total_jobs = len(data)
job_title_percentages = job_title_counts / total_jobs * 100

filtered_job_titles = job_title_percentages[job_title_percentages >= 1]

# Sort job titles by percentage in descending order
sorted_job_titles = filtered_job_titles.sort_values(ascending=False)

# Calculate the percentage labels for the pie chart
percent_labels = [f'{title}' for title, percentage in zip(sorted_job_titles.index, sorted_job_titles)]

# Create the pie chart
plt.pie(sorted_job_titles, labels=percent_labels, autopct=lambda pct: f'{pct:.1f}%')

# Set the title
plt.title('Job Title Distribution')

# Display the chart
plt.show()

