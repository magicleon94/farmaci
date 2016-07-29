# coding=utf-8
#nomi dei campi della collection
principioAttivo = "Principio attivo"
confezioneRef = "Confezione di Riferimento"
confezione="Confezione"
atc = "ATC"
aic = "AIC"
farmaco = "Farmaco"
ditta="Ditta"
prezzoRef = "Prezzo riferimento 15 aprile 2011"
prezzoPub = "Prezzo Pubblico 16 febbraio 2015"
nota = "Nota"
differenza = "Differenza"
codiceEquivalenza = "Codice gruppo equivalenza"

infolist = [principioAttivo,farmaco,prezzoRef,prezzoPub,confezione]

#TODO fixare la tabulazione
row_format = u'{:40}' * (len(infolist)+1)

def getEquivalenti(db,nomefarmaco,sortKey=None,sortVal=None):

    try:
        res = db.farmaci.find({farmaco:{'$regex': nomefarmaco,'$options':'i'}}).limit(1)
        principio = res[0][principioAttivo]
        res = db.farmaci.find({principioAttivo:principio},{info:1 for info in infolist})

        if sortKey is not None and sortVal is not None:
            res.sort([(sortKey,sortVal)])

        print "Gli equivalenti di " + nomefarmaco.title() + " sono: "
        print row_format.format("",*infolist)
        for obj in res:
            data = [obj[info] for info in infolist]
            print row_format.format("",*data)


    except IndexError:
        print("Il farmaco non è presente nella lista\n")

def getFarmaciPerPrincipio(db,nomeprincipio,sortKey=None,sortVal=None):

        try:
            res = db.farmaci.find({principioAttivo:{'$regex':nomeprincipio,'$options':'i'}},{info:1 for info in infolist})

            if sortKey is not None and sortVal is not None:
                res.sort([(sortKey,sortVal)])
            print "I farmaci caratterizzati dal principio attivo " + nomeprincipio.title() + " sono: \n"
            print row_format.format("", *infolist)
            for obj in res:
                data = [obj[info] for info in infolist]
                print row_format.format("",*data)
        except IndexError:
            print "Il principio attivo non è presente nella lista\n"
