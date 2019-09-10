#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 17:56:55 2019

@author: jaketoruk
"""
import pandas as pd
import numpy as np
import matplotlib .pyplot as plt
from datetime import datetime

df_user = pd.read_csv('/home/jaketoruk/Documents/Kaggle_Competition/airbnb/DataBase/airbnb-recruiting-new-user-bookings/train_users_2.csv', parse_dates=['date_first_booking', 'date_account_created', 'timestamp_first_active'])

pd.options.display.max_columns = 50
###___________________
# estudio del dataframe user

df_user.isnull().sum()
df_user.shape
df_user.head()
df_user.date_first_booking.value_counts()
df_user.country_destination.value_counts()

##-------------
# signup_method la dejamos asi para hacer dummies
df_user['signup_method'].value_counts()

##-------------
# signup_flow no se qeu significa pero esta bastante bien a la vista, tendriamos qeu ver con calma a ver qeu...
df_user['signup_flow'].value_counts()

##-------------
# language este dejar asi para hacer dummies, esta bien cuadrado
df_user.language.value_counts()

##-------------
# affiliate_channel, affiliate_provider, signup_app, first_device_type
df_user.affiliate_channel.value_counts()
df_user.signup_app.value_counts()
df_user.first_device_type.value_counts()

# en esta creo qeu podria agrupar por debajo de naver qeu son pocos y asi qeudan menos columnas para los dummies
df_user.affiliate_provider.value_counts()

##--------------
# first_browser creo agrupare por los qeu etan debajo de 1270 porque sumamdolos todos no pasan el 19 mil de los proxima mas usado 
df_user.first_browser.value_counts()

##------------
# date_first_booking y date_account_created 
#aqui los nan los pondre igual a el valor de la columna date_account_created correspondiente, para que la resta me de cero en la nueva columna
# =============================================================================
# 
# df_user['date_first_booking'] = np.where((df_user['date_first_booking'] < 1960), np.NaN, df_user['date_first_booking'])
# =============================================================================
df_user['date_first_booking'] = df_user['date_first_booking'].fillna(df_user['date_account_created'])


df_user['first_booking_menus_create_account'] = df_user['date_first_booking'] - df_user['date_account_created']

# =============================================================================
#me dijo migue que no lo categurizara, que lo dejara numerico
# df_user['first_booking_menus_create_account'] = df_user['first_booking_menus_create_account'].dt.days.astype('int64')
# 
# df_user['antes_despues'] = np.where(df_user['first_booking_menus_create_account'] < 0, 'despues', df_user['first_booking_menus_create_account'])
# 
# df_user['antes_despues'] = np.where(df_user['first_booking_menus_create_account'] > 0, 'antes', df_user['antes_despues'])
# 
# df_user['antes_despues'] = np.where(df_user['first_booking_menus_create_account'] == 0, 'desconocido', df_user['antes_despues'])
# =============================================================================

# elimino la columnas correspondientes

df_user = df_user.drop(['date_first_booking','date_account_created' ], axis = 1)

##--------------------

df_user['first_affiliate_tracked'].value_counts()

df_user['first_affiliate_tracked'] = df_user['first_affiliate_tracked'].fillna('desconocido')

##-----------------------
# aqui el target lo cogi y lo agrupe para balancear mejor los targuet y sea menos complejo la jugada


df_user['country_destination'].value_counts()

df_user['country_destination'] = df_user['country_destination'].replace(['FR', 'IT', 'GB', 'ES', 'PT', 'DE', 'NL', 'AU'], 'eurp')

df_user['country_destination'] = df_user['country_destination'].replace(['US', 'CA'], 'North_America')

