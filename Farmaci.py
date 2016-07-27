import pymongo
import Menu
import Queries
from pymongo import MongoClient
sortKey= None
sortVal= None
# il client
client = MongoClient()

# seleziono il database locale
db = client['local']

# chiedo all'utente l'azione
choice = Menu.getChoice()

if choice==1:
    pass #placeholder
elif choice==2:
    nomefarmaco =raw_input("Immettere il nome del farmaco di cui cercare gli equivalenti:\n")
    Queries.getEquivalenti(db,nomefarmaco,sortKey,sortVal)
elif choice==3:
    (sortKey,sortVal) = Menu.getSettings()
