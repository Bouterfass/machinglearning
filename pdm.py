from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='',
                                 host='localhost',
                                 port='3306',
                                 database='test')
print('Connexion has been done !')
cnx.close()
