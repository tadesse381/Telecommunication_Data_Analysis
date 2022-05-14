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
  file_name = 'data/clean_telecommunication_data.csv'
  data = pd.read_csv(file_name)
  #Aggregate per user the following information in the column
  df_clean = data.copy()
  aggregate = {"Bearer Id": 'count', 'Dur. (ms).1':'sum', 'Total UL (Bytes)': 'sum', 'Total DL (Bytes)': 'sum'}
  aggregation_result = df_clean.groupby('MSISDN/Number').agg(aggregate)
  aggregation_result.head()
  #Aggregate the above metrics per customer id (MSISDN) and report the top 10 customers per engagement metric
  df_task2 = df_clean.copy()
  df_task2['Total'] = df_task2['Total UL (Bytes)'] + df_task2['Total DL (Bytes)']
  df_task2 = df_task2.groupby('MSISDN/Number')\
    .agg({"Bearer Id": "count", 'Dur. (ms).1':'sum', 'Total':'sum'})
  #Normalize each engagement metric and run a k-means (k=3) to classify customers in three groups of engagement.
  min_max_scaler = preprocessing.MinMaxScaler()
  df_values = df_task2.values
  scalled_values = min_max_scaler.fit_transform(df_values)
  df_normalized = pd.DataFrame(data=scalled_values, columns=df_task2.columns)
  kmeans = KMeans(n_clusters=3).fit(df_normalized)
  handset= network_per_user_df['Handset Type'].unique()
  # catagory = {}
  # for index, each in enumerate(handset.tolist()):
  #     catagory[each] = index
  net_cluster_df = network_per_user_df.copy()
  net_cluster_df.drop('Handset Type', axis=1, inplace=True)
  net_cluster_df = net_cluster_df.set_index('MSISDN/Number')
   ## First normalize the Data, Then Cluster
  min_max_scaler = preprocessing.MinMaxScaler()
  network_values = net_cluster_df.values
  scalled_values = min_max_scaler.fit_transform(network_values)
  df_network_normalized = pd.DataFrame(data=scalled_values, columns=df_task2.columns)
  kmeans = KMeans(n_clusters=3).fit(df_normalized)
  cluster = kmeans.predict(df_network_normalized)
  experiance_df = network_per_user_df.copy()
  experiance_df['cluster-experiance']  = cluster
  experiance_df = experiance_df.set_index('MSISDN/Number')
  experiance_df.head()
  #Compute the minimum, maximum, average & total non- normalized metrics for each cluster.
  cluster = kmeans.predict(df_normalized)
  engagement_df = df_task2.copy()
  engagement_df['cluster-engagement']  = cluster
  cluster_group_df = engagement_df.groupby('cluster-engagement')
  cluster_0 = cluster_group_df.get_group(0)
  cluster_1 = cluster_group_df.get_group(1)
  cluster_2 = cluster_group_df.get_group(2)
  ## Engagement Score
  lowest_engagement = engagement_df.groupby('cluster-engagement').get_group(0).mean()
  st.write(lowest_engagement)
  def get_engagement_score(df, lowest):
    x = float(lowest['Bearer Id'])
    y = float(lowest['Dur. (ms).1'])
    z = float(lowest['Total'])
    new_df = df.copy()
    new_df['engagement score'] = ((df['Bearer Id'] - x)**2 + (df['Dur. (ms).1'] - y)**2 + (df['Total'] - z)**2)**0.5
    return new_df
  engagement_scored_df = get_engagement_score(engagement_df, lowest_engagement)
  st.write(engagement_scored_df.head())
  lowest_experiance = experiance_df.groupby('cluster-experiance').get_group(0).mean()
  st.write(lowest_experiance)
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
