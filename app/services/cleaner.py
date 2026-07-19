import time
import uuid
import re
from pathlib import Path

import pandas as pd

from app.services.report import generate_report
from app.services.quality import calculate_quality_score


def inspect_csv(file_path: Path):
    """
    Read a CSV file and return basic information about it.
    """
    df = pd.read_csv(file_path)
    
    print(df.head())
    print(df.dtypes)
    print(df["quantity"].head())   # or price
    print(type(df["quantity"].iloc[0]))  # or price

    return {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "column_names": df.columns.tolist(),
    }


def remove_duplicates(df):
    """
    Remove duplicate rows from a DataFrame.
    Returns (cleaned_df, removed_count).
    """
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    removed = before - after
    return df, removed


def remove_empty_rows(df):
    """
    Remove rows where every column is empty.
    Returns (cleaned_df, removed_count).
    """
    before = len(df)
    df = df.dropna(how="all")
    after = len(df)
    removed = before - after
    return df, removed


def save_cleaned_csv(df, output_path: Path):
    """
    Save the cleaned DataFrame to a CSV file.
    """
    df.to_csv(output_path, index=False)


def trim_whitespace(df):
    """
    Remove leading and trailing whitespace from text columns.
    """
    df = df.copy()
    text_columns = df.select_dtypes(include=["object"]).columns
    for column in text_columns:
        df[column] = df[column].astype(str).str.strip()
    return df


def standardize_column_names(df):
    """
    Standardize DataFrame column names.
    """
    new_columns = []
    for column in df.columns:
        col = str(column)
        col = col.strip().lower()
        col = col.replace(" ", "_")
        col = col.replace("-", "_")
        col = re.sub(r"_+", "_", col)
        new_columns.append(col)
    df.columns = new_columns
    return df


def clean_csv(file_path: Path):
    """
    Read a CSV, clean it, save it, and return statistics.
    Pipeline: Read → Remove empty rows → Trim whitespace → Standardize column names → Remove duplicates → Generate report → Save CSV
    Returns a dict with stats and `output_path`.
    """
    cleaning_history = []

    total_start = time.perf_counter()

    read_start = time.perf_counter()
    df = pd.read_csv(file_path)
    read_time = time.perf_counter() - read_start

    report_start = time.perf_counter()
    original_report = generate_report(df)
    original_quality = calculate_quality_score(original_report)
    report_time = time.perf_counter() - report_start
    rows_before = len(df)

    clean_start = time.perf_counter()
    df, empty_rows_removed = remove_empty_rows(df)
    cleaning_history.append({
        "step": "Remove Empty Rows",
        "rows_removed": empty_rows_removed,
    })

    df = trim_whitespace(df)
    columns_trimmed = len(df.select_dtypes(include=["object"]).columns)
    cleaning_history.append({
        "step": "Trim Whitespace",
        "columns_processed": columns_trimmed,
    })

    df = standardize_column_names(df)
    renamed_columns = len(df.columns)
    cleaning_history.append({
        "step": "Standardize Column Names",
        "columns_renamed": renamed_columns,
    })

    df, duplicates_removed = remove_duplicates(df)
    cleaning_history.append({
        "step": "Remove Duplicates",
        "rows_removed": duplicates_removed,
    })
    clean_time = time.perf_counter() - clean_start

    rows_after = len(df)

    output_dir = Path("cleaned")
    output_dir.mkdir(parents=True, exist_ok=True)

    unique_id = uuid.uuid4().hex[:8]
    output_path = output_dir / f"{unique_id}_cleaned_{file_path.name}"

    save_start = time.perf_counter()
    save_cleaned_csv(df, output_path)
    save_time = time.perf_counter() - save_start

    final_report_start = time.perf_counter()
    cleaned_report = generate_report(df)
    cleaned_quality = calculate_quality_score(cleaned_report)
    final_report_time = time.perf_counter() - final_report_start

    total_time = time.perf_counter() - total_start

    return {
        "rows_before": rows_before,
        "rows_after": rows_after,
        "duplicates_removed": duplicates_removed,
        "empty_rows_removed": empty_rows_removed,
        "output_path": str(output_path),
        "original_report": original_report,
        "cleaned_report": cleaned_report,
        "original_quality": original_quality,
        "cleaned_quality": cleaned_quality,
        "processing_time": {
            "read_csv": round(read_time, 4),
            "original_report": round(report_time, 4),
            "cleaning": round(clean_time, 4),
            "save_csv": round(save_time, 4),
            "cleaned_report": round(final_report_time, 4),
            "total": round(total_time, 4),
            "cleaning_history": cleaning_history,
        },
    }
