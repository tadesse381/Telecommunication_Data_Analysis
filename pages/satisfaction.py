import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import scripts.ploting as plot
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
def run_satisfaction():
  st.write("## User Satisfaction Analysis")
  file_name = 'data/clean_telecommunication_data.csv'
  data = pd.read_csv(file_name)
  df_clean = data.copy()
  aggregate = {"Bearer Id": 'count', 'Dur. (ms).1':'sum', 'Total UL (Bytes)': 'sum', 'Total DL (Bytes)': 'sum'}
  aggregation_result = df_clean.groupby('MSISDN/Number').agg(aggregate)
  aggregation_result.head()
  df_task2 = df_clean.copy()
  df_task2['Total'] = df_task2['Total UL (Bytes)'] + df_task2['Total DL (Bytes)']
  df_task2 = df_task2.groupby('MSISDN/Number')\
           .agg({"Bearer Id": "count", 'Dur. (ms).1':'sum', 'Total':'sum'})
  df_task2.head()
  min_max_scaler = preprocessing.MinMaxScaler()
  df_values = df_task2.values
  scalled_values = min_max_scaler.fit_transform(df_values)
  df_normalized = pd.DataFrame(data=scalled_values, columns=df_task2.columns)
  kmeans = KMeans(n_clusters=3).fit(df_normalized)
  cluster = kmeans.predict(df_normalized)
  engagement_df = df_task2.copy()
  engagement_df['cluster-engagement']  = cluster
  ## Engagement Score
  lowest_engagement = engagement_df.groupby('cluster-engagement').get_group(0).mean()
  st.write(lowest_engagement)
  def get_experiance_score(df, low):
    x = float(low['Total RTT'])
    y = float(low['Total TCP Retrans'])
    z = float(low['Total Throughput'])
    new_df = df.copy()
    new_df['experience score'] = ((df['Total RTT'] - x)**2 + (df['Total TCP Retrans'] - y)**2 \
                              + (df['Total Throughput'] - z)**2 )**0.5
    return new_df
  experiance_scored_df = get_experiance_score(experiance_df, lowest_experiance)
  st.write(experiance_scored_df.head())
