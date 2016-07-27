import pymongo
import Menu
import Queries
from pymongo import MongoClient
sortKey= Queries.prezzoPub
sortVal= 1
# il client
client = MongoClient()

# seleziono il database locale
db = client['local']

#looping
while (True):

    # chiedo all'utente l'azione
    choice = Menu.getChoice()

    if choice==1:
        nomeprincipio = raw_input("Immettere il nome del principio attivo:\n")
        Queries.getFarmaciPerPrincipio(db,nomeprincipio,sortKey,sortVal)
    elif choice==2:
        nomefarmaco =raw_input("Immettere il nome del farmaco di cui cercare gli equivalenti:\n")
        Queries.getEquivalenti(db,nomefarmaco,sortKey,sortVal)
    elif choice==3:
        (sortKey,sortVal) = Menu.getSettings(sortKey,sortVal)
    elif choice==0:
        print "Ciao!"
        break
