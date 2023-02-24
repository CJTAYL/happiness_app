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

st.header("World Happiness Report - 2016")
st.write("The data for this app were collected by the United Nation through the World Happiness Report and shared with Kaggle.")
st.write("""
        The interactive chart below displays results from the World Happiness Report in 2016. 
        The data may be filtered by selecting a specific region from the legend.
        """)

st.altair_chart(gdp, use_container_width=True)

st.altair_chart(family, use_container_width=True)

st.altair_chart(freedom, use_container_width=True)

st.altair_chart(health, use_container_width=True)

st.write("App created by Chris Taylor")

