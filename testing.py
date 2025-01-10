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
    # if the data file does NOT exist, DO NOTHING
    datafile = './data/adh26-2024-10-28.csv'
    if os.path.isfile(datafile):
        test("26", datafile)



if __name__ == '__main__':
    main()
