import numpy as np
import pandas as pd
import streamlit as st

# pages
import pages.intro as intro
import pages.marketing as marketing
import pages.engagement as enngagement
import pages.experiance as experiance
import pages.satisfaction as satisfaction

st.set_page_config(page_title="TelCo Data Analysis", layout="wide")
st.title("TelCo Data analysis")
st.sidebar.markdown("# TellCo Data Analysis")


#page = st.sidebar.selectbox('TellCo Menu', ['Intro', 'Marketing', 'Engagement', 'Experiance', 'Satisfaction'])
page = st.sidebar.option_menu('TellCo Menu', ['Intro', 'Marketing', 'Engagement', 'Experiance', 'Satisfaction'],
                            icons=['house', 'gear','house', 'gear','house'], menu_icon="cast", default_index=1)
if(page == 'Intro'):
  intro.run()
elif(page == 'Marketing'):
  marketing.run_marketing()
elif(page == 'Engagement'):
  enngagement.run_engagement()
elif(page == 'Experiance'):
  experiance.run_experiance()
elif(page == 'Satisfaction'):
  satisfaction.run_satisfaction()
else:
  intro.run()
