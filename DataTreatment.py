import csv
from Data import Data
from copy import deepcopy

class DataTreatment:
    def fromCSVtoDATA(f, state, dataname):
        ################# LECTURE #######################
        with open(f,'r') as file: #j'ouvre un csv en tant que file
            fieldnames = ['id','pays','Annee','critere','valeur','balec','balec2']
            reader = csv.DictReader(file,fieldnames=fieldnames, delimiter = '\t') #je le lis avec la méthode DictReader de la classe csv




            ################## ECRITURE #########################
            line_number = 0
            with open('newfile.csv', 'w') as newfile:
                #populationecrire2, c'est le nouveau fichier dans lequelle je réecris les données de maniere à ce quelle soit exploitable
                writer = csv.DictWriter(newfile, fieldnames=fieldnames, delimiter='\t') #varialble dans laquelle j'écris les données
                i = 0
                for line in reader: # je lis les données de population.csv
                    del line['balec'] #j'efface les deux dernières colonnes qui ne sont que des informations inutiles
                    del line['balec2']
                    if line['critere'] == dataname: #'Population mid-year estimates (millions)'
                        if line['pays'] == state:
                            del line['critere']
                            del line['id']
                            writer.writerow(line)
                            line_number = line_number + 1
        #    print(line_number)
        newfile.close()
        file.close()



    ##################### INTO DATA ###########################

        datalist= [Data() for i in range(line_number)]
        i = 1
        j = 0

        with open('newfile.csv','r') as newfile:
            for line in newfile:
                if j == line_number:
                    break
                for word in line.split():
            #    print('j = '+str(j)+ 'et i = ' + str(i)+ " Mot : " +word)
                    if i == 1:
                        datalist[j].state = word
                    if i == 2:
                        datalist[j].year = word
                    if i == 3:
                        datalist[j].value = word
                    i = i + 1
                    if i == 4:
                        j = j + 1
                        i = 1
        return datalist
    
    def NormalizeData(ListData):
        """Fonction qui normalise une liste de données"""   
        #a = acces a la bdd (on arriva pas a la faire du coup jai fais sans)
        a = ListData[0].normalize

        def one():
            """code de la premiere normalisation"""
            #Ici depense de santee, rien a faire
            return ListData
    
        def two():
            """code de la deuxieme normalisation"""
            #Ici indice de prod

            #Je declare un tableau de float qui va contenir les valeurs normalisee
            valuenormalize = [float]*len(ListData)
            #je remplis le tableau avec les donnees normalisee
            for i in range (1,len(ListData)):
                valueiteration = ListData[i].value
                b = ListData[i-1].value
                valuenormalize[i-1]=(float(valueiteration)-float(b))/float(b)

            #Je duplique la liste car je ne dois pas toucher à loriginal sinon cela affecte la suite du code
            ListData2=deepcopy(ListData)

            #je remplace les donnees bruts par les donnees normalisees dans le tableau precedent
            for i in range (len(ListData)):
                ListData2[i].value=valuenormalize[i]

            #jefface la derniere case du tableau qui contient un float sans valeur
            ListData2.pop(-1)
            
            #je retourne la liste modifie
            return ListData2
    
        def three():
            """code de la troisieme normalisation"""
            #Ici pib

            #Je declare un tableau de float qui va contenir les valeurs normalisee et un float qui contient la valeur de la premiere data
            valuenormalize = [float]*len(ListData)
            firstvalue = ListData[0].value
            #Je remplis le tableau avec les donnees normalisees
            for i in range(1,len(ListData)):
                a = ListData[i].value
                valuenormalize[i-1] = ((float(a)-float(firstvalue))/float(firstvalue))
            
            #Je duplique la liste car je ne dois pas toucher à loriginal sinon cela affecte la suite du code
            ListData3 = deepcopy(ListData)

            #je remplace les donnees bruts par les donnees normalisees dans le tableau precedent
            for i in range (len(ListData)):
                ListData3[i].value=valuenormalize[i]
            #jefface la derniere case du tableau qui contient un float sans valeur
            ListData3.pop(-1)
            
            #je retourne la liste modifie
            return ListData3

        #Verifie quelle fonction de normalisation utiliser
        switcher = {
            1: one(),
            2: two(),
            3: three()
        }

        #je retourne le resultat de la fonction appelee par le switcher
        return switcher.get(a)
