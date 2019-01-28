import csv



################# LECTURE #######################
with open('population.csv','r') as file: #j'ouvre un csv en tant que file
    fieldnames = ['id','pays','Annee','critere','valeur','balec','balec2']
    reader = csv.DictReader(file,fieldnames=fieldnames, delimiter = '\t') #je le lis avec la méthode DictReader de la classe csv
################## ECRITURE #########################
    with open('populationecrire2.csv', 'w') as newfile:
#populationecrire2, c'est le nouveau fichier dans lequelle je réecris les données de maniere à ce quelle soit exploitable
        writer = csv.DictWriter(newfile, fieldnames=fieldnames, delimiter='\t') #varialble dans laquelle j'écris les données
        writer.writeheader() #j'écris les attributs de fieldnames en haut du fichier (mais je n'arrive pas encore à les aligner)
        for line in reader: # je lis les données de population.csv
            del line['balec'] #j'efface les deux dernières colonnes qui ne sont que des informations inutiles
            del line['balec2']
            if line['pays'] == 'Africa': #j'écris que les données concernant l'Afrique en 2015
                if line['Annee'] == '2015':
                    writer.writerow(line) #du coup si le pays est "l'Afrique" (??) et l'année est 2015 alors, j'écris les données dans populationecrire2.csv
        
