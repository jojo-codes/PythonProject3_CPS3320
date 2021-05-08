import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("/Users/joanjohn/Desktop/Covid-19-NJ-Counties.csv")

#print(data)

#shows columns in the data
print(data.columns)
#Get project description
print(data.describe)
#seaborn shows relationship between variable using scatter plot
sns.relplot(x="Deaths", y="Total Positive Cases", hue="Deaths", data=data)
#seaborn shows relationship between variable using line graph
sns.relplot(x="Deaths", y="Total Positive Cases", kind="line", data=data)
plt.show()



