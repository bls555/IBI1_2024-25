import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("Practical10")
#C:/Users/玄青石/Downloads/
print("Current working directory:", os.getcwd())  
print("Files in directory:", os.listdir())  
columns=[True, True, False,False,True]
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

print(dalys_data.head(5))  # show the first 5 rows of the DataFrame
print(dalys_data.info())  # show the DataFrame's information
print(dalys_data.describe())  # show the DataFrame's descriptive statistics

years = dalys_data.iloc[0:10, 2]
print("Third column (Year) for the first 10 rows:\n", years)
#the 10th year with DALYs data recorded in Afghanistan is 1999.

#dalys_data[,"Year"]="1990"
#print(dalys_data.head(5))
#print(dalys_data.info())
#print(dalys_data.describe())
#print(dalys_data.columns)

is_1990 = dalys_data["Year"] == 1990
dalys_1990 = dalys_data.loc[is_1990, "DALYs"]
print("DALYs for all countries in 1990:\n", dalys_1990)

uk = dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["DALYs", "Year"]]
france = dalys_data.loc[dalys_data["Entity"] == "France", ["DALYs", "Year"]]
mean_uk = uk["DALYs"].mean()
mean_france = france["DALYs"].mean()
print("Mean DALYs in the UK:", mean_uk)
print("Mean DALYs in France:", mean_france)
#the mean DALYs in the UK was greater than that in France.
plt.plot(uk["Year"], uk["DALYs"], 'b+-')  # use blue color with plus markers
plt.title("DALYs in the UK over Time")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(uk["Year"], rotation=-90)  # rotate x-axis labels for better readability
plt.show()


#question: How has the relationship between the DALYs in China and the UK changed over time? Are they becoming more similar, less similar?
uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]]
plt.plot(uk["Year"], uk["DALYs"],'b',label="UK")
plt.title("DALYs in UK and China from 1990 to 2019")
plt.xticks(uk.Year,rotation=-90)


ch=dalys_data.loc[dalys_data.Entity=="China", ["DALYs", "Year"]]
plt.plot(ch["Year"], ch["DALYs"],'r',label="China")

plt.legend(loc='upper right',fontsize=10)


plt.show()
#They are decreasing, and becoming similar


'''
max=dalys_data.loc[dalys_data["DALYs"]>=650000,["Entity","Year","DALYs"]]
print(max)
'''
'''
ok=dalys_data.loc[dalys_data["Year"]==1990,["Entity","DALYs"]]
ok=ok.sort_values(by="DALYs",ascending=False)
lk=ok[0:10]
plt.plot(lk["Entity"],lk["DALYs"],'b')
plt.xticks(lk.Entity,rotation=-90)
plt.show()
print(ok.Entity)
'''