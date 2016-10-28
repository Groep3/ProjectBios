from lezenenschrijven import *
import time
date = time.strftime('%d-%m-%Y', time.localtime())
database = 'mogelijke films'+ ' '+date+'.csv'
database2 = 'aanbiedingMaarten' + ' '+date+'.csv'


def filmsaanbieden(database,databasekeuzes,aanbieder):
    inhoud = lezen(database)
    inhoud2 = lezen(databasekeuzes)

    lst = []
    for line in inhoud2:
        if line in inhoud:
            lst.append(line)

    schijvenlijst(lst,'aanbieding'+aanbieder+ ' '+date+'.csv')

def change(database,aanbiederdata):
    inhoud = lezen(database)
    inhoud2 = lezen(aanbiederdata)

    lst = []
    for line in inhoud:
       if line not in inhoud2:
            lst.append(line)

    schijvenlijst(lst,'mogelijke films'+ ' '+date+'.csv')

change(database,database2)
