x = 10 #x è un intero
x = "ciao" #x è una stringa




def incrementa(valore):
    if isinstance(valore, int) or isinstance(valore, float):
        return valore + 1
    if isinstance(valore, str):
        return valore + "aggiunto"
    else: 
        return "Tipo non supportato"
    
lista = []
lista.append("ciao")
lista.append(15)


dati = [1, 2, "ciao", 3.5, [1 ,2], None, 18, "mondo", 3.14]
#crea un metodo che analizzi la lista e le divida in 2 base al tipo di dato:
#stringlist e numberlist. 

numberlist = []
stringlist = []

def dividiStringa(dati):
    for i in range(len(dati)):
        if isinstance(dati[i], int):
            numberlist.append(dati[i])
        elif isinstance(dati[i], float):
            numberlist.append(dati[i])
        elif isinstance(dati[i], str):
            stringlist.append(dati[i])
    return numberlist, stringlist

#print(dividiStringa(dati)) 

numbers = [4, 8, 56, 36, 478]

def sommaLista(numbers):
    somma = sum(numbers)
    print(somma)


def mediaLista(numbers): 
    media = sum(numbers) / len(numbers)
    print(media)


#es compito funzione che accetti la lista e faccia la somma e la media dei numeri

sommaLista(numbers)
mediaLista(numbers)


    
