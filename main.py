from Data import Data
from DataTreatment import DataTreatment
from controler import controler

import csv


ctrler = controler()

ctrler.post('population.csv','France')

ctrler.closeDB()

##Test de la fonction fromCSVtoDATA

#for data in fromCSVtoDATA('population.csv',	'Argentina'):
#    data.printData()

#for data in fromCSVtoDATA('population.csv',	'Germany'):
#    print(data.getName())
