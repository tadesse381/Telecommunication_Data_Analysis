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
  file_name = 'data/Week1_challenge_data_source.csv'
  df_task_3 = pd.read_csv(file_name)
  new_netwok_df = df_task_3[['MSISDN/Number', 'Handset Type','TCP DL Retrans. Vol (Bytes)', 'TCP UL Retrans. Vol (Bytes)',\
                         'Avg RTT DL (ms)', 'Avg RTT UL (ms)',\
                         'Avg Bearer TP DL (kbps)', 'Avg Bearer TP UL (kbps)']]
  ## Fill Mising Values
  for col in new_netwok_df.columns:
    if(new_netwok_df[col].isnull().sum()):
      new_netwok_df[col] = new_netwok_df[col].fillna(new_netwok_df[col].mode()[0])
  net_cluster_df = network_per_user_df.copy()
  net_cluster_df.drop('Handset Type', axis=1, inplace=True)
  net_cluster_df = net_cluster_df.set_index('MSISDN/Number')
  net_cluster_df.head()
  new_netwok_df['Total TCP Retrans'] = new_netwok_df['TCP DL Retrans. Vol (Bytes)'] +\
                                       new_netwok_df['TCP UL Retrans. Vol (Bytes)']
  new_netwok_df['Total Throughput'] = new_netwok_df['Avg Bearer TP DL (kbps)'] +\
                                      new_netwok_df['Avg Bearer TP DL (kbps)']
  new_netwok_df['Total RTT'] = new_netwok_df['Avg RTT DL (ms)'] + new_netwok_df['Avg RTT UL (ms)']
  handset= network_per_user_df['Handset Type'].unique()
  def get_experiance_score(df, low):
    x = float(low['Total RTT'])
    y = float(low['Total TCP Retrans'])
    z = float(low['Total Throughput'])
    new_df = df.copy()
    new_df['experience score'] = ((df['Total RTT'] - x)**2 + (df['Total TCP Retrans'] - y)**2 \
                              + (df['Total Throughput'] - z)**2 )**0.5
    return new_df
  ## First normalize the Data, Then Cluster
  min_max_scaler = preprocessing.MinMaxScaler()
  network_values = net_cluster_df.values
  scalled_values = min_max_scaler.fit_transform(network_values)
  df_network_normalized = pd.DataFrame(data=scalled_values, columns=df_task2.columns)
  cluster = kmeans.predict(df_network_normalized)
  experiance_df = network_per_user_df.copy()
  experiance_df['cluster-experiance']  = cluster
  experiance_df = experiance_df.set_index('MSISDN/Number')
  kmeans = KMeans(n_clusters=3).fit(df_normalized)
  experiance_scored_df = get_experiance_score(experiance_df, lowest_experiance)
  st.write(experiance_scored_df.head())
