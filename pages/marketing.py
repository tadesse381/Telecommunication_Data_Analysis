import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

import scripts.ploting as plot


st.set_option('deprecation.showPyplotGlobalUse', False)
def run_marketing():
  st.write("## User Overview or Marketing Analysis")

  file_name = 'data/clean_telecommunication_data.csv'
  df_clean = pd.read_csv(file_name)
  
  top_10_handset = df_clean.groupby("Handset Type")['MSISDN/Number'].nunique().nlargest(10)
  top_3_manufacturers = df_clean.groupby("Handset Manufacturer")['MSISDN/Number'].nunique().nlargest(3)

  fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(12,7))
  plot.serious_bar(top_3_manufacturers, ax1)
  plot.serious_bar(top_10_handset, ax2)
  plt.xticks(rotation=75)
  st.pyplot()
  top_manufacturers = df_clean.groupby("Handset Manufacturer").agg({"MSISDN/Number":'count'}).reset_index()
  top_3_manufacturers = top_manufacturers.sort_values(by='MSISDN/Number', ascending=False).head(3)
  manufacturers = df_clean.groupby("Handset Manufacturer")
  st.write("The top 5 handsets per top 3 handset manufacturer")
  for column in top_3_manufacturers['Handset Manufacturer']:
      result = manufacturers.get_group(column).groupby("Handset Type")['MSISDN/Number'].nunique().nlargest(5)
      st.write(f"**** { column } ***")
      print(result)
      st.write(result.head())
  st.write("## Analysis Results")
  st.write("Graph a)  and b) shows that from the top 3 manufacturers of handset the Apple is leading , and the phone which sold on number one is Huawei B528S-23A .\
           But next to Huawei most of the customers use Apple Handset.Since Apple is highly manufactured and it is also used next to Huawei, the marketing department of Telcco should sell the apple handsets in order to be productiveTherefore, the company will generate a good income from selling the Apple handset.")

