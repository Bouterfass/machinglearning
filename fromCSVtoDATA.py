import csv
from Data import Data

def fromCSVtoDATA(f, pays):
################# LECTURE #######################
    with open(f,'r') as file: #j'ouvre un csv en tant que file
        fieldnames = ['id','pays','Annee','critere','valeur','balec','balec2']
        reader = csv.DictReader(file,fieldnames=fieldnames, delimiter = '\t') #je le lis avec la méthode DictReader de la classe csv




################## ECRITURE #########################
        with open('newfile.csv', 'w') as newfile:
#populationecrire2, c'est le nouveau fichier dans lequelle je réecris les données de maniere à ce quelle soit exploitable
            writer = csv.DictWriter(newfile, fieldnames=fieldnames, delimiter='\t') #varialble dans laquelle j'écris les données
            i = 0
            for line in reader: # je lis les données de population.csv
                del line['balec'] #j'efface les deux dernières colonnes qui ne sont que des informations inutiles
                del line['balec2']
                if line['critere'] == 'Population mid-year estimates (millions)': #j'écris que les données concernant l'Afrique en 2015
                    if line['pays'] == pays:
                        del line['critere']
                        del line['id']
                        writer.writerow(line)
        newfile.close()
        file.close()

##################### INTO DATA ###########################
    datalist= [Data(), Data(), Data()]
    i = 1
    j = 0
    with open('newfile.csv','r') as newfile:
        for line in newfile:
            if j == 3:
                break
            for word in line.split():
            #    print('j = '+str(j)+ 'et i = ' + str(i)+ " Mot : " +word)
                if i == 1:
                    datalist[j].setName(word)
                if i == 2:
                    datalist[j].setYear(word)
                if i == 3:
                    datalist[j].setValue(word)
                i = i+1
                if i == 4:
                    j = j + 1
                    i = 1
    return datalist
    #for data in datalist:
    #    data.printData()


#for data in fromCSVtoDATA('population.csv','France'):
#    data.printData()
