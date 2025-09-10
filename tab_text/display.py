import streamlit as st
from .logics import display_text_statistics

def display_text_tab(df):
    display_text_statistics(df)
