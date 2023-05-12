import os
import sqlite3
from sqlite3 import Row


class DatabaseMemory:
    """ DB en memoria para pruebas unitarias, con setUp inicial
    """

    def __init__(self):
        self.connection = sqlite3.connect(':memory:')
        self.connection.row_factory = sqlite3.Row
        self.db_session = self.connection.cursor()

        self.setUp()

    def setUp(self):
        print("setUp DB en memoria")
        # Obtiene la ruta absoluta del directorio que contiene el script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        scriptsTest_folder = script_dir+'\\scriptsTests\\'
        listScripts = os.listdir(scriptsTest_folder)
        for script in listScripts:
            fullpath = scriptsTest_folder+script
            with open(fullpath, 'r') as sql_file:
                sql_script = sql_file.read()
                self.db_session.executescript(sql_script)
                self.connection.commit()

    def execute_query(self, sqlquery):
        self.db_session.execute(sqlquery)
        rows = self.db_session.fetchall()
        result = []
        for r in rows:
            result.append(self._dict_from_row(r))

        return result

    def _dict_from_row(self, row: Row):
      return dict(zip(row.keys(), row))

    def close(self):
        self.connection.close()