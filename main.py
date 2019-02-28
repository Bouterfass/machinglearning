from Data import Data
from DataTreatment import DataTreatment
from controler import controler

import csv


ctrler = controler()

#ctrler.post('population.csv', 'Italy', 'Population mid-year estimates (millions)')
#for data in ctrler.get('pibrut', 'annee', '2005'):
#    data.printData()

for data in ctrler.get("pibrut","annee","2005"):
    data.printData()



ctrler.closeDB()
