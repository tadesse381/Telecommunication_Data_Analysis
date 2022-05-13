import numpy as np
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
# pages
import pages.home as home
import pages.marketing as marketing
import pages.engagement as enngagement
import pages.experiance as experiance
import pages.satisfaction as satisfaction

st.set_page_config(page_title="TelCo Data Analysis", layout="wide")
st.title("TelCo Data analysis")
st.sidebar.markdown("# TellCo Data Analysis")


#page = st.sidebar.selectbox('TellCo Menu', ['Intro', 'Marketing', 'Engagement', 'Experiance', 'Satisfaction'])
with st.sidebar:
  page = option_menu('TellCo Home', ['Home', 'Marketing', 'Engagement', 'Experiance', 'Satisfaction'],
                            icons=['house', 'bi-currency-exchange','house', 'gear','house'], menu_icon="cast", default_index=1)
  page
if(page == 'Home'):
  home.run()
elif(page == 'Marketing'):
  marketing.run_marketing()
elif(page == 'Engagement'):
  enngagement.run_engagement()
elif(page == 'Experiance'):
  experiance.run_experiance()
elif(page == 'Satisfaction'):
  satisfaction.run_satisfaction()
else:
  home.run()
