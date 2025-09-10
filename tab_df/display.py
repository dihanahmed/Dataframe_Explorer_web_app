import streamlit as st
import pandas as pd
from .logics import display_overview, display_interactive_exploration

# Main function to call in this tab
def display_dataframe_tab(df):
    display_overview(df)
    display_interactive_exploration(df)
