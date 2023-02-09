import streamlit as st
import altair as alt
import pandas as pd
import matplotlib.pyplot as plt

# DATA
df = pd.DataFrame({ 
    'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
})

# Bar Chart
alt_fig = alt.Chart(df).mark_bar().encode(
    x='a',
    y='b'
).properties(
    width=600,
    height=400
).interactive()

# Show 
st.write(alt_fig)