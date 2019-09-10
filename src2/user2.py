#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:08:33 2019

@author: jaketoruk
"""

import seaborn as sns
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib .pyplot as plt
import datetime

df_user2 = pd.read_csv('/home/jaketoruk/Documents/Kaggle_Competition/airbnb/DataBase/airbnb-recruiting-new-user-bookings/train_users_2.csv', parse_dates=['date_first_booking', 'date_account_created', 'timestamp_first_active'])

pd.options.display.max_columns = 50
pd.options.display.max_rows = 200

df_user2.shape

df_user2.head()

df_user2.isnull().sum()

# =============================================================================
# 
# =============================================================================

df_user2['timestamp_f_menus_create_account'] = df_user2['date_account_created'] - df_user2['timestamp_first_active']

df_user2['timestamp_f_menus_create_account'] = df_user2['timestamp_f_menus_create_account'].dt.total_seconds()

df_user2 = df_user2.drop(['date_first_booking', 'date_account_created', 'timestamp_first_active'], axis = 1)

# =============================================================================
# 
# =============================================================================

df_user2.columns
columns = [ 'gender', 'signup_method',
       'signup_flow', 'language', 'affiliate_channel', 'affiliate_provider', 'signup_app', 'first_device_type',
       'first_browser']

for column in columns:
    
    sns.set_style('ticks') #column = 'first_browser'
    fig, ax = plt.subplots()
    fig.set_size_inches(11.7, 8.27)
    column_percentage = df_user2[column].value_counts() / df_user2.shape[0] * 100
    column_percentage.plot(kind='bar',color='#3498DB')
    plt.xlabel(column)
    plt.ylabel('Percentage')
    sns.despine()
    fig.savefig('/home/jaketoruk/Documents/Kaggle_Competition/airbnb/graficos/data_user/Univariate analysis/%_{0}.png'.format(column))

df_user2['first_browser'].value_counts()

df_user2['first_browser'] = df_user2['first_browser'].replace(['AOL Explorer', 'Opera', 'Silk', 'Chromium', 'BlackBerry Browser', 'Maxthon', 'Apple Mail', 'IE Mobile', 'Sogou Explorer', 'Mobile Firefox', 'SiteKiosk', 'RockMelt', 'Iron', 'IceWeasel', 'Pale Moon', 'Yandex.Browser', 'CometBird', 'SeaMonkey','Camino', 'TenFourFox', 'wOSBrowser', 'CoolNovo', 'Avant Browser', 'Opera Mini', 'Mozilla', 'OmniWeb', 'SlimBrowser', 'Opera Mobile', 'Crazy Browser', 'Comodo Dragon', 'TheWorld Browser', 'Flock', 'IceDragon', 'Kindle Browser', 'Palm Pre web browser', 'Epic', 'PS Vita browser', 'Stainless', 'Googlebot', 'Google Earth', 'Arora', 'Outlook 2007', 'NetNewsWire', 'Conkeror', 'Chrome Mobile', 'Mobile Safari', 'Android Browser'], 'others_browsers')

# =============================================================================
# 
# =============================================================================

df_user2['age'] = np.where(df_user2['age'] > 120, np.NaN, df_user2['age'])

df_user2['age'] = df_user2['age'].fillna(df_user2['age'].mean()) 

df_user2['country_destination'].value_counts()
df_user2['country_destination'] = np.where(df_user2['country_destination'] == 'NDF', 0, 1)



# =============================================================================
# =============================================================================
# # 
# =============================================================================
# =============================================================================
df_user2.columns
columns = ['gender', 'age', 'signup_method', 'affiliate_channel', 'affiliate_provider',
       'first_affiliate_tracked', 'signup_app', 'first_device_type',
       'first_browser', 'country_destination']

columns = [ 'age',
       'signup_flow','timestamp_f_menus_create_account']

for column in columns:
    
    sns.set_style('ticks') 
    fig, ax = plt.subplots()
    fig.set_size_inches(11.7, 8.27)

    sns.countplot(x=column, hue='country_destination',data=df_user2)
    plt.xlabel(' {0} based on Destination Country'.format(column))
    plt.ylabel('Number of users')
    sns.despine()
    fig.savefig('/home/jaketoruk/Documents/Kaggle_Competition/airbnb/graficos/data_user/Bivariante analysis/{0} if reserba o no.png'.format(column))

for column in columns:
    sns.set_style('ticks')
    fig, ax = plt.subplots()
    fig.set_size_inches(11.7, 8.27)
    sns.boxplot(y=column , x='country_destination', data=df_user2)
    plt.xlabel('Destination Country box plot')
    plt.ylabel('{0} of Users'.format(column))
    sns.despine()
    fig.savefig('/home/jaketoruk/Documents/Kaggle_Competition/airbnb/graficos/data_user/Bivariante analysis/boxes_{0} if reserva o no.png'.format(column))

# =============================================================================
# 
# =============================================================================

df_user2['first_device_type'].value_counts()
df_user2['first_device_type'] = df_user2['first_device_type'].replace( ['Desktop (Other)', 'SmartPhone (Other)'], 'Other/Unknown')

df_user2['signup_method'].value_counts()

df_user2['signup_app'].value_counts()

df_user2['affiliate_channel'].value_counts()

df_user2['first_browser'].value_counts()

df_user2['affiliate_provider'].value_counts()
df_user2['affiliate_provider'] = df_user2['affiliate_provider'].replace( ['daum', 'wayn', 'yandex', 'baidu', 'naver' ], 'other')
df_user2['affiliate_provider'] = df_user2['affiliate_provider'].replace( ['email-marketing', 'meetup', 'gsp', 'yahoo', 'facebook-open-graph', 'padmapper', 'vast' ], 'other2')

df_user2 = df_user2.drop(['language', 'first_affiliate_tracked'], axis = 1)

df_user2 = pd.get_dummies(df_user2, prefix=['gen', 'sin_met', 'aff_ch', 'aff_prov', 'sin_app', 'firs_dev', 'firs_brow'], columns=['gender', 'signup_method', 'affiliate_channel', 'affiliate_provider', 'signup_app', 'first_device_type', 'first_browser' ])

df_user2.head()
df_user2.to_csv(r'/home/jaketoruk/Documents/Kaggle_Competition/airbnb/DataBase/TidyDatabase/tidy_user2.csv')
