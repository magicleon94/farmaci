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

#TODO fixare i duplicati

def getEquivalenti(db,nomefarmaco,sortKey=None,sortVal=None):

    try:
        res = db.farmaci.find({farmaco:{'$regex': nomefarmaco,'$options':'i'}}).limit(1)
        principio = res[0][principioAttivo]
        res = db.farmaci.find({principioAttivo:principio})

        if sortKey is not None and sortVal is not None:
            res.sort([(sortKey,sortVal)])

        equivalenti = []
        for i in res:
            nome = i[farmaco]
            prezzo = i[prezzoPub]
            if (nomefarmaco,prezzo) not in equivalenti:
                equivalenti.append((nome,prezzo))

        print "Gli equivalenti di " + nomefarmaco.title() + " sono: "
        for (i,j) in equivalenti:
            print "Nome: " + i
            print "Prezzo: " + str(j)
    except IndexError:
        print("Il farmaco non è presente nella lista\n")

def getFarmaciPerPrincipio(db,nomeprincipio,sortKey=None,sortVal=None):

        try:
            res = db.farmaci.find({principioAttivo:{'$regex':nomeprincipio,'$options':'i'}})

            if sortKey is not None and sortVal is not None:
                res.sort([(sortKey,sortVal)])
            print "I farmaci caratterizzati dal principio attivo " + nomeprincipio.title() + " sono: \n"
            for obj in res:
                print "Nome: " + obj[farmaco]
                print "Confezione: " + obj[confezione]
                print "Prezzo: " + str(obj[prezzoPub])

        except IndexError:
            print "Il principio attivo non è presente nella lista\n"