import streamlit as st
from streamlit_pandas_profiling import st_profile_report

import dataLoader
import wildfireView
import pandasProfiling


def main():
    with st.sidebar.header("Source Data Selection:"):
        st.sidebar.write("select Wildfire dataset")
        source_data = st.sidebar.file_uploader("Upload/select source (.csv) data", type=['csv'])
    df = None
    if source_data is not None:
        df = dataLoader.read_load_dataset(source_data)
    if df is not None:
        user_choices = ['Dataset Sample', 'Yearly Wildfire', 'Pandas Profiling']
        selected_choice = st.sidebar.selectbox("Please select your choice:", user_choices)
        if selected_choice is not None:
            if selected_choice == 'Dataset Sample':
                st.info("Select dataset has " + str(df.shape[0]) + " rows and " + str(df.shape[1]) + " columns.")
                st.write(df.sample(10))
            elif selected_choice == 'Yearly Wildfire':
                year_keys = df['year'].unique()
                if len(year_keys) > 0:
                    st.write('Select three known variables:')
                    opts = [('s', 'displacement'), ('u', 'initial velocity'), ('v', 'final velocity'),
                            ('a', 'acceleration'), ('t', 'time')]
                    # known_variables = {symbol: st.sidebar.checkbox(f"{name} ({symbol})") for symbol, name in opts}
                    year_selection = {year: st.sidebar.checkbox(f"{year}") for year in year_keys}
                    all_selected_years = [k for k, v in year_selection.items() if v == True]
                    if len(all_selected_years) > 0:
                        df = df[df['year'].isin(all_selected_years)]
                        wildfireView.create_mapbox_graph(df)
                    else:
                        st.info("Please select one or more years from the left side list")
            elif selected_choice == "Pandas Profiling":
                df_100 = df.sample(100)
                df_report = pandasProfiling.pandas_profiling_report(df_100)
                st.write("Pandas Profiling Report (only 100 Rows Sample)")
                st_profile_report(df_report)
    else:
        st.error("Please select your source data to get started")


if __name__ == "__main__":
    st.set_page_config(page_title="Worldwide WildFire Visualization", layout="wide")
    st.header("Select specific country dataset and view last 20 years of wildfire")
    main()
