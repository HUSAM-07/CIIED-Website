import streamlit as st
import pandas as pd

# Load the data
df = pd.read_csv('founders_resources.csv')

# Create a search bar
search_bar = st.text_input('Search for a website:')

# Search for the website
if search_bar:
    results = df[df['Website'].str.contains(search_bar)]

    # Display the results
    if results.empty:
        st.write('No results found.')
    else:
        st.table(results)

# Display the categories
categories = df['Category'].unique()

# Create a dropdown menu for the categories
category_dropdown = st.selectbox('Select a category:', categories)

# Filter the data by category
if category_dropdown:
    results = df[df['Category'] == category_dropdown]

    # Display the results
    if results.empty:
        st.write('No results found.')
    else:
        st.table(results)
