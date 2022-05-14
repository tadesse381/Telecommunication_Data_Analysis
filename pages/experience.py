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
    print(f"Data Fraame contain null values of { percentage }%")
def run_experiance():
#Read the cleaned csv file and store it on data
file_name = 'data/clean_telecommunication_data.csv'
df_task_3 = pd.read_csv(file_name)
new_netwok_df = df_task_3[['MSISDN/Number', 'Handset Type','TCP DL Retrans. Vol (Bytes)', 'TCP UL Retrans. Vol (Bytes)',\
                         'Avg RTT DL (ms)', 'Avg RTT UL (ms)',\
                         'Avg Bearer TP DL (kbps)', 'Avg Bearer TP UL (kbps)']]
null_percentage(new_netwok_df)
new_netwok_df.isnull().sum()
st.write("## User Experiance Analysis")
  
