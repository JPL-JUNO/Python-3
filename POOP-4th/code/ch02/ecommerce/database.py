"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 20:09:32
@Description: 
"""
from typing import Optional


class DataBase:
    def __init__(self, connection: Optional[str] = None) -> None:
        pass


def initialize_database(connection: Optional[str] = None) -> None:
    global db
    db = DataBase(connection)
    print(f"initialized {db!r} with {connection!r}")


# database = DataBase("path/to/data")

db: Optional[DataBase] = None

# We could import this function everywhere we needed access to the database


def get_database(connection: Optional[str] = None) -> DataBase:
    global db
    if not db:
        db = DataBase(connection)
    return db
