lista = [ [[1, 2, 3, 7], [4, 5, 6]], [[7, 8, 9], [10, 11, 12, 21], [3, 4, 11]], [[13, 14, 15], [16, 17, 18]] ]

#provoni
#
#  print(f"Lunghezza lista: {len(lista)}")
#   print(f"Lunghezza lista[0]: {len(lista[0])}")
#   print(f"Lunghezza lista[0][0]: {len(lista[0][0])}")
#   print(f"Lunghezza lista[0][1]: {len(lista[0][1])}")


#   print(f"Lunghezza lista: {range(len(lista))}")
#   print(f"Lunghezza lista[0]: {range(len(lista[0]))}")
#   print(f"Lunghezza lista[0][0]: {range(len(lista[0][0]))}")
#   print(f"Lunghezza lista[0][1]: {range(len(lista[0][1]))}")

for i in range(len(lista)):
    print(i) #(0, 5)

for a in range(len(lista)):
    for b in range(len(lista[a])):
        for c in range(len(lista[a][b])):
            lista[a][b][c] += 1

print(lista)


    






