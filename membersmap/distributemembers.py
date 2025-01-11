# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

# Copyright © 2024, Place publique, Xavier Schoepfer
# GNU GENERAL PUBLIC LICENSE Version 3


"""
classe DistributeMembers :

    Cette classe fournit un outil pour répartir
    géographiquement les adhétrents d'un département.

    liste des méthodes de cette classe :

        • extractMembersData()
            Extraction des données des adhérents.
            Remplissage de la table "self.data".

            Entrée :
                — fichier des adhérents, format csv.

            Sortie :
                — aucune (écrit les variables internes de l'objet)

        • distributeMembers()
            Ventilation du nombre de membres par communes ou
            par arrondissement pour les villes de Paris, Lyon et Marseille.

            Entrée :
                — aucune (lit les variables internes de l'objet)

            Sortie :
                — dictionnaire "code_commune: effectif"

        • printWarnings()
            Affiche le journal des anomalies détectées dans le fichier des
            adhérents lors de l'appel de la méthode "extractMembersData()".

            Entrée :
                — aucune (lit les variables internes de l'objet)

            Sortie :
                — affichage sur la console (sortie standard)
"""



class DistributeMembers:
    """
    cf. documentation du module.
    """
    refFileList = ['./data/insee/v_commune_2024.csv', './data/insee/v_commune_comer_2024.csv']

    def __init__(self, department):
        if self.__validDept(department):
            self.dept = department
        else:
            msg = '"' + department + '" n\'est pas un № de département valide !'
            raise ValueError(msg)
        self.data = []
        self.warnings = []

    def __validDept(self, department):
        """
        Vérification de la validité du № de département.
        (cette méthode ne devrait être appellée qu'à l'intérieur de la classe !)

        Entrée :
            • № de département

        Sortie :
            • Valeur bouléenne
        """
        import re

        # valid departmental numbers are:
        # numbers from "01" to "09"
        m1 = re.fullmatch('0[1-9]', department, flags=0)
        # numbers from "10" to "19" and from "30" to "89"
        m2 = re.fullmatch('[13-8][0-9]', department, flags=0)
        # numbers from "21" to "29", number "2A" and number "2B"
        m3 = re.fullmatch('2[1-9AaBb]', department, flags=0)
        # numbers from "90" to "95" and number "99"
        m4 = re.fullmatch('9[0-59]', department, flags=0)
        # numbers from "971" to "976"
        m5 = re.fullmatch('97[1-6]', department, flags=0)
        # number "984" and numbers from "986" to "988"
        m6 = re.fullmatch('98[46-8]', department, flags=0)
        # if one test matches…
        if (m1, m2, m3, m4, m5, m6) != (None, None, None, None, None, None):
            return(True)
        else:
            return(False)

 
    def __intheDpt(self, zc):
        """
        Appartenance d'un code postal à un département.
        (cette méthode ne devrait être appellée qu'à l'intérieur de la classe !)

        Entrée :
            • code postal

        Sortie :
            • Valeur bouléenne
        """
        match len(self.dept):
            # the number for French departments is made up
            # of the first 2 digits of the zip code
            case 2:
                return(self.dept == zc[:2])
            # the number for French overseas departments & territories is made up
            # of the first 3 digits of the postcode
            case 3:
                return(self.dept == zc[:3])


    def __readRefTable(self):
        """
        Lecture du fichier des communes de France.
        (cette méthode ne devrait être appellée qu'à l'intérieur de la classe !)

        Entrée :
            • aucune
        Sortie :
            • table de référence des communes, sans en-tête :
            | code | nom en clair, maj. | nom en clair, typo. riche | Libellé |
        """
        import os.path, csv

        refTable = []

        for refFile in self.refFileList:
            if not os.path.isfile(refFile):
                msg = 'Le fichier des communes ' + refFile + ' n\'existe pas !'
                raise RuntimeError(msg)
            with open(refFile, newline='') as csvfile:
                table = []
                # read the CSV file
                reader = csv.reader(csvfile, delimiter=',')
                for row in reader:
                    table.append(row)
                typecom = -1
                # identify index of usefull columns
                for i in range(0, len(table[0])):
                    match table[0][i]:
                        case 'TYPECOM':
                            typecom = i
                        case 'COM' | 'COM_COMER':
                            com = i
                        case 'DEP' | 'ARM' | 'COMER':
                            dep = i
                        case 'NCC':
                            ncc = i
                        case 'NCCENR':
                            nccenr = i
                        case 'LIBELLE':
                            libelle = i
                        case _:
                            pass
                # extract data
                for i in range (1, len(table)):
                    if (typecom == -1) or (table[i][typecom] in {'COM', 'ARM'}):
                        if table[i][dep] == self.dept:
                            refTable.append([table[i][com], table[i][ncc], table[i][nccenr], table[i][libelle]])
        return(refTable)


    def extractMembersData(self, membersDataFile):
        """
        cf. documentation du module.
        """
        import csv

        table = []  # empty list
        self.data = []    # empty list

        # extract data
        with open(membersDataFile, newline='') as csvfile:
            # read the CSV file
            reader = csv.reader(csvfile, delimiter=';')
            # append each file row to the list
            for row in reader:
                table.append(row)
        # get number of rows and columns
        rowsNumber = len(table)
        if rowsNumber > 0:
            columnsNumber = len(table[0])
        else:
            # "The files contains no data!"
            msg = 'Le fichier ' + membersDataFile + ' ne contient pas de données !'
            raise RuntimeError(msg)
        # parse the fist row and identify the numbers of required columns
        isActiveIndex = communeIndex = zipcodeIndex = -1  # undefined index value
        for i in range(0, columnsNumber):
            match table[0][i]:
                case 'Adhésion active ?':
                    isActiveIndex = i
                case 'Ville':
                    communeIndex = i
                case 'Code postal':
                    zipcodeIndex = i
                case _:
                    pass
        # check that nothing is missing
        if isActiveIndex == -1:
            # isActiveIndex in undefined, column is missing
            msg = 'La colonne "Adhésion active ?" est manquante !'
            raise RuntimeError(msg)
        if communeIndex == -1:
            # communeIndex in undefined, column is missing
            msg = 'La colonne "Ville" est manquante !'
            raise RuntimeError(msg)
        if zipcodeIndex == -1:
            # zipcodeIndex in undefined, column is missing
            msg = 'La colonne "Code postal" est manquante !'
            raise RuntimeError(msg)
        # Scroll the table data and extract the zipcode and commune of active members
        for i in range(1, rowsNumber):
            if table[i][isActiveIndex] == 'Oui':
                # member is active
                self.data.append([table[i][zipcodeIndex], table[i][communeIndex]])
            elif table[i][isActiveIndex] != 'Non':
                # value other than that expected
                msg = 'Le champ "Adhésion active ?" est bouléen ("Oui" ou "Non").\nLa valeur "'
                msg += table[i][isActiveIndex] + '" n\'est pas autorisée.'
                raise RuntimeError(msg)

    def distributeMembers(self):
        """
        cf. documentation du module.
        """
        mb = {}
        # indexes for "refTable"
        (com, ncc, nccenr, libelle) = (0, 1, 2, 3)
        # initialize the reference table with a list of the French communes
        refTable = self.__readRefTable()

        # for each member location
        for i in range(0, len(self.data)):
            zipcode = self.data[i][0]
            town = str(self.data[i][1])
            # whether the location is in the département
            if self.__intheDpt(zipcode):
                # look for the code of commune in the reference table
                for j in range(0, len(refTable)):
                    if town in {refTable[j][ncc], refTable[j][nccenr], refTable[j][libelle]}:
                        comcode = refTable[j][com]
                        # aditionnal process for "PARIS", "LYON", "MARSEILLE"
                        match comcode:
                            case '75056':
                                district = int(zipcode[-3:])
                                if (district >= 1 and district <= 20):
                                    comcode = str(75100 + district)
                                else:
                                    msg = "Le code postal \"" + zipcode
                                    msg += "\" n'a pas permis de déterminer l'arrondissement."
                                    self.warnings.append(msg)
                            case '69123':
                                district = int(zipcode[-3:])
                                if (district >= 1 and district <= 9):
                                    comcode = str(69380 + district)
                                else:
                                    msg = "Le code postal \"" + zipcode
                                    msg += "\" n'a pas permis de déterminer l'arrondissement."
                                    self.warnings.append(msg)
                            case '13055':
                                district = int(zipcode[-3:])
                                if (district >= 1 and district <= 16):
                                    comcode = str(13200 + district)
                                else:
                                    msg = "Le code postal \"" + zipcode
                                    msg += "\" n'a pas permis de déterminer l'arrondissement."
                                    self.warnings.append(msg)
                            case _:
                                pass
                        # update counter
                        # if counter not exists
                        if comcode not in mb:
                            # create counter
                            mb[comcode] = 0
                        # increment the counter
                        mb[comcode] += 1
                        break
                # not found
                else:
                    msg = "\"" + town + "\" n'est pas dans la liste de référence des communes."
                    self.warnings.append(msg)
            # outside the department
            else:
                msg = "\"" + zipcode + " " + town + "\" n'est pas dans le département № "
                msg += self.dept +"."
                self.warnings.append(msg)
        return(mb)

    def printWarnings(self):
        """
        cf. documentation du module.
        """
        # display warning messages
        if len(self.warnings) != 0:
            print('\nAttention :')
            for i in range (0, len(self.warnings)):
                print(self.warnings[i])

