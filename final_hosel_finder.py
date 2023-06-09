# -*- coding: utf-8 -*-
"""FINAL Hosel Finder

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k_O7EXVjkjmkTvGzIf6HOdtdcjYCZ7XW
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn.preprocessing import StandardScaler

sns.set()
from sklearn.cluster import KMeans

df=pd.read_csv('Hostel-Final-16_10_22 - Sheet1.csv')
df.head()

from google.colab import drive
drive.mount('/content/drive')

df.shape

plt.scatter(df["lat"],df["long"])
plt.show()

df.isnull().sum()

df.head()

df.columns

df['price'][0]='? 21,000'

df['distance_'][0]='0.2 km'



df

pd.set_option('display.max_rows', 62)

df

df['distance_']=df['distance_'].str[0:3]

df['price']=df['price'].str[2:]

df

df['long'].isnull()

df.isnull().sum()

df['Gender'][0]='Boys'

df['Gender']=df['Gender'].map({'Boys':1,'Girls':0,'Coed':3})

df



df['distance_']

df[' price ']





df[' price ']=df[' price '].str.replace(',','')

df[' price '][0]=21000.00

df[' price ']

df.head()

df[' price ']=df[' price '].str[0:-3]

df[' price '][0]=21000

df.head()

data=df.copy()
x=df[['lat' , 'long']]

x

wcss=[]
scaler = StandardScaler()
scaled_features = scaler.fit_transform(x)

for i in range(1,11):
    kmeans=KMeans(i)
    kmeans.fit(scaled_features)
    wcss_iter=kmeans.inertia_
    wcss.append(wcss_iter)

df_sub=df[['lat','long']].values
df_sub

wcss

plt.plot(range(1,11),wcss)
plt.title('The Elbow Point Graph')
plt.xlabel('clusters')
plt.ylabel('wcss')
plt.show()

kmeans=KMeans(4)
predict=kmeans.fit_predict(scaled_features)

predict
df['Clusters']=predict

df['location'][0]='Sion'
df

plt.scatter(df['lat'],df['long'],c=df['Clusters'],cmap="rainbow")
plt.xlim((19.03,19.13))
plt.ylim((72.85,72.94))
plt.show()

area_name=input('Enter the area you want to search hostels in: ')

import difflib
list_of_area=df['location']
find_close_match = difflib.get_close_matches(area_name,list_of_area)
close_match = find_close_match[0]
df[df.location==close_match]['Clusters'].values[0]

df[['name',' price ','location' ,'Gender']][df['Clusters']==df[df.location==close_match]['Clusters'].values[0]]

close_match

