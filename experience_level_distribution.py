import pandas as pd
import matplotlib.pyplot as plt


def save_experience_distribution_plot(data, filename, title='ai-jobs.net'):
    plt.figure()

    # Calculate the experience level percentages
    experience_counts = data['experience_level'].value_counts()
    total_jobs = len(data)
    experience_percentages = experience_counts / total_jobs * 100

    # Sort experience levels by percentage in descending order
    sorted_experience_levels = experience_percentages.sort_values(ascending=False)

    # Define the mapping for experience level categories
    mapping = {
        "SE": "Senior",
        "EX": "Executive",
        "EN": "Entry-level",
        "MI": "Mid-level"
    }

    # Map the experience level categories to the desired labels
    percent_labels = [mapping.get(level, level) for level in sorted_experience_levels.index]

    # Create the pie chart
    plt.pie(sorted_experience_levels, labels=percent_labels, autopct=lambda pct: f'{pct:.1f}%')

    # Set the title and subtitle
    plt.title(title, fontsize=12)
    plt.suptitle('Experience Level Distribution', fontsize=15, fontweight='bold')  # Adjust fontsize, fontweight, and y position as needed

    # Save the chart as PNG file
    plt.savefig(filename, dpi=300, bbox_inches='tight')

