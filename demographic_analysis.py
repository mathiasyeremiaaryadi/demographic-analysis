#!/usr/bin/env python
# coding: utf-8

# ### DEMOGRAPHIC ANALYZER

# In[1]:


import pandas as pd
import math


# In[2]:


df = pd.read_csv('adult.data.csv')


# In[3]:


df.head()


# ### Exploration and Cleaning

# In[4]:


df.shape


# In[5]:


df.columns


# In[6]:


df.describe()


# In[7]:


df.isna().sum()


# ### How many people of each race are represented in this dataset?

# In[20]:


df_race = df.groupby('race').size().sort_values(ascending=False)
print('How many people of each race are represented in this dataset?')
print(df_race)


# ### What is the average age of men?

# In[9]:


df_men_age_avg = df[df['sex'] == 'Male']['age']
men_age_avg = df_men_age_avg.mean()
print('What is the average age of men?')
print(round(men_age_avg, 1))


# ### What is the percentage of people who have a Bachelor's degree?

# In[10]:


df_bachelors_degree = df[df['education'] == 'Bachelors']
bachelors_degree_percentage = (df_bachelors_degree.size / df.size) * 100
print("What is the percentage of people who have a Bachelor's degree?")
print('{:.2f}%'.format(bachelors_degree_percentage.item()))


# ###  What percentage of people with advanced education (Bachelors, Masters, or Doctorate) ?

# In[11]:


df_advanced_education = df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
percentage_advanced_education = (df_advanced_education.size / df.size) * 100
print('What percentage of people without advanced education ?')
print('{:.2f}%'.format(percentage_advanced_education.item()))


# ### What percentage of people without advanced education ?

# In[12]:


df_non_advanced_education = df[~((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))]
percentage_non_advanced_education = (df_non_advanced_education.size / df.size) * 100
print('What percentage of people without advanced education ?')
print('{:.2f}%'.format(percentage_non_advanced_education.item()))


# ### What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?

# In[13]:


df_advanced_education = df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
df_more_than_50 = df_advanced_education[df_advanced_education['salary'] == '>50K']
more_than_50_percentage = (df_more_than_50.size / df_advanced_education.size) * 100
print('What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?')
print('{:.2f}%'.format(more_than_50_percentage.item()))


# ### What percentage of people without advanced education make more than 50K?

# In[14]:


df_not_advanced_education = df[~((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))]
df_more_than_50 = df_not_advanced_education[df_not_advanced_education['salary'] == '>50K']
more_than_50_percentage = (df_more_than_50.size / df_not_advanced_education.size) * 100
print('What percentage of people without advanced education make more than 50K?')
print('{:.2f}%'.format(more_than_50_percentage.item()))


# ### What is the minimum number of hours a person works per week?

# In[15]:


min_hours_per_week = df['hours-per-week'].min()
print('What is the minimum number of hours a person works per week?')
print(min_hours_per_week)


# ### What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?

# In[16]:


min_hours_per_week = df['hours-per-week'].min()
df_min_hours_per_week = df[df['hours-per-week'] == min_hours_per_week]
df_salary_more_than_50 = df_min_hours_per_week[df_min_hours_per_week['salary'] == '>50K']
percentage_min_hours_per_week = (df_salary_more_than_50.size / df_min_hours_per_week.size) * 100
print('What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?')
print('{:.2f}%'.format(percentage_min_hours_per_week))


# ### What country has the highest percentage of people that earn >50K and what is that percentage?

# In[24]:


df_country_high_salary = df.groupby(['native-country', 'salary'])['salary'].agg({'count'}).unstack().reset_index()
df_country_high_salary['total'] = df_country_high_salary['count']['<=50K'] + df_country_high_salary['count']['>50K']
df_country_high_salary['percentage'] = round((df_country_high_salary['count']['>50K'] / df_country_high_salary['total']) * 100, 2)
df_country_high_salary = df_country_high_salary.sort_values('percentage', ascending=False).reset_index()
country_high_salary = df_country_high_salary['native-country'][0]
percentage_country_high_salary = round(df_country_high_salary['percentage'][0], 1)
print('What country has the highest percentage of people that earn >50K and what is that percentage?')
print('{:s}, the percentage is {:.2f}%'.format(country_high_salary, percentage_country_high_salary))


# ### Identify the most popular occupation for those who earn >50K in India.

# In[18]:


df_india_country = df[df['native-country'] == 'India']
df_more_than_50 = df_india_country[df_india_country['salary'] == '>50K']
df_popular_occupation = df_more_than_50.groupby('occupation').size().sort_values(ascending=False)
popular_occupation = df_popular_occupation[df_popular_occupation == df_popular_occupation[0]].index[0]
print('Identify the most popular occupation for those who earn >50K in India?')
print(popular_occupation)


# In[ ]:




