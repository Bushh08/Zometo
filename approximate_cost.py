import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df=pd.read_csv(r'C:/Users/win10/Downloads/Zomato data .csv')
# majority of couples prefer resturant with an aproximte cost 300 rupees.
couple_data = df['approx_cost(for two people)']
sns.countplot(x=couple_data)
plt.show()