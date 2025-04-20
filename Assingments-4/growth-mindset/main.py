# Growth Mindset Challange Streamlit Python Project -1

import streamlit as st
import pandas as pd
from io import BytesIO

# Page Configuration
st.set_page_config(page_title="File Converter", layout="wide", page_icon="📊")

# Link the CSS file
st.markdown(
    '<link rel="stylesheet" href="styles.css">',
    unsafe_allow_html=True
)

# Title and description
st.title("File Converter & Cleaner")
st.write("Upload CSV or Excel files, clean data, and convert formats.")

# File upload section
files = st.file_uploader("Upload CSV or Excel files:", type=["csv", "xlsx"], accept_multiple_files=True)

# Processing uploaded files
if files:
    for file in files:
        ext = file.name.split(".")[-1]
        df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)

        # Display file preview
        st.subheader(f"{file.name} - Preview")
        st.dataframe(df.head(), use_container_width=True)

        # Remove duplicates
        if st.checkbox(f"Remove Duplicates - {file.name}"):
            df = df.drop_duplicates()
            st.success("Duplicates removed!")
            st.dataframe(df.head())

        # Fill missing values
        if st.checkbox(f"Fill Missing Values - {file.name}"):
            df.fillna(df.select_dtypes(include=['number']).mean(), inplace=True)
            st.success("Missing values filled!")
            st.dataframe(df.head())

        # Select columns to display
        selected_columns = st.multiselect(f"Select Columns - {file.name}", df.columns, default=df.columns)
        df = df[selected_columns]
        st.dataframe(df.head(), use_container_width=True)

        # Show chart
        if st.checkbox(f"Show Chart - {file.name}") and not df.select_dtypes(include='number').empty:
            st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])

        # Format choice for file conversion
        format_choice = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

        # Download converted file
        if st.button(f"Download {file.name} as {format_choice}"):
            output = BytesIO()
            if format_choice == "CSV":
                df.to_csv(output, index=False)
                mime = "text/csv"
                new_name = file.name.replace(ext, "csv")
            else:
                df.to_excel(output, index=False, engine='openpyxl')
                mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                new_name = file.name.replace(ext, "xlsx")

            output.seek(0)
            st.download_button("Download File", data=output, file_name=new_name, mime=mime)

st.success("Processing complete!")
