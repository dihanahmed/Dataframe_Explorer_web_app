import streamlit as st
from .logics import display_datetime_statistics
 
def display_datetime_tab(df):
    display_datetime_statistics(df)