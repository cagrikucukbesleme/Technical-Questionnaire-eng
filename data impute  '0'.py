# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 12:23:22 2021

@author: monster
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
veriler = pd.read_csv('country_vaccination_stats.csv')
print(veriler)
a=veriler['daily_vaccinations']

b=a.fillna((veriler['daily_vaccinations'].min()), inplace=True)
