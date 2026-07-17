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
    
    
def remove_duplicates(df):
    """
    Remove duplicate rows from a DataFrame.
    """
    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    removed = before - after

    return df, removed    



from pathlib import Path

def save_cleaned_csv(df, output_path: Path):
    """
    Save the cleaned DataFrame to a CSV file.
    """
    df.to_csv(output_path, index=False)
    
def clean_csv(file_path: Path):
    """
    Read a CSV, clean it, save it, and return statistics.
    """
    df = pd.read_csv(file_path)

    rows_before = len(df)

    df, duplicates_removed = remove_duplicates(df)

    rows_after = len(df)

    output_dir = Path("cleaned")
    output_dir.mkdir(exist_ok=True)

    output_path = output_dir / f"cleaned_{file_path.name}"

    save_cleaned_csv(df, output_path)

    return {
        "rows_before": rows_before,
        "rows_after": rows_after,
        "duplicates_removed": duplicates_removed,
        "output_path": str(output_path),
    }    