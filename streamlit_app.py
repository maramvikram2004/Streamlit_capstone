import pandas as pd
import streamlit as st
import altair as alt

# Streamlit page configuration
st.set_page_config(page_title="Urban Metro Station Site Predictor", page_icon="🚇")
st.title("Urban Metro Station Site Predictor")

st.write(
    """
    Explore population density, schools, hospitals, rent, traffic, and other metrics for Chandigarh's urban areas.
    """
)

# Load Excel dataset
@st.cache_data
def load_data():
    file_path = "chandigarh_test.csv"  # Replace with your CSV file path
    return pd.read_csv(file_path)

df = load_data()

columns = st.multiselect(
    "Select columns to view details:",
    df.columns.tolist(),
    ["name", "pop_den", "hospitals", "rent", "traffic", "city"],  # Default columns
)

# Filter the dataset to display only selected columns
filtered_df = df[columns]

# Display the filtered table
st.write("### Selected Area Details")
st.dataframe(filtered_df)

# Visualization section
st.write("### Visualize Selected Data")

# Allow the user to choose the X and Y axes
x_axis = st.selectbox("Select X-axis column:", filtered_df.columns, index=0)
y_axis = st.selectbox("Select Y-axis column:", filtered_df.columns, index=1)

# Altair chart to display visualization
chart = (
    alt.Chart(filtered_df)
    .mark_circle(size=80, color="steelblue")
    .encode(
        x=alt.X(x_axis, title=f"{x_axis}"),
        y=alt.Y(y_axis, title=f"{y_axis}"),
        tooltip=columns,  # Show tooltips for all selected columns
    )
    .interactive()
)

# Render chart
st.altair_chart(chart, use_container_width=True)

