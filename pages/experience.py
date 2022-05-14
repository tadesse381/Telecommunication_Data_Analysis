import streamlit as st
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from scripts import file
def null_percentage(df):
    number_of_rows, number_of_columns = df.shape
    df_size = number_of_rows * number_of_columns
    
    null_size = (df.isnull().sum()).sum()
    percentage = round((null_size / df_size) * 100, 2)
    st.write("Data Fraame contain null values of:",percentage)
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
  
  
