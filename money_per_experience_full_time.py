import pandas as pd
import matplotlib.pyplot as plt

from filtered_data_set import us_filtered_data


def money_per_experience_full_time_plot(data, filename, title='ai-jobs.net'):
    plt.figure()

    mapping = {
        "SE": "Senior",
        "EX": "Executive",
        "EN": "Entry-level",
        "MI": "Mid-level"
    }

    # Map the values in the "experience_level" column to the desired names
    data['experience_level'] = data['experience_level'].map(mapping)


    # Define the desired order of experience levels
    experience_order = ['Entry-level', 'Mid-level', 'Senior', 'Executive']

    # Group the data by year, experience level, and calculate the average salary
    grouped_data = data.groupby(['work_year', 'experience_level'])['salary_in_usd'].mean().unstack()

    # Reorder the columns based on the desired experience level order
    grouped_data = grouped_data[experience_order]

    # Create the bar graph
    ax = grouped_data.plot(kind='bar')

    # Set the labels and title
    plt.xlabel('Year')
    plt.ylabel('Average Salary')
    plt.title(title, fontsize=12)
    plt.suptitle('Full Time Salaries by Experience Level for Each Year', fontsize=15, fontweight='bold')  # Adjust fontsize, fontweight, and y position as needed

    # Add labels for the bars
    for i, column in enumerate(grouped_data.columns):
        for j, value in enumerate(grouped_data[column]):
            try:
                bar_color = ax.patches[j + i * len(grouped_data.columns)].get_facecolor()
                ax.annotate(f'{value:.0f}', xy=(j, value), xytext=(0, 3), textcoords='offset points',
                            ha='center', va='bottom', color=bar_color)
            except:
                print("An exception occurred")

    # Display the graph
    plt.savefig(filename, dpi=300, bbox_inches='tight')
