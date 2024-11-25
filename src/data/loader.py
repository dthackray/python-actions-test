import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def generate_sample_data():
    """Generate sample sales data."""
    np.random.seed(42)

    # Generate dates
    start_date = datetime(2023, 1, 1)
    dates = [start_date + timedelta(days=x) for x in range(365)]

    # Generate data
    data = {
        "date": dates,
        "product": np.random.choice(["Laptop", "Phone", "Tablet", "Monitor"], 365),
        "region": np.random.choice(["North", "South", "East", "West"], 365),
        "sales": np.random.normal(1000, 200, 365).round(2),
        "units": np.random.randint(1, 50, 365),
    }

    df = pd.DataFrame(data)
    df["sales"] = df["sales"] * (1 + 0.3 * np.sin(np.pi * df.index / 180))

    return df


def load_data():
    """Load the sales data."""
    try:
        # In a real app, you would load from a file or database
        # df = pd.read_csv('sales_data.csv')
        df = generate_sample_data()
        df["date"] = pd.to_datetime(df["date"])
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()
