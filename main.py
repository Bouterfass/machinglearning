from Data import Data
from DataTreatment import DataTreatment
from controler import controler

import csv


#ctrler = controler()

#ctrler.post('population.csv', 'Italy', 'Population mid-year estimates (millions)')
#for data in ctrler.get('pibrut', 'annee', '2005'):
#    data.printData()
#ctrler.closeDB()

##Test de la fonction fromCSVtoDATA

#for data in comp(fromCSVtoDATA('population.csv',	'Argentina')):
 #   data.printData()

#for data in fromCSVtoDATA('population.csv',	'Germany'):
#    print(data.getName())
listdata = DataTreatment.fromCSVtoDATA('population.csv', 'Italy', 'Population mid-year estimates (millions)')

print(float(listdata[1].value) - float(listdata[0].value))
