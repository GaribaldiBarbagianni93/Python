
libreria_iniziale = [
    {"Titolo": "LOTR", "Autore": "J.R.R. TOLKIEN", "Valutazioni": [7, 8, 9]},
    {"Titolo": "Se questo è una dpnna", "Autore": "Secondo Metti", "Valutazioni": [1, 2, 3]},
]


def aggiungi_libro(libreria, titolo, autore):
    libro = {"Titolo": titolo, "Autore": autore, "Valutazioni": []}
    libreria.append(libro)
    return libreria


def aggiungi_valutazione(libreria, titolo, valutazione):
    for libro in libreria:
        if libro["Titolo"] == titolo:
            libro["Valutazioni"].append(valutazione)
    return libreria


print(f"Valutazioni nuove: {aggiungi_valutazione(libreria_iniziale, 'LOTR', 7)}")


def calcola_media(libreria, titolo):
    for libro in libreria:
        if libro["Titolo"] == titolo:
            valutazioni = libro["Valutazioni"]
            if valutazioni:
                media = sum(valutazioni) / len(valutazioni)
                return (media)
            else:
                return "Nessuna valutazione"
    return "Libro non esistente"

print(f"Media delle valutazioni del libro 'Se questo è una donna': {calcola_media(libreria_iniziale, 'Se questo è una donna')}")

def mostra_libreria(libreria):
    for libro in libreria:
        media = calcola_media(libreria, libro["Titolo"])
        print(f"Titolo: {libro['Titolo']}, Autore: {libro['Autore']}, Media Valutazioni: {media}")


mostra_libreria(libreria_iniziale)