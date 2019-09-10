#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:09:04 2019

@author: jaketoruk
"""
import seaborn as sns
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib .pyplot as plt
import datetime

pd.options.display.max_columns = 50
pd.options.display.max_rows = 200

df_user2 = pd.read_csv('/home/jaketoruk/Documents/Kaggle_Competition/airbnb/DataBase/airbnb-recruiting-new-user-bookings/train_users_2.csv', parse_dates=['date_first_booking', 'date_account_created', 'timestamp_first_active'])

df_user2['user_id'] = df_user2['id'] 
df_user2 = df_user2.drop(['id'], axis = 1)

df_user2['timestamp_f_menus_create_account'] = df_user2['date_account_created'] - df_user2['timestamp_first_active']

df_user2['timestamp_f_menus_create_account'] = df_user2['timestamp_f_menus_create_account'].dt.total_seconds()

df_user2['age'] = np.where(df_user2['age'] > 120, np.NaN, df_user2['age'])

df_user2['age'] = df_user2['age'].fillna(df_user2['age'].mean()) 

df_user2['country_destination'].value_counts()
df_user2['country_destination'] = np.where(df_user2['country_destination'] == 'NDF', 0, 1)

df_user2 = df_user2.drop(['language', 'first_affiliate_tracked', 'date_first_booking'], axis = 1)

df_user2.isnull().sum()

# =============================================================================
# 
# =============================================================================

df_seccion2 = pd.read_csv('/home/jaketoruk/Documents/Kaggle_Competition/airbnb/DataBase/airbnb-recruiting-new-user-bookings/sessions.csv')

df_seccion2['action'] = df_seccion2['action'].fillna('other_action')

df_seccion2['freq_act'] = df_seccion2.groupby(['user_id', 'action'])['action'].transform('count')

df_seccion2['action_type'].value_counts()
df_seccion2['action_type'] = df_seccion2['action_type'].fillna('-unknown-')

df_seccion2['action_detail'] = df_seccion2['action_detail'].fillna('other_action_detail')

df_seccion2['freq_act_detail'] = df_seccion2.groupby(['user_id', 'action_detail'])['action_detail'].transform('count')

df_seccion2['device_type'].value_counts()
df_seccion2['device_type'] = df_seccion2['device_type'].fillna('-unknown-')

df_seccion2.secs_elapsed = df_seccion2.secs_elapsed.fillna(0)

#Para hacer el conteo de forma más eficiente
df_seccion2['count'] = 1
df_seccion2["count_secc"] = df_seccion2.groupby("user_id").cumcount() + 1

df_seccion2 = df_seccion2.dropna()

df_seccion2.isnull().sum()



# =============================================================================
# 
# =============================================================================

result = pd.merge(df_seccion2, df_user2, how= 'left', on = 'user_id')

result.shape
result = result.dropna()
result.isnull().sum()

result.head()


sns.set_style('ticks') 
fig, ax = plt.subplots()
fig.set_size_inches(11.7, 8.27)
sns.countplot(x='action', hue='country_destination',data=result.loc[result['freq_act']>200])
plt.xlabel(' {0} based on Destination Country'.format('action'))
plt.ylabel('Number of users')
sns.despine()



action = result[['action','country_destination']]
action=action.dropna()

action_final = action.groupby('action', as_index=False).agg({'country_destination': [np.mean,np.sum]})
action_final.columns = (['action','mean', 'sum'])

action_bajo = list(action_final.loc[action_final['mean']<=0.1,'action'])

action_medio_bajo = list(action_final.loc[(action_final['mean']>0.1) & (action_final['mean']<= 0.3),'action'])

action_medio_bajo = list(action_final.loc[(action_final['mean']>0.3) & (action_final['mean']<= 0.5),'action'])

action_alto= list(action_final.loc[action_final['mean']>0.5,'action'])






