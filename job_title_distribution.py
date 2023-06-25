import pandas as pd
import re
import matplotlib.pyplot as plt


def save_job_title_distribution_plot(data, filename, title='ai-jobs.net'):
    plt.figure()

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
    plt.title(title, fontsize=12)
    plt.suptitle('Job Title Distribution', fontsize=15,
                 fontweight='bold')  # Adjust fontsize, fontweight, and y position as needed

    # Save the chart as PNG file
    plt.savefig(filename, dpi=300, bbox_inches='tight')
