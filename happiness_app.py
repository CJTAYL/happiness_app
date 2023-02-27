# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ad5jn3x3MdL4zkXwHu3aK8lkp1YRpk7S
"""

import pandas as pd
import altair as alt
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="World Happiness Report", page_icon=":tada:")

# --- SIDEBAR MENU ---
with st.sidebar:
    select = option_menu(
        menu_title=None,
        options=['Background', 'All Countries', 'Influential Variables', 'Americas', 'Africa and Middle East', 'Asia', 'Europe', 'Oceania']
        )

url = "https://raw.githubusercontent.com/CJTAYL/happiness_app/main/2016.csv"

data = pd.read_csv(url)

selection = alt.selection_multi(fields = ['Region'], bind = 'legend')

america = data.loc[(data['Region'] == 'North America') | (data['Region'] == 'Latin America and Caribbean')]
aus_nz = data.loc[data['Region'] == 'Australia and New Zealand']
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

all = alt.Chart(data).mark_bar().encode(
    x=alt.X('sum(Happiness Score)', title='Happiness Score'),
    y=alt.Y('Country', sort='-x', title = ''),
    color='Region',
    tooltip=['Country', 'Happiness Score']
).properties(
    title='All Countries'
)

africa_me = alt.Chart(africa_me).mark_bar().encode(
    x=alt.X('sum(Happiness Score)', title='Happiness Score'),
    y=alt.Y('Country', sort='-x', title = ''),
    color='Region',
    tooltip=['Country', 'Happiness Score']
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

euro = alt.Chart(euro).mark_bar().encode(
    x=alt.X('sum(Happiness Score)', title='Happiness Score'),
    y=alt.Y('Country', sort='-x', title = ''),
    color='Region',
    tooltip=['Country', 'Happiness Score']
)

oceania = alt.Chart(aus_nz).mark_bar().encode(
    x=alt.X('sum(Happiness Score)', title='Happiness Score'),
    y=alt.Y('Country', sort='-x', title = ''),
    color='Region',
    tooltip=['Country', 'Happiness Score']
)

if select == 'Background':
    st.header('World Happiness Report - 2016')
    st.write("The data for this app were collected by the United Nations and shared through Kaggle.")
    st.write("A comprehensive description of the World Happiness Report can be found on Wikipedia.")
    st.write("""
        Although the World Happiness Report is published annually and provides a wealth of information, 
        one feature it lacks is interactive graphs. The dashboard presented below is intended to augment the annual report
        and provide users with additional information and control.
        """)
    st.write("App created by Chris Taylor")

if select == 'All Countries':
    st.header('All Countries')
    st.altair_chart(hist, use_container_width=True)
    st.altair_chart(all, use_container_width=True) 

if select == 'Africa and Middle East':
    st.header('Africa and Middle East')
    st.altair_chart(africa_me, use_container_width=True)
    
if select == 'Americas':
    st.header('Latin and North America')
    st.altair_chart(americas, use_container_width=True)

if select == 'Asia':
    st.header('Asia')
    st.altair_chart(asias, use_container_width=True)
    
if select == 'Europe':
    st.header('Europe')
    st.altair_chart(euro, use_container_width=True)
    
if select == 'Oceania':
    st.header('Oceania')
    st.altair_chart(oceania, use_container_width=True)


