import pymysql
import os
import sys

#print(sys.argv[1])

#if not os.getenv("DATABASE_URL") | (not os.getenv("DATABASE_NAME")) \
#       | (not os.getenv("DATABASE_USER")) | (not os.getenv("DATABASE_PASS")):
#    raise RuntimeError("DATABASE_URL is not set")

class DataBase:
    def __init__(self):
        self._connection = pymysql.connect(
            host='localhost',
            user='root',
            password='rootPass',
            db='cpi_unqbot'
        )
        self._cursor = self._connection.cursor()

    def execute_query(self, sqlString):
        self._cursor.execute(query=sqlString)
        return self._cursor.fetchall()

    def close(self):
        self._connection.close();