lista1 = [3,6,7,10,4,12,9,5]
alvo = 12

def função_linear(lista, alvo):
    for i in range (len(lista1)):
        if lista1[i] == alvo:
            return i
        return -1
    
função_linear(lista1,alvo)

indice = função_linear(lista1, alvo)

if indice != -1:
    print(f"o elemento {alvo} foi encontrado na posição {indice} da lista")