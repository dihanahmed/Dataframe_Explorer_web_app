import streamlit as st
import pandas as pd
import altair as alt

def display_numeric_statistics(df):
    st.subheader("Numeric Series Overview")
    df.columns = df.columns.map(str)
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    if len(numeric_columns) == 0:
        st.write("No numeric columns found in the dataset.")
        return
    
    selected_numeric = st.selectbox("Select a numeric column", numeric_columns)

    if selected_numeric:
        st.write(f"**Statistics for {selected_numeric}**")
        numeric_stats = pd.DataFrame({
            'Description': [
                'Number of Unique Values', 
                'Number of Rows with Missing Values', 
                'Number of Rows with 0 Value', 
                'Number of Negative Values', 
                'Average Value', 
                'Standard Deviation Value', 
                'Minimum Value', 
                'Maximum Value', 
                'Median Value'
            ],
            'Value': [
                df[selected_numeric].nunique(),
                df[selected_numeric].isnull().sum(),
                (df[selected_numeric] == 0).sum(),
                (df[selected_numeric] < 0).sum(),
                df[selected_numeric].mean(),
                df[selected_numeric].std(),
                df[selected_numeric].min(),
                df[selected_numeric].max(),
                df[selected_numeric].median()
            ]
        })
        st.table(numeric_stats)

        safe_selected_numeric = selected_numeric.replace(':', '\\:')
        st.write(f"**Histogram for {selected_numeric}**")
        hist_chart = alt.Chart(df).mark_bar().encode(
            alt.X(f"{safe_selected_numeric}:Q", bin=True),
            alt.Y('count()', title='Count of Records')
        ).properties(width=700, height=400)
        st.altair_chart(hist_chart)

        st.write(f"**Most Frequent Values for {selected_numeric}**")
        most_frequent_values = df[selected_numeric].value_counts().reset_index().head(20)
        most_frequent_values.columns = ['Value', 'Occurrence']
        most_frequent_values['Percentage'] = (most_frequent_values['Occurrence'] / df.shape[0]) * 100
        st.table(most_frequent_values)
