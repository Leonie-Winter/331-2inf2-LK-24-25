class Ampel(object):

    __slots__ = ('zustand')
    
    def __init__(self, anfangszustand):
        """nachher:
           Ein Objekt der Klasse Ampel ist erzeugt.
           Der Wert des Attributs zustand wird auf den übergebenen
           Parameter gesetzt.
        """

        self.zustand = anfangszustand

    def setZustand(self, z):
        """ vorher:
           Der Wert des Attributs zustand beschreibt eine Ampelphase.
           nachher:
           Dem Attribut zustand ist der Wert des übergebenen Parameters
           z zugewiesen.
        """
        
        self.zustand = z

    def getZustand(self):
        """Die Funktion ändert den Objektzustand nicht.
           Die Funktion liefert als Ergebnis den Wert von zustand zurück.
        """
        
        return self.zustand

    def schalten(self):
        """vorher:
           Der Wert des Attributs zustand beschreibt eine Ampelphase.
           nachher:
           Der Wert des Attributs zustand beschreibt die nächste Phase gemäß 
           des üblichen Ampelzyklus "rot -> rotgelb > gruen -> gelb -> rot".
        """
        
        if self.zustand == 'rot':
            self.zustand = 'rotgelb'
        elif self.zustand == 'rotgelb':
            self.zustand = 'gruen'
        elif self.zustand == 'gruen':
            self.zustand = 'gelb'
        elif self.zustand == 'gelb':
            self.zustand = 'rot'

    def getLampen(self):
        """Die Funktion ändert den Objektzustand nicht.
           Die Funktion liefert als Ergebnis ein Tripel aus Wahrheitswerten,
           die den zur Phase passenden Lampenzustand in der Reihenfolge
           (Lampe-rot, Lampe-gelb, Lampe-grün) beschreibt.
        """
        
        if self.zustand == 'rot':
            lampen = (True, False, False)
        elif self.zustand == 'rotgelb':
            lampen = (True, True, False)
        elif self.zustand == 'gruen':
            lampen = (False, False, True)
        elif self.zustand == 'gelb':
            lampen = (False, True, False)
        return lampen
