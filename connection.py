from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='UNML_user',
                                    password='',
                                    host='sqlprive-dn717-001.privatesql',
                                    port='3306',
                                    database='UNMLbase')
