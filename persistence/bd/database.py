import pymysql
import os
import sys

from pymysql.cursors import DictCursor


#print(sys.argv[1])

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='rootPass',
            db='cpi_unqbot'
        )
        self.cursor = self.connection.cursor(DictCursor)

    def execute_query(self, sqlString):
        print('query '+sqlString)
        self.cursor.execute(query=sqlString)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()