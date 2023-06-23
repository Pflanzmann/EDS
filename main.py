import pandas as pd
import re
import matplotlib.pyplot as plt

from filtered_data_set import *
from experience_level_distribution import save_experience_distribution_plot
from job_title_distribution import save_job_title_distribution_plot
from money_per_experience_full_time import money_per_experience_full_time_plot
from salary_increase_absolut_numbers_line import save_salary_increase_absolut_numbers_line_plot
from salary_increase_absolut_numbers_scatter import save_salary_increase_absolut_numbers_scatter_plot
from salary_increase_percentage_lines import save_salary_increase_percentage_lines_plot

data = us_filtered_data_with_others()
filename = 'pngs/us_experience_distribution.png'
save_experience_distribution_plot(data, filename)

data = non_us_filtered_data_with_others()
filename = 'pngs/non_us_experience_distribution.png'
save_experience_distribution_plot(data, filename)

data = us_filtered_data_with_others()
filename = 'pngs/us_job_title_distribution.png'
save_job_title_distribution_plot(data, filename)

data = non_us_filtered_data_with_others()
filename = 'pngs/non_us_job_title_distribution.png'
save_job_title_distribution_plot(data, filename)

data = us_filtered_data()
filename = 'pngs/us_money_per_experience_full_time.png'
money_per_experience_full_time_plot(data, filename)

data = non_us_filtered_data()
filename = 'pngs/non_us_money_per_experience_full_time.png'
money_per_experience_full_time_plot(data, filename)

data = us_filtered_data_with_others()
filename = 'pngs/us_salary_increase_absolut_numbers_line.png'
save_salary_increase_absolut_numbers_line_plot(data, filename)

data = non_us_filtered_data_with_others()
filename = 'pngs/non_us_salary_increase_absolut_numbers_line.png'
save_salary_increase_absolut_numbers_line_plot(data, filename)

data = us_filtered_data_with_others()
filename = 'pngs/us_salary_increase_absolut_numbers_scatter.png'
save_salary_increase_absolut_numbers_scatter_plot(data, filename)

data = non_us_filtered_data_with_others()
filename = 'pngs/non_us_salary_increase_absolut_numbers_scatter.png'
save_salary_increase_absolut_numbers_scatter_plot(data, filename)

data = us_filtered_data_with_others()
filename = 'pngs/us_salary_increase_percentage_lines.png'
save_salary_increase_percentage_lines_plot(data, filename)

data = non_us_filtered_data_with_others()
filename = 'pngs/non_us_salary_increase_percentage_lines.png'
save_salary_increase_percentage_lines_plot(data, filename)

data = us_filtered_data_with_others()
filename = 'pngs/us_salary_increase_percentage_scatter.png'
save_salary_increase_absolut_numbers_line_plot(data, filename)

data = non_us_filtered_data_with_others()
filename = 'pngs/non_us_salary_increase_percentage_scatter.png'
save_salary_increase_absolut_numbers_line_plot(data, filename)

