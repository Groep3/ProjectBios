def schijvenlijst(lst,bestand):
    bestand = open(bestand, 'w')
    bestand.writelines(lst)
    bestand.close()

def schijvenstring(str,bestand):
    bestand = open(bestand, 'a')
    bestand.write(str)
    bestand.close()

def lezen(bestand):
    bestand = open(bestand)
    inhoud = bestand.readlines()
    bestand.close()
    return(inhoud)

