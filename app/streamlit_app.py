import streamlit as st
import pandas as pd
from chardet import detect
from tab_df.display import display_dataframe_tab
from tab_numeric.display import display_numeric_tab
from tab_text.display import display_text_tab
from tab_date.display import display_datetime_tab

# Function to upload CSV and load data with encoding handling and automatic type conversion
def load_data():
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        try:
            raw_data = uploaded_file.read()
            encoding = detect(raw_data)['encoding']
            uploaded_file.seek(0)
            
            df = pd.read_csv(uploaded_file, encoding=encoding)
            st.success(f"File uploaded successfully with {encoding} encoding!")

            for col in df.columns:
                if df[col].dtype == 'object':
                    if pd.to_numeric(df[col], errors='coerce').notna().mean() > 0.95:
                        df[col] = pd.to_numeric(df[col], errors='coerce')
                        st.info(f"Converted '{col}' to numeric.")
                    elif pd.to_datetime(df[col], errors='coerce').notna().mean() > 0.95:
                        df[col] = pd.to_datetime(df[col], errors='coerce')
                        st.info(f"Converted '{col}' to datetime64[ns].")

            st.info("Automatic type conversion completed.")
            return df
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
    return None

# Main App
def main():
    st.title("CSV Explorer")
    st.subheader("1. Menu for uploading a CSV file")
    df = load_data()

    if df is not None:
        st.subheader("2. Tabs Container")
        tab1, tab2, tab3, tab4 = st.tabs(["DataFrame", "Numeric Series", "Text Series", "Datetime Series"])

        with tab1:
            st.header("DataFrame Overview")
            display_dataframe_tab(df)

        with tab2:
            st.header("Numeric Series")
            display_numeric_tab(df)

        with tab3:
            st.header("Text Series")
            display_text_tab(df)

        with tab4:
            st.header("Datetime Series")
            datetime_df = df.select_dtypes(include=['datetime64[ns]'])
            if not datetime_df.empty:
                display_datetime_tab(datetime_df)
            else:
                st.write("No datetime columns found.")

if __name__ == "__main__":
    main()
