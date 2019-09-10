#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:00:31 2019

@author: jaketoruk
"""
import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


df_seccion2 = pd.read_csv('/home/jaketoruk/Documents/Kaggle_Competition/airbnb/DataBase/airbnb-recruiting-new-user-bookings/sessions.csv')

pd.options.display.max_columns = 50
pd.options.display.max_rows = 200

df_seccion2.shape

df_seccion2.isnull().sum()

df_seccion2.head()

###-------------------------
# aqui hice una columna con la frecuencia de la accion por cada usuario.
df_seccion2['action'].value_counts()

df_seccion2['action'] = df_seccion2['action'].fillna('other_action')


df_seccion2['freq_act'] = df_seccion2.groupby(['user_id', 'action'])['action'].transform('count')

# =============================================================================
# 
# =============================================================================
df_seccion2['action_type'].value_counts()
df_seccion2['action_type'] = df_seccion2['action_type'].fillna('-unknown-')

sns.set_style('ticks')
fig, ax = plt.subplots()
fig.set_size_inches(11.7, 8.27)
action_type_percentage = df_seccion2.action_type.value_counts() / df_seccion2.shape[0] * 100
action_type_percentage.plot(kind='bar',color='#3498DB')
plt.xlabel('action type')
plt.ylabel('Percentage')
sns.despine()
fig.savefig('/home/jaketoruk/Documents/Kaggle_Competition/airbnb/graficos/data_seccion/Univariate analysis/%_action_type.png')
# =============================================================================
# 
# =============================================================================
df_seccion2['action_detail'].value_counts()

df_seccion2['action_detail'] = df_seccion2['action_detail'].fillna('other_action_detail')

df_seccion2['freq_act_detail'] = df_seccion2.groupby(['user_id', 'action_detail'])['action_detail'].transform('count')

# =============================================================================
# 
# =============================================================================

df_seccion2['device_type'].value_counts()
df_seccion2['device_type'] = df_seccion2['device_type'].fillna('-unknown-')

sns.set_style('ticks')
fig, ax = plt.subplots()
fig.set_size_inches(11.7, 8.27)
device_type_percentage = df_seccion2['device_type'].value_counts() / df_seccion2.shape[0] * 100
device_type_percentage.plot(kind='bar',color='#3498DB')
plt.xlabel('device type')
plt.ylabel('Percentage')
sns.despine()
fig.savefig('/home/jaketoruk/Documents/Kaggle_Competition/airbnb/graficos/data_seccion/Univariate analysis/%_device_type.png')

## aqui se puede observar que se puede agrupar por ipad/tablet, tablet, ....... 

df_seccion2['device_type'] = df_seccion2['device_type'].replace(['Linux Desktop', 'Chromebook', 'Windows Phone', 'Blackberry', 'Opera Phone', '-unknown-'], 'Others Devices')

df_seccion2['device_type'] = df_seccion2['device_type'].replace(['iPad Tablet', 'Tablet', 'iPodtouch', 'Android App Unknown Phone/Tablet'], 'Ipad/Tablet/iPodtouch')

sns.set_style('ticks')
fig, ax = plt.subplots()
fig.set_size_inches(11.7, 8.27)
device_type_percentage = df_seccion2['device_type'].value_counts() / df_seccion2.shape[0] * 100
device_type_percentage.plot(kind='bar',color='#3498DB')
plt.xlabel('device type')
plt.ylabel('Percentage')
sns.despine()
fig.savefig('/home/jaketoruk/Documents/Kaggle_Competition/airbnb/graficos/data_seccion/Univariate analysis/%_device_type_tudy.png')


# =============================================================================
# 
# =============================================================================

df_seccion2.secs_elapsed.value_counts()

## aqui para quitar los nan lo que hace sera ponerlos en cero....

df_seccion2.secs_elapsed = df_seccion2.secs_elapsed.fillna(0)

# =============================================================================
# 
# =============================================================================

#finalmente borrare los na que quedan porque son los id qeu no hay por lo que no tenemos informacion de ello

df_seccion2 = df_seccion2.dropna()

df_seccion2['count_secc'] = 1 # para despues cuando haga el groupby tener el conteo de las secciones de cada usuario

df_seccion2 = df_seccion2.drop(['action', 'action_detail'], axis = 1)

df_seccion2.head()

df_seccion2 = pd.get_dummies(df_seccion2, prefix=['act_type', 'dev_type'], columns=['action_type', 'device_type'])

df_seccion2.columns

df_seccion2 = df_seccion2.groupby(['user_id']).agg({'secs_elapsed': np.mean, 'freq_act': np.mean, 'freq_act_detail': np.mean, 'count_secc': np.sum,
       'act_type_-unknown-': np.sum, 'act_type_booking_request': np.sum,
       'act_type_booking_response': np.sum, 'act_type_click': np.sum, 'act_type_data': np.sum,
       'act_type_message_post': np.sum, 'act_type_modify': np.sum, 'act_type_partner_callback': np.sum,
       'act_type_submit': np.sum, 'act_type_view': np.sum, 'dev_type_Android Phone': np.sum,
       'dev_type_Ipad/Tablet/iPodtouch': np.sum, 'dev_type_Mac Desktop': np.sum,
       'dev_type_Others Devices': np.sum, 'dev_type_Windows Desktop': np.sum,
       'dev_type_iPhone': np.sum})

df_seccion2.to_csv(r'/home/jaketoruk/Documents/Kaggle_Competition/airbnb/DataBase/TidyDatabase/tidy_seccion2.csv')
