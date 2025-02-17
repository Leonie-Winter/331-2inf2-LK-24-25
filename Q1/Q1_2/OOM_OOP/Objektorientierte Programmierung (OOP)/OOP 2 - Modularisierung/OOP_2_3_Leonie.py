'''
Aufgabe 1

(a) Mache dich mit dem Quelltext vertraut. Ergänze die Ereignisverarbeitungsprozedur und teste das Programm.

(b) Ergänze das Programm so, dass zwei Ampeln simuliert werden. 
'''
#------------------------------------------------------------------------------
# Datenmodell
#------------------------------------------------------------------------------

from ampel import Ampel

# Erstellen von zwei Ampeln
ampel1 = Ampel('rot')
ampel2 = Ampel('gruen')

#------------------------------------------------------------------------------
# GUI
#------------------------------------------------------------------------------

def anzeigeAktualisieren(lampeRot1, lampeGelb1, lampeGruen1, lampeRot2, lampeGelb2, lampeGruen2):
    # Aktualisierung der ersten Ampel
    if lampeRot1:
        labelRot1.config(background='red')
    else:
        labelRot1.config(background='gray')
    if lampeGelb1:
        labelGelb1.config(background='yellow')
    else:
        labelGelb1.config(background='gray')
    if lampeGruen1:
        labelGruen1.config(background='green')
    else:
        labelGruen1.config(background='gray')

    # Aktualisierung der zweiten Ampel
    if lampeRot2:
        labelRot2.config(background='red')
    else:
        labelRot2.config(background='gray')
    if lampeGelb2:
        labelGelb2.config(background='yellow')
    else:
        labelGelb2.config(background='gray')
    if lampeGruen2:
        labelGruen2.config(background='green')
    else:
        labelGruen2.config(background='gray')

def buttonWeiterClick():
    """Verarbeitung der Daten
       ... Ampeln weiter schalten
       Aktualisierung der Anzeige
       ... Lampenzustand abfragen und anzeigen
    """
    ampel1.schalten()
    ampel2.schalten()
    
    (lampeRot1, lampeGelb1, lampeGruen1) = ampel1.getLampen()
    (lampeRot2, lampeGelb2, lampeGruen2) = ampel2.getLampen()
    
    anzeigeAktualisieren(lampeRot1, lampeGelb1, lampeGruen1, lampeRot2, lampeGelb2, lampeGruen2)
    automaticSwitch()

def automaticSwitch():
    fenster.after(1000, buttonWeiterClick)


from tkinter import *

# Erzeugung des Fensters
fenster = Tk()
fenster.title("Ampeln")
fenster.geometry("300x200")
automaticSwitch()
# Rahmen für die erste Ampel
frameAmpel1 = Frame(master=fenster, background='darkgray')
frameAmpel1.place(x=30, y=20, width=40, height=100)

# Label Rot-Licht für die erste Ampel
labelRot1 = Label(master=frameAmpel1, background='gray')
labelRot1.place(x=10, y=10, width=20, height=20)
# Gelb-Licht für die erste Ampel
labelGelb1 = Label(master=frameAmpel1, background='gray')
labelGelb1.place(x=10, y=40, width=20, height=20)
# Grün-Licht für die erste Ampel
labelGruen1 = Label(master=frameAmpel1, background='gray')
labelGruen1.place(x=10, y=70, width=20, height=20)

# Rahmen für die zweite Ampel
frameAmpel2 = Frame(master=fenster, background='darkgray')
frameAmpel2.place(x=200, y=20, width=40, height=100)

# Label Rot-Licht für die zweite Ampel
labelRot2 = Label(master=frameAmpel2, background='gray')
labelRot2.place(x=10, y=10, width=20, height=20)
# Gelb-Licht für die zweite Ampel
labelGelb2 = Label(master=frameAmpel2, background='gray')
labelGelb2.place(x=10, y=40, width=20, height=20)
# Grün-Licht für die zweite Ampel
labelGruen2 = Label(master=frameAmpel2, background='gray')
labelGruen2.place(x=10, y=70, width=20, height=20)

# Aktualisierung der Anzeige
(lampeRot1, lampeGelb1, lampeGruen1) = ampel1.getLampen()
(lampeRot2, lampeGelb2, lampeGruen2) = ampel2.getLampen()
anzeigeAktualisieren(lampeRot1, lampeGelb1, lampeGruen1, lampeRot2, lampeGelb2, lampeGruen2)

# Button zum Auswerten
buttonWeiter = Button(master=fenster,
                      text="weiter",
                      command=buttonWeiterClick)
buttonWeiter.place(x=100, y=150, width=100, height=20)

# Start der Ereigniss
fenster.mainloop()
