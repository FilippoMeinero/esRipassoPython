lista1 = [1, 2, 3, 4, 5]

#list comprehension --> for x in lista1 è il ciclo che itera su ogni elemento di lista1
#                   --> x * 2 vuol dire che ogni elemento di lista1 viene moltiplicato per 2
lista2 = [x * 2 for x in lista1]

print("Lista originale:", lista1)
print("Lista con valori raddoppiati:", lista2)
