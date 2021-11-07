# lista declarata
# lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6,]
lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6,]

lista.sort()
print(lista)

new_list = lista.copy()

lista.reverse()
print(lista)

lista_para = new_list[1::2]
print(lista_para)

lista_impara = new_list[::2]
print(lista_impara)

for divizor in new_list:
    if divizor % 3 == 0:
        print(divizor)
