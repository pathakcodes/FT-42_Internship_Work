#coded by - Shivam Kumar Pathak

import pandas as pd 
import numpy as np
import matplotlib.pylab as plt
# %matplotlib inline

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6 #plot size

df= pd.read_csv('event.txt') 


df['Date'] = pd.to_datetime(df['Date']) #to convert object data type to date-time object

#making paramneters used for prediction

OH = df['Open']-df['High']
OH = OH.abs() #took avsolute so  we have to only see positive side

OL = df['Open'] - df['Low']
OL = OL.abs()

HL = df['High'] - df['Low']
HL = HL.abs()

CH = df['Close'] - df['High']
CH = CH.abs()

CL = df['Close'] - df['Low']
CL = CL.abs()

#adding all parameters to make a main parameter
change = OH + OL + HL + CH + CL

df['Change'] = change

#df.head()

#visualising change distribution
rcParams['figure.figsize'] = 16 , 6
plt.plot(df['Date'],df['Change'] , 'ro')

#adding selected part of change as different columns to dataframe

df['y1'] = df['Change'].loc[df['Date'] <= '1996']

df['y2'] = df['Change'].loc [ (df['Date'] <= '1998') & (df['Date'] > '1996') ]

df['y3'] = df['Change'].loc[(df['Date'] <= '2002') & (df['Date'] > '1998') ]

df['y4'] = df['Change'].loc[(df['Date'] <= '2008') & (df['Date'] > '2002') ]

df['y5'] = df['Change'].loc[(df['Date'] > '2008') ]

#making boundary line parameter by intuition omly
stdy1 = (df['y1'].std() + df['y1'].mean())*3
stdy2 = (df['y2'].std() + df['y2'].mean())*2.8
stdy3 = (df['y3'].std() + df['y3'].mean())*2.5
stdy4 = (df['y4'].std() + df['y4'].mean())*3
stdy5 = (df['y5'].std() + df['y5'].mean())*3

df['Date'] = pd.to_datetime(df['Date']).dt.date  #to take only dates

datelist = []  #list to store events

# adding events to datelist LIST
i = 0
cnt = 0

for i in range (df['y1'].size):
  if df['y1'].iloc[i] > stdy1:
    #print (df['Date'].iloc[i])
    cnt= cnt+1
    datelist.append(df['Date'].iloc[i])

i = 0
for i in range (df['y2'].size):
  if df['y2'].iloc[i] > stdy1:
    cnt= cnt+1
    datelist.append(df['Date'].iloc[i])


i = 0
for i in range (df['y3'].size):
  if df['y3'].iloc[i] > stdy1:
    cnt= cnt+1
    datelist.append(df['Date'].iloc[i])
i = 0
for i in range (df['y4'].size):
  if df['y4'].iloc[i] > stdy1:
    cnt= cnt+1
    datelist.append(df['Date'].iloc[i])
i = 0
for i in range (df['y5'].size):
  if df['y5'].iloc[i] > stdy1:
    cnt= cnt+1
    datelist.append(df['Date'].iloc[i])



#converting datlist LIST to dateframe DATAFRAME
dateframe = pd.DataFrame(datelist,columns = ['Date'])
dateframe['Date'] = pd.to_datetime(dateframe['Date'])

#plotting the final graph with lines
rcParams['figure.figsize'] = 16 , 6
plt.plot(df['Date'],df['Change'] , 'ro')
plt.axhline(y=stdy1, xmin=0, xmax=.38,color='r',linestyle= '-')
plt.axhline(y=stdy2, xmin=0.38, xmax=.45,color='b',linestyle= '-')
plt.axhline(y=stdy3, xmin=0.45, xmax=.6,color='g',linestyle= '-')
plt.axhline(y=stdy4,xmin=0.6, xmax=.7,color='y',linestyle= '-')
plt.axhline(y=stdy5,xmin=0.7, xmax=1,color='b',linestyle= '-')

#printing final events
print ("Total no. of prdicted events  = %d" % (cnt))
print(dateframe)
