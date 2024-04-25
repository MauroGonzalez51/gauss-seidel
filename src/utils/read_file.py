import pandas as pd
from typing import Dict
import numpy as np

def read_file(__path: str) -> Dict[np.ndarray, np.ndarray]:
    try:
        raw_data = pd.read_excel(__path, engine="openpyxl")
        num_equations = raw_data.shape[0]
        coefficients = raw_data.iloc[:, :num_equations].to_numpy().astype(np.float64)
        independent_terms = raw_data.iloc[:, num_equations].to_numpy().astype(np.float64)

        return coefficients, independent_terms
    except Exception as e:
        print(f"<Exception> {e}")


if __name__ == "__main__":
    read_file()