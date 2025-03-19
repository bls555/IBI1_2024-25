#make dictionary
#make lists
#draw bar chart
#ask user for input
#output the popularity of the language

languag={'JavaScript':62.3,'HTML':52.9,'Python':51,'SQL':51,'TypeScript':38.5}#the dictionay storing language percentation
print(languag)

import numpy as np
import matplotlib.pyplot as plt
perc=list(languag.values())#get the values of the dictionary
lang=list(languag.keys())#get the keys of the dictionary
plt.bar(lang,perc)#plot the bar chart
plt.xlabel('Programming Language')#x-axis label
plt.ylabel('Popularity (%)')#y-axis label
plt.title('Programming Language Popularity')#title
plt.show()#show the bar chart
#please close the bar chart to continue, or it stuck

ques=input("Which programming language do you want to know the popularity of?")#ask the user for the language
print(languag[ques],'%')#print the popularity of the language




