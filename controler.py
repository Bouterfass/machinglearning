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

    def post(self, file, state, dataname):
        for data in DataTreatment.fromCSVtoDATA(file, state, dataname):
                val = [data.state, data.year, data.value]
                add_data_query = (  "INSERT INTO pibrut"
                    "(pays, annee, valeur) "
                    "VALUES (%s,%s,%s)")
                self.cursor.execute(add_data_query, val)
                self.cnx.commit()

    def get(self, table, data, value):
        add_data_query = ("SELECT * FROM " +table+ " WHERE " +data+ "=" +"'"+value+"';")
        self.cursor.execute(add_data_query)
        result = self.cursor.fetchall()
        print(len(result))
        datalist = [Data() for i in range(len(result))]
        print("longueur de datalist : "+ str(len(datalist)))
        for data in result:
            print(data)

        k = 0
        for i in range(len(result)):
            for j in range(3):
                print(str(i) + " " + str(j)+ " " +str(result[i][j]))
                if j == 0:
                    datalist[k].state = result[i][j]
                if j == 1:
                    datalist[k].year = result[i][j]
                if j == 2:
                    datalist[k].value = result[i][j]
            if k <= i:
                k = k + 1

        return datalist

    def closeDB(self):
        self.cursor.close()
        self.cnx.close()
        print("You're disconnected !")
