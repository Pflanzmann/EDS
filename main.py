import pandas as pd
import re
import matplotlib.pyplot as plt

from filtered_data_set import filtered_data

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
