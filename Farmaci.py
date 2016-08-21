import Menu
import Queries
from pymongo import MongoClient

import Updater

sortKey= Queries.prezzoPub
sortVal= 1
# il client
client = MongoClient()

# seleziono il database locale
db = client['local']

try:
    #looping
    while (True):

        # chiedo all'utente l'azione
        choice = Menu.getChoice()

        if choice==1:
            nomeprincipio = raw_input("Immettere il nome del principio attivo:\n")
            Queries.getFarmaciPerPrincipio(db,nomeprincipio,sortKey,sortVal)
            blbl = raw_input("Premere un tasto per continuare")

        elif choice==2:
            nomefarmaco =raw_input("Immettere il nome del farmaco di cui cercare gli equivalenti:\n")
            Queries.getEquivalenti(db,nomefarmaco,sortKey,sortVal)
            blbl = raw_input("Premere un tasto per continuare")

        elif choice==3:
            (sortKey,sortVal) = Menu.getSettings(sortKey,sortVal)

        elif choice==4:
            #path=raw_input("Immettere il percorso del file di aggiornamento")
            path = './csvs/Lista_equivalenti-16_febbraio_2015_0.csv'
            Updater.update(db,path)

        elif choice==0:
            client.close()
            print "Ciao!"
            break

except EOFError:
    client.close()
    print "Ciao!"
