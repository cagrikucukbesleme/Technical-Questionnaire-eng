# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 12:51:13 2021

@author: monster
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
veriler = pd.read_csv('country_vaccination_stats.csv')
a=veriler['daily_vaccinations']

b=a.fillna((veriler['daily_vaccinations'].min()), inplace=True)

ortalama=veriler.groupby('country').mean()
ort2=ortalama['daily_vaccinations'].sort_values(ascending=False)
ort3=ort2[0:3]

