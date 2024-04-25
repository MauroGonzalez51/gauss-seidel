import pandas as pd

def read_file(__path: str) -> None:
    try:
        raw_data = pd.read_excel(__path, sheet_name="Equations", engine="openpyxl")
        return raw_data
    except Exception as e:
        print(f"<Exception> {e}")


if __name__ == "__main__":
    read_file()