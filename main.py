#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

# Copyright © 2024, Place publique, Xavier Schoepfer
# GNU GENERAL PUBLIC LICENSE Version 3

import os.path

from membersmap import DistributeMembers

 
def main():
    # if the data file does NOT exist, DO NOTHING
    datafile = './data/adh26-2024-10-28.csv'
    if os.path.isfile(datafile):
        # initialize an object for the department № 26
        count26 = DistributeMembers('26')
        # extract informations (zip code and town) for active members
        count26.extractMembersData(datafile)
        # get counters
        membersCounter = count26.distributeMembers()
        # display counters by town or arrondissement
        for key in sorted(membersCounter):
            print (key, membersCounter[key])
        # display warning messages
        count26.printWarnings()



if __name__ == '__main__':
    main()
