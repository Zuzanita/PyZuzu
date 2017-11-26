#Napiš funkci, která pro zadané číslo n vytvoří a vrátí slovník, kde jako klíče budou čísla od jedné do n a
#jako hodnoty k nim jejich druhé mocniny.


def mocnina(cislo_n):
    from random import randint
    slovnik_mocnin = {}
    for i in range(1,cislo_n+1):
        slovnik_mocnin[i] = i**2
    print(slovnik_mocnin)

mocnina(5)
