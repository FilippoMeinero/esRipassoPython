#funzione per calcolare il fattoriale
def fattoriale(n):
    if n == 0:
        return 1
    else:
        return n * fattoriale(n-1)

#int() converte la stringa inserita dall'utente in un intero --> la funzione input() legge il valore come stringa
numero = int(input("Inserisci un numero: "))

risultato = fattoriale(numero)

print(f"Il fattoriale di {numero} è {risultato}")
