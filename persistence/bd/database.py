import pymysql
import os
import sys

from pymysql.cursors import DictCursor
from local_settings import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

#print(sys.argv[1])

class Database:
    def __init__(self):
        self._connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            db=DB_NAME
        )
        self._cursor = self._connection.cursor(DictCursor)

    def execute_query(self, sqlString):
        self._cursor.execute(query=sqlString)
        return self._cursor.fetchall()

    def close(self):
        self._connection.close()