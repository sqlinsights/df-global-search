# DataFrame Global Search

This library will create a search grid for your Pandas DataFrame. If a match is found, a styled dataframe will be returned with matching columns highlighted. Search can be performed using Text or Regular Expressions. 

## PyPi Project
You can access the PyPi project [here](https://pypi.org/project/df-global-search/)
## Installation 
```shell
pip install df-global-search
```

## Available Arguments

|Arg|Type|Default Value|Optional|
|---|---|---|---|
|dataframe|pd.DataFrame||🚫|
|text_search| str| None|✅|
|highlight_matches|bool|True|✅|
|regex_search|bool|False|✅|
|case_sensitive|bool|False|✅
|match_font_color|str|black|✅|
|match_background_color|str|lightgray|✅|

## Usage (with Streamlit)
``` python
from df_global_search import DataFrameSearch

with DataFrameSearch(
        dataframe=df,
        text_search='hello',
        case_sensitive=False
) as df:
    st.dataframe(df, use_container_width=True)
    
```


## Sample

### Regular Search
![sample](images/regular_search.png "Regular Search")

### Regex Search

![sample](images/regex_search.png "Regular Search")
