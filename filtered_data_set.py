import pandas as pd


def filter_dataset():
    # Read the CSV file
    data = pd.read_csv('salaries.csv')

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
        r'.*Machine Learning.*': 'Machine Learning Engineer',
        r'.*.*': 'Other'
    }

    # Apply job title mapping to create a new column 'job_group'
    data['job_group'] = data['job_title'].replace(title_mapping, regex=True)

    job_title_counts = data['job_title'].value_counts()
    total_jobs = len(data)
    job_title_percentages = job_title_counts / total_jobs * 100

    filtered_data = data[data['job_title'].isin(job_title_percentages[job_title_percentages >= 1].index)]
    filtered_data = filtered_data[filtered_data['employment_type'] == 'FT']

    return filtered_data
