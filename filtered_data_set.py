import pandas as pd
import re


def getNonUs():
    data = pd.read_csv('datensatz-Stichprobe.csv')
    data2 = pd.read_csv('salaries.with_salaries_only.csv')

    data2 = data2.rename(
        columns={'work_year': 'work_year', 'experience_level': 'experience_level', 'employment_type': 'employment_type',
                 'job_title': 'job_title', 'salary': 'salary', 'salary_currency': 'salary_currency',
                 'salary_in_usd': 'salary_in_usd', 'employee_residence': 'filename', 'remote_ratio': 'remote_ratio',
                 'company_location': 'company_location', 'company_size': 'company_size'})

    merged_df = pd.concat([data, data2])
    merged_df = merged_df.reset_index(drop=True)

    merged_df.to_csv('merged_file.csv', index=False)

    return pd.read_csv('merged_file.csv')


def getUs():
    data = pd.read_csv('salaries.csv')
    return data


def filtered_data():
    data = getNonUs()

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

    data['job_title'] = data['job_title'].apply(
        lambda x: next((val for pattern, val in title_mapping.items() if re.match(pattern, x)), x))

    job_title_counts = data['job_title'].value_counts()
    total_jobs = len(data)
    job_title_percentages = job_title_counts / total_jobs * 100

    filtered_data = data[data['job_title'].isin(job_title_percentages[job_title_percentages >= 1].index)]
    filtered_data = filtered_data[filtered_data['employment_type'] == 'FT']
    #filtered_data = filtered_data[filtered_data['company_location'] == 'US']

    filtered_data.to_csv('filtered_salaries.csv', index=False)

    return filtered_data


def filtered_data_with_others():
    data = getNonUs()

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

    data['job_title'] = data['job_title'].apply(
        lambda x: next((val for pattern, val in title_mapping.items() if re.match(pattern, x)), 'Others'))

    job_title_counts = data['job_title'].value_counts()
    total_jobs = len(data)
    job_title_percentages = job_title_counts / total_jobs * 100

    filtered_data = data[data['job_title'].isin(job_title_percentages[job_title_percentages >= 1].index)]
    filtered_data = filtered_data[filtered_data['employment_type'] == 'FT']
    #filtered_data = filtered_data[filtered_data['company_location'] == 'US']

    filtered_data.to_csv('filtered_salaries.csv', index=False)

    return filtered_data
