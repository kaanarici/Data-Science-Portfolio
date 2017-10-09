"""
Created on Mon Oct  9 18:06:13 2017

@author: Alp
"""
import pandas as pd

# Load Training Data
filename = "C:/Users/Alp/Desktop/Data-Science-Portfolio/Kaggle/Titanic/data/train.csv"
train = pd.read_csv(filename)

# Explore training dataset
print(train.shape)
print(list(train))
train.head()
train.describe()
