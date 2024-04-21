import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:\\Users\\NIKKON DAS\\OneDrive\\Desktop\\COVID 19 PROJECT'\\archive\\Latest Covid-19 India Status.csv")
print(df)
x=df['Deaths']
y=df['Total Cases']
plt.plot(x,y)
plt.title("India Covid-19 Analysis",loc="left")
plt.xlabel("Deaths")
plt.ylabel("Total Cases")
plt.show()
