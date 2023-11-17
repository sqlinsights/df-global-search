import pandas as pd
import numpy as np


class DataFrameSearch:
    def __init__(
        self,
        dataframe: pd.DataFrame,
        text_search: str = None,
        case_sensitive: bool = False,
        match_font_color: str = "black",
        match_background_color: str = "lightgray",
    ) -> None:
        """Returns a Pandas Styled Dataframe if search argument is a match"""
        self.dataframe = dataframe
        self.text_search = text_search
        self.case_sensitive = case_sensitive
        self.match_font_color = match_font_color
        self.match_background_color = match_background_color

    def selection_hightlight(self, val):
        color = self.match_font_color if val else "black"
        background = self.match_background_color if val else "white"
        return f"color: {color}; background-color:{background};"

    def __enter__(self):
        if self.text_search:
            filter_mask = np.column_stack(
                [
                    self.dataframe[col]
                    .astype(str)
                    .str.contains(self.text_search, na=False, case=self.case_sensitive)
                    for col in self.dataframe
                ]
            )
            df_bool = pd.DataFrame(
                data=filter_mask.tolist(), columns=self.dataframe.columns
            ).loc[filter_mask.any(axis=1)]
            return self.dataframe.loc[filter_mask.any(axis=1)].style.apply(
                lambda _: df_bool.applymap(self.selection_hightlight), axis=None
            )
        else:
            return self.dataframe

    def __exit__(self, *exc):
        pass
