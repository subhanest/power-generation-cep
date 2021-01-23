import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import pydeck as pdk
from streamlit_folium import folium_static
import folium
import math


def Average(lst): 
    return sum(lst) / len(lst) 

def main():
     st.title("Complex Engineering Problem ( PG )")
     menu = ["Load Profiles","Worst Cases","Power Plant Design","Calculator UI","References"]
     st.sidebar.title("Group Details")
     st.sidebar.subheader("Bilal Khan   EE-17167")
     st.sidebar.subheader("Subhan Ahmed EE-17156")
     st.sidebar.subheader("Humayun Khan EE-17150")
     st.sidebar.subheader("Usama Khan   EE-17140")
     st.sidebar.title("More Options")
     choice = st.sidebar.selectbox("Menu",menu)

     if choice == "Load Profiles":
          page_bg_img = '''
          <style>
          body {
          background-image: url("https://bs-uploads.toptal.io/blackfish-uploads/uploaded_file/file/252832/image-1589414925946-28e4d0912682e877c15d3d381cd4a7c1.png");
          background-size: cover;
          }
          </style>
          '''

          st.markdown(page_bg_img, unsafe_allow_html=True)
          df = pd.read_csv(r'USA_AL_Birmingham.Muni.AP.722280_TMY3_HIGH.csv');

          
          st.markdown("This application is a Streamlit dashboard that can be used "
                    "to visualize Load profile of commerial and industrial load on"
                    "weekly monthly and annual based for our Power Generation CEP. ")

          menu1 = ["Load Profile 1","Load Profile 2","Load Profile 3","Load Profile 4","Load Profile 5","Load Profile 6","Load Profile 7","Load Profile 8","Load Profile 9","Load Profile 10"]
          choice1 = st.selectbox("Menu",menu1)

          if choice1 == "Load Profile 1":
                    st.markdown("The load profile of the hospitals in Houston south west florida ")
                    df = pd.read_csv(r'RefBldgHospitalNew2004_v1.3_7.1_2A_USA_TX_HOUSTON.csv');
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
                    n=a+b+c+d+e+f+g+h+i+j
                    df2 = df.head(85)
                    if st.checkbox('Weekly Load Profile 1',True): 
                         st.title("Weekly Load Profile")

                         nweek = n.head(168)
                         
                         fig1 = plt.figure()
                         sns.lineplot(data=nweek).set(title='Weekly Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig1)
                         nweekmax1 = max(nweek)
                         nweekavg1 = Average(nweek)
                         nweekLF1  = (nweekavg1/nweekmax1)
                         m1 = ["TECHNICAL ANALYSIS","ECONOMIC ANALYSIS"]
                         c1 = st.selectbox("TYPE OF ANALYSIS",m1)
                         if c1 == "TECHNICAL ANALYSIS":
                              st.subheader("TECHNICAL ANALYSIS")
                              nsum1 = sum(nweek);
                              nsum2 = nsum1 * 3600000;
                              nmin1 = min(nweek) 
                              st.markdown("The Total energy generated in one week is: ")
                              st.subheader(nsum2);
                              st.subheader(" Joules");
                              st.markdown("or ")
                              st.subheader(nsum1);
                              st.subheader(" KWh");
                              st.markdown("The Base energy is: ")
                              st.subheader(nmin1);
                              st.subheader("KWh")
                              st.markdown("The Maximum demand is: ") 
                              st.subheader(nweekmax1)
                              st.markdown("The Average demand is: ")
                              st.subheader(nweekavg1)
                              st.markdown("The Load Factor is: ")
                              st.subheader(nweekLF1)
                         else:
                              st.subheader("ECONOMIC ANALYSIS")
                              nweeksum1 = sum(nweek)
                              nweeksum2 = math.ceil(nweeksum1)
                              nweekmax1 = max(nweek)
                              nweekmax2 = math.ceil(nweekmax1)
                              nweekmax3 = nweekmax2 + (0.1*nweekmax2)
                              st.subheader("The install capacity is (KW):")
                              st.subheader(nweekmax3)
                              capcosthy = nweekmax3*1400
                              st.subheader("The Capital cost for power plant will be (one time):")
                              st.subheader(capcosthy)
                              runhy = nweeksum2*24*7*0.01
                              st.subheader("The running cost of power plant will be (per week):")
                              st.subheader(runhy)
                              totco = runhy+capcosthy
                              st.subheader("Total cost will be:")
                              st.subheader(totco)
                    if st.checkbox('Monthly Load Profile 1'): 
                         st.title("Monthly Load Profile")

                         nmonth = n.head(720)
                         fig2 = plt.figure()
                         sns.lineplot(data=nmonth).set(title='Monthly Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig2)
                         nmonthmax1 = max(nmonth)
                         nmonthavg1 = Average(nmonth)
                         nmonthLF1  = (nmonthavg1/nmonthmax1)
                         st.subheader("TECHNICAL ANALYSIS")
                         st.markdown("The Maximum demand is: ") 
                         st.subheader(nmonthmax1)
                         st.markdown("The Average demand is: ")
                         st.subheader(nmonthavg1)
                         st.markdown("The Load Factor is: ")
                         st.subheader(nmonthLF1)
                    if st.checkbox('Annual Load Profile 1'): 
                         st.title("Annual Load Profile")

                         fig3 = plt.figure()
                         sns.lineplot(data=n).set(title='Annual Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig3)
                         nannualmax1 = max(n)
                         nannualavg1 = Average(n)
                         nannualLF1  = (nannualavg1/nannualmax1)
                         st.subheader("TECHNICAL ANALYSIS")
                         st.markdown("The Maximum demand is: ") 
                         st.subheader(nannualmax1)
                         st.markdown("The Average demand is: ")
                         st.subheader(nannualavg1)
                         st.markdown("The Load Factor is: ")
                         st.subheader(nannualLF1)

                    if st.checkbox('Show sample of data'): 
                         st.write(df2)

          if choice1 == "Load Profile 2":
                    st.markdown("The load profile of the primary schools in south west florida ")
                    df = pd.read_csv(r'RefBldgPrimarySchoolNew2004_v1.3_7.1_2A_USA_TX_HOUSTON.csv');
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
                    n=a+b+c+d+e+f+g+h+i+j
                    df2 = df.head(85)
                    if st.checkbox('Weekly Load Profile 2',True): 
                         st.title("Weekly Load Profile")

                         nweek = n.head(168)
                         
                         fig1 = plt.figure()
                         sns.lineplot(data=nweek).set(title='Weekly Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig1)
                         nweekmax1 = max(nweek)
                         nweekavg1 = Average(nweek)
                         nweekLF1  = (nweekavg1/nweekmax1)
                         m1 = ["TECHNICAL ANALYSIS","ECONOMIC ANALYSIS"]
                         c1 = st.selectbox("TYPE OF ANALYSIS",m1)
                         if c1 == "TECHNICAL ANALYSIS":
                              st.subheader("TECHNICAL ANALYSIS")
                              st.markdown("The Maximum demand is: ") 
                              st.subheader(nweekmax1)
                              st.markdown("The Average demand is: ")
                              st.subheader(nweekavg1)
                              st.markdown("The Load Factor is: ")
                              st.subheader(nweekLF1)
                              nsum1 = sum(nweek);
                              nsum2 = nsum1 * 3600000;
                              nmin1 = min(nweek) 
                              st.markdown("The Total energy generated in one week is: ")
                              st.subheader(nsum2);
                              st.subheader(" Joules");
                              st.markdown("or ")
                              st.subheader(nsum1);
                              st.subheader(" KWh");
                              st.markdown("The Base energy is: ")
                              st.subheader(nmin1);
                              st.subheader("KWh")
                         else:
                              st.subheader("ECONOMICAL ANALYSIS")
                              nweeksum1 = sum(nweek)
                              nweeksum2 = math.ceil(nweeksum1)
                              nweekmax1 = max(nweek)
                              nweekmax2 = math.ceil(nweekmax1)
                              nweekmax3 = nweekmax2 + (0.1*nweekmax2)
                              st.subheader("The install capacity is (KW):")
                              st.subheader(nweekmax3)
                              capcosthy = nweekmax3*1400
                              st.subheader("The Capital cost for power plant will be (one time):")
                              st.subheader(capcosthy)
                              runhy = nweeksum2*24*7*0.01
                              st.subheader("The running cost of power plant will be (per week):")
                              st.subheader(runhy)
                              totco = runhy+capcosthy
                              st.subheader("Total cost will be:")
                              st.subheader(totco)
                    if st.checkbox('Monthly Load Profile 2'): 
                         st.title("Monthly Load Profile")

                         nmonth = n.head(720)
                         fig2 = plt.figure()
                         sns.lineplot(data=nmonth).set(title='Monthly Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig2)
                         nmonthmax1 = max(nmonth)
                         nmonthavg1 = Average(nmonth)
                         nmonthLF1  = (nmonthavg1/nmonthmax1)
                         st.subheader("TECHNICAL ANALYSIS")
                         st.markdown("The Maximum demand is: ") 
                         st.subheader(nmonthmax1)
                         st.markdown("The Average demand is: ")
                         st.subheader(nmonthavg1)
                         st.markdown("The Load Factor is: ")
                         st.subheader(nmonthLF1)
                    if st.checkbox('Annual Load Profile 2'): 
                         st.title("Annual Load Profile")

                         fig3 = plt.figure()
                         sns.lineplot(data=n).set(title='Annual Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig3)
                         nannualmax1 = max(n)
                         nannualavg1 = Average(n)
                         nannualLF1  = (nannualavg1/nannualmax1)
                         st.subheader("TECHNICAL ANALYSIS")
                         st.markdown("The Maximum demand is: ") 
                         st.subheader(nannualmax1)
                         st.markdown("The Average demand is: ")
                         st.subheader(nannualavg1)
                         st.markdown("The Load Factor is: ")
                         st.subheader(nannualLF1)

                    if st.checkbox('Show sample of data'): 
                         st.write(df2)


          if choice1 == "Load Profile 3":
                    st.markdown("The load profile of the super markets in Jackson holes fairbanks alaska")
                    df = pd.read_csv(r'RefBldgSuperMarketNew2004_v1.3_7.1_8A_USA_AK_FAIRBANKS.csv');
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
                    n=a+b+c+d+e+f+g+h+i+j
                    df2 = df.head(85)
                    if st.checkbox('Weekly Load Profile 3',True): 
                         st.title("Weekly Load Profile")

                         nweek = n.head(168)
                         
                         fig1 = plt.figure()
                         sns.lineplot(data=nweek).set(title='Weekly Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig1)
                         nweekmax1 = max(nweek)
                         nweekavg1 = Average(nweek)
                         nweekLF1  = (nweekavg1/nweekmax1)
                         m1 = ["TECHNICAL ANALYSIS","ECONOMIC ANALYSIS"]
                         c1 = st.selectbox("TYPE OF ANALYSIS",m1)
                         if c1 == "TECHNICAL ANALYSIS":
                              st.subheader("TECHNICAL ANALYSIS")
                              st.markdown("The Maximum demand is: ") 
                              st.subheader(nweekmax1)
                              st.markdown("The Average demand is: ")
                              st.subheader(nweekavg1)
                              st.markdown("The Load Factor is: ")
                              st.subheader(nweekLF1)
                              nsum1 = sum(nweek);
                              nsum2 = nsum1 * 3600000;
                              nmin1 = min(nweek) 
                              st.markdown("The Total energy generated in one week is: ")
                              st.subheader(nsum2);
                              st.subheader(" Joules");
                              st.markdown("or ")
                              st.subheader(nsum1);
                              st.subheader(" KWh");
                              st.markdown("The Base energy is: ")
                              st.subheader(nmin1);
                              st.subheader("KWh")
                         else:
                              st.subheader("ECONOMICAL ANALYSIS")
                              nweeksum1 = sum(nweek)
                              nweeksum2 = math.ceil(nweeksum1)
                              nweekmax1 = max(nweek)
                              nweekmax2 = math.ceil(nweekmax1)
                              nweekmax3 = nweekmax2 + (0.1*nweekmax2)
                              st.subheader("The install capacity is (KW):")
                              st.subheader(nweekmax3)
                              capcosthy = nweekmax3*1400
                              st.subheader("The Capital cost for power plant will be (one time):")
                              st.subheader(capcosthy)
                              runhy = nweeksum2*24*7*0.01
                              st.subheader("The running cost of power plant will be (per week):")
                              st.subheader(runhy)
                              totco = runhy+capcosthy
                              st.subheader("Total cost will be:")
                              st.subheader(totco)
                    if st.checkbox('Monthly Load Profile 3'): 
                         st.title("Monthly Load Profile")

                         nmonth = n.head(720)
                         fig2 = plt.figure()
                         sns.lineplot(data=nmonth).set(title='Monthly Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig2)
                         nmonthmax1 = max(nmonth)
                         nmonthavg1 = Average(nmonth)
                         nmonthLF1  = (nmonthavg1/nmonthmax1)
                         st.subheader("TECHNICAL ANALYSIS")
                         st.markdown("The Maximum demand is: ") 
                         st.subheader(nmonthmax1)
                         st.markdown("The Average demand is: ")
                         st.subheader(nmonthavg1)
                         st.markdown("The Load Factor is: ")
                         st.subheader(nmonthLF1)
                    if st.checkbox('Annual Load Profile 3'): 
                         st.title("Annual Load Profile")

                         fig3 = plt.figure()
                         sns.lineplot(data=n).set(title='Annual Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig3)
                         nannualmax1 = max(n)
                         nannualavg1 = Average(n)
                         nannualLF1  = (nannualavg1/nannualmax1)
                         st.subheader("TECHNICAL ANALYSIS")
                         st.markdown("The Maximum demand is: ") 
                         st.subheader(nannualmax1)
                         st.markdown("The Average demand is: ")
                         st.subheader(nannualavg1)
                         st.markdown("The Load Factor is: ")
                         st.subheader(nannualLF1)

                    if st.checkbox('Show sample of data'): 
                         st.write(df2)
          
          if choice1 == "Load Profile 4":
                    st.markdown("The load profile of the mid rise apartments in Helena ")
                    df = pd.read_csv(r'RefBldgMidriseApartmentNew2004_v1.3_7.1_6B_USA_MT_HELENA.csv');
                    a=df.iloc[:,1]
                    b=df.iloc[:,2]
                    c=df.iloc[:,3]
                    d=df.iloc[:,4]
                    e=df.iloc[:,5]
                    f=df.iloc[:,6]
                    g=df.iloc[:,7]
                    h=df.iloc[:,8]
                    i=df.iloc[:,9]
                    n=a+b+c+d+e+f+g+h+i
                    df2 = df.head(85)
                    if st.checkbox('Weekly Load Profile 4',True): 
                         st.title("Weekly Load Profile")

                         nweek = n.head(168)
                         
                         fig1 = plt.figure()
                         sns.lineplot(data=nweek).set(title='Weekly Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig1)
                         nweekmax1 = max(nweek)
                         nweekavg1 = Average(nweek)
                         nweekLF1  = (nweekavg1/nweekmax1)
                         m1 = ["TECHNICAL ANALYSIS","ECONOMIC ANALYSIS"]
                         c1 = st.selectbox("TYPE OF ANALYSIS",m1)
                         if c1 == "TECHNICAL ANALYSIS":
                              st.subheader("TECHNICAL ANALYSIS")
                              st.markdown("The Maximum demand is: ") 
                              st.subheader(nweekmax1)
                              st.markdown("The Average demand is: ")
                              st.subheader(nweekavg1)
                              st.markdown("The Load Factor is: ")
                              st.subheader(nweekLF1)
                              nsum1 = sum(nweek);
                              nsum2 = nsum1 * 3600000;
                              nmin1 = min(nweek) 
                              st.markdown("The Total energy generated in one week is: ")
                              st.subheader(nsum2);
                              st.subheader(" Joules");
                              st.markdown("or ")
                              st.subheader(nsum1);
                              st.subheader(" KWh");
                              st.markdown("The Base energy is: ")
                              st.subheader(nmin1);
                              st.subheader("KWh")
                         else:
                              st.subheader("ECONOMICAL ANALYSIS")
                              nweeksum1 = sum(nweek)
                              nweeksum2 = math.ceil(nweeksum1)
                              nweekmax1 = max(nweek)
                              nweekmax2 = math.ceil(nweekmax1)
                              nweekmax3 = nweekmax2 + (0.1*nweekmax2)
                              st.subheader("The install capacity is (KW):")
                              st.subheader(nweekmax3)
                              capcosthy = nweekmax3*1400
                              st.subheader("The Capital cost for power plant will be (one time):")
                              st.subheader(capcosthy)
                              runhy = nweeksum2*24*7*0.01
                              st.subheader("The running cost of power plant will be (per week):")
                              st.subheader(runhy)
                              totco = runhy+capcosthy
                              st.subheader("Total cost will be:")
                              st.subheader(totco)
                    if st.checkbox('Monthly Load Profile 4'): 
                         st.title("Monthly Load Profile")

                         nmonth = n.head(720)
                         fig2 = plt.figure()
                         sns.lineplot(data=nmonth).set(title='Monthly Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig2)
                         nmonthmax1 = max(nmonth)
                         nmonthavg1 = Average(nmonth)
                         nmonthLF1  = (nmonthavg1/nmonthmax1)
                         st.subheader("TECHNICAL ANALYSIS")
                         st.markdown("The Maximum demand is: ") 
                         st.subheader(nmonthmax1)
                         st.markdown("The Average demand is: ")
                         st.subheader(nmonthavg1)
                         st.markdown("The Load Factor is: ")
                         st.subheader(nmonthLF1)
                    if st.checkbox('Annual Load Profile 4'): 
                         st.title("Annual Load Profile")

                         fig3 = plt.figure()
                         sns.lineplot(data=n).set(title='Annual Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig3)
                         nannualmax1 = max(n)
                         nannualavg1 = Average(n)
                         nannualLF1  = (nannualavg1/nannualmax1)
                         st.subheader("TECHNICAL ANALYSIS")
                         st.markdown("The Maximum demand is: ") 
                         st.subheader(nannualmax1)
                         st.markdown("The Average demand is: ")
                         st.subheader(nannualavg1)
                         st.markdown("The Load Factor is: ")
                         st.subheader(nannualLF1)

                    if st.checkbox('Show sample of data'): 
                         st.write(df2)

          if choice1 == "Load Profile 5":
                    st.markdown("The load profile of the warehouses in Houston south west florida ")
                    df = pd.read_csv(r'RefBldgWarehouseNew2004_v1.3_7.1_2A_USA_TX_HOUSTON.csv');
                    a=df.iloc[:,1]
                    b=df.iloc[:,2]
                    c=df.iloc[:,3]
                    d=df.iloc[:,4]
                    e=df.iloc[:,5]
                    f=df.iloc[:,6]
                    g=df.iloc[:,7]
                    h=df.iloc[:,8]
                    n=a+b+c+d+e+f+g+h
                    df2 = df.head(85)
                    if st.checkbox('Weekly Load Profile 5',True): 
                         st.title("Weekly Load Profile")

                         nweek = n.head(168)
                         
                         fig1 = plt.figure()
                         sns.lineplot(data=nweek).set(title='Weekly Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig1)
                         nweekmax1 = max(nweek)
                         nweekavg1 = Average(nweek)
                         nweekLF1  = (nweekavg1/nweekmax1)
                         m1 = ["TECHNICAL ANALYSIS","ECONOMIC ANALYSIS"]
                         c1 = st.selectbox("TYPE OF ANALYSIS",m1)
                         if c1 == "TECHNICAL ANALYSIS":
                              st.subheader("TECHNICAL ANALYSIS")
                              st.markdown("The Maximum demand is: ") 
                              st.subheader(nweekmax1)
                              st.markdown("The Average demand is: ")
                              st.subheader(nweekavg1)
                              st.markdown("The Load Factor is: ")
                              st.subheader(nweekLF1)
                              nsum1 = sum(nweek);
                              nsum2 = nsum1 * 3600000;
                              nmin1 = min(nweek) 
                              st.markdown("The Total energy generated in one week is: ")
                              st.subheader(nsum2);
                              st.subheader(" Joules");
                              st.markdown("or ")
                              st.subheader(nsum1);
                              st.subheader(" KWh");
                              st.markdown("The Base energy is: ")
                              st.subheader(nmin1);
                              st.subheader("KWh")
                         else:
                              st.subheader("ECONOMICAL ANALYSIS")
                              nweeksum1 = sum(nweek)
                              nweeksum2 = math.ceil(nweeksum1)
                              nweekmax1 = max(nweek)
                              nweekmax2 = math.ceil(nweekmax1)
                              nweekmax3 = nweekmax2 + (0.1*nweekmax2)
                              st.subheader("The install capacity is (KW):")
                              st.subheader(nweekmax3)
                              capcosthy = nweekmax3*1400
                              st.subheader("The Capital cost for power plant will be (one time):")
                              st.subheader(capcosthy)
                              runhy = nweeksum2*24*7*0.01
                              st.subheader("The running cost of power plant will be (per week):")
                              st.subheader(runhy)
                              totco = runhy+capcosthy
                              st.subheader("Total cost will be:")
                              st.subheader(totco)
                    if st.checkbox('Monthly Load Profile 5'): 
                         st.title("Monthly Load Profile")

                         nmonth = n.head(720)
                         fig2 = plt.figure()
                         sns.lineplot(data=nmonth).set(title='Monthly Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig2)
                         nmonthmax1 = max(nmonth)
                         nmonthavg1 = Average(nmonth)
                         nmonthLF1  = (nmonthavg1/nmonthmax1)
                         st.subheader("TECHNICAL ANALYSIS")
                         st.markdown("The Maximum demand is: ") 
                         st.subheader(nmonthmax1)
                         st.markdown("The Average demand is: ")
                         st.subheader(nmonthavg1)
                         st.markdown("The Load Factor is: ")
                         st.subheader(nmonthLF1)
                    if st.checkbox('Annual Load Profile 5'): 
                         st.title("Annual Load Profile")

                         fig3 = plt.figure()
                         sns.lineplot(data=n).set(title='Annual Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig3)
                         nannualmax1 = max(n)
                         nannualavg1 = Average(n)
                         nannualLF1  = (nannualavg1/nannualmax1)
                         st.subheader("TECHNICAL ANALYSIS")
                         st.markdown("The Maximum demand is: ") 
                         st.subheader(nannualmax1)
                         st.markdown("The Average demand is: ")
                         st.subheader(nannualavg1)
                         st.markdown("The Load Factor is: ")
                         st.subheader(nannualLF1)

                    if st.checkbox('Show sample of data'): 
                         st.write(df2)

 
          if choice1 == "Load Profile 6":
                    st.markdown("The load profile of the large offices in Houston south west florida ")
                    df = pd.read_csv(r'RefBldgLargeOfficeNew2004_v1.3_7.1_2A_USA_TX_HOUSTON.csv');
                    a=df.iloc[:,1]
                    b=df.iloc[:,2]
                    c=df.iloc[:,3]
                    d=df.iloc[:,4]
                    e=df.iloc[:,5]
                    f=df.iloc[:,6]
                    g=df.iloc[:,7]
                    h=df.iloc[:,8]
                    i=df.iloc[:,9]
                    n=a+b+c+d+e+f+g+h+i
                    df2 = df.head(85)
                    if st.checkbox('Weekly Load Profile 6',True): 
                         st.title("Weekly Load Profile")

                         nweek = n.head(168)
                         
                         fig1 = plt.figure()
                         sns.lineplot(data=nweek).set(title='Weekly Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig1)
                         nweekmax1 = max(nweek)
                         nweekavg1 = Average(nweek)
                         nweekLF1  = (nweekavg1/nweekmax1)
                         m1 = ["TECHNICAL ANALYSIS","ECONOMIC ANALYSIS"]
                         c1 = st.selectbox("TYPE OF ANALYSIS",m1)
                         if c1 == "TECHNICAL ANALYSIS":
                              st.subheader("TECHNICAL ANALYSIS")
                              st.markdown("The Maximum demand is: ") 
                              st.subheader(nweekmax1)
                              st.markdown("The Average demand is: ")
                              st.subheader(nweekavg1)
                              st.markdown("The Load Factor is: ")
                              st.subheader(nweekLF1)
                              nsum1 = sum(nweek);
                              nsum2 = nsum1 * 3600000;
                              nmin1 = min(nweek) 
                              st.markdown("The Total energy generated in one week is: ")
                              st.subheader(nsum2);
                              st.subheader(" Joules");
                              st.markdown("or ")
                              st.subheader(nsum1);
                              st.subheader(" KWh");
                              st.markdown("The Base energy is: ")
                              st.subheader(nmin1);
                              st.subheader("KWh")
                         else:
                              st.subheader("ECONOMICAL ANALYSIS")
                              nweeksum1 = sum(nweek)
                              nweeksum2 = math.ceil(nweeksum1)
                              nweekmax1 = max(nweek)
                              nweekmax2 = math.ceil(nweekmax1)
                              nweekmax3 = nweekmax2 + (0.1*nweekmax2)
                              st.subheader("The install capacity is (KW):")
                              st.subheader(nweekmax3)
                              capcosthy = nweekmax3*1400
                              st.subheader("The Capital cost for power plant will be (one time):")
                              st.subheader(capcosthy)
                              runhy = nweeksum2*24*7*0.01
                              st.subheader("The running cost of power plant will be (per week):")
                              st.subheader(runhy)
                              totco = runhy+capcosthy
                              st.subheader("Total cost will be:")
                              st.subheader(totco)
                    if st.checkbox('Monthly Load Profile 6'): 
                         st.title("Monthly Load Profile")

                         nmonth = n.head(720)
                         fig2 = plt.figure()
                         sns.lineplot(data=nmonth).set(title='Monthly Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig2)
                         nmonthmax1 = max(nmonth)
                         nmonthavg1 = Average(nmonth)
                         nmonthLF1  = (nmonthavg1/nmonthmax1)
                         st.subheader("TECHNICAL ANALYSIS")
                         st.markdown("The Maximum demand is: ") 
                         st.subheader(nmonthmax1)
                         st.markdown("The Average demand is: ")
                         st.subheader(nmonthavg1)
                         st.markdown("The Load Factor is: ")
                         st.subheader(nmonthLF1)
                    if st.checkbox('Annual Load Profile 6'): 
                         st.title("Annual Load Profile")

                         fig3 = plt.figure()
                         sns.lineplot(data=n).set(title='Annual Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig3)
                         nannualmax1 = max(n)
                         nannualavg1 = Average(n)
                         nannualLF1  = (nannualavg1/nannualmax1)
                         st.subheader("TECHNICAL ANALYSIS")
                         st.markdown("The Maximum demand is: ") 
                         st.subheader(nannualmax1)
                         st.markdown("The Average demand is: ")
                         st.subheader(nannualavg1)
                         st.markdown("The Load Factor is: ")
                         st.subheader(nannualLF1)

                    if st.checkbox('Show sample of data'): 
                         st.write(df2)

          if choice1 == "Load Profile 7":
                    st.markdown("The load profile of residental areas Birmingham ")
                    df = pd.read_csv(r'USA_AL_Birmingham.Muni.AP.722280_TMY3_HIGH.csv');
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
                    if st.checkbox('Weekly Load Profile 7',True): 
                         st.title("Weekly Load Profile")

                         nweek = n.head(168)
                         
                         fig1 = plt.figure()
                         sns.lineplot(data=nweek).set(title='Weekly Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig1)
                         nweekmax1 = max(nweek)
                         nweekavg1 = Average(nweek)
                         nweekLF1  = (nweekavg1/nweekmax1)
                         m1 = ["TECHNICAL ANALYSIS","ECONOMIC ANALYSIS"]
                         c1 = st.selectbox("TYPE OF ANALYSIS",m1)
                         if c1 == "TECHNICAL ANALYSIS":
                              st.subheader("TECHNICAL ANALYSIS")
                              st.markdown("The Maximum demand is: ") 
                              st.subheader(nweekmax1)
                              st.markdown("The Average demand is: ")
                              st.subheader(nweekavg1)
                              st.markdown("The Load Factor is: ")
                              st.subheader(nweekLF1)
                              nsum1 = sum(nweek);
                              nsum2 = nsum1 * 3600000;
                              nmin1 = min(nweek) 
                              st.markdown("The Total energy generated in one week is: ")
                              st.subheader(nsum2);
                              st.subheader(" Joules");
                              st.markdown("or ")
                              st.subheader(nsum1);
                              st.subheader(" KWh");
                              st.markdown("The Base energy is: ")
                              st.subheader(nmin1);
                              st.subheader("KWh")
                         else:
                              st.subheader("ECONOMICAL ANALYSIS")
                              nweeksum1 = sum(nweek)
                              nweeksum2 = math.ceil(nweeksum1)
                              nweekmax1 = max(nweek)
                              nweekmax2 = math.ceil(nweekmax1)
                              nweekmax3 = nweekmax2 + (0.1*nweekmax2)
                              st.subheader("The install capacity is (KW):")
                              st.subheader(nweekmax3)
                              capcosthy = nweekmax3*1400
                              st.subheader("The Capital cost for power plant will be (one time):")
                              st.subheader(capcosthy)
                              runhy = nweeksum2*24*7*0.01
                              st.subheader("The running cost of power plant will be (per week):")
                              st.subheader(runhy)
                              totco = runhy+capcosthy
                              st.subheader("Total cost will be:")
                              st.subheader(totco)
                    if st.checkbox('Monthly Load Profile 7'): 
                         st.title("Monthly Load Profile")

                         nmonth = n.head(720)
                         fig2 = plt.figure()
                         sns.lineplot(data=nmonth).set(title='Monthly Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig2)
                         nmonthmax1 = max(nmonth)
                         nmonthavg1 = Average(nmonth)
                         nmonthLF1  = (nmonthavg1/nmonthmax1)
                         st.subheader("TECHNICAL ANALYSIS")
                         st.markdown("The Maximum demand is: ") 
                         st.subheader(nmonthmax1)
                         st.markdown("The Average demand is: ")
                         st.subheader(nmonthavg1)
                         st.markdown("The Load Factor is: ")
                         st.subheader(nmonthLF1)
                    if st.checkbox('Annual Load Profile 7'): 
                         st.title("Annual Load Profile")

                         fig3 = plt.figure()
                         sns.lineplot(data=n).set(title='Annual Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig3)
                         nannualmax1 = max(n)
                         nannualavg1 = Average(n)
                         nannualLF1  = (nannualavg1/nannualmax1)
                         st.subheader("TECHNICAL ANALYSIS")
                         st.markdown("The Maximum demand is: ") 
                         st.subheader(nannualmax1)
                         st.markdown("The Average demand is: ")
                         st.subheader(nannualavg1)
                         st.markdown("The Load Factor is: ")
                         st.subheader(nannualLF1)

                    if st.checkbox('Show sample of data'): 
                         st.write(df2)

          if choice1 == "Load Profile 8":
                    st.markdown("The load profile of the secondary schools in Anchorage, Alaska ")
                    df = pd.read_csv(r'RefBldgSecondarySchoolNew2004_v1.3_7.1_8A_USA_AK_FAIRBANKS.csv');
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
                    n=a+b+c+d+e+f+g+h+i+j
                    df2 = df.head(85)
                    if st.checkbox('Weekly Load Profile 8',True): 
                         st.title("Weekly Load Profile")

                         nweek = n.head(168)
                         
                         fig1 = plt.figure()
                         sns.lineplot(data=nweek).set(title='Weekly Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig1)
                         nweekmax1 = max(nweek)
                         nweekavg1 = Average(nweek)
                         nweekLF1  = (nweekavg1/nweekmax1)
                         m1 = ["TECHNICAL ANALYSIS","ECONOMIC ANALYSIS"]
                         c1 = st.selectbox("TYPE OF ANALYSIS",m1)
                         if c1 == "TECHNICAL ANALYSIS":
                              st.subheader("TECHNICAL ANALYSIS")
                              st.markdown("The Maximum demand is: ") 
                              st.subheader(nweekmax1)
                              st.markdown("The Average demand is: ")
                              st.subheader(nweekavg1)
                              st.markdown("The Load Factor is: ")
                              st.subheader(nweekLF1)
                              nsum1 = sum(nweek);
                              nsum2 = nsum1 * 3600000;
                              nmin1 = min(nweek) 
                              st.markdown("The Total energy generated in one week is: ")
                              st.subheader(nsum2);
                              st.subheader(" Joules");
                              st.markdown("or ")
                              st.subheader(nsum1);
                              st.subheader(" KWh");
                              st.markdown("The Base energy is: ")
                              st.subheader(nmin1);
                              st.subheader("KWh")
                         else:
                              st.subheader("ECONOMICAL ANALYSIS")
                              nweeksum1 = sum(nweek)
                              nweeksum2 = math.ceil(nweeksum1)
                              nweekmax1 = max(nweek)
                              nweekmax2 = math.ceil(nweekmax1)
                              nweekmax3 = nweekmax2 + (0.1*nweekmax2)
                              st.subheader("The install capacity is (KW):")
                              st.subheader(nweekmax3)
                              capcosthy = nweekmax3*1400
                              st.subheader("The Capital cost for power plant will be (one time):")
                              st.subheader(capcosthy)
                              runhy = nweeksum2*24*7*0.01
                              st.subheader("The running cost of power plant will be (per week):")
                              st.subheader(runhy)
                              totco = runhy+capcosthy
                              st.subheader("Total cost will be:")
                              st.subheader(totco)
                    if st.checkbox('Monthly Load Profile 8'): 
                         st.title("Monthly Load Profile")

                         nmonth = n.head(720)
                         fig2 = plt.figure()
                         sns.lineplot(data=nmonth).set(title='Monthly Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig2)
                         nmonthmax1 = max(nmonth)
                         nmonthavg1 = Average(nmonth)
                         nmonthLF1  = (nmonthavg1/nmonthmax1)
                         st.subheader("TECHNICAL ANALYSIS")
                         st.markdown("The Maximum demand is: ") 
                         st.subheader(nmonthmax1)
                         st.markdown("The Average demand is: ")
                         st.subheader(nmonthavg1)
                         st.markdown("The Load Factor is: ")
                         st.subheader(nmonthLF1)
                    if st.checkbox('Annual Load Profile 8'): 
                         st.title("Annual Load Profile")

                         fig3 = plt.figure()
                         sns.lineplot(data=n).set(title='Annual Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig3)
                         nannualmax1 = max(n)
                         nannualavg1 = Average(n)
                         nannualLF1  = (nannualavg1/nannualmax1)
                         st.subheader("TECHNICAL ANALYSIS")
                         st.markdown("The Maximum demand is: ") 
                         st.subheader(nannualmax1)
                         st.markdown("The Average demand is: ")
                         st.subheader(nannualavg1)
                         st.markdown("The Load Factor is: ")
                         st.subheader(nannualLF1)

                    if st.checkbox('Show sample of data'): 
                         st.write(df2)


          if choice1 == "Load Profile 9":
                    st.markdown("The load profile of the super markets in Houston south west florida ")
                    df = pd.read_csv(r'RefBldgSuperMarketNew2004_v1.3_7.1_2A_USA_TX_HOUSTON.csv');
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
                    n=a+b+c+d+e+f+g+h+i+j
                    df2 = df.head(85)
                    if st.checkbox('Weekly Load Profile 9',True): 
                         st.title("Weekly Load Profile")

                         nweek = n.head(168)
                         
                         fig1 = plt.figure()
                         sns.lineplot(data=nweek).set(title='Weekly Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig1)
                         nweekmax1 = max(nweek)
                         nweekavg1 = Average(nweek)
                         nweekLF1  = (nweekavg1/nweekmax1)
                         m1 = ["TECHNICAL ANALYSIS","ECONOMIC ANALYSIS"]
                         c1 = st.selectbox("TYPE OF ANALYSIS",m1)
                         if c1 == "TECHNICAL ANALYSIS":
                              st.subheader("TECHNICAL ANALYSIS")
                              st.markdown("The Maximum demand is: ") 
                              st.subheader(nweekmax1)
                              st.markdown("The Average demand is: ")
                              st.subheader(nweekavg1)
                              st.markdown("The Load Factor is: ")
                              st.subheader(nweekLF1)
                              nsum1 = sum(nweek);
                              nsum2 = nsum1 * 3600000;
                              nmin1 = min(nweek) 
                              st.markdown("The Total energy generated in one week is: ")
                              st.subheader(nsum2);
                              st.subheader(" Joules");
                              st.markdown("or ")
                              st.subheader(nsum1);
                              st.subheader(" KWh");
                              st.markdown("The Base energy is: ")
                              st.subheader(nmin1);
                              st.subheader("KWh")
                         else:
                              st.subheader("ECONOMICAL ANALYSIS")
                              nweeksum1 = sum(nweek)
                              nweeksum2 = math.ceil(nweeksum1)
                              nweekmax1 = max(nweek)
                              nweekmax2 = math.ceil(nweekmax1)
                              nweekmax3 = nweekmax2 + (0.1*nweekmax2)
                              st.subheader("The install capacity is (KW):")
                              st.subheader(nweekmax3)
                              capcosthy = nweekmax3*1400
                              st.subheader("The Capital cost for power plant will be (one time):")
                              st.subheader(capcosthy)
                              runhy = nweeksum2*24*7*0.01
                              st.subheader("The running cost of power plant will be (per week):")
                              st.subheader(runhy)
                              totco = runhy+capcosthy
                              st.subheader("Total cost will be:")
                              st.subheader(totco)
                    if st.checkbox('Monthly Load Profile 9'): 
                         st.title("Monthly Load Profile")

                         nmonth = n.head(720)
                         fig2 = plt.figure()
                         sns.lineplot(data=nmonth).set(title='Monthly Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig2)
                         nmonthmax1 = max(nmonth)
                         nmonthavg1 = Average(nmonth)
                         nmonthLF1  = (nmonthavg1/nmonthmax1)
                         st.subheader("TECHNICAL ANALYSIS")
                         st.markdown("The Maximum demand is: ") 
                         st.subheader(nmonthmax1)
                         st.markdown("The Average demand is: ")
                         st.subheader(nmonthavg1)
                         st.markdown("The Load Factor is: ")
                         st.subheader(nmonthLF1)
                    if st.checkbox('Annual Load Profile 9'): 
                         st.title("Annual Load Profile")

                         fig3 = plt.figure()
                         sns.lineplot(data=n).set(title='Annual Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig3)
                         nannualmax1 = max(n)
                         nannualavg1 = Average(n)
                         nannualLF1  = (nannualavg1/nannualmax1)
                         st.subheader("TECHNICAL ANALYSIS")
                         st.markdown("The Maximum demand is: ") 
                         st.subheader(nannualmax1)
                         st.markdown("The Average demand is: ")
                         st.subheader(nannualavg1)
                         st.markdown("The Load Factor is: ")
                         st.subheader(nannualLF1)

                    if st.checkbox('Show sample of data'): 
                         st.write(df2)


          if choice1 == "Load Profile 10":
                    st.markdown("The load profile of the full service restaurant in Houston south west florida ")
                    df = pd.read_csv(r'RefBldgFullServiceRestaurantNew2004_v1.3_7.1_2A_USA_TX_HOUSTON.csv');
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
                    n=a+b+c+d+e+f+g+h+i+j
                    df2 = df.head(85)
                    if st.checkbox('Weekly Load Profile 10',True): 
                         st.title("Weekly Load Profile")

                         nweek = n.head(168)
                         
                         fig1 = plt.figure()
                         sns.lineplot(data=nweek).set(title='Weekly Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig1)
                         nweekmax1 = max(nweek)
                         nweekavg1 = Average(nweek)
                         nweekLF1  = (nweekavg1/nweekmax1)
                         m1 = ["TECHNICAL ANALYSIS","ECONOMIC ANALYSIS"]
                         c1 = st.selectbox("TYPE OF ANALYSIS",m1)
                         if c1 == "TECHNICAL ANALYSIS":
                              st.subheader("TECHNICAL ANALYSIS")
                              st.markdown("The Maximum demand is: ") 
                              st.subheader(nweekmax1)
                              st.markdown("The Average demand is: ")
                              st.subheader(nweekavg1)
                              st.markdown("The Load Factor is: ")
                              st.subheader(nweekLF1)
                              nsum1 = sum(nweek);
                              nsum2 = nsum1 * 3600000;
                              nmin1 = min(nweek) 
                              st.markdown("The Total energy generated in one week is: ")
                              st.subheader(nsum2);
                              st.subheader(" Joules");
                              st.markdown("or ")
                              st.subheader(nsum1);
                              st.subheader(" KWh");
                              st.markdown("The Base energy is: ")
                              st.subheader(nmin1);
                              st.subheader("KWh")
                         else:
                              st.subheader("ECONOMICAL ANALYSIS")
                              nweeksum1 = sum(nweek)
                              nweeksum2 = math.ceil(nweeksum1)
                              nweekmax1 = max(nweek)
                              nweekmax2 = math.ceil(nweekmax1)
                              nweekmax3 = nweekmax2 + (0.1*nweekmax2)
                              st.subheader("The install capacity is (KW):")
                              st.subheader(nweekmax3)
                              capcosthy = nweekmax3*1400
                              st.subheader("The Capital cost for power plant will be (one time):")
                              st.subheader(capcosthy)
                              runhy = nweeksum2*24*7*0.01
                              st.subheader("The running cost of power plant will be (per week):")
                              st.subheader(runhy)
                              totco = runhy+capcosthy
                              st.subheader("Total cost will be:")
                              st.subheader(totco)
                    if st.checkbox('Monthly Load Profile 10'): 
                         st.title("Monthly Load Profile")

                         nmonth = n.head(720)
                         fig2 = plt.figure()
                         sns.lineplot(data=nmonth).set(title='Monthly Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig2)
                         nmonthmax1 = max(nmonth)
                         nmonthavg1 = Average(nmonth)
                         nmonthLF1  = (nmonthavg1/nmonthmax1)
                         st.subheader("TECHNICAL ANALYSIS")
                         st.markdown("The Maximum demand is: ") 
                         st.subheader(nmonthmax1)
                         st.markdown("The Average demand is: ")
                         st.subheader(nmonthavg1)
                         st.markdown("The Load Factor is: ")
                         st.subheader(nmonthLF1)
                    if st.checkbox('Annual Load Profile 10'): 
                         st.title("Annual Load Profile")

                         fig3 = plt.figure()
                         sns.lineplot(data=n).set(title='Annual Load Profile', xlabel='Hours', ylabel='Power')
                         st.pyplot(fig3)
                         nannualmax1 = max(n)
                         nannualavg1 = Average(n)
                         nannualLF1  = (nannualavg1/nannualmax1)
                         st.subheader("TECHNICAL ANALYSIS")
                         st.markdown("The Maximum demand is: ") 
                         st.subheader(nannualmax1)
                         st.markdown("The Average demand is: ")
                         st.subheader(nannualavg1)
                         st.markdown("The Load Factor is: ")
                         st.subheader(nannualLF1)

                    if st.checkbox('Show sample of data'): 
                         st.write(df2)



     elif choice == "Worst Cases":
          page_bg_img = '''
          <style>
          body {
          background-image: url("https://wonderfulengineering.com/wp-content/uploads/2016/02/white-wallpaper-11.jpg");
          background-size: cover;
          }
          </style>
          '''

          st.markdown(page_bg_img, unsafe_allow_html=True)
          st.subheader("The two worst case scenarios are load profile 2 and load profile load profile 8.")
          st.markdown("The load factor of load profile 2 is: 0.3074")
          st.markdown("The load factor of load profile 8 is: 0.398")
          st.markdown("Both of these load profile are of schools, primary and secondary respectively.")
          st.markdown("The reason for the poor load factor is uneven use power of during the day and night.")
          df2  = pd.read_csv(r'RefBldgPrimarySchoolNew2004_v1.3_7.1_2A_USA_TX_HOUSTON.csv');
          a=df2.iloc[:,1]
          b=df2.iloc[:,2]
          c=df2.iloc[:,3]
          d=df2.iloc[:,4]
          e=df2.iloc[:,5]
          f=df2.iloc[:,6]
          g=df2.iloc[:,7]
          h=df2.iloc[:,8]
          i=df2.iloc[:,9]
          j=df2.iloc[:,10]
          n=a+b+c+d+e+f+g+h+i+j
          st.header("\u0332".join("Worst Case Load Profile 2"))
          n5 = n.head(168)
          nsum1 = sum(n5);
          nsum2 = nsum1 * 3600000;
          nmin1 = min(n5) 
          st.markdown("The Total energy generated in one week is: ")
          st.subheader(nsum2);
          st.subheader(" Joules");
          st.markdown("or ")
          st.subheader(nsum1);
          st.subheader(" KWh");
          st.markdown("The Base energy is: ")
          st.subheader(nmin1);
          st.subheader("KWh")
          if st.checkbox('Worst load profile 2 load curve',False):
               fig11 = plt.figure()
               sns.lineplot(data=n5).set(title='Weekly Load Profile', xlabel='Hours', ylabel='Power')
               st.pyplot(fig11)


          df8  = pd.read_csv(r'RefBldgSecondarySchoolNew2004_v1.3_7.1_8A_USA_AK_FAIRBANKS.csv');
          a1=df8.iloc[:,1]
          b1=df8.iloc[:,2]
          c1=df8.iloc[:,3]
          d1=df8.iloc[:,4]
          e1=df8.iloc[:,5]
          f1=df8.iloc[:,6]
          g1=df8.iloc[:,7]
          h1=df8.iloc[:,8]
          i1=df8.iloc[:,9]
          j1=df8.iloc[:,10]
          n1=a1+b1+c1+d1+e1+f1+g1+h1+i1+j1
          st.header("\u0332".join("Worst Case Load Profile 8"))
          n2 = n1.head(168)
          nsum3 = sum(n2);
          nsum4 = nsum3 * 3600000;
          nmin2 = min(n2) 
          st.markdown("The Total energy generated in one week is: ")
          st.subheader(nsum4);
          st.subheader(" Joules");
          st.markdown("or ")
          st.subheader(nsum3);
          st.subheader(" KWh");
          st.markdown("The Base energy is: ")
          st.subheader(nmin2);
          st.subheader("KWh")
          if st.checkbox('Worst load profile 8 load curve',False):
               fig12 = plt.figure()
               sns.lineplot(data=n2).set(title='Weekly Load Profile', xlabel='Hours', ylabel='Power')
               st.pyplot(fig12)

     elif choice == "Power Plant Design":
          page_bg_img = '''
          <style>
          body {
          background-image: url("https://cdn.lynda.com/course/418967/418967-637286179665471004-16x9.jpg");
          background-size: cover;
          }
          </style>
          '''

          st.markdown(page_bg_img, unsafe_allow_html=True)
          st.subheader("")

          st.subheader("The pictures our the second power plant is:")
          st.markdown("https://drive.google.com/file/d/1fJu85e0Hv9HOfzMg1TYdK_lfg0a0KJ5Y/view?usp=sharing")
          st.markdown("https://drive.google.com/file/d/1wsbLLaj38l2mzhM3RZ4NozGC2PhfdMFY/view?usp=sharing")
          st.markdown("https://drive.google.com/file/d/17fytwHdoDct3yKYJ1gb0z2Z3qI0ZOpeF/view?usp=sharing")
          st.markdown("https://drive.google.com/file/d/1FZX-wucOQwZSLGGUx02S46HjaiFH_VPx/view?usp=sharing")

          
          st.subheader("The location of our first power plant is:")

          n = folium.Map(location=[29.6301, -82.2589], zoom_start=14)

          tooltip = "Power Plant"
          folium.Marker(
               [29.6301, -82.2589], popup="Diesel Power Plant of Southwest florida", tooltip=tooltip
          ).add_to(n)
          folium_static(n)

          st.subheader("The pictures our the second power plant is:")
          st.markdown("https://drive.google.com/file/d/1zoaj1t_eCBAKnhAiW6zQF9qdWOoOe-L_/view?usp=sharing")
          st.markdown("https://drive.google.com/file/d/1iulHbiaarH4w8gh8t7NSKzVqRUYfZRA8/view?usp=sharing")
          st.markdown("https://drive.google.com/file/d/1pgzXBdX6fe09UcGPm-do1XxB6Z86Vwxg/view?usp=sharing")
          st.markdown("https://drive.google.com/file/d/1CB0aFtdH3583fuHapdgPY6W5s0sVbzMK/view?usp=sharing")
          

          st.subheader("The location of our second power plant is:")
          m = folium.Map(location=[61.1639, -149.8103], zoom_start=14)

          tooltip = "Power Plant"
          folium.Marker(
               [61.1639, -149.8103], popup="Anchorage Steam Power Plant", tooltip=tooltip
          ).add_to(m)
          folium_static(m)
          

     

     elif choice == "Calculator UI":
          page_bg_img = '''
          <style>
          body {
          background-image: url("https://bs-uploads.toptal.io/blackfish-uploads/uploaded_file/file/252832/image-1589414925946-28e4d0912682e877c15d3d381cd4a7c1.png");
          background-size: cover;
          }
          </style>
          '''

          st.markdown(page_bg_img, unsafe_allow_html=True)
          avg1 = st.text_input("Average Load", )
          pea1 = st.text_input("Peak Load Load", )
          con1 = st.text_input("Connected Load")
          plc1 = st.text_input("Plant Capacity")
          try:
               avg2 = int(avg1)
               pea2 = int(pea1)
               lf  = (avg2/pea2)
               st.markdown("The Load Factor is:")
               st.subheader(lf)
          except:
               pass
          try:
               con2 = int(con1)
               pea2 = int(pea1)
               df  = (pea2/con2)
               st.markdown("The Demand Factor is:")
               st.subheader(df)
          except:
               pass
          try:
               avg2 = int(avg1)
               plc2 = int(plc1)
               pcf  = (avg2/plc2)
               st.markdown("The Load Factor is:")
               st.subheader(pcf)
          except:
               pass
          sim1 = st.text_input("Sum of individual max demand")
          mpp1 = st.text_input("Max demand on Power Station")
          try:
               sim2 = int(sim1)
               mpp2 = int(mpp1)
               dff  = (sim2/mpp2)
               st.markdown("The Diversity Factor is:")
               st.subheader(dff)
          except:
               pass

     

     else:
          page_bg_img = '''
          <style>
          body {
          background-image: url("https://bs-uploads.toptal.io/blackfish-uploads/uploaded_file/file/252832/image-1589414925946-28e4d0912682e877c15d3d381cd4a7c1.png");
          background-size: cover;
          }
          </style>
          '''

          st.markdown(page_bg_img, unsafe_allow_html=True)
          st.markdown("[1] OpenEI (2004).Dataset listing for cross-country(US) energy use.URL:https://openei.org/datasets/files/961/pub")
          st.subheader("Visualization of Load Profile Dataset")
          df1  = pd.read_csv(r'RefBldgHospitalNew2004_v1.3_7.1_2A_USA_TX_HOUSTON.csv');
          df2  = pd.read_csv(r'RefBldgPrimarySchoolNew2004_v1.3_7.1_2A_USA_TX_HOUSTON.csv');
          df3  = pd.read_csv(r'RefBldgSuperMarketNew2004_v1.3_7.1_8A_USA_AK_FAIRBANKS.csv');
          df4  = pd.read_csv(r'RefBldgMidriseApartmentNew2004_v1.3_7.1_6B_USA_MT_HELENA.csv');
          df5  = pd.read_csv(r'RefBldgWarehouseNew2004_v1.3_7.1_2A_USA_TX_HOUSTON.csv');
          df6  = pd.read_csv(r'RefBldgLargeOfficeNew2004_v1.3_7.1_2A_USA_TX_HOUSTON.csv');
          df7  = pd.read_csv(r'USA_AL_Birmingham.Muni.AP.722280_TMY3_HIGH.csv');
          df8  = pd.read_csv(r'RefBldgSecondarySchoolNew2004_v1.3_7.1_8A_USA_AK_FAIRBANKS.csv');
          df9  = pd.read_csv(r'RefBldgSuperMarketNew2004_v1.3_7.1_2A_USA_TX_HOUSTON.csv');
          df10 = pd.read_csv(r'RefBldgFullServiceRestaurantNew2004_v1.3_7.1_2A_USA_TX_HOUSTON.csv');
          if st.checkbox('Show Load Profile 1 data'): 
               st.write(df1)
          if st.checkbox('Show Load Profile 2 data'): 
               st.write(df2)
          if st.checkbox('Show Load Profile 3 data'): 
               st.write(df3)
          if st.checkbox('Show Load Profile 4 data'): 
               st.write(df4)
          if st.checkbox('Show Load Profile 5 data'): 
               st.write(df5)
          if st.checkbox('Show Load Profile 6 data'): 
               st.write(df6)
          if st.checkbox('Show Load Profile 7 data'): 
               st.write(df7)
          if st.checkbox('Show Load Profile 8 data'): 
               st.write(df8)
          if st.checkbox('Show Load Profile 9 data'): 
               st.write(df9)
          if st.checkbox('Show Load Profile 10 data'): 
               st.write(df10)
if __name__ == "__main__":
     main()
