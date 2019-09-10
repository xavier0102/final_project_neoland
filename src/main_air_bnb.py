#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:29:05 2019

@author: jaketoruk
"""

import pandas as pd
import numpy as np

df_user2 = pd.read_csv('/home/jaketoruk/Documents/Kaggle_Competition/airbnb/DataBase/TidyDatabase/tidy_user2.csv')
df_seccion2 = pd.read_csv('/home/jaketoruk/Documents/Kaggle_Competition/airbnb/DataBase/TidyDatabase/tidy_seccion2.csv')

df_user2.head()
df_user2['user_id'] = df_user2['id'] 
df_user2 = df_user2.drop(['Unnamed: 0', 'id'], axis = 1)

df_seccion2.head()
result = pd.merge(df_user2, df_seccion2, how = 'inner', on = 'user_id')

result.head()

result.shape

result.columns

x = result.drop(['user_id', 'country_destination'], axis = 1)
y = result['country_destination']

import itertools
list(itertools.combinations(columns, r))

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2)

from sklearn.preprocessing import StandardScaler

scalar = StandardScaler()
x_train = scalar.fit_transform(x_train)
x_test = scalar.transform(x_test)

from sklearn.linear_model import LogisticRegression

algoritmo = LogisticRegression()
algoritmo.fit(x_train, y_train)

y_predic = algoritmo.predict(x_test)

from sklearn.metrics import confusion_matrix

confusion_matrix(y_test, y_predic)

from sklearn.metrics import accuracy_score

accuracy_score(y_test, y_predic)

from sklearn.metrics import precision_score

precision_score(y_test, y_predic)

from sklearn.metrics import recall_score

recall_score(y_test, y_predic)

