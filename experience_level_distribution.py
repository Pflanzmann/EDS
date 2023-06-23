import pandas as pd
import re
import matplotlib.pyplot as plt


def save_experience_distribution_plot(data, filename):
    plt.figure()

    # Calculate the experience level percentages
    experience_counts = data['experience_level'].value_counts()
    total_jobs = len(data)
    experience_percentages = experience_counts / total_jobs * 100

    # Sort experience levels by percentage in descending order
    sorted_experience_levels = experience_percentages.sort_values(ascending=False)

    # Calculate the percentage labels for the pie chart
    percent_labels = [f'{level}' for level, percentage in zip(sorted_experience_levels.index, sorted_experience_levels)]

    # Create the pie chart
    plt.pie(sorted_experience_levels, labels=percent_labels, autopct=lambda pct: f'{pct:.1f}%')

    # Set the title and subtitle
    plt.title('ai-jobs.net', fontsize=12)
    plt.suptitle('Experience Level Distribution', fontsize=15, fontweight='bold')  # Adjust fontsize, fontweight, and y position as needed

    # Save the chart as PNG file
    plt.savefig(filename, dpi=300, bbox_inches='tight')
