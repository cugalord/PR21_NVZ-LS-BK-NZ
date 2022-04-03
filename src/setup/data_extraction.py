import pandas as pd
import numpy as np


def read(path: str):
    """
    """
    return pd.read_csv(path, sep=',', encoding='utf-8').replace(to_replace='-', value=np.nan)
