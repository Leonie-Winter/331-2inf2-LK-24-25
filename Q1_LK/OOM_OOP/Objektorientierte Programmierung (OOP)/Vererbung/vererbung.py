class Ampel(object):
    def __init__(self, pListeZustaende):
        self.listeZustaende = pListeZustaende
        self.indexAktuellerZustand = 0

    def schalten(self):
        if self.indexAktuellerZustand < len(self.listeZustaende) - 1:
            self.indexAktuellerZustand += 1
        else:
            self.indexAktuellerZustand = 0

    def getZustand(self):
        return self.listeZustaende[self.indexAktuellerZustand]

    def setZustand(self, z):
        self.indexAktuellerZustand = self.listeZustaende.index(z)

class AmpelAmerikanisch(Ampel):
    def __init__(self, anfangszustand):
        # Die Liste der möglichen Zustände enthält nur 'rot', 'gruen', 'gelb'
        self.listeZustaende = ['rot', 'gruen', 'gelb']
        self.indexAktuellerZustand = self.listeZustaende.index(anfangszustand)
        self.blinkend = False  # Startzustand: keine blinkende Ampel
        self.blinkStatus = False  # Gibt an, ob die Ampel im "Blink"-Zustand ist

    def getLampen(self):
        if self.blinkend:
            # Wenn der blinkende Modus aktiv ist, wechselt die Ampel zwischen rot und schwarz
            if self.blinkStatus:
                lampen = (True, False, False)  # Rot ist an
            else:
                lampen = (False, False, False)  # Alle Lampen aus (schwarz)
            # Nach jedem Aufruf wechseln wir den Blinkstatus
            self.blinkStatus = not self.blinkStatus
        else:
            # Normale Zustände
            zustand = self.listeZustaende[self.indexAktuellerZustand]
            if zustand == 'rot':
                lampen = (True, False, False)
            elif zustand == 'gruen':
                lampen = (False, False, True)
            elif zustand == 'gelb':
                lampen = (False, True, False)
        return lampen

    def schalten(self):
        if not self.blinkend:  # Nur wenn der Blinkmodus nicht aktiv ist, kann geschaltet werden
            if self.indexAktuellerZustand < len(self.listeZustaende) - 1:
                self.indexAktuellerZustand += 1
            else:
                self.indexAktuellerZustand = 0

    def setBlinkendModus(self, aktivieren):
        # Funktion zum Aktivieren oder Deaktivieren des blinkenden Modus
        self.blinkend = aktivieren
        self.blinkStatus = False  # Starten bei "schwarz", wenn der Modus aktiviert wird

    def getZustand(self):
        if self.blinkend:
            # Im Blinkmodus wird immer 'rot' angezeigt
            if self.blinkStatus:
                zustand = 'rot'  # Rot leuchtet
            else:
                zustand = 'schwarz'  # Alle Lampen aus (schwarz)
            # Nach jedem Aufruf wechseln wir den Blinkstatus
            self.blinkStatus = not self.blinkStatus
        else:
            zustand = super().getZustand()  # Normale Zustände (rot, gruen, gelb)
        return zustand


# Test der Ampel mit getZustand

ampel = AmpelAmerikanisch('rot')

# Zunächst sollte die Ampel auf 'rot' sein
print(ampel.getZustand())  # Sollte 'rot' ausgeben

ampel.schalten()
# Jetzt sollte die Ampel auf 'gruen' sein
print(ampel.getZustand())  # Sollte 'gruen' ausgeben

ampel.schalten()
# Jetzt sollte die Ampel auf 'gelb' sein
print(ampel.getZustand())  # Sollte 'gelb' ausgeben

# Aktivieren des blinkenden Modus
ampel.setBlinkendModus(True)

# Jetzt sollte die Ampel im "rot blinkend" Modus sein
print(ampel.getZustand())  # Sollte 'rot' ausgeben (blinkend)

# Beim nächsten Aufruf sollte sie "schwarz" sein
ampel.schalten()
print(ampel.getZustand())  # Sollte 'schwarz' ausgeben

# Wieder "rot"
ampel.schalten()
print(ampel.getZustand())  # Sollte 'rot' ausgeben (blinkend)

# Deaktivieren des blinkenden Modus
ampel.setBlinkendModus(False)
print(ampel.getZustand())  # Sollte 'rot' ausgeben (zurück zu rot)
