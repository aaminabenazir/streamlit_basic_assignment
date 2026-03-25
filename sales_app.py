import streamlit as st
import pandas as pd

# Title and subheader
st.title("Sales Summary Dashboard")
st.subheader("Interactive sales data filtered by category")

# Hardcoded dataset (at least 5 rows, 3 columns)
data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Headphones", "Webcam","phone"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Electronics", "Accessories", "Electronics","electronics"],
    "Sales": [45000, 1200, 2500, 18000, 8500, 3200, 6500,7000]
}

df = pd.DataFrame(data)

# Task 2: Sidebar filter
st.sidebar.title("Filters")
selected_category = st.sidebar.selectbox(
    "Select Category",
    options=df["Category"].unique(),
    index=0
)

# Filter the dataframe based on selection
filtered_df = df[df["Category"] == selected_category]

# Display in main area
st.write(f"### Showing data for category: *{selected_category}*")
st.dataframe(filtered_df)

# Line chart for Sales
st.write("### Sales Trend")
st.line_chart(filtered_df.set_index("Product")["Sales"])