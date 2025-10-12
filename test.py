import streamlit as st
import plotly.express as px
import pandas as pd


url = 'https://raw.githubusercontent.com/nurinn-bot/EC2024/refs/heads/main/arts_df_exported.csv'
arts_df = pd.read_csv(url)

display(arts_df.head())
# Count the occurrences of each gender
gender_counts = arts_df['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']

# Create a pie chart using Plotly
fig = px.pie(
    gender_counts,
    names='Gender',
    values='Count',
    title='Distribution of Gender in Arts Faculty',
    color_discrete_sequence=px.colors.qualitative.Pastel,  # optional for nice colors
)

# Display the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)

st.set_page_config(
    page_title="Genetic Algorithm"
)

st.header("Scientific Visualzation", divider="gray")


# Count the occurrences of each gender
gender_counts = arts_df['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']

# Create a pie chart using Plotly
fig = px.pie(
    gender_counts,
    names='Gender',
    values='Count',
    title='Distribution of Gender in Arts Faculty',
    color_discrete_sequence=px.colors.qualitative.Pastel,  # optional for nice colors
)

# Display the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Count the occurrences of each gender
gender_counts = arts_df['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']

# Create a pie chart using Plotly
fig = px.pie(
    gender_counts,
    names='Gender',
    values='Count',
    title='Distribution of Gender in Arts Faculty',
    color_discrete_sequence=px.colors.qualitative.Pastel,  # optional for nice colors
)

# Display the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Count the occurrences of each gender
gender_counts = arts_df['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']

# Create a bar chart using Plotly
fig = px.bar(
    gender_counts,
    x='Gender',
    y='Count',
    title='Distribution of Gender in Arts Faculty',
    text='Count',  # show count labels on bars
    color='Gender',  # optional: color by gender
    color_discrete_sequence=px.colors.qualitative.Pastel  # optional nice colors
)

# Customize layout
fig.update_traces(textposition='outside')
fig.update_layout(
    xaxis_title='Gender',
    yaxis_title='Count',
    uniformtext_minsize=8,
    uniformtext_mode='hide'
)

# Display the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)
