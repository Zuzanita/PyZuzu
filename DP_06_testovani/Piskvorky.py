import ai

def vyhodnotit(pole):
    """Vyhodnotí stav hry"""
    if "xxx" in pole:
        return("x")
    elif "ooo" in pole:
        return("o")
    elif "-" not in pole:
        return("!")
    else:
        return("-")



def tah_hrace(pole):
    """Zeptá se na tah a doplní do herního pole"""

    while True:
        cislo_policka = input("Zadej číslo pole, na které chceš hrát, tj. 0 až 19: ")
        cislo_policka = int(cislo_policka)
        if cislo_policka > 19 or cislo_policka < 0:
            print("Hahaha, asi máš nějaké větší herní pole než já. Zkus to znovu! Věřím, že teď to dáš!")
        elif 0 <= cislo_policka <= 19 and pole[cislo_policka] != "-":
            print("Tam už někdo hrál, zkus to znovu")
        else:
            return ai.tah(pole, cislo_policka, "x")

def piskvorky1d():
    "Počítač a hráč hrají piškovrky"
    pole = "-"*20
    na_tahu = "x"

    while True:
        if na_tahu == "x":
            pole = tah_hrace(pole)
            na_tahu = "o"
        else:
            pole = ai.tah_pocitace(pole)
            na_tahu = "x"
        vysledek = vyhodnotit(pole)
        print(pole)

        if vysledek != "-":
            if vysledek == "x":
                print("Gratuluji, porazil si mě.")
            elif vyhodnotit(pole) == "o":
                print("Jsem lepší, ale můžeme to zkusit ještě jednou!")
            else:
                print("Zkusíme to ještě jednou? Alias remíza je nuda")
            break
