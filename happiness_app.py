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

gdp = alt.Chart(data).mark_point().encode(
    x='Economy (GDP per Capita)', 
    y='Happiness Score',
    color='Region', 
    opacity = alt.condition(selection, alt.value(1), alt.value(.1)),
    tooltip=['Country', 'Region', 'Happiness Score', 'Economy (GDP per Capita)']
    ).properties(
        title = 'GDP and Happiness'
    ).add_selection(
        selection
    )

family = alt.Chart(data).mark_point().encode(
    x='Family',
    y='Happiness Score',
    color='Region',
    opacity = alt.condition(selection, alt.value(1), alt.value(.1)),
    tooltip=['Country', 'Region', 'Happiness Score', 'Family']
    ).properties(
        title = 'Family and Happiness'
    ).add_selection(
        selection
    )

freedom = alt.Chart(data).mark_point().encode(
    x='Freedom',
    y='Happiness Score',
    color='Region',
    opacity = alt.condition(selection, alt.value(1), alt.value(.1)),
    tooltip=['Country', 'Region', 'Happiness Score', 'Freedom']
    ).properties(
        title = 'Freedom and Happiness'
    ).add_selection(
        selection
    )

health = alt.Chart(data).mark_point().encode(
    x='Health (Life Expectancy)',
    y='Happiness Score',
    color='Region',
    opacity = alt.condition(selection, alt.value(1), alt.value(.1)),
    tooltip=['Country', 'Region', 'Happiness Score', 'Health (Life Expectancy)']
    ).properties(
        title = 'Life Expectancy and Happiness'
    ).add_selection(
        selection
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

st.altair_chart(gdp, use_container_width=True)

st.altair_chart(family, use_container_width=True)

st.altair_chart(freedom, use_container_width=True)

st.altair_chart(health, use_container_width=True)

st.write("App created by Chris Taylor")

