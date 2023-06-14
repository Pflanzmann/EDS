import pandas as pd
import re

def filtered_data():
    # Read the CSV file
    #data = pd.read_csv('datensatz-Stichprobe.csv')
    data = pd.read_csv('salaries.csv')

    # Define a dictionary to map similar job titles to the desired group
    title_mapping = {
        r'.*Learning.*': 'Machine Learning Engineer',
        r'.*Data Scientist.*': 'Data Scientist',
        r'.*Data Science.*': 'Data Scientist',
        r'.*Applied Scientist.*': 'Applied Scientist',
        r'.*Data Engineer.*': 'Data Engineer',
        r'.*Research Engineer.*': 'Research Engineer',
        r'.*Research Scientist.*': 'Research Scientist',
        r'.*Data Architect.*': 'Data Architect',
        r'.*Data Analyst.*': 'Data Analyst',
        r'.*Analy.*': 'Data Analyst',
        r'.*Manager.*': 'Data Science Manager',
        r'.*Lead.*': 'Data Science Manager',
        r'.*Head.*': 'Data Science Manager',
        r'.*ML.*': 'Machine Learning Engineer',
        r'.*ML Engineer.*': 'Machine Learning Engineer',
        r'.*Machine Learning.*': 'Machine Learning Engineer',
    }

    data['job_title'] = data['job_title'].apply(lambda x: next((val for pattern, val in title_mapping.items() if re.match(pattern, x)), x))

    job_title_counts = data['job_title'].value_counts()
    total_jobs = len(data)
    job_title_percentages = job_title_counts / total_jobs * 100

    filtered_data = data[data['job_title'].isin(job_title_percentages[job_title_percentages >= 1].index)]
    filtered_data = filtered_data[filtered_data['employment_type'] == 'FT']
    filtered_data = filtered_data[filtered_data['company_location'] == 'US']

    filtered_data.to_csv('filtered_salaries.csv', index=False)

    return filtered_data


def filtered_data_with_others():
    # Read the CSV file
    #data = pd.read_csv('datensatz-Stichprobe.csv')
    data = pd.read_csv('salaries.csv')

    # Define a dictionary to map similar job titles to the desired group
    title_mapping = {
        r'.*Learning.*': 'Machine Learning Engineer',
        r'.*Data Scientist.*': 'Data Scientist',
        r'.*Data Science.*': 'Data Scientist',
        r'.*Applied Scientist.*': 'Applied Scientist',
        r'.*Data Engineer.*': 'Data Engineer',
        r'.*Research Engineer.*': 'Research Engineer',
        r'.*Research Scientist.*': 'Research Scientist',
        r'.*Data Architect.*': 'Data Architect',
        r'.*Data Analyst.*': 'Data Analyst',
        r'.*Analy.*': 'Data Analyst',
        r'.*Manager.*': 'Data Science Manager',
        r'.*Lead.*': 'Data Science Manager',
        r'.*Head.*': 'Data Science Manager',
        r'.*ML.*': 'Machine Learning Engineer',
        r'.*ML Engineer.*': 'Machine Learning Engineer',
        r'.*Machine Learning.*': 'Machine Learning Engineer',
    }

    data['job_title'] = data['job_title'].apply(lambda x: next((val for pattern, val in title_mapping.items() if re.match(pattern, x)), 'Others'))

    job_title_counts = data['job_title'].value_counts()
    total_jobs = len(data)
    job_title_percentages = job_title_counts / total_jobs * 100

    filtered_data = data[data['job_title'].isin(job_title_percentages[job_title_percentages >= 1].index)]
    filtered_data = filtered_data[filtered_data['employment_type'] == 'FT']
    filtered_data = filtered_data[filtered_data['company_location'] == 'US']

    filtered_data.to_csv('filtered_salaries.csv', index=False)

    return filtered_data
