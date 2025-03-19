#make lists
#sort lists
#import packages
#plot pie charts

uk_countries=[57.11,3.13,1.91,5.45] 
ch_countries=[41.88,45.28,61.27,85.15]
uk_sort=sorted(uk_countries)#sort the list
ch_sort=sorted(ch_countries)
print("UK:",uk_sort)
print("China:",ch_sort)

import numpy as np#import packages
import matplotlib.pyplot as plt


labels_uk=["England","Wales","Northern Ireland","Scotland"]
labels_ch=["Fujian","Jiangxi","Anhui","Jiangsu"]
plt.pie(uk_countries,labels=labels_uk,autopct='%1.1f%%')
plt.title('UK Population Distribution')
plt.show()
plt.pie(ch_countries,labels=labels_ch,autopct='%1.1f%%')
plt.title('China Population Distribution')  
plt.show()#show the chart