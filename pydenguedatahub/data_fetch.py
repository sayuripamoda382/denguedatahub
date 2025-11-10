import pandas as pd
import importlib.resources as pkg_resources
from . import data

def list_datasets():
    """
    Return a list of all available dataset names in the package.
    """
    return [
        f.name.replace(".csv", "")
        for f in pkg_resources.files(data).iterdir()
        if f.name.endswith(".csv")
    ]

def load_dataset(name):
    """
    Load a dataset by name.

    Example:
        df = load_dataset("srilanka_weekly_data")
    """
    file_path = pkg_resources.files(data) / f"{name}.csv"
    return pd.read_csv(file_path)
