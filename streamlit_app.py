import streamlit as st

# Sample data
websites = {
    'Productivity': [
        {'name': 'Trello', 'url': 'https://trello.com'},
        {'name': 'Asana', 'url': 'https://asana.com'},
        {'name': 'Notion', 'url': 'https://www.notion.so'},
    ],
    'Design': [
        {'name': 'Figma', 'url': 'https://www.figma.com'},
        {'name': 'Sketch', 'url': 'https://www.sketch.com'},
        {'name': 'Canva', 'url': 'https://www.canva.com'},
    ],
    'Marketing': [
        {'name': 'HubSpot', 'url': 'https://www.hubspot.com'},
        {'name': 'Google Analytics', 'url': 'https://analytics.google.com'},
        {'name': 'Mailchimp', 'url': 'https://mailchimp.com'},
    ],
}

# Sidebar - Categories
categories = list(websites.keys())
selected_category = st.sidebar.selectbox('Select a category', ['All'] + categories)

# Search bar
search_query = st.sidebar.text_input('Search for a website')

# Filter websites based on category and search query
filtered_websites = []
for category, websites_list in websites.items():
    if selected_category == 'All' or selected_category == category:
        if search_query:
            filtered_websites += [website for website in websites_list if search_query.lower() in website['name'].lower()]
        else:
            filtered_websites += websites_list

# Display filtered websites
if filtered_websites:
    st.write(f"Found {len(filtered_websites)} websites")
    for website in filtered_websites:
        st.write(f"- [{website['name']}]({website['url']})")
else:
    st.write("No websites found")

