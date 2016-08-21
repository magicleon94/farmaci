# Il file di update deve utilizzare come delimitatori le virgole.
import csv
from Constants import *
import os

keys = [principioAttivo,confezioneRef,atc,aic,farmaco,confezione,ditta,prezzoRef,prezzoPub,differenza,nota,codiceEquivalenza]

def update(db,filepath):
    try:
        #genero il file formattato correttamente
        os.system("./transform.sh " + filepath)
        #apro il file
        updateFile = open("./farmaciUpdate.csv",'rU')

        #leggo il file
        reader = csv.reader(updateFile)

        #salto la prima riga, quella degli header
        next(reader,None)

        #Aggiorno tutto
        for row in reader:
            data = {key:val for (key,val) in zip(keys,row)}
            db.farmaci.update({principioAttivo:data[principioAttivo],farmaco:data[farmaco],confezioneRef:data[confezioneRef]},{'$set':data},upsert=True)

        updateFile.close()
        os.remove("./farmaciUpdate.csv")
    except IOError:
        print "File non trovato"


