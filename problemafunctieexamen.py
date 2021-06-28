lista_nume = ["Maria", "Irina", "Claudiu", "Ionut", "Irina", "Matei", "Irina", "Maria", "Claudiu"]
maxim = 0
minim = 2
sortare_listac= sorted(lista_nume)
print(f"lista sortata acesndent in functie de nume este:\n{sortare_listac}")

for x in set(lista_nume):
    if lista_nume.count(x) > maxim:
        maxim = lista_nume.count(x)
    print([x,lista_nume.count(x)])
    if lista_nume.count(x) < minim:
        minim = lista_nume.count(x)
    print([x,lista_nume.count(x)])

for x in set(lista_nume):
    if lista_nume.count(x) < minim:
        minim = lista_nume.count(x)

for x in set(lista_nume):
    if minim == lista_nume.count(x):
        print(f"Nr. minim de aparitii: ", [x,lista_nume.count(x)])

for x in set(lista_nume):
    if maxim == lista_nume.count(x):
        print(f"Nr. max de aparitii: ", [x,lista_nume.count(x)])
