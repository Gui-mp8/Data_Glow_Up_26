from sqlalchemy import create_engine, Table

from .models import Base

class DataBase():
    def __init__(self) -> None:
        self._conn = None

    @property
    def conn(self):
        return self._conn

    @conn.setter
    def conn(self, database_url: str):
        self._conn = database_url

    def create_table(self) -> Table:
        engine = create_engine(self.conn)
        Base.metadata.create_all(engine)

    def drop_table(self) -> None:
        engine = create_engine(self.conn)
        Base.metadata.drop_all(engine)