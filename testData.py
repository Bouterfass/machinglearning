from Data import Data
from fromCSVtoDATA import fromCSVtoDATA

##Test de la fonction fromCSVtoDATA

for data in fromCSVtoDATA('population.csv',	'Argentina'):
    data.printData()
