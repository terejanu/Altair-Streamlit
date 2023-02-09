import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data():
    df = pd.read_csv('daily_electricity.csv', index_col='Date')
    return df

st.title('Electricity Production by Source')

# load the data
df = load_data()

# show the data in a table
if st.sidebar.checkbox('Show dataframe'):
    st.write(df)

# choose the sources of interest
cols = ['Coal_MW', 'Gas_MW', 'Hidroelectric_MW', 'Nuclear_MW', 'Wind_MW', 'Solar_MW', 'Biomass_MW']
option = st.multiselect('What sources do you want to display?', cols, cols[0])

# plot the data
if st.sidebar.checkbox('Show Streamlit line_chart'):
    st.line_chart( df[option] )
else:
    fig, ax = plt.subplots()
    df[option].plot(ax=ax)
    st.write( fig )    

# # MINI-HMW
# # TODO - when a checkbox in sidebar checked:
# #        (1) print the mean daily production for the sources selected
# #        (2) show a bar chart using the mean daily production for the sources selected
# #            (check the Streamlit API to find how a bar chart can be created)