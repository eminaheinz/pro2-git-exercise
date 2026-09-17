from funktionen import *

faecher = {}

while True:
    print()
    print("1 ... Fächer mit zugehörigen Noten eingeben")
    print("2 ... Notendurchschnitt berechnen")
    print("3 ... Drei besten Fächer ausgeben")
    print("4 ... Drei schlechtesten Fächer ausgeben")
    print("5 ... Nach Fächern suchen")
    print("0 ... Exit")

    auswahl = input("Auswahl: ")

    if auswahl == "1":
        fach = input("Fach: ")
        note = float(input("Note: "))

        faecher[fach] = note

    elif auswahl == "2":
        durchschnitt = durchschnitt_berechnen(faecher)
        print("Notendurchschnitt:", durchschnitt)

    elif auswahl == "3":
        beste = beste_faecher(faecher)

        for fach, note in beste:
            print(fach, note)

    elif auswahl == "4":
        schlechteste = schlechteste_faecher(faecher)

        for fach, note in schlechteste:
            print(fach, note)

    elif auswahl == "5":
        suchbegriff = input("Nach welchem Fach suchen? ")

        gefunden = fach_suchen(faecher, suchbegriff)

        for fach, note in gefunden.items():
            print(fach, note)

    elif auswahl == "0":
        print("Programm beendet.")
        break

    else:
        print("Ungültige Eingabe.")