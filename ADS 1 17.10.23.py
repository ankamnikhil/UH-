# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


df_countries = pd.read_csv('countries_top10.csv')
print('df_countries.head()')

df_countries['gdp/pop'] = df_countries['GDP'] / df_countries['Population']
df_countries['pop/km2'] = df_countries['Population'] / df_countries['Area']

df_countries.to_excel('countries_top10.xlsx')
print(df_countries)