# Il file di update deve utilizzare come delimitatori le virgole.
import csv
from Constants import *

keys = [principioAttivo,confezioneRef,atc,aic,confezione,farmaco,ditta,prezzoRef,prezzoPub,differenza,nota,codiceEquivalenza]
def update(db,filepath):
    try:
        limit = 10  # limite di righe da leggere per l'update, dato che ho un file completo, per avere un minore carico computazionale
        updateFile = open(filepath,'rU')
        reader = csv.reader(updateFile)
        for row in reader:
            data = {key:val for (key,val) in zip(keys,row)}
            #print data
            db.farmaci.update({principioAttivo:data[principioAttivo],farmaco:data[farmaco],confezioneRef:data[confezioneRef]},{'$set':data},upsert=True)
            limit -= 1
            if limit == 0:
                break
        updateFile.close()
    except IOError:
        print "File non trovato"


