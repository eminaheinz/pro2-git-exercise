def durchschnitt_berechnen(faecher):
    if len(faecher) == 0:
        return 0

    summe = 0

    for note in faecher.values():
        summe += note

    return summe / len(faecher)


def beste_faecher(faecher):
    sortiert = sorted(
        faecher.items(),
        key=lambda fach: fach[1],
        reverse=True
    )

    return sortiert[:3]


def schlechteste_faecher(faecher):
    sortiert = sorted(
        faecher.items(),
        key=lambda fach: fach[1]
    )

    return sortiert[:3]


def fach_suchen(faecher, suchbegriff):
    gefunden = {}

    for fach, note in faecher.items():
        if suchbegriff.lower() in fach.lower():
            gefunden[fach] = note

    return gefunden