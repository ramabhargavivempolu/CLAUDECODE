"""Module for creating sample pandas DataFrames."""

import pandas as pd


def create_dataframe() -> pd.DataFrame:
    """Create a pandas DataFrame with 3 columns and 5 rows.

    Returns:
        pd.DataFrame: A DataFrame with columns 'Name', 'Age', and 'Score',
                      containing 5 rows of sample data.
    """
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'Age': [25, 30, 35, 28, 32],
        'Score': [85.5, 92.0, 78.5, 88.0, 95.5]
    }
    return pd.DataFrame(data)


if __name__ == '__main__':
    df = create_dataframe()
    print(df)
