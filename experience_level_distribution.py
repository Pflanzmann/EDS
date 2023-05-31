import pandas as pd
import re
import matplotlib.pyplot as plt

from filtered_data_set import filtered_data_with_others

# Read the CSV file
data = filtered_data_with_others()

# Calculate the experience level percentages
experience_counts = data['work_year'].value_counts()
total_jobs = len(data)
experience_percentages = experience_counts / total_jobs * 100

# Sort experience levels by percentage in descending order
sorted_experience_levels = experience_percentages.sort_values(ascending=False)

# Calculate the percentage labels for the pie chart
percent_labels = [f'{level}' for level, percentage in zip(sorted_experience_levels.index, sorted_experience_levels)]

# Create the pie chart
plt.pie(sorted_experience_levels, labels=percent_labels, autopct=lambda pct: f'{pct:.1f}%({pct / 100 * total_jobs:.0f})')

# Set the title
plt.title('Experience Level Distribution')

# Display the chart
plt.show()