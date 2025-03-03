from tkinter import *
from random import randint
# Ereignisverarbeitung

def Button_Wuerfel_Click():
    # Verarbeitung der Daten
    wuerfelA = randint(1,6)
    # Verwaltung und Anzeige der Daten
    labelWuerfelA.config(text=str(wuerfelA))
    # Anzeige der Daten
    if wuerfelA == 1:
        labelWuerfelA.config(image=imageWuerfel1)
    elif wuerfelA == 2:
        labelWuerfelA.config(image=imageWuerfel2)
    elif wuerfelA == 3:
        labelWuerfelA.config(image=imageWuerfel3)
    elif wuerfelA == 4:
        labelWuerfelA.config(image=imageWuerfel4)
    elif wuerfelA == 5:
        labelWuerfelA.config(image=imageWuerfel5)
    elif wuerfelA == 6:
        labelWuerfelA.config(image=imageWuerfel6)

# Verarbeitung der Daten
    wuerfelB = randint(1,6)
    # Verwaltung und Anzeige der Daten
    labelWuerfelB.config(text=str(wuerfelB))
    # Anzeige der Daten
    if wuerfelB == 1:
        labelWuerfelB.config(image=imageWuerfel1)
    elif wuerfelB == 2:
        labelWuerfelB.config(image=imageWuerfel2)
    elif wuerfelB == 3:
        labelWuerfelB.config(image=imageWuerfel3)
    elif wuerfelB == 4:
        labelWuerfelB.config(image=imageWuerfel4)
    elif wuerfelB == 5:
        labelWuerfelB.config(image=imageWuerfel5)
    elif wuerfelB == 6:
        labelWuerfelB.config(image=imageWuerfel6)
# Verarbeitung der Daten
    wuerfelC = randint(1,6)
    # Verwaltung und Anzeige der Daten
    labelWuerfelC.config(text=str(wuerfelC))
    # Anzeige der Daten
    if wuerfelC == 1:
        labelWuerfelC.config(image=imageWuerfel1)
    elif wuerfelC == 2:
        labelWuerfelC.config(image=imageWuerfel2)
    elif wuerfelC == 3:
        labelWuerfelC.config(image=imageWuerfel3)
    elif wuerfelC == 4:
        labelWuerfelC.config(image=imageWuerfel4)
    elif wuerfelC == 5:
        labelWuerfelC.config(image=imageWuerfel5)
    elif wuerfelC == 6:
        labelWuerfelC.config(image=imageWuerfel6)



# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title("Test")
tkFenster.geometry("330x110")
# Rahmen Würfel
frameWuerfel = Frame(master=tkFenster,
                     background="#FBD975")
frameWuerfel.place(x=5, y=5, width=330, height=100)
# Label mit Überschrift für die Würfel
labelUeberschriftWuerfel = Label(master=frameWuerfel,
                                 text="Würfel",
                                 background="white")
labelUeberschriftWuerfel.place(x=5, y=5, width=100, height=20)
# Bilder
imageWuerfel1 = PhotoImage(file="w1.gif")
imageWuerfel2 = PhotoImage(file="w2.gif")
imageWuerfel3 = PhotoImage(file="w3.gif")
imageWuerfel4 = PhotoImage(file="w4.gif")
imageWuerfel5 = PhotoImage(file="w5.gif")
imageWuerfel6 = PhotoImage(file="w6.gif")
# Label Würfel B
labelWuerfelA = Label(master=frameWuerfel,
                      image=imageWuerfel1)
labelWuerfelA.place(x=40, y=35, width=30, height=30)

labelWuerfelB = Label(master=frameWuerfel,
                      image=imageWuerfel1)
labelWuerfelB.place(x=140, y=35, width=30, height=30)

labelWuerfelC = Label(master=frameWuerfel,
                      image=imageWuerfel1)
labelWuerfelC.place(x=90, y=35, width=30, height=30)
# Button zum Würfeln
buttonWuerfel = Button(master=frameWuerfel,
                       text="Wuerfel werfen",
                       command=Button_Wuerfel_Click)
buttonWuerfel.place(x=5, y=75, width=100, height=20)
# Aktivierung des Fensters
tkFenster.mainloop()