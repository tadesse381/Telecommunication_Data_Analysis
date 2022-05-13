import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import scripts.ploting as plot
import scripts.utils as utils
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
  plot_bar(result, result['Handset Type'], result['Total TCP Retrans'], 'Highest Total TCP Retrans Handsets','','')
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
  # new_netwok_df["Handset Type"] = [catagory[x] for x in new_netwok_df["Handset Type"]]
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
  plot_scatter(experiance_df,"Total Throughput", "Total RTT","Clustering with Kmean", "cluster-experiance", "")
  experiance_df['cluster-experiance'].value_counts()
  ## dont' know what kind of description am gonna provide for this 
  st.write("## User Experiance Analysis")
  
