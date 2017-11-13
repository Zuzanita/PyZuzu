import random

def tah(herni_pole, cislo_policka, symbol):
    return herni_pole[:cislo_policka] + symbol + herni_pole[cislo_policka + 1:]

def tah_pocitace(herni_pole):

    while True:
        cislo_policka = random.randrange(len(herni_pole))
        if herni_pole[cislo_policka] == "-":
            return tah(herni_pole, cislo_policka, "o")
