import numpy as np
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
# pages
import pages.home as home
import pages.marketing as marketing
import pages.engagement as enngagement
import pages.experience as experience
import pages.satisfaction as satisfaction

st.set_page_config(page_title="TellCo Data Analysis", layout="wide")
st.title("TelCo Data analysis")
st.sidebar.markdown("# TellCo Data Analysis")


#page = st.sidebar.selectbox('TellCo Menu', ['Intro', 'Marketing', 'Engagement', 'Experiance', 'Satisfaction'])
with st.sidebar:
  page = option_menu('TellCo Menu', ['Home', 'Marketing', 'Engagement', 'Experience', 'Satisfaction'],
                            icons=['house', 'bi-currency-exchange','bi-cloud-check-fill', 'bi-briefcase-fill','bi-check-square-fill'], menu_icon="cast", default_index=1)
  page
if(page == 'Home'):
  home.run()
elif(page == 'Marketing'):
  marketing.run_marketing()
elif(page == 'Engagement'):
  enngagement.run_engagement()
elif(page == 'Experience'):
  experience.run_experiance()
elif(page == 'Satisfaction'):
  satisfaction.run_satisfaction()
else:
  home.run()
