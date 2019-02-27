from mysql.connector import (connection)

from DataTreatment import DataTreatment
from Data import Data


class controler:
    def __init__(self):
        self.cnx = connection.MySQLConnection(user='root', password='',
                                 host='localhost',
                                 port='3306',
                                 database='test')
        self.cursor = self.cnx.cursor()
        print('You are connected !')

    def post(self, file, state):
        for data in DataTreatment.fromCSVtoDATA(file, state):
                val = [data.state, data.year, data.value]
                add_data_query = (  "INSERT INTO pibrut"
                    "(pays, annee, valeur) "
                    "VALUES (%s,%s,%s)")
                self.cursor.execute(add_data_query, val)
                self.cnx.commit()


    def closeDB(self):
        self.cursor.close()
        self.cnx.close()
        print("You're disconnected !")
