import pandas as pd


def normalize_dtype(dtype):
    """
    Convert pandas data types into user-friendly names.
    """
    mapping = {
        "object": "string",
        "str": "string",
        "float64": "float",
        "float32": "float",
        "int64": "int",
        "int32": "int",
        "bool": "boolean",
        "datetime64[ns]": "datetime",
    }

    return mapping.get(str(dtype), str(dtype))


def suggest_data_type(series):
    """
    Suggest a suitable data type and confidence score.
    """

    sample = series.dropna()

    if sample.empty:
        return "unknown", 0

    values = sample.astype(str).str.strip()

    # Integer
    if values.str.match(r"^-?\d+$").all():
        return "int", 98

    # Float
    if values.str.match(r"^-?\d+(\.\d+)?$").all():
        return "float", 98

    # Datetime
    converted = pd.to_datetime(values, errors="coerce")

    success_rate = converted.notna().mean()

    if success_rate >= 0.80:
        return "datetime", round(success_rate * 100)

    # Default
    return "string", 100


def generate_report(df):
    """
    Generate a data quality report.
    """

    report = {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": df.columns.tolist(),
        "data_types": {},
        "missing_values": {},
        "duplicate_rows": int(df.duplicated().sum())
    }

    total_rows = len(df)

    for column in df.columns:

        # Missing values
        missing_count = int(df[column].isnull().sum())

        missing_percentage = (
            round((missing_count / total_rows) * 100, 2)
            if total_rows > 0
            else 0
        )

        report["missing_values"][column] = {
            "count": missing_count,
            "percentage": missing_percentage
        }

        # Data types
        current = normalize_dtype(df[column].dtype)

        suggested, confidence = suggest_data_type(df[column])

        report["data_types"][column] = {
            "current": current,
            "suggested": suggested,
            "confidence": confidence
        }

    return report