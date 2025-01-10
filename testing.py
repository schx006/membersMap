#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

# Copyright © 2024, Place publique, Xavier Schoepfer
# GNU GENERAL PUBLIC LICENSE Version 3

import os.path

from membersmap import DistributeMembers


def test(dept, df):
    # initialize an object for a department
    mapping = DistributeMembers(dept)
    # extract informations (zip code and town) for active members
    mapping.extractMembersData(df)
    # get counters
    membersCounter = mapping.distributeMembers()
    # display counters by town or arrondissement
    for key in sorted(membersCounter):
        print (key, membersCounter[key])
    # display warning messages
    mapping.printWarnings()


def main():
    """
    Programme de test de la bibliothèque « membersmap »,
    choix des options du jeu de test :

        0   département № 26, fichier d'extration correct ;

        1   code départemental erroné ;
        2   fichier d'extraction des membres vide ;
        3   fichier d'extraction avec une erreur du libellé colonne 1 ;
        4   fichier d'extraction avec une erreur du libellé colonne 2 ;
        5   fichier d'extraction avec une erreur du libellé colonne 3 ;
        6   valeur erronée dans la colonne « Adhésion active ? » ;

        7   tri par arrondissements, ville de Paris ;
        8   tri par arrondissements, ville de Lyon ;
        9   tri par arrondissements, ville de Marseille ;

        Q   Arrêt du programme de test.
    """
    while True:
        print(main.__doc__)
        choice = input("Saisissez votre choix : ")

        match choice:
            case '0':
                dept = '26'
                datafile = './data/adh26-2024-10-28.csv'
            case '1':
                dept = '98'
                datafile = './data/adh26-2024-10-28.csv'
            case '2':
                dept = '01'
                datafile = './data/testing/empty.csv'
            case '3':
                dept = '2a'
                datafile = './data/testing/erreur-label-col1.csv'
            case '4':
                dept = '2A'
                datafile = './data/testing/erreur-label-col2.csv'
            case '5':
                dept = '2b'
                datafile = './data/testing/erreur-label-col3.csv'
            case '6':
                dept = '2B'
                datafile = './data/testing/erreur-champ-membre_actif.csv'
            case '7':
                dept = '75'
                datafile = './data/testing/test-arrt-paris.csv'
            case '8':
                dept = '69'
                datafile = './data/testing/test-arrt-lyon.csv'
            case '9':
                dept = '13'
                datafile = './data/testing/test-arrt-marseille.csv'
            case 'q' | 'Q':
                exit(0)
            case _:
                pass
    
        if os.path.isfile(datafile):
            test(dept, datafile)
        else:
            print("Fichier \"" + datafile + "\" non trouvé !")
            exit(1)



if __name__ == '__main__':
    main()
