import streamlit as st
import pandas as pd
import altair as alt
 
def display_datetime_statistics(df):
    st.subheader("Datetime Series Overview")
    df.columns = df.columns.map(str)
    datetime_columns = df.select_dtypes(include=['datetime64']).columns
    if len(datetime_columns) == 0:
        st.write("No valid datetime columns found in the dataset.")
        return
 
    selected_datetime = st.selectbox("Select a datetime column", datetime_columns)
 
    if selected_datetime:
        st.write(f"**Statistics for {selected_datetime}**")
        datetime_stats = pd.DataFrame({
            'Description': [
                'Number of Unique Values', 
                'Number of Rows with Missing Values', 
                'Minimum Date', 
                'Maximum Date', 
                'Number of Weekend Dates (Saturday & Sunday)', 
                'Number of Weekday Dates (Monday - Friday)', 
                'Number of Future Dates (After Today)', 
                'Number of 1900-01-01 Values', 
                'Number of 1970-01-01 Values'
            ],
            'Value': [
                df[selected_datetime].nunique(),
                df[selected_datetime].isnull().sum(),
                df[selected_datetime].min(),
                df[selected_datetime].max(),
                df[selected_datetime].dt.dayofweek.isin([5, 6]).sum(),
                df[selected_datetime].dt.dayofweek.isin([0, 1, 2, 3, 4]).sum(),
                (df[selected_datetime] > pd.Timestamp.today()).sum(),
                (df[selected_datetime] == '1900-01-01').sum(),
                (df[selected_datetime] == '1970-01-01').sum()
            ]
        })
        st.table(datetime_stats)
 
        st.write(f"**Histogram for {selected_datetime}**")
        hist_chart = alt.Chart(df).mark_bar().encode(
            alt.X(f"{selected_datetime}:T", title="Date", bin=alt.Bin(maxbins=50)),
            alt.Y('count()', title='Count of Records')
        ).properties(width=700, height=400)
        st.altair_chart(hist_chart)
 
        st.write(f"**Most Frequent Dates for {selected_datetime}**")
        most_frequent_dates = df[selected_datetime].value_counts().reset_index().head(20)
        most_frequent_dates.columns = ['Date', 'Occurrence']
        most_frequent_dates['Percentage'] = (most_frequent_dates['Occurrence'] / df.shape[0]) * 100
        st.table(most_frequent_dates)