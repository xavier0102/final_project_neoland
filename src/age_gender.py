#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:00:06 2019

@author: jaketoruk
"""
import pandas as pd
import numpy as np

df_a_g = pd.read_csv('/home/jaketoruk/Documents/Kaggle_Competition/airbnb/DataBase/airbnb-recruiting-new-user-bookings/age_gender_bkts.csv')

###_____________________
# estudio del dataframe a_g

df_a_g.isnull().sum()
df_a_g.shape
df_a_g.head()