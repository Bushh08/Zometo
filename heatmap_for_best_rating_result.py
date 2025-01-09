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

pivote_table = df.pivot_table(index='listed_in(type)',columns='online_order',aggfunc='size',fill_value=0)
sns.heatmap(pivote_table,annot=True,fmt='d')
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("listed In(Type)")
plt.show()