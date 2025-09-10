import streamlit as st
import pandas as pd
import altair as alt

def display_text_statistics(df):
    st.subheader("Text Series Overview")
    df.columns = df.columns.map(str)
    text_columns = df.select_dtypes(include=['object']).columns
    if len(text_columns) == 0:
        st.write("No text columns found in the dataset.")
        return
    
    selected_text = st.selectbox("Select a text column", text_columns)

    if selected_text:
        text_data = df[selected_text].astype(str)
        text_data = text_data.replace(['', 'nan', 'NaT'], '<MISSING>').fillna('<MISSING>')
        unique_values_count = text_data.nunique()

        if unique_values_count <= 1:
            st.write(f"The column `{selected_text}` contains only {unique_values_count} unique value(s), so no meaningful analysis can be performed.")
            return

        st.write(f"**Statistics for {selected_text}**")
        text_stats = pd.DataFrame({
            'Description': [
                'Number of Unique Values', 
                'Number of Rows with Missing Values', 
                'Number of Rows with Empty Strings', 
                'Number of Rows with Only Whitespaces', 
                'Number of Rows with Only Lowercase Characters', 
                'Number of Rows with Only Uppercase Characters', 
                'Number of Rows with Only Alphabet Characters', 
                'Number of Rows with Only Digits', 
                'Mode Value'
            ],
            'Value': [
                text_data.nunique(),
                (df[selected_text].isnull()).sum(),
                (text_data == '').sum(),
                text_data.str.isspace().sum(),
                text_data.str.islower().sum(),
                text_data.str.isupper().sum(),
                text_data.str.isalpha().sum(),
                text_data.str.isdigit().sum(),
                text_data.mode()[0] if not text_data.mode().empty and text_data.mode()[0] != '<MISSING>' else "<No Mode>"
            ]
        })
        st.table(text_stats)

        st.write(f"**Bar Chart of Most Frequent Values for {selected_text}**")
        most_frequent_values = text_data.value_counts().reset_index().head(20)
        most_frequent_values.columns = ['Value', 'Occurrence']
        most_frequent_values['Percentage'] = (most_frequent_values['Occurrence'] / df.shape[0]) * 100
        
        bar_chart = alt.Chart(most_frequent_values).mark_bar().encode(
            x=alt.X('Value:N', sort='-y'),
            y=alt.Y('Occurrence:Q', title='Count of Records')
        ).properties(width=700, height=400)
        st.altair_chart(bar_chart)

        st.write(f"**Most Frequent Values for {selected_text}**")
        st.table(most_frequent_values)
