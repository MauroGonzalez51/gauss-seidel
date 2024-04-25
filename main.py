from typing import NoReturn
from src.utils.read_file import read_file
from config.settings import FILE_PATH

def main() -> NoReturn:
    read_file(__path=FILE_PATH)
    ...

if __name__ == "__main__":
    main()