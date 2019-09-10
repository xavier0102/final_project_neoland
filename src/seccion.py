#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 17:57:35 2019

@author: jaketoruk
"""
import pandas as pd
import numpy as np

df_seccion = pd.read_csv('/home/jaketoruk/Documents/Kaggle_Competition/airbnb/DataBase/airbnb-recruiting-new-user-bookings/sessions.csv')


###______________________
# estudio del dataframe seccion

pd.options.display.max_columns = 50
pd.options.display.max_rows = 20

df_seccion.isnull().sum()

df_seccion.shape

df_seccion.head()
df_seccion.action_type.value_counts()

df_seccion.action_detail.value_counts()

df_seccion.secs_elapsed.value_counts()

df_seccion.action.value_counts()

## creo deberia borrar las filas con los id nan porque no tengo manera de relacionarlos con las demas cosas

##---------------
# sustituyendo los nan por 'otros' action_detail column

df_seccion['action_detail'].value_counts()

df_seccion['action_detail'] = np.where(df_seccion['action_detail'].isnull(), 'otro', df_seccion['action_detail'])

# ver que tambien tengo -unknown- que los trae la tabla, no se si unirlos o que..

##--------------
# hacer columna de frecuencia de action_detail
df_seccion.columns
df_seccion['freq_act_detail'] = df_seccion.groupby('action_detail')['action_detail'].transform('count')

##---------------
# uni las acciones qeu menos se repetian y las puse en otro, para hacer dummies mas tarde y a los nan le puse desconocidos no se si unirlos a los unknown qeu ya teniamos
df_seccion['action_type'].value_counts()

df_seccion['action_type'] = df_seccion.action_type.replace(['booking_response', 'modify', 'booking_request', 'partner_callback', 'message_post', 'submit'], 'otros')

df_seccion['action_type'] = df_seccion['action_type'].fillna('desconocidos')

##----------------
# aqui hice el groupby por usuario y saque la media de los lapsec para sustituirlos por los nan pero no se como aun

# df_seccion['secs_elapsec_mean'] = df_seccion['secs_elapsed'].fillna(df_seccion.groupby('user_id')['secs_elapsed'].mean())

df_seccion.groupby('user_id')['secs_elapsed'].mean().value_counts()

#df_seccion['secs_elapsed'] = df_seccion['secs_elapsed'].fillna('u')

df_seccion['secs_elapsed'].value_counts()

# creo que lo que pasa es qeu los id que tienen nan solo tienen nan por lo que no tienen media y no tengo manera de ver eso

df_prueba = df_seccion.loc[df_seccion.secs_elapsed.isnull(),:]

df_prueba.columns

df_prueba = df_prueba.drop(['action', 'action_type', 'action_detail', 'device_type', 'freq_act_detail'], axis = 1)

df_prueba.user_id.value_counts()
# aqui podemos ver q al final los nan son solo en usuarios que q han entrado una sola vez, creo tendre que hacer la media de toda la columna....

# probamos con los mean de toda la columna a ver qeu vuelta

df_seccion['secs_elapsed'] = df_seccion['secs_elapsed'].fillna(df_seccion['secs_elapsed'].mean())

##----------------------
# veamos la columna action a ver qeu tal, trataremos de sustituirla por la frecuencia y separar en grupos para despues hacer dummies o algo asi, en dependencia de la cantidad de grupos qeu salgan

df_seccion['action'].value_counts()

# solo lo dejare en la frecuencia porque agrupar no me parece prudente ya qeu hay un monton de acciones.... pero los nan los pondre como others_action

df_seccion['action'] = df_seccion['action'].fillna('other_action')

df_seccion['freq_act'] = df_seccion.groupby('action')['action'].transform('count')

##----------------------
# vemos la columna device_type

df_seccion['device_type'].value_counts()

df_seccion['device_type'] = df_seccion['device_type'].replace(['iPodtouch', 'Windows Phone', 'Blackberry', 'Opera Phone'], 'others')
##----------------------
# borremos los user_id nulos qeu son pocos y no se puede hacer nada con eso...

df_seccion.isnull().sum()

df_seccion = df_seccion.dropna()

##----------------------
# borremos las columnas qeu sobran y dejemos las nuevas qeu hemos creado para hacer los dummies pertinentes

df_seccion = df_seccion.drop(['action_detail', 'action'], axis = 1)

# =============================================================================
# hasta aqui todo casi listo, hare dummies en las columnas de actiorn tipe y en la de device y ya hago mi csv para cerrar
# =============================================================================
df_seccion = pd.get_dummies(df_seccion)