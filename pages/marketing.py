import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

import scripts.ploting as plot


st.set_option('deprecation.showPyplotGlobalUse', False)
def pareto_plot(df, x=None, y=None, title=None, show_pct_y=False, pct_format='{0:.0%}'):
    xlabel = x
    ylabel = y
    tmp = df.sort_values(y, ascending=False)
    x = tmp[x].values
    y = tmp[y].values
    weights = y / y.sum()
    cumsum = weights.cumsum()
    
    fig, ax1 = plt.subplots()
    ax1.bar(x, y)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)

    ax2 = ax1.twinx()
    ax2.plot(x, cumsum, '-ro', alpha=0.5)
    ax2.set_ylabel('', color='r')
    ax2.tick_params('y', colors='r')
    
    vals = ax2.get_yticks()
    ax2.set_yticklabels(['{:,.2%}'.format(x) for x in vals])

    # hide y-labels on right side
    if not show_pct_y:
        ax2.set_yticks([])
    
    formatted_weights = [pct_format.format(x) for x in cumsum]
    for i, txt in enumerate(formatted_weights):
        ax2.annotate(txt, (x[i], cumsum[i]), fontweight='heavy')    
    
    if title:
        plt.title(title)
    
    plt.tight_layout()
    plt.show()

def run_marketing():
  st.write("## Marketing Analysis")

  file_name = 'data/clean_telecommunication_data.csv'
  df_clean = pd.read_csv(file_name)
  
  top_10_handset = df_clean.groupby("Handset Type")['MSISDN/Number'].nunique().nlargest(10)
  top_3_manufacturers = df_clean.groupby("Handset Manufacturer")['MSISDN/Number'].nunique().nlargest(3)
  pareto_plot(top_3_manufacturers, x='MSISDN/Number', y='Handset Manufacturer', title='Top 3 handset manufacturers')

  fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(12,7))

  plot.serious_bar(top_3_manufacturers, ax1)
  plot.serious_bar(top_10_handset, ax2)
  plt.xticks(rotation=75)
  st.pyplot()

  st.write("## Analysis Insight")
  st.write("From The above two graphes, the Most sold phone rancking number 1 is Huawei B528S-23A \
    And The Number one Manufacturer is Apple. So, when we look at the handset next to Huawei most of them are \
      Products of Apple. ")
  st.write("## So this shows, The Marketing Team Need to focus on selling Apple Products")
