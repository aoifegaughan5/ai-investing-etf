import streamlit as st
import pandas as pd
import numpy as np
import os
from etf_ai import picking_top_etf

# Define ETFs for different risk levels
# Grouping these tickers based on how much risk they're associated with.
ETF = {
    "Low": ["VTI", "BND", "SPY"],
    "Medium": ["VOO", "VXUS", "QQQ"],
    "High": ["BITO", "XBI", "ARKK"]
}

# Initialise session state variables only if they don't exist
if "selected_etfs" not in st.session_state:
    # Track selected ETFs separately for each risk level
    st.session_state.selected_etfs = {"Low": [], "Medium": [], "High": []}
if "top_etf" not in st.session_state:
    st.session_state.top_etf = None
if "selected_risk" not in st.session_state:
    st.session_state.selected_risk = "Low"  # Default risk level

# Building the Streamlit UI
st.title("📊 AI ETF Investment Advisor")
st.write("Select your risk level, and we will suggest the best ETF (ticker) for you based on risk-adjusted performance!")

# Letting user choose a risk level
risk_level = st.selectbox(
    "Please select your Risk Level:", 
    ["Low", "Medium", "High"], 
    index=["Low", "Medium", "High"].index(st.session_state.selected_risk),
    key="selected_risk"
)

# Find Best ETF button on their selected risk level 
if st.button("Find Best ETF (ticker)"):
    top_etf = picking_top_etf(
        st.session_state.selected_risk,
        exclude_etfs=st.session_state.selected_etfs[st.session_state.selected_risk]
    )
    if isinstance(top_etf, dict):
        # Append the ticker to the list corresponding to the selected risk level
        st.session_state.selected_etfs[st.session_state.selected_risk].append(top_etf["ETF"])
        st.session_state.top_etf = top_etf
        st.rerun()  # Refresh UI to update ETF selection
    else:
        st.error("There are no more ETFs available for this risk level. Please try another.")

# Display selected ETF details if available
if st.session_state.top_etf and isinstance(st.session_state.top_etf, dict):
    top_etf = st.session_state.top_etf
    # The success message now shows the ETF ticker and its Sharpe Ratio.
    st.success(
        f"📈 Best ETF ticker for {st.session_state.selected_risk} investors: {top_etf['ETF']} | Sharpe Ratio: {float(top_etf['Sharpe Ratio']):.2f}"
    )
    st.write(f"**Annual Returns**: {float(top_etf['Annual returns']):.2%}")
    st.write(f"**Volatility**: {float(top_etf['Volatility']):.2%}")
    st.write("📌 A higher Sharpe Ratio means better risk-adjusted performance.")

# Button to check another ETF in the same risk level
if st.button("Check Another ETF in the Same Risk Level"):
    # Make sure you haven't already checked all available ETFs for this category.
    if len(st.session_state.selected_etfs[st.session_state.selected_risk]) >= len(ETF[st.session_state.selected_risk]):
        st.error("You've already checked all available ETFs in this category!")
    else:
        new_etf = picking_top_etf(
            st.session_state.selected_risk,
            exclude_etfs=st.session_state.selected_etfs[st.session_state.selected_risk]
        )
        if isinstance(new_etf, dict):
            st.session_state.selected_etfs[st.session_state.selected_risk].append(new_etf["ETF"])
            st.session_state.top_etf = new_etf
            st.rerun()  # Refresh UI to update ETF selection.
        else:
            st.error("No new ETF found.")

# Reset button to clear your ETF selections for the current risk level.
if st.button("Reset Selection"):
    st.session_state.selected_etfs[st.session_state.selected_risk] = []
    st.session_state.top_etf = None
    st.rerun()  # Refresh UI
