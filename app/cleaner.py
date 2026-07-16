import pandas as pd
from pathlib import Path


def inspect_csv(file_path: Path):
    """
    Read a CSV file and return basic information about it.
    """
    df = pd.read_csv(file_path)

    return {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "column_names": df.columns.tolist(),
    }