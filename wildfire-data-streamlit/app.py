import streamlit as st
from streamlit_pandas_profiling import st_profile_report

import dataLoader
import pandasProfiling
import wildfireView


def main():
    with st.sidebar.header("Wildfire Data Selection:"):
        st.sidebar.write("select dataset")
        source_data = st.sidebar.file_uploader("Upload/select source (.csv) data", type=['csv'])
    df = None
    if source_data is not None:
        df = dataLoader.read_load_dataset(source_data)
    if df is not None:
        user_choices = ['Wildfire Data Sample', 'Yearly Wildfire Data', 'Pandas Profiling']
        selected_choice = st.sidebar.selectbox("Please select your choice:", user_choices)
        if selected_choice is not None:
            if selected_choice == 'Wildfire Data Sample':
                st.info("Select data has " + str(df.shape[0]) + " rows and " + str(df.shape[1]) + " columns.")
                st.write(df.sample(10))
            elif selected_choice == 'Yearly Wildfire Data':
                year_keys = df['year'].unique()
                if len(year_keys) > 0:
                    st.write("Please select wildfire by year:")
                    year_selection = {year: st.sidebar.checkbox(f"{year}") for year in year_keys}
                    all_selected_years = [k for k, v in year_selection.items() if v == True]
                    if len(all_selected_years) > 0:
                        df = df[df['year'].isin(all_selected_years)]
                        wildfireView.show_wildfire_map(df)
            elif selected_choice == "Pandas Profiling":
                df_report = pandasProfiling.pandas_profiling_report(df)
                st.write("Pandas Profiling Report")
                st_profile_report(df_report)

    else:
        st.error("Please select your source data to get started")


if __name__ == "__main__":
    st.set_page_config(page_title="Wildfire Visualization", layout="wide")
    st.header("Select your country or region with Wildfire dataset")
    main()