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

america = data.loc[(data['Region'] == 'North America') | (data['Region'] == 'Latin America and Caribbean')]
aus_nz = data.loc[data['Region'] == 'Austrailia and New Zealand']
euro = data.loc[(data['Region'] == 'Central and Eastern Europe') | (data['Region'] == 'Western Europe')]
asia = data.loc[(data['Region'] == 'Eastern Asia') | (data['Region'] == 'Southern Asia') | (data['Region'] == 'Southeastern Asia')]
africa_me = data.loc[(data['Region'] == 'Middle East and Northern Africa') | (data['Region'] == 'Sub-Saharan Africa')]

hist = alt.Chart(data).mark_bar().encode(
    alt.X('Happiness Score', bin=alt.BinParams(maxbins=8)),
    y='count()',
    color='Region',
    tooltip=['Country']
    ).properties(
    title='Histogram of Happiness Scores'
    )

americas = alt.Chart(america).mark_bar().encode(
    x=alt.X('sum(Happiness Score)', title='Happiness Score'),
    y=alt.Y('Country', sort='-x', title = ''),
    color='Region',
    tooltip=['Country', 'Happiness Score']
)

asias = alt.Chart(asia).mark_bar().encode(
    x=alt.X('sum(Happiness Score)', title='Happiness Score'),
    y=alt.Y('Country', sort='-x', title = ''),
    color='Region',
    tooltip=['Country', 'Happiness Score']
)

st.header("World Happiness Report Data - 2016")
st.write("The data for this app were collected by the United Nations and shared through Kaggle.")
st.write("A comprehensive description of the World Happiness Report can be found on Wikipedia.")
st.write("""
        Although the World Happiness Report is published annually and provides a wealth of information, 
        one feature it lacks is interactive graphs. The dashboard presented below is intended to augment the annual report
        and provide users with additional information and control.
        """)

st.altair_chart(hist, use_container_width=True)
st.write('In 2016, the mean Happiness Score was 5.38')
st.write('To provide a fine grained analysis, regions from around the world were grouped together based on proximity.') 
st.header('Latin and North America')
st.altair_chart(americas, use_container_width=True)
st.header('Asia')
st.altair_chart(asias, use_container_width=True)
st.write("App created by Chris Taylor")

