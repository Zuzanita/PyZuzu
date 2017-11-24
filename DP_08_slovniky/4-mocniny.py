#Napiš funkci, která pro zadané číslo n vytvoří a vrátí slovník, kde jako klíče budou čísla od jedné do n a
#jako hodnoty k nim jejich druhé mocniny.
def mocnina():
    """Vypíše slovník čísel do n a jejich druhé mocniny"""
    cislo_n = int(input("Zadej číslo: "))
    slovnik_mocnin = {}
    for i in range(1,cislo_n+1):
        slovnik_mocnin[i] = i**2
    return(slovnik_mocnin)

mocnina()

def sectu_klice_hodnoty(slovnik):
    """funkce sečte sumu všech klíčů a všech hodnot ve slovníku"""
    soucet_klicu = 0
    soucet_hodnot = 0
    for klic in slovnik:
        soucet_klicu = soucet_klicu + slovnik[klic]
    print(soucet_klicu)

sectu_klice_hodnoty(slovnik_mocnin)
