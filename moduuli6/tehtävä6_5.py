def karsi_parittomat(lista):
    for i in lista:
        if i % 2 == 0:
            pariton_lista.append(i)
    return lista

lista_alkuperainen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pariton_lista = []
karsi_parittomat(lista_alkuperainen)
print(f"Alkuperäinen lista: {lista_alkuperainen}")
print(f"Lista ilman parittomia lukuja: {pariton_lista}")