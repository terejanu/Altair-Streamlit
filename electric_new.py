import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

@st.cache
def load_data():
    df = pd.read_csv('daily_electricity.csv', index_col='Date')
    return df

st.title('Electricity Production by Source')

# load the data
df = load_data()

# choose the sources of interest
cols = ['Coal_MW', 'Gas_MW', 'Hidroelectric_MW', 'Nuclear_MW', 'Wind_MW', 'Solar_MW', 'Biomass_MW']
option = st.multiselect('What sources do you want to display?', cols, cols[0])

###
start_date = datetime.strptime(df.index.min(), '%Y-%m-%d')
end_date = datetime.strptime(df.index.max(), '%Y-%m-%d')
date_range = st.slider(label='Select Date Range', min_value=start_date, max_value=end_date, value=[start_date, end_date])
###

# show the data in a table
if st.sidebar.checkbox('Show dataframe'):
    st.write( df.loc[date_range[0].strftime('%Y-%m-%d'):date_range[1].strftime('%Y-%m-%d'), option] )

# plot the data
if st.sidebar.checkbox('Show Streamlit line_chart'):
    st.line_chart( df.loc[date_range[0].strftime('%Y-%m-%d'):date_range[1].strftime('%Y-%m-%d'), option] )
else:
    fig, ax = plt.subplots()
    df.loc[date_range[0].strftime('%Y-%m-%d'):date_range[1].strftime('%Y-%m-%d'), option].plot(ax=ax)
    st.write( fig )    

# # MINI-HMW
# # TODO - when a checkbox in sidebar checked:
# #        (1) print the mean daily production for the sources selected
# #        (2) show a bar chart using the mean daily production for the sources selected
# #            (check the Streamlit API to find how a bar chart can be created)