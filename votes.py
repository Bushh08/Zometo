import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df=pd.read_csv(r'C:/Users/win10/Downloads/Zomato data .csv')

# dining resturant are preferred by a large number of individuals.
grouped_data = df.groupby('listed_in(type)')['votes'].sum()
result=pd.DataFrame({'votes':grouped_data})
plt.plot(result,c='red',marker="o")
plt.xlabel("Type of Resturant",c="blue")
plt.ylabel("Votes",c="blue")
plt.show()