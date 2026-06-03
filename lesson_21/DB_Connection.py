import logging
import os
from sqlalchemy import create_engine, Column, Integer, String, Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

from lesson_21.courses_table import Course
from lesson_21.declarative_base import Base
#from students_table import Student
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
load_dotenv()
class SQLAlchemyClient:

    def __init__(self):
        self.db_url = os.getenv("POSTGRES_DB_URL")
        self.__engine: Engine = create_engine(self.db_url)
        self.__session = self.__create_session()

    @property
    def session(self):
        return self.__session

    @property
    def engine(self):
        return self.__engine

    def __create_session(self):
        session = sessionmaker(bind=self.engine)
        return session()

    def create_table(self, table_model):
        table_model.metadata.create_all(self.engine)

    def create_all_tables(self):
        Base.metadata.create_all(self.engine)

    def close_connection(self):
        self.session.close()

    def __repr__(self):
        return f"{self.first_name} {self.last_name} ({self.age})"


if __name__ == "__main__":
    sqlalchemy_client = SQLAlchemyClient()
    sqlalchemy_client.create_table(table_model=Course)
    sqlalchemy_client.create_table(table_model=Student)
