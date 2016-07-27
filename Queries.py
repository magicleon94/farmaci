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

def getEquivalenti(db,nomefarmaco,sortKey=None,sortVal=None):
    res = db.farmaci.find({farmaco:nomefarmaco.upper()}).limit(1)
    principio = res[0][principioAttivo]
    res = db.farmaci.find({principioAttivo:principio})
    equivalenti = []
    for i in res:
        nome = i[farmaco]
        prezzo = i[prezzoPub]
        if nomefarmaco not in equivalenti:
            equivalenti.append((nome,prezzo))

    print "Gli equivalenti di " + nomefarmaco.upper() + " sono: "
    for (i,j) in equivalenti:
        print "Nome: " + i + "\t\t Prezzo: " + str(j)