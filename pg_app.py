import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv(r'USA_AL_Birmingham.Muni.AP.722280_TMY3_HIGH.csv');

st.title("Complex Engineering Problem ( PG )")
st.markdown("This application is a Streamlit dashboard that can be used "
            "to visualize Load profile of Birmingham on weekly monthly "
            "and annual based for our Power Generation CEP. ")

a=df.iloc[:,1]
b=df.iloc[:,2]
c=df.iloc[:,3]
d=df.iloc[:,4]
e=df.iloc[:,5]
f=df.iloc[:,6]
g=df.iloc[:,7]
h=df.iloc[:,8]
i=df.iloc[:,9]
j=df.iloc[:,10]
k=df.iloc[:,11]
l=df.iloc[:,12]
m=df.iloc[:,13]
n=a+b+c+d+e+f+g+h+i+j+k+l+m
df2 = df.head(85)

st.title("Weekly Load Profile")

nweek = n.head(168)
fig1 = plt.figure()
sns.lineplot(data=nweek).set(title='Weekly Load Profile', xlabel='Hours', ylabel='Power')
st.pyplot(fig1)

st.title("Monthly Load Profile")

nmonth = n.head(720)
fig2 = plt.figure()
amonth = sns.lineplot(data=nmonth).set(title='Monthly Load Profile', xlabel='Hours', ylabel='Power')
st.pyplot(fig2)

st.title("Annual Load Profile")

fig3 = plt.figure()
aannual = sns.lineplot(data=n).set(title='Annual Load Profile', xlabel='Hours', ylabel='Power')
st.pyplot(fig3)


if st.checkbox('Show sample of data'): 
     st.write(df2)