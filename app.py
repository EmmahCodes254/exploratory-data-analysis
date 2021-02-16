import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns  

data = pd.read_csv('Iris.csv') 
#data = pd.read_jsoN('iris.json')
#data = pd.read_excel("iris.xlsx")

#prints the fist five
print(data.head())

#prints the last five
print(data.tail())

#describes data
print(data.describe())

#gives the shape of the cdata in terms of how many rows and colunns it consists
print(data.shape)

#returns count of all data
print(data.count())

#shows null where there is null values
print(data.isnull().sum())

#fills up the null value with the value of the cdata before it
data = data.fillna(method = "bfill")

#shows null where there is null values
print(data.isnull().sum())