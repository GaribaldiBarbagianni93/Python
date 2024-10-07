
libreria_iniziale = [
    {"Titolo": "bella ciao", "Autore": "Garibaldi", "Valutazioni": [7, 8, 9]},
    {"Titolo": "L_insostenibile leggerezza dell_essere", "Autore": "Paolo Franchi", "Valutazioni": [1, 2, 3]},
]


def aggiungi_libro(libreria, titolo, autore):
    libro = {"Titolo": titolo, "Autore": autore, "Valutazioni": []}
    libreria.append(libro)



def aggiungi_valutazione(libreria, titolo, valutazione):
    for libro in libreria:
        if libro["Titolo"] == titolo:
            libro["Valutazioni"].append(valutazione)
    return libreria

def calcola_media(libreria, titolo):
    for libro in libreria:
        if libro["Titolo"] == titolo:
            valutazioni = libro["Valutazioni"]
            if valutazioni:
                media = sum(valutazioni) / len(valutazioni)
                return (media)
            else:
                return "No valutazioni"
    return "Libro non esistente"


def mostra_libreria(libreria):
    for libro in libreria:
        media = calcola_media(libreria, libro["Titolo"])
        print(f"Titolo: {libro['Titolo']}, Autore: {libro['Autore']}, Media Valutazioni: {media}")


print(f"New Valutations: {aggiungi_valutazione(libreria_iniziale, 'bella ciao', 7)}")
print(f"Media delle valutazioni del libro 'L_insostenibile leggerezza dell_essere': {calcola_media(libreria_iniziale, 'L_insostenibile leggerezza dell_essere')}")
mostra_libreria(libreria_iniziale)