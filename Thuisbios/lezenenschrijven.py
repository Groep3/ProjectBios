def schijven(lst,bestand):
    bestand = open(bestand, 'w')
    bestand.writelines(lst)
    bestand.close()

def lezen(bestand):
    bestand = open(bestand)
    inhoud = bestand.readlines()
    bestand.close()
    return(inhoud)

