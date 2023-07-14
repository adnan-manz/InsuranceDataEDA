# -*- coding: utf-8 -*-
"""Project-II.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f3pPcJ5z745M1NSwrILBLH64kA9ljZa4
"""

#computing libraries
import numpy as np
import pandas as pd

#ploting libararies
import matplotlib.pyplot as plt
import seaborn as sns

#pre processing modules
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

data = pd.read_csv("/content/train_qWM28Yl.csv")
data

"""#Pandas Basic Commands"""

data.head()

data.tail()

data.shape

data.describe()

data.info()

data.columns

data.duplicated().sum()

data.isnull().sum()

gp = data.groupby('is_claim').count()
gp

"""Visualization"""

sns.countplot(x=data['is_claim'], data = data)

"""Basic EDA"""

data1 = data

data1= data1.drop('policy_id' , axis=1)
data1

data1.info()

#Checking Numerical variable of age of car

data1["age_of_car"].describe()

#Making a histogram of

plt.hist(data1["age_of_car"], bins = 10)
plt.show

#Checking Skewness and Kurtosis

print(f"Skewness : {data1['age_of_car'].skew()}")
print(f"Kurtosis : {data1['age_of_car'].kurt()}")

#Checking Numerical variable of age of Policy Holder

data1["age_of_policyholder"].describe()

#Making a histogram of

plt.hist(data1["age_of_policyholder"], bins = 10)
plt.show

#Checking Numerical variable of Policy Tenure

data1["policy_tenure"].describe()

#Making a histogram of

plt.hist(data1["policy_tenure"], bins = 10)
plt.show

data1.corr()

plt.figure(figsize = (17,17))
correlation_matrix = data1.corr()
sns.heatmap(correlation_matrix , annot = True, cmap = 'Pastel1')
plt.title("Correlation Matrix of Iris Dataset")
plt.show()

#Extracting Categorical Features
catfeatures = [col for col in data1.columns if col in data1.select_dtypes(include = object). columns]

#Extracting All Features
features = [col for col in data1.columns if col not in ['is_claim']]
print(features)

catfeatures

#Spliting features and Target Variable

X , y = data1.loc[:,features],data1.loc[:,"is_claim"]
print(X.shape)

X

y

#Encoding categorical data

labelEncode = LabelEncoder()

#Iterating over each categorical variable
for col in catfeatures :
  X[col] = labelEncode.fit_transform(data1[col])

X