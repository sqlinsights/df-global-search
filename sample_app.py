import streamlit as st
from vega_datasets import local_data
import pandas as pd
from df_global_search import DataFrameSearch

st.set_page_config(layout="wide")
st.subheader("Filter DataFrame based on Search")
search_bar_columns = st.columns((2, 1, 0.5, 0.75, 1))
with search_bar_columns[1]:
    search_text = st.text_input(
        "Search", label_visibility="collapsed", placeholder="Search Text"
    )
with search_bar_columns[2]:
    is_regex = st.toggle("Regex", value=False)
with search_bar_columns[3]:
    case_sensitive = st.toggle("Case Sensitive", value=False)
with search_bar_columns[4]:
    highlight_match = st.toggle("Highlight Matching Cells", value=True)
df = pd.DataFrame(local_data.airports())

with st.echo():
    with DataFrameSearch(
        dataframe=df,
        text_search=search_text,
        case_sensitive=case_sensitive,
        regex_search=is_regex,
        highlight_matches=highlight_match,
    ) as df:
        st.dataframe(data=df, use_container_width=True, hide_index=True)
