
from pathlib import Path

import pandas as pd


# Find the dataset relative to this Python file.
PROJECT_DIR = Path(__file__).resolve().parent
DATA_PATH = PROJECT_DIR / "data" / "battery_data.csv"


def load_battery_data(path=DATA_PATH):
    """Load the battery research dataset from a CSV file."""
    return pd.read_csv(path)


def main():
    data = load_battery_data()

    print("\nBATTERY MATERIALS RESEARCH")
    print("=" * 35)

    print("\nTechnologies in the dataset:")
    print(data["technology"].to_string(index=False))

    print("\nMissing values in each column:")
    print(data.isna().sum().to_string())

    print("\nDataset loaded successfully.")
    print(f"Number of technologies: {len(data)}")


if __name__ == "__main__":
    main()
