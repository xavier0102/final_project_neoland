#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 07:36:01 2019

@author: jaketoruk
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

df_user = pd.read_csv('/home/jaketoruk/Documents/Kaggle_Competition/airbnb/airbnb-recruiting-new-user-bookings/train_users_2.csv', parse_dates=['date_first_booking', 'date_account_created', 'timestamp_first_active'])

pd.options.display.max_columns = 50

df_user.head()
df_user.isnull().sum()
y_user = df_user['country_destination']
df_user = df_user.drop(['country_destination', 'id'], axis = 1)

df_user['age'].value_counts()

plt.scatter(df_user['age'], y_user)
plt.xlabel('age')
plt.ylabel('destination')

for column in df_user.columns:
    plt.scatter(df_user[column], y_user)
    plt.xlabel(column)
    plt.ylabel('destination')
    
    