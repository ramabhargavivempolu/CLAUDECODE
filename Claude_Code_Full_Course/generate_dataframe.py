"""
Module for generating pandas DataFrames with sample data.
"""

import pandas as pd


def createSampleDataFrame() -> pd.DataFrame:
    """
    Create a pandas DataFrame with 3 columns and 5 rows of sample data.

    Returns:
        pd.DataFrame: A DataFrame with columns 'Name', 'Age', and 'Score',
                     containing 5 rows of sample data.
    """
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'Age': [25, 30, 28, 35, 29],
        'Score': [85.5, 92.3, 78.9, 88.1, 95.6]
    }
    return pd.DataFrame(data)


if __name__ == '__main__':
    # Example usage
    df = createSampleDataFrame()
    print(df)
    print("\nDataFrame Info:")
    print(df.info())
