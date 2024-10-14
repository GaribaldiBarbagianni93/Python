# List Comprehension
# [espression for elemento in iterabile if condizione]


numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrati = [x**2 for x in numeri]
#print(quadrati)

#--------------------------------------------------#


numeri_pari = [x for x in range(10) if x % 2 == 0]
#print(numeri_pari)


def cubo(x):
    return x**3

cubi = [cubo(x) for x in range(5)]
#print(cubi)

#----------------------------------------------------------#

parole = ["ciao", "a", "Phyton", "mango"]
parole_lunghe = [parola for parola in parole if len(parola)]
#print(parole_lunghe)





#----------------------------------------------------------#


frutti = ["mela", "banana", "ciliegina"]
maiuscole = [frutto.upper() for frutto in frutti]
#print(maiuscole)



#----------------------------------------------------------#


valori = ["a", "b", "c"]
tuples = [(i, valore) for i, valore in enumerate(valori)]
#print(tuples)


#----------------------------------------------------------#

matrice = [[i * j for j in range(3)] for i in range(4)]
# print(matrice)


#----------------------------------------------------------#


numeri = [1, 2, 3, 4, 5]
numeri_sommati = sum([x for x in numeri if x % 2 == 0])
#print(numeri_sommati)




#---------------------ES 5----------------------------------#

# Hai a disposizione un dataset che rappresenta l’inventario di un negozio sotto
# forma di una lista di dizionari. Ogni dizionario rappresenta un prodotto e contiene le seguenti informazioni:
# "nome": il nome del prodotto (stringa)
# "categoria": la categoria a cui appartiene (es. "elettronica", "abbigliamento", "cucina") (stringa)
# "prezzo": il prezzo del prodotto (numero float)
# "quantita": la quantità disponibile in magazzino (intero)


prodotti = [
    {
        "nome": "televisore",
        "categoria": "elettronica",
        "prezzo": 499.99,
        "quantita": 10,
    },
    {
        "nome": "frullatore",
        "categoria": "cucina",
        "prezzo": 79.99,
        "quantita": 20,
    },
    {
        "nome": "maglietta",
        "categoria": "abbigliamento",
        "prezzo": 15.99,
        "quantita": 100,
    },
    {
        "nome": "laptop",
        "categoria": "elettronica",
        "prezzo": 899.99,
        "quantita": 5,
    },
    {
        "nome": "pentola",
        "categoria": "cucina",
        "prezzo": 29.99,
        "quantita": 50,
    },
]

# Prodotti in Offerta:
# Crea una lista di nomi di prodotti il cui prezzo è inferiore a 100 euro.
prodotti_economici = [prodotto["nome"] for prodotto in prodotti if prodotto["prezzo"] < 100]
print(prodotti_economici)

# Valore Totale dell'Inventario:
# Calcola il valore totale sommato dei prodotti
valore_inventario_tot = sum(prodotto["prezzo"] for prodotto in prodotti)
print(valore_inventario_tot)

# Valore Totale per ogni prodotto:
# Crea una lista di tuple con nome e costo totale
valore_prodotto = [(prodotto["nome"], prodotto["prezzo"]*prodotto["quantita"]) for prodotto["nome"], prodotto["prezzo"] in prodotti]
print(valore_prodotto)

# Crea un set con l'elenco di categorie
categorie_uniche = {prodotto["categoria"] for prodotto in prodotti}
print(categorie_uniche)

# Prodotti da Riordinare: Un prodotto deve essere riordinato se la sua
# quantità è inferiore a 10.
prodotti_riordinare = [prodotto["nome"] for prodotto in prodotti if prodotto["quantita"] < 10]
print(prodotti_riordinare)

# Crea un dizionario con categorie e liste di tuple (nome prodotto, valore totale)
# Serve usare il set creato in precedenza
# cat_valore_prodotto = //
# print(cat_valore_prodotto)

# DIFFICILE
# Valore Totale dell'Inventario per categoria:
# Crea un dizionario in cui le chiavi sono le categorie e i valori sono
# il totale del valore dei prodotti # appartenenti a quella categoria.