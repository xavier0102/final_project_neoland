#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 17:58:55 2019

@author: jaketoruk
"""
import pandas as pd
import numpy as np

df_country = pd.read_csv('/home/jaketoruk/Documents/Kaggle_Competition/airbnb/DataBase/airbnb-recruiting-new-user-bookings/countries.csv')


###____________________
# estudio del dataframe country

df_country.isnull().sum()
df_country.shape
df_country.head(10)