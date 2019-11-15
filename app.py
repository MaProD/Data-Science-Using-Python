#Everything  starting with "#" is a comment and is ignored by compilers.
#Pairplots using Iris.csv dataset.
#Importing libraries
import numpy as np 
import pandas as pd  
import seaborn as sns 
from matplotlib import pyplot  as plt
%matplotlib inline
#reading your data set.
data = pd.read_csv("Iris.csv")
#Printing the first 5 data  rows.
data.head()
#Droping the Id column from the dataset
temp =data.drop('Id', axis =1)
temp.head()
#Ploting pairplots using seaborn library
g =sns.pairplot(temp, hue = 'Species', markers = '+')
#Showing your plot
plt.show()
