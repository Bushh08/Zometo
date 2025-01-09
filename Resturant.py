import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df=pd.read_csv(r'C:/Users/win10/Downloads/Zomato data .csv')
# print(df.head())
def handRate(value):
    value = str(value).split('/')
    value = value[0]
    return float(value)
df['rate']=df['rate'].apply(handRate)
print(df.head())
df.info()
#the majority of the resturant fall into the dining catogery
sns.countplot(x=df['listed_in(type)'])
plt.xlabel("Type of Resturent",c="red")
plt.show()


