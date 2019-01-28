import requests
import json
import csv

headers = {'authorization': "Basic API Key Ommitted", 'accept': "application/json", 'accept': "text/csv"}

rcomp = requests.get('http://moncsv.com/foo/bar//lol.csv', headers = headers)

data = rcomp.text

with open('SYB61_T12_Intentional Homicides and Other Crimes (2).csv',"wb") as csvFile:
    writer = csv.writer(csvFile, delimiter = ',')
    for line in data:
        writer.writerow(line)
