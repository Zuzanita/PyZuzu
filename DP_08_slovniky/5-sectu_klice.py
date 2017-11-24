#Napiš , která sečte a vypíše sumu všech klíčů a sumu všech hodnot ve slovníku, který dostane jako
#argument. K vyzkoušení můžeš použít slovník z minulé úlohy

zkouska = {1:1,2:4,3:9}

def sectu_klice_hodnoty(slovnik):
    """funkce sečte sumu všech klíčů a všech hodnot ve slovníku"""
    soucet_klicu = 0
    soucet_hodnot = 0
    for klic in slovnik.keys():
        soucet_klicu = soucet_klicu + klic
    print(soucet_klicu)
    for hodnota in slovnik:
        soucet_hodnot = soucet_hodnot + slovnik[hodnota]
    print(soucet_hodnot)

sectu_klice_hodnoty(zkouska)
