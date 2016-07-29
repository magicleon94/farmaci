import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def getChoice():
    while (True):
        clear()
        print "---- MENU ----"
        print "1. Ricerca farmaci per principio attivo"
        print "2. Ricerca equivalenti ad un farmaco specificandone il nome"
        print "3. Impostazioni generali"
        print "4. Aggiorna banca dati"
        print "0. Esci"
        choice = raw_input("Scelta: \t")
        if choice.isdigit():
            choice = int(choice)
            if choice>=0 and choice<=4:
                return choice
        blbl = raw_input("Scelta non valida, riprovare.\nPremere un tasto per continuare\t")

def getSettings(oldKey,oldVal):
    while(True):
        clear()
        newKeySet = 0
        newValSet = 0
        print "---- IMPOSTAZIONI INTERROGAZIONI ----"
        print "1. Parametro di ordine"
        print "2. Criterio di ordinamento del parametro di ordine"
        print "0. Indietro"
        choice = raw_input("Scelta: \t")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                newKey = _getNewKey()
                newKeySet = 1
            elif choice==2:
                newVal = _getNewVal()
                newValSet = 1
            elif choice == 0:
                if newKeySet == 0:
                    newKey = oldKey
                if newValSet == 0:
                    newVal = oldVal
                return (newKey,newVal)
            else:
                blbl = raw_input("Scelta non valida, riprovare.\nPremere un tasto per continuare\t")


def _getNewKey():
    clear()
    while(True):
        print "Seleziona la nuova chiave di ordinamento: "
        print "1. Nome Farmaco"
        print "2. Prezzo"
        print "3. Nessuno"
        choice = raw_input("Scelta: \t")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                return "Farmaco"
            elif choice == 2:
                return "Prezzo Pubblico 16 febbraio 2015"
            elif choice == 3:
                return None
        blbl = raw_input("Scelta non valida, riprovare.\nPremere un tasto per continuare\t")

def _getNewVal():
    while(True):
        clear()
        print "Seleziona il nuovo criterio di ordinamento: "
        print "1. Ascendente"
        print "2. Discendente"
        print "3. Nessuno"
        choice = raw_input("Scelta: \t")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                return 1
            elif choice == 2:
                return -1
            elif choice == 3:
                return None
        blbl = raw_input("Scelta non valida, riprovare.\nPremere un tasto per continuare\t")
