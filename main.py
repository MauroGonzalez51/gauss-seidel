from typing import NoReturn
from src.utils.read_file import read_file
from src.gauss_seidel import gauss_seidel
from config.settings import FILE_PATH

def main() -> NoReturn:
    coefficients, independent_terms = read_file(__path=FILE_PATH)

    try:
        x = gauss_seidel(coefficients=coefficients, independent_terms=independent_terms)
    except Exception as e:
        print(e)
        
    for i in range(len(x)):
        print(f"x{i} = {x[i]}")

if __name__ == "__main__":
    main()