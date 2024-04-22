import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:\\Users\\NIKKON DAS\\OneDrive\\Desktop\\COVID 19 PROJECT'\\archive\\worldometer_data.csv")
print(df)
x=df['TotalCases']
y=df['Population']
font1={'family':'serif','size':15}
font2={'family':'serif','size':15}
plt.plot(x,y,color="r")
plt.title("COVID-19 ANALYSIS",fontdict=font1)
plt.xlabel("TOTAL CASES",color="r",fontdict=font1)
plt.ylabel("POPULATION",color="b",fontdict=font2)
plt.show()