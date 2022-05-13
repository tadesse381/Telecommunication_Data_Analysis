import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import scripts.ploting as plot
import scripts.utils as utils
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pickle
# My Custom Modules Importing
from scripts import file
def null_percentage(df):
    number_of_rows, number_of_columns = df.shape
    df_size = number_of_rows * number_of_columns
    
    null_size = (df.isnull().sum()).sum()
    percentage = round((null_size / df_size) * 100, 2)
    print(f"Data Fraame contain null values of { percentage }%")
def run_experiance():
  #Read the cleaned csv file and store it on data
  file_name = 'data/Week1_challenge_data_source.csv'
  df_task_3 = pd.read_csv(file_name)
  #Read the cleaned csv file and store it on data
  file_name1 = 'data/clean_telecommunication_data.csv'
  data =  pd.read_csv(file_name1)
  df_clean = data.copy()
  aggregate = {"Bearer Id": 'count', 'Dur. (ms).1':'sum', 'Total UL (Bytes)': 'sum', 'Total DL (Bytes)': 'sum'}
  aggregation_result = df_clean.groupby('MSISDN/Number').agg(aggregate)
  aggregation_result.head()
  new_netwok_df = df_task_3[['MSISDN/Number', 'Handset Type','TCP DL Retrans. Vol (Bytes)', 'TCP UL Retrans. Vol (Bytes)',\
                         'Avg RTT DL (ms)', 'Avg RTT UL (ms)',\
                         'Avg Bearer TP DL (kbps)', 'Avg Bearer TP UL (kbps)']]
  null_percentage(new_netwok_df)
  new_netwok_df.isnull().sum()
  new_netwok_df['Total TCP Retrans'] = new_netwok_df['TCP DL Retrans. Vol (Bytes)'] +\
                                       new_netwok_df['TCP UL Retrans. Vol (Bytes)']
  new_netwok_df['Total Throughput'] = new_netwok_df['Avg Bearer TP DL (kbps)'] +\
                                      new_netwok_df['Avg Bearer TP DL (kbps)']
  new_netwok_df['Total RTT'] = new_netwok_df['Avg RTT DL (ms)'] + new_netwok_df['Avg RTT UL (ms)']
  new_netwok_df.head()
  aggregate = {'Handset Type':'first','Total TCP Retrans':'sum', 'Total Throughput':'sum', 'Total RTT':'sum'}
  columns = ['MSISDN/Number','Bearer Id','Handset Type', 'Total TCP Retrans', 'Total Throughput', 'Total RTT']
  network_per_user_df = new_netwok_df.groupby('MSISDN/Number').agg(aggregate).reset_index()
  network_per_user_df.head()
  # top 5
  result = network_per_user_df.sort_values(by='Total TCP Retrans', ascending=False)[:100]
  #plot_bar(result, result['Handset Type'], result['Total TCP Retrans'], 'Highest Total TCP Retrans Handsets','','')
  # Bottom 5
  network_per_user_df.sort_values(by='Total TCP Retrans', ascending=True)[:5]
  # most frequent
  network_per_user_df['Total TCP Retrans'].value_counts().head(5)
  handset_throughput = network_per_user_df.groupby('Handset Type').agg({'Total Throughput': 'sum'}).reset_index()
  handset_throughput.sort_values(by='Total Throughput', ascending=False).head(5)
  ## Huawi is leading but apple is follwoing closely
  handset= network_per_user_df['Handset Type'].unique()
  # catagory = {}
  # for index, each in enumerate(handset.tolist()):
  #     catagory[each] = index
  net_cluster_df = network_per_user_df.copy()
  net_cluster_df.drop('Handset Type', axis=1, inplace=True)
  net_cluster_df = net_cluster_df.set_index('MSISDN/Number')
  net_cluster_df.head()
  df_task2 = df_clean.copy()
  df_task2['Total'] = df_task2['Total UL (Bytes)'] + df_task2['Total DL (Bytes)']
  df_task2 = df_task2.groupby('MSISDN/Number')\
             .agg({"Bearer Id": "count", 'Dur. (ms).1':'sum', 'Total':'sum'})
  df_task2.head()
  # new_netwok_df["Handset Type"] = [catagory[x] for x in new_netwok_df["Handset Type"]
  ### so Number 3 is the optimum, and we should run with 3 cluster
  min_max_scaler = preprocessing.MinMaxScaler()
  df_values = df_task2.values
  scalled_values = min_max_scaler.fit_transform(df_values)
  df_normalized = pd.DataFrame(data=scalled_values, columns=df_task2.columns)
  kmeans = KMeans(n_clusters=3).fit(df_normalized)
  min_max_scaler = preprocessing.MinMaxScaler()
  df_values = df_task2.values
  scalled_values = min_max_scaler.fit_transform(df_values)
  df_normalized = pd.DataFrame(data=scalled_values, columns=df_task2.columns)
  kmeans = KMeans(n_clusters=3).fit(df_normalized)
  cluster = kmeans.predict(df_normalized)
  engagement_df = df_task2.copy()
  engagement_df['cluster-engagement']  = cluster
  distortions = []
  K = range(1,10)
  for k in K:
      kmeanModel = KMeans(n_clusters=k)
      kmeanModel.fit(df_normalized)
      distortions.append(kmeanModel.inertia_)
  kmeans = KMeans(n_clusters=3)
  kmeans.fit(df_normalized)
  cluster = kmeans.predict(df_normalized)
  cluster_df = df_task2.copy()
  cluster_df['cluster']  = cluster
  cluster_df['cluster']
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
  #plot_scatter(experiance_df,"Total Throughput", "Total RTT","Clustering with Kmean", "cluster-experiance", "")
  experiance_df['cluster-experiance'].value_counts()
  ## dont' know what kind of description am gonna provide for this 
  st.write("## User Experiance Analysis")
  
