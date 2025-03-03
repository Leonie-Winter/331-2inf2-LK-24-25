"""Softwareobjekte zur Simulation von Ampeln, Aufgabe 2, Alexander Pfeffer"""
from time import sleep


class Ampel(object):
    def __init__(self):
        self.lampeRot = False
        self.lampeGelb = False
        self.lampeGruen = False

    def setLampen(self, startwertLampeRot, startwertLampeGelb, startwertLampeGruen):
        self.lampeRot = startwertLampeRot
        self.lampeGelb = startwertLampeGelb
        self.lampeGruen = startwertLampeGruen

    def schalten(self):
        # Rot auf Gelb
        if (self.lampeRot, self.lampeGelb, self.lampeGruen) == (True, False, False):
            self.lampeGelb = True

        # Gelb auf Grün
        elif (self.lampeRot, self.lampeGelb, self.lampeGruen) == (True, True, False):
            self.lampeRot = False
            self.lampeGelb = False
            self.lampeGruen = True

        # Grün auf Gelb
        elif (self.lampeRot, self.lampeGelb, self.lampeGruen) == (False, False, True):
            self.lampeGruen = False
            self.lampeGelb = True
        # Gelb auf Rot
        elif (self.lampeRot, self.lampeGelb, self.lampeGruen) == (False, True, False):
            self.lampeGelb = False
            self.lampeRot = True

# Aufgabe 3
"""
a) Man erzeugt die ampel1 mit Ampel(). Den Zustand
kriegt man mit ampel1.variablennamen
Um eine Methode auf ein Objekt zu verwenden, funktioniert das ähnlich
"""


ampel1 = Ampel() # Init das Objekt
print(f"Zustand Lampe Rot: {ampel1.lampeRot}") 
# ampel1.lampeGelb
print(f"Zustand Lampe Gelb: {ampel1.lampeRot}") 

# ampel1.lampeGruen
print(f"Zustand Lampe Grün: {ampel1.lampeGruen}") 

print("------")
ampel1.setLampen(True, False, False)
# ampel1.lampeRot
print(f"Zustand Lampe Rot: {ampel1.lampeRot}") 

#ampel1.lampeGelb
print(f"Zustand Lampe Gelb: {ampel1.lampeGelb}") 

#ampel1.lampeGruen
print(f"Zustand Lampe Grün: {ampel1.lampeGruen}") 

print("------")
ampel1.schalten()
#ampel1.lampeRot
print(f"Zustand Lampe Rot: {ampel1.lampeRot}") 

#ampel1.lampeGelb
print(f"Zustand Lampe Gelb: {ampel1.lampeGelb}")
#ampel1.lampeGruen
print(f"Zustand Lampe Grün: {ampel1.lampeGruen}") 

print("------")
ampel1.schalten()
#ampel1.lampeRot
print(f"Zustand Lampe Rot: {ampel1.lampeRot}") 

#ampel1.lampeGelb
print(f"Zustand Lampe Gelb: {ampel1.lampeGelb}")
#ampel1.lampeGruen
print(f"Zustand Lampe Grün: {ampel1.lampeGruen}") 

print("------")
ampel1.schalten()
#ampel1.lampeRot
print(f"Zustand Lampe Rot: {ampel1.lampeRot}") 

#ampel1.lampeGelb
print(f"Zustand Lampe Gelb: {ampel1.lampeGelb}")
#ampel1.lampeGruen
print(f"Zustand Lampe Grün: {ampel1.lampeGruen}") 

print("------")
ampel1.schalten()
#ampel1.lampeRot
print(f"Zustand Lampe Rot: {ampel1.lampeRot}") 

#ampel1.lampeGelb
print(f"Zustand Lampe Gelb: {ampel1.lampeGelb}")
#ampel1.lampeGruen
print(f"Zustand Lampe Grün: {ampel1.lampeGruen}") 


# Aufgabe 4

# a) Printet den Zustand wie oben

# b)

ampel1 = Ampel()
ampel2 = Ampel()
ampel3 = Ampel()
ampel4 = Ampel()

ampel1.setLampen(True, False, False)
ampel2.setLampen(False, False, True)
ampel3.setLampen(True, False, False)
ampel4.setLampen(False, False, True)

for i in range(4):
    sleep(1)

    for index, ampel in enumerate((ampel1, ampel2, ampel3, ampel4)):
        ampel.schalten()
        #ampel1.lampeRot
        print("------")
        print(f"Ampel {index + 1}:")

        print(f"Zustand Lampe Rot: {ampel.lampeRot}") 
        print(f"Zustand Lampe Gelb: {ampel.lampeGelb}")
        print(f"Zustand Lampe Grün: {ampel.lampeGruen}") 
