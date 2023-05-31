import pandas as pd
import re
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('salaries.csv')

# Calculate the job title percentages
job_title_counts = data['job_title'].value_counts()
total_jobs = len(data)
job_title_percentages = job_title_counts / total_jobs * 100

# Define a dictionary to map similar job titles to the desired group
title_mapping = {
    r'.*Learning.*': 'Machine Learning Engineer',
    r'.*Data Scientist.*': 'Data Scientist',
    r'.*Data Science.*': 'Data Scientist',
    r'.*Data Engineer.*': 'Data Engineer',
    r'.*Data Architect.*': 'Data Architect',
    r'.*Data Analyst.*': 'Data Analyst',
    r'.*Analy.*': 'Data Analyst',
    r'.*Manager.*': 'Data Science Manager',
    r'.*Lead.*': 'Data Science Manager',
    r'.*Head.*': 'Data Science Manager',
    r'.*ML.*': 'Machine Learning Engineer',
    r'.*Machine Learning.*': 'Machine Learning Engineer'
}

# Group similar job titles together based on the mapping dictionary
grouped_job_titles = job_title_percentages.rename(index=lambda x: next((val for pattern, val in title_mapping.items() if re.match(pattern, x)), x))

# Group job titles and sum their percentages
grouped_job_titles = grouped_job_titles.groupby(grouped_job_titles.index).sum()

# Filter job titles above 1% presence
filtered_job_titles = grouped_job_titles[grouped_job_titles >= 1]

# Group the remaining job titles as "Others"
other_percentage = grouped_job_titles[grouped_job_titles < 1].sum()
filtered_job_titles['Others'] = other_percentage

# Sort job titles by percentage in descending order
sorted_job_titles = filtered_job_titles.sort_values(ascending=False)

# Calculate the percentage labels for the pie chart
percent_labels = [f'{title}' for title, percentage in zip(sorted_job_titles.index, sorted_job_titles)]

# Create the pie chart
plt.pie(sorted_job_titles, labels=percent_labels, autopct=lambda pct: f'{pct:.1f}%({pct / 100 * total_jobs:.0f})')

# Set the title
plt.title('Job Title Distribution')

# Get the job titles in "Others"
others_job_titles = grouped_job_titles[grouped_job_titles < 1].index.tolist()

# Print the job titles in "Others"
print("Job Titles in 'Others':")
for job_title in others_job_titles:
    print(f"{job_title} ({job_title_counts[job_title]})")


# Display the chart
plt.show()

