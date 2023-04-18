import pymysql
import os
import sys

from pymysql.cursors import DictCursor


#print(sys.argv[1])

class Database:
    def __init__(self):
        self._connection = pymysql.connect(
            host='localhost',
            user='root',
            password='rootPass',
            db='cpi_unqbot'
        )
        self._cursor = self._connection.cursor(DictCursor)

    def execute_query(self, sqlString):
        self._cursor.execute(query=sqlString)
        return self._cursor.fetchall()

    def close(self):
        self._connection.close()