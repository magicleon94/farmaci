# coding=utf-8
from Constants import *
from tabulate import tabulate

#lista dei campi da mostrare
infolist = [principioAttivo,farmaco,prezzoPub,confezione]

def getEquivalenti(db,nomefarmaco,sortKey=None,sortVal=None):

    try:
        #Determino il principio attivo
        res = db.farmaci.find({farmaco:{'$regex': nomefarmaco,'$options':'i'}}).limit(1)
        principio = res[0][principioAttivo]

        #Trovo gli equivalenti
        res = db.farmaci.find({principioAttivo:principio},{info:1 for info in infolist})
        table = []

        #Effettuo il sorting dei risultati
        if sortKey is not None and sortVal is not None:
            res.sort([(sortKey,sortVal)])

        print "Gli equivalenti di " + nomefarmaco.title() + " sono: "

        #Costruisco la tabella
        for obj in res:
            data = [obj[info] for info in infolist]
            table.append(data)

        #Stampo la tabella
        print tabulate(table,headers=infolist)

    except IndexError:
        print("Il farmaco non è presente nella lista\n")


def getFarmaciPerPrincipio(db,nomeprincipio,sortKey=None,sortVal=None):

        try:
            #Trovo i farmaci caratterizzati dal principio attivo
            res = db.farmaci.find({principioAttivo:{'$regex':nomeprincipio,'$options':'i'}},{info:1 for info in infolist})
            table = []

            #Effettuo il sorting dei risultati
            if sortKey is not None and sortVal is not None:
                res.sort([(sortKey,sortVal)])
            print "I farmaci caratterizzati dal principio attivo " + nomeprincipio.title() + " sono: \n"

            #Costruisco la tabella
            for obj in res:
                data = [obj[info] for info in infolist]
                table.append(data)

            #Stampo la tabella
            print tabulate(table,headers=infolist)

        except IndexError:
            print "Il principio attivo non è presente nella lista\n"
