dizionario = {"a": 1, "b": 2, "c": 3}

#dictionary comprehension --> dizionario.items(): restituisce una vista degli elementi del dizionario come coppie (chiave, valore)
#                         --> for chiave, valore in dizionario.items(): ciclo for che itera su ciascuna coppia (chiave, valore) del dizionario
#                         --> {valore: chiave for chiave, valore in dizionario.items()}: per ogni coppia (chiave, valore) nel dizionario originale, crea una nuova coppia (valore, chiave) nel nuovo dizionario 
dizionarioInvertito = {valore: chiave for chiave, valore in dizionario.items()}

print("Dizionario originale:", dizionario)
print("Dizionario invertito:", dizionarioInvertito)
