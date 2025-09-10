import streamlit as st
import pandas as pd

def display_overview(df):
    st.subheader("DataFrame Overview")
    st.write("**Basic Information**")
    basic_info = pd.DataFrame({
        'Description': [
            'Number of Rows', 
            'Number of Columns', 
            'Number of Duplicated Rows', 
            'Number of Rows with Missing Values'
        ],
        'Value': [
            df.shape[0],
            df.shape[1],
            df.duplicated().sum(),
            df.isnull().any(axis=1).sum()
        ]
    })
    st.table(basic_info)

    st.write("**Column Information**")
    column_info = pd.DataFrame({
        'Column': df.columns,
        'Data Type': df.dtypes.values,
        'Memory Usage (bytes)': df.memory_usage(deep=True, index=False).values
    })
    st.table(column_info)

def display_interactive_exploration(df):
    st.write("**Explore DataFrame**")
    row_selection = st.slider("Select the number of rows to be displayed", min_value=5, max_value=50, value=5, step=5)
    exploration_method = st.radio("Exploration Method", options=['Head', 'Tail', 'Sample'])

    if exploration_method == 'Head':
        st.write(df.head(row_selection))
    elif exploration_method == 'Tail':
        st.write(df.tail(row_selection))
    else:
        st.write(df.sample(row_selection))
