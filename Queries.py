# coding=utf-8
from Constants import *
from tabulate import tabulate

infolist = [principioAttivo,farmaco,prezzoPub,confezione]

#TODO fixare la tabulazione
row_format = u'{:15}' * (len(infolist)+1)

def getEquivalenti(db,nomefarmaco,sortKey=None,sortVal=None):

    try:
        res = db.farmaci.find({farmaco:{'$regex': nomefarmaco,'$options':'i'}}).limit(1)
        principio = res[0][principioAttivo]
        res = db.farmaci.find({principioAttivo:principio},{info:1 for info in infolist})
        table = []

        if sortKey is not None and sortVal is not None:
            res.sort([(sortKey,sortVal)])

        print "Gli equivalenti di " + nomefarmaco.title() + " sono: "
        # print row_format.format("",*infolist)
        for obj in res:
            data = [obj[info] for info in infolist]
            #print row_format.format("",*data)
            table.append(data)
        print tabulate(table,headers=infolist)


    except IndexError:
        print("Il farmaco non è presente nella lista\n")

def getFarmaciPerPrincipio(db,nomeprincipio,sortKey=None,sortVal=None):

        try:
            res = db.farmaci.find({principioAttivo:{'$regex':nomeprincipio,'$options':'i'}},{info:1 for info in infolist})
            table = []
            if sortKey is not None and sortVal is not None:
                res.sort([(sortKey,sortVal)])
            print "I farmaci caratterizzati dal principio attivo " + nomeprincipio.title() + " sono: \n"
            # print row_format.format("", *infolist)
            for obj in res:
                data = [obj[info] for info in infolist]
                #print row_format.format("",*data)
                table.append(data)
            print tabulate(table,headers=infolist)
        except IndexError:
            print "Il principio attivo non è presente nella lista\n"
