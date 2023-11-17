import streamlit as st
from vega_datasets import data
import pandas as pd
import numpy as np
from df_global_search import DataFrameSearch

st.subheader("Filter DataFrame based on Search")
search_bar_columns = st.columns((2, 1, 1))
with search_bar_columns[1]:
    search_text = st.text_input(
        "Search", label_visibility="collapsed", placeholder="Search Text"
    )
with search_bar_columns[2]:
    case_sensitive = st.toggle("Case Sensitive", value=False)
df = pd.DataFrame(data.airports())

with st.echo():
    with DataFrameSearch(
        dataframe=df, text_search=search_text, case_sensitive=case_sensitive
    ) as df:
        st.dataframe(data=df, use_container_width=True, hide_index=True)
