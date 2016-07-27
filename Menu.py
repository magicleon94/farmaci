def getChoice():
    while (True):
        print "---- MENU ----"
        print "1. Ricerca farmaci per principio attivo"
        print "2. Ricerca equivalenti ad un farmaco specificandone il nome"
        print "3. Impostazioni generali"
        print "0. Esci"
        choice = raw_input("Scelta: \n")
        if choice.isdigit():
            choice = int(choice)
            if choice>0 and choice<=2:
                return choice
        print "Scelta non valida, riprovare"

def getSettings(oldKey,oldVal):
    while(True):
        newKeySet = 0
        newValSet = 0
        print "---- IMPOSTAZIONI INTERROGAZIONI ----"
        print "1. Parametro di ordine"
        print "2. Criterio di ordinamento del parametro di ordine"
        print "0. Esci"
        choice = raw_input("Scelta: \n")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                newKey = getNewKey()
                newKeySet = 1
            elif choice==2:
                newVal = getNewVal()
                newValSet = 1
            elif choice == 0:
                if newKeySet == 0:
                    newKey = oldKey
                if newValSet == 0:
                    newVal = oldVal
                return (newKey,newVal)

        print "Scelta non valida, riprovare"


def _getNewKey():
    while(True):
        print "Seleziona la nuova chiave di ordinamento: "
        print "1. Nome Farmaco"
        print "2. Prezzo"
        print "3. Nessuno"
        choice = raw_input("Scelta: \n")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                return "Farmaco"
            elif choice == 2:
                return "Prezzo Pubblico 16 febbraio 2015"
            elif choice == 3:
                return None
        print "Scelta non valida, riprovare"

def _getNewVal():
    while(True):
        print "Seleziona il nuovo criterio di ordinamento: "
        print "1. Ascendente"
        print "2. Discendente"
        print "3. Nessuno"
        choice = raw_input("Scelta: \n")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                return 1
            elif choice == 2:
                return 2
            elif choice == 3:
                return None
        print "Scelta non valida, riprovare"
