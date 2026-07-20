import pandas as pd

from app.services.cleaner import remove_duplicates
from app.services.cleaner import standardize_column_names


def test_remove_duplicates():
    """
    Test duplicate row removal.
    """

    df = pd.DataFrame(
        {
            "Name": [
                "Alice",
                "Bob",
                "Bob",
                "Charlie",
            ]
        }
    )

    cleaned_df, removed = remove_duplicates(df)

    assert len(cleaned_df) == 3

    assert removed == 1
    
    
    
    
def test_standardize_column_names():
    """
    Test column name standardization.
    """

    df = pd.DataFrame(
        {
            "First Name": ["Alice"],
            "Last Name": ["Smith"],
            "Phone-Number": ["123"],
        }
    )

    cleaned_df = standardize_column_names(df)

    assert cleaned_df.columns.tolist() == [
        "first_name",
        "last_name",
        "phone_number",
    ]