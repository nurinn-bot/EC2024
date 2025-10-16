import streamlit as st
import pandas as pd
import plotly.express as px

# --- Streamlit Configuration ---
st.set_page_config(
    page_title="Arts Faculty Gender Visualization",
    layout="wide"
)

st.header("Arts Faculty Data Analysis and Visualization 📊", divider="blue")

# ######################################################################
# --- 1. DATA LOADING FROM URL (Replaced Dummy Data) ---
url = 'https://raw.githubusercontent.com/izzatimahrup/SV2025/refs/heads/main/arts_student_survey_output.csv'

# Load data from the remote CSV file
# Consider using @st.cache_data for improved performance in a real Streamlit app
arts_df = pd.read_csv(url)

# Calculate the counts and reset the index to create a Plotly-friendly DataFrame
# Assumes the loaded CSV has a column named 'Gender'
gender_counts_df = arts_df['Gender'].value_counts().reset_index()
gender_counts_df.columns = ['Gender', 'Count']

st.write("Data summary (Counts):")
st.dataframe(gender_counts_df, hide_index=True)

# ----------------------------------------------------------------------
## Bar Chart (Plotly Express)

st.subheader("Gender Distribution: Bar Chart")

# Create the Plotly Bar Chart
fig_bar = px.bar(
    gender_counts_df,
    x='Gender',
    y='Count',
    title='Distribution of Gender in Arts Faculty (Bar Chart)',
    color='Gender', # Color bars by gender
    labels={'Count': 'Number of Students', 'Gender': 'Student Gender'},
    template='plotly_white'
)

# Customize the layout
fig_bar.update_layout(
    xaxis={'categoryorder':'total descending'}, # Order bars by count
    margin=dict(t=50, l=0, r=0, b=0) # Adjust margins
)

# Display the chart in Streamlit
st.plotly_chart(fig_bar, use_container_width=True)

# ----------------------------------------------------------------------
## Pie Chart (Plotly Express)

st.subheader("Gender Distribution: Pie Chart")

# Create the Plotly Pie Chart
fig_pie = px.pie(
    gender_counts_df,
    names='Gender',
    values='Count',
    title='Distribution of Gender in Arts Faculty (Pie Chart)',
    hole=0.4, # Creates a donut chart (optional)
    color='Gender'
)

# Customize the traces for better text display
fig_pie.update_traces(
    textposition='inside',
    textinfo='percent+label', # Shows percentage and label (gender)
    marker=dict(line=dict(color='#000000', width=1)),
)

# Update layout for a better circular appearance
fig_pie.update_layout(
    margin=dict(t=50, l=0, r=0, b=0)
)

# Display the chart in Streamlit
# Note: use_container_width=False is often better for preserving the circular shape
st.plotly_chart(fig_pie, use_container_width=False)

# Count the occurrences of each academic year
academic_year_counts = arts_df['Bachelor  Academic Year in EU'].value_counts().reset_index()
academic_year_counts.columns = ['Academic Year', 'Count']

# Create a bar chart using Plotly
fig = px.bar(
    academic_year_counts,
    x='Academic Year',
    y='Count',
    title='Distribution of Bachelor Academic Year in Arts Faculty',
    text='Count',
    color='Academic Year',  # optional: adds color variation by category
    color_discrete_sequence=px.colors.qualitative.Pastel  # optional: soft color palette
)

# Customize layout and labels
fig.update_traces(textposition='outside')
fig.update_layout(
    xaxis_title='Academic Year',
    yaxis_title='Count',
    xaxis_tickangle=-45,  # rotate x-axis labels
    uniformtext_minsize=8,
    uniformtext_mode='hide',
    margin=dict(l=20, r=20, t=60, b=60)
)

# Display in Streamlit
st.plotly_chart(fig, use_container_width=True)

