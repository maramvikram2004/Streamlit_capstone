import streamlit as st
import pandas as pd

# Title of the Streamlit app
st.title("Urban Navigator: Metro Site Predictor")

# Sidebar for dataset upload
st.sidebar.header("Upload Your Dataset")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        # Load the dataset
        df = pd.read_csv(uploaded_file)
        st.success("Dataset loaded successfully!")

        # Display the column names in the dataset
        st.write("### Available Columns in the Dataset")
        st.write(df.columns.tolist())

        # Multi-select widget to select columns to display
        st.write("### Select Columns to View Details:")
        default_columns = ["name", "pop_den", "hospitals", "rent", "traffic", "city"]
        valid_defaults = [col for col in default_columns if col in df.columns]

        columns = st.multiselect(
            "Select columns:",
            options=df.columns.tolist(),
            default=valid_defaults
        )

        # Display selected columns from the dataset
        if columns:
            st.write("### Selected Columns:")
            st.dataframe(df[columns])
        else:
            st.warning("No columns selected. Please choose at least one column.")

    except Exception as e:
        st.error(f"Error loading the dataset: {e}")

else:
    st.info("Please upload a CSV file to proceed.")

# Footer
st.sidebar.markdown("---")
st.sidebar.text("Urban Metro Site Predictor v1.0")


