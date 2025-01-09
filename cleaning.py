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
print(df)