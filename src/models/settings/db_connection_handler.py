import sqlite3
from sqlite3 import Connection


class __DbConectionHandler:
    def __init__(self)-> None:
        self.__connection_string = "storage.db"
        self.__conn = None

    def connect(self) -> None:
        self.__conn = sqlite3.connect(self.__connection_string)

    def get_connect(self) -> Connection:
        return self.__conn


db_connect_handler = __DbConectionHandler()