from Data import Data
from DataTreatment import DataTreatment
from controler import controler

import csv


#ctrler = controler()

#ctrler.post('population.csv', 'Italy', 'Population mid-year estimates (millions)')
#for data in ctrler.get('pibrut', 'annee', '2005'):
#    data.printData()

#for data in ctrler.get("pibrut","annee","2005"):
#    data.printData()

for data in DataTreatment.fromCSVtoDATA("population.csv","France","Population mid-year estimates (millions)"):
    print(data.value)
    
#print(type(DataTreatment.fromCSVtoDATA("population.csv","France")))

test = DataTreatment.fromCSVtoDATA("population.csv","France","Population mid-year estimates (millions)")
#print(DataTreatment.NormalizeData(DataTreatment.fromCSVtoDATA("population.csv","France","Population mid-year estimates (millions)")))

for data in test: 
    data.normalize=3

for data in DataTreatment.NormalizeData(test):
    print(data.value)



#ctrler.closeDB()
