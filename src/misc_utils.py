"""
This module contains miscellaneous utility functions used in .ipynb files.
They are stored here so they don't clutter the main code.
"""

from IPython.display import display_html
from itertools import chain, cycle
import pandas as pd


def display_side_by_side(*args, titles=cycle([''])) -> None:
    """
    Assembles html output of multiple dataframes side by side.
    """
    html_str = ''
    for df, title in zip(args, chain(titles, cycle(['</br>']))):
        html_str += '<th style="text-align:center"><td style="vertical-align:top">'
        html_str += f'<h2>{title}</h2>'
        html_str += df.to_html().replace('table', 'table style="display:inline"')
        html_str += '</td></th>'
    display_html(html_str, raw=True)


def init_dict_based_on_column(df: pd.DataFrame, column_name: str) -> dict:
    """
    Initializes a dict based on a column of a dataframe.
    """
    d = dict()
    for value in df[column_name]:
        if value not in d:
            d[value] = dict()
    return d


def flatten_internal_dict(d: dict) -> dict:
    """
    Flattens a dict of dicts.
    """
    hits = dict()
    for key, value in d.items():
        hits[key] = list(value.values())
    return hits


def get_percentage_diff(v1: float, v2: float) -> float:
    """
    Calculates differences between two values and returns the percentage.
    """
    if v1 == v2:
        return 0
    try:
        return (abs(v1 - v2) / v2) * 100.0
    except ZeroDivisionError:
        return float('inf')
