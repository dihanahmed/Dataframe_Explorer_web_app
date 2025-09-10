# Dataframe Explorer

## Author
Hasnaine Ahmed Dihan
## Description
The Dataframe Explorer is a web application for exploratory data analysis (EDA) using Streamlit. It allows users to upload CSV files and analyze their data through various statistical and visualization features. This tool provides functionality to examine numeric and categorical columns, including viewing unique values, identifying missing values, and computing statistical metrics such as mean, median, standard deviation, etc.

Some of the challenges faced during development included integrating diverse data types within a single, cohesive analysis framework, ensuring compatibility with different CSV formats, and writing comprehensive tests to validate each function’s accuracy. Future features planned for implementation include enhanced data visualization options, custom filtering tools, and support for additional file formats.

## How to Setup
Clone the Repository:
#### `git clone https://github.com/dihanahmed/Dataframe_Explorer_web_app`
#### `cd app\`

Set Up Virtual Environment:
Create a virtual environment using Python 3.10 (or the latest compatible version):
#### `python3 -m venv env`

Activate the virtual environment:
#### `.\env\Scripts\activate`

Install Dependencies:
#### `python3 -m pip install -r requirements.txt`

Python Version: This application was developed and tested using Python 3.10.

Required Packages:
Pandas: For data manipulation
Streamlit: For building the web application interface
unittest: For testing functionality
Additional packages, if needed, can be found in requirements.txt.

## How to Run the Program
1. Start the Streamlit App: From the project root directory, run:
#### `python3 -m streamlit run app/streamlit_app.py`

2. Upload a CSV:
Once the app is running, upload a CSV file to explore its data.
Use the provided buttons and features to analyze the columns, view statistical summaries, and generate visualizations.


## Project Structure
app/streamlit_app.py — main Streamlit app: uploads CSV with encoding detection (chardet), performs light auto type conversion, and wires up four tabs (DataFrame, Numeric, Text, Datetime). 

app/tab_df/ — DataFrame tab: overview (rows, columns, duplicates, missing; dtype/memory table) and interactive head/tail/sample explorer. Exposed via display_dataframe_tab. 

app/tab_numeric/ — Numeric tab: pick a numeric column, show stats (unique/missing/zeros/negatives/mean/std/min/max/median), Altair histogram, and top values. Exposed via display_numeric_tab. 

app/tab_text/ — Text tab: pick a text column, normalize empties, show text-centric stats (missing/empty/whitespace/lower/upper/alpha/digit/mode), bar chart of most frequent values. Exposed via display_text_tab. 

app/tab_date/ — Datetime tab: pick a datetime column, show min/max, weekday/weekend/future counts, sentinel dates, and an Altair histogram; table of most frequent dates. Exposed via display_datetime_tab. 

test/ — unit tests. If you use these, update their imports to the app. package (e.g., from app.tab_numeric.logics import NumericColumn, from app.tab_text.logics import TextColumn) and switch to from pandas.testing import assert_frame_equal

## Citations
Streamlit Documentation: [Streamlit](https://docs.streamlit.io/get-started)

Pandas Documentation: [Pandas](https://pandas.pydata.org/docs/)

