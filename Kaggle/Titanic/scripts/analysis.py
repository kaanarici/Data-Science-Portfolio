"""
Created on Mon Oct  9 18:06:13 2017

@author: Alp
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load Training Data
filename = "C:/Users/Alp/Desktop/Data-Science-Portfolio/Kaggle/Titanic/data/train.csv"
train = pd.read_csv(filename)

# Explore training dataset
print(train.shape)
print(train.info())
print(list(train))
print(train.head())
print(train.describe())

# Create a function to plot stacked bar chart for survived vs other variables
def plot_stacked_bar(dataset, varname):    
    ind = np.unique(dataset[varname])
    class_num_survived = [sum(dataset[dataset[varname]==i]["Survived"]) for i in ind]
    class_num_drowned = [len(dataset[dataset[varname]==i]["Survived"]) - 
                     sum(dataset[dataset[varname]==i]["Survived"]) for i in ind]
    width = 0.35 

    p1 = plt.bar(ind, class_num_drowned, width)
    p2 = plt.bar(ind, class_num_survived, width, bottom = class_num_drowned)

    plt.xlabel(str(varname))
    plt.title("Survived Count by " + varname)
    if varname == "Pclass":
        plt.xticks(ind, ('P1', 'P2', 'P3'))
    plt.yticks(np.arange(0, 500, 100))
    plt.legend((p1[0], p2[0]), ('Drowned', 'Survived'))
    plt.show()

plot_stacked_bar(train, "Pclass")
plot_stacked_bar(train, "SibSp")
plot_stacked_bar(train, "Parch")
