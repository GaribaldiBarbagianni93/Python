from collections import Counter

#----------------LISTE-------------------









#----------------DUPLE-------------------
#raccolta ordinata, immutabile, permette duplicati
colori = ("rosso", "verde", "blu")
primo_colore = colori
#non modificabile

#-----------------SET-------------
#raccolta non ordinata di elementi unici. Non permette duplicati
numeri = {1, 2, 3, 4, 5}
set_iniziale_ = numeri
numeri.add(6)
set_aggiornato = numeri


#-----------------DICT----------------
#raccolta non ordinata (ma per noi si) di coppie chiave-valore. 
dizionario = {"nome" : "Mario","eta" : 38}
valore_nome = dizionario["nome"]
dizionario["citta"] = "Roma"
del dizionario["citta"]
eta = dizionario.pop(
    "eta" 
) # Rimuovve e restituisce il valore associato a "eta"
dizionario.get(
    "nome" , "non trovato"
) # è come il dizionario["nome"], ma gestisce il non trovato
dizionario_aggiornato = dizionario

for chiave in dizionario:
    print(chiave, dizionario[chiave]) # stampa ogni chiave ed il suo valore

for chiave, valore in dizionario.items():
    print(chiave, valore) #oppure per ottenere le coppie chiave-valore

#len(dizionario): Restituisce il numero di elementi
#dizionario.keys(): restituisce un oggetto vista delle chiavi
#dizionario.values(): restituisce un oggetto vista dei valori
#dizionario.items(): restituisce un oggetto delle coppie

#-------------------STRING-----------------------
frase = "ciao, come va?"
lunghezza_stringa = len(frase)


#--------------------COUNTER-------------------------
#una sequenza di caratteri, immutabili
lettere_counter = Counter("hello world") #contare la frequenza delle lettere
frutti = ["mela", "banana", "mela", "pera", "banana", "banana"]
string_modificata = Counter(frutti)

#crea un programma che gestisca un registro di studenti. Ogni studenti ha un nome e punteggio. Implementa:

#Aggiungere un nuovo studente (✔)
#restituisce il punteggio dello studente (✔)
#calcolare la media dei punteggi (✔)
#resituisce un dizionario con il nome degli studenti con un punteggio superiore alla media

#Specifiche
#utilizza un dizionario per memorizzare i nomi come chiavi e i punteggi come valori
#Implementare una funzione per ciascuna delle funzionalita 


#------------------------ESERCIZIO------------------------#


registro = {"Rogal Dorn" : 5, "Konrad Curze" : 3, "Lion El'Johnson" : 8, "Vulkan" : 10}


def addStudente(nome, valore): 
    registro[nome] = valore
    print(registro)

def visualizzaPunteggio(nome):
    valore_studente = registro[nome]
    print(valore_studente) 
    
def calcolaMediePunteggi():
    media = 0
    for valore in registro.values():
        media = media + valore
    media = media / len(registro)
    return media

def studentiEccellenti():
    registroStudentiEccellenti = { }
    for nome in registro:
        if (registro[nome] > calcolaMediePunteggi()):
            registroStudentiEccellenti[nome] = registro[nome]
    return registroStudentiEccellenti



addStudente("jaghatai kahn", 5)
visualizzaPunteggio("Rogal Dorn")
print(calcolaMediePunteggi())
print(studentiEccellenti())



