import streamlit as st
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import scripts.ploting as plot
from scripts import file
import seaborn as sns
def null_percentage(df):
    number_of_rows, number_of_columns = df.shape
    df_size = number_of_rows * number_of_columns
    
    null_size = (df.isnull().sum()).sum()
    percentage = round((null_size / df_size) * 100, 2)
    st.write("Data Fraame contain null values of:",percentage)
def plot_bar(df:pd.DataFrame, x_col:str, y_col:str, title:str, xlabel:str, ylabel:str)->None:
  plt.figure(figsize=(12, 7))
  sns.barplot(data = df, x=x_col, y=y_col)
  plt.title(title, size=20)
  plt.xticks(rotation=75, fontsize=14)
  plt.yticks( fontsize=14)
  plt.xlabel(xlabel, fontsize=16)
  plt.ylabel(ylabel, fontsize=16)
  plt.show()
  st.pyplot()
def run_experiance():
  #Read the csv file
  st.write("## User Experiance Analysis")
  file_name = 'data/Week1_challenge_data_source.csv'
  df_task_3 = pd.read_csv(file_name)
  new_netwok_df = df_task_3[['MSISDN/Number', 'Handset Type','TCP DL Retrans. Vol (Bytes)', 'TCP UL Retrans. Vol (Bytes)',\
                         'Avg RTT DL (ms)', 'Avg RTT UL (ms)',\
                         'Avg Bearer TP DL (kbps)', 'Avg Bearer TP UL (kbps)']]
  null_percentage(new_netwok_df)
  new_netwok_df.isnull().sum()
  ## Fill Mising Values
  for col in new_netwok_df.columns:
    if(new_netwok_df[col].isnull().sum()):
      new_netwok_df[col] = new_netwok_df[col].fillna(new_netwok_df[col].mode()[0])
  null_percentage(new_netwok_df)
  new_netwok_df.isnull().sum()
  new_netwok_df['Total TCP Retrans'] = new_netwok_df['TCP DL Retrans. Vol (Bytes)'] +\
                                       new_netwok_df['TCP UL Retrans. Vol (Bytes)']
  new_netwok_df['Total Throughput'] = new_netwok_df['Avg Bearer TP DL (kbps)'] +\
                                      new_netwok_df['Avg Bearer TP DL (kbps)']
  new_netwok_df['Total RTT'] = new_netwok_df['Avg RTT DL (ms)'] + new_netwok_df['Avg RTT UL (ms)']
  st.write(new_netwok_df.head())
  aggregate = {'Handset Type':'first','Total TCP Retrans':'sum', 'Total Throughput':'sum', 'Total RTT':'sum'}
  columns = ['MSISDN/Number','Bearer Id','Handset Type', 'Total TCP Retrans', 'Total Throughput', 'Total RTT']
  network_per_user_df = new_netwok_df.groupby('MSISDN/Number').agg(aggregate).reset_index()
  st.write(network_per_user_df.head())
  # top 5
  result = network_per_user_df.sort_values(by='Total TCP Retrans', ascending=False)[:100]
  plot_bar(result, result['Handset Type'], result['Total TCP Retrans'], 'Highest Total TCP Retrans Handsets','','')
 
