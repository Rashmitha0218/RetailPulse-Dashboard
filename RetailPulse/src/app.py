import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="RetailPulse Dashboard", layout="wide")

# Title
st.title("📊 RetailPulse Dashboard")

# Load data
df = pd.read_csv("RetailPulse/data/cleaned_retail_data.csv")
# Sidebar
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    ["Home", "Customer Segments", "Churn Prediction", "Forecasting", "Inventory"]
)

# HOME PAGE
if page == "Home":

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Shape")
    st.write(df.shape)

    if 'Country' in df.columns:

        st.subheader("Top Countries")

        country_counts = df['Country'].value_counts().head(10)

        fig, ax = plt.subplots(figsize=(10,5))

        country_counts.plot(kind='bar', ax=ax)

        st.pyplot(fig)

# CUSTOMER SEGMENTS
elif page == "Customer Segments":

    st.subheader("Customer Segments")

    try:
        seg_df = pd.read_csv("outputs/customer_segments.csv")

        st.dataframe(seg_df.head())

    except:
        st.error("customer_segments.csv not found")

# CHURN PREDICTION
elif page == "Churn Prediction":

    st.subheader("Churn Predictions")

    try:
        churn_df = pd.read_csv("outputs/churn_predictions.csv")

        st.dataframe(churn_df.head())

    except:
        st.error("churn_predictions.csv not found")

# FORECASTING PAGE
elif page == "Forecasting":

    st.subheader("Sales Forecasting")

    try:
        forecast_df = pd.read_csv("outputs/forecast.csv")

        st.dataframe(forecast_df)

    except:
        st.error("forecast.csv not found")


elif page == "Inventory":

    st.subheader("Inventory Optimization")

    try:
        inventory_df = pd.read_csv("outputs/inventory.csv")

        st.dataframe(inventory_df)

    except:
        st.error("inventory.csv not found")