import pymysql

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
        self.cursor = self.connection.cursor(DictCursor)

    def execute_query(self, sqlString):
        print('query '+sqlString)
        self.cursor.execute(query=sqlString)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()