# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 09:04:51 2024

@author: MicaiahTakudzwaNhamb
"""
#importing liablaries 
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as sk
import sklearn.preprocessing as sks
#data
years_experience=np.array([1,2,3,4,5,6,7,8,9,10])
education_level=np.array([0,0,1,1,0,2,1,2,1,2])
salary=np.array([50,55,65,75,80,95,90,105,110,125])
#1 creating scattter plot
plt.figure(figsize=(12,8))
for educational_level in range(3):
    data = education_level == educational_level
    plt.scatter(years_experience[data],salary[data])# label=f"{'Bachelor\'s' if educational_level == 0 else 'Master\'s' if educational_level == 1 else 'PhD'}")
#2. adding lines 
colors=['b','g','r']
for educational_level in range(3):
    data = education_level == educational_level
    if np.sum(data)>1:
        coeffs=np.polyfit(years_experience[data],salary[data],1)
        poly=np.poly1d(coeffs)
        plt.plot(years_experience,poly(years_experience),color=colors[educational_level],linestyle='--')
