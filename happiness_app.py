# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ad5jn3x3MdL4zkXwHu3aK8lkp1YRpk7S
"""

import pandas as pd
import altair as alt
import streamlit as st

url = "https://raw.githubusercontent.com/CJTAYL/happiness_app/main/2016.csv"

data = pd.read_csv(url)

selection = alt.selection_multi(fields = ['Region'], bind = 'legend')

hist = alt.Chart(data).mark_bar().encode(
    alt.X('Happiness Score', bin=alt.BinParams(maxbins=8)),
    y='count()',
    color='Region',
    tooltip=['Country']
    ).properties(
    title='Histogram of Happiness Scores'
    )

st.header("World Happiness Report Data - 2016")
st.write("The data for this app were collected by the United Nations and shared through Kaggle.")
st.write("""
        The World Happiness Report is a 
        Although the World Happiness Report is published annually and provides a wealth of information, one feature it lacks The interactive charts below display results from the World Happiness Report in 2016. 
        The data may be filtered by selecting a specific region from the legend. 
        The filter may be reset by clicking on any area of the chart.
        """)

st.altair_chart(hist, use_container_width=True)
st.write('In 2016, the mean Happiness Score was 5.38')
st.write('To provide a fine grained analysis') 
st.write("App created by Chris Taylor")

