import pandas as pd
import re
import matplotlib.pyplot as plt
from adjustText import adjust_text

def save_salary_increase_percentage_lines_plot(data, filename):
    plt.figure()

    # Calculate the average salary for each year and job title
    avg_salary = data.groupby(['work_year', 'job_title'])['salary_in_usd'].mean().unstack()

    # Calculate the salary increase percentage per year for each job title
    salary_increase_percentage = avg_salary.pct_change().iloc[1:] * 100

    # Create a line plot for each job title and get the corresponding color
    lines = []
    labels = []
    for i, job_title in enumerate(salary_increase_percentage.columns):
        line, = plt.plot(salary_increase_percentage.index, salary_increase_percentage[job_title], marker='o',
                         label=job_title)
        lines.append(line)
        # Add labels on each point with the associated percentage increase, colored to match the job dots
        for j, value in enumerate(salary_increase_percentage[job_title]):
            label = plt.text(salary_increase_percentage.index[j], value, f'{value:.2f}%', color=line.get_color())
            labels.append(label)

    # Set the labels and title
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Salary Increase Percentage', fontsize=14)
    plt.title('ai-jobs.net', fontsize=12)
    plt.suptitle('Salary Increase Percentage per Year by Job Title', fontsize=15,
                 fontweight='bold')  # Adjust fontsize, fontweight, and y position as needed

    # Set the X-axis ticks to one year intervals
    plt.xticks(range(min(salary_increase_percentage.index), max(salary_increase_percentage.index) + 1, 1), fontsize=10)

    # Adjust the positions of labels to avoid overlaps
    adjust_text(labels)

    # Create a legend with line plots
    plt.legend(lines, [line.get_label() for line in lines])

    # Save the chart as PNG file
    plt.savefig(filename, dpi=300, bbox_inches='tight')
