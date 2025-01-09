import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df=pd.read_csv(r'C:/Users/win10/Downloads/Zomato data .csv')

def handRate(value):
    value = str(value).split('/')
    value = value[0]
    return float(value)
df['rate']=df['rate'].apply(handRate)

# the majority of resturant recieve rating from 3.5 to 4.
plt.hist(df['rate'],bins=5)
plt.title("Rating Distribution")
plt.show()