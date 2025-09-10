import streamlit as st
from .logics import display_numeric_statistics

def display_numeric_tab(df):
    display_numeric_statistics(df)
