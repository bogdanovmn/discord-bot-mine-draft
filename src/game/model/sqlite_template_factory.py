import os
from dotenv import load_dotenv

import sqlite3
import logging


class SqliteTemplate:
    def __init__(self, db_file):
        self.__connection = sqlite3.connect(db_file)

    def select(self, sql, params):
        logging.debug(f"SQL: {sql} PARAMS: {params}")
        try:
            cursor = self.__connection.cursor()
            cursor.execute(sql, (params,))
            return cursor.fetchall()
        except Exception as ex:
            logging.error(f"SQL select error: {ex}")
            self.close()
            raise ex

    def select_one(self, sql, params):
        rows = self.select(sql, params)
        return rows[0] if rows and len(rows) > 0 else None

    def select_value(self, sql, params):
        row = self.select_one(sql, params)
        return row[0] if row else None

    def execute(self, sql, params):
        logging.debug(f"SQL: {sql} PARAMS: {params}")
        try:
            cursor = self.__connection.cursor()
            cursor.execute(sql, params)
            return cursor.lastrowid
        except Exception as ex:
            logging.error(f"SQL execute error: {ex}")
            self.close()
            raise ex

    def commit(self):
        if self.__connection:
            self.__connection.commit()

    def close(self):
        if self.__connection:
            self.__connection.close()


class TemplateFactory:
    def __init__(self, db_name):
        self.db_name = db_name

    def new(self):
        return SqliteTemplate(self.db_name)


load_dotenv()
template_factory = TemplateFactory(
    os.getenv("DB_FILE")
)




