#Napiš funkci, která jako argument dostane řetězec a vrátí slovník, ve kterém budou jako klíče jednotlivé
#znaky ze zadaného řetězce a jako hodnoty počty výskytů těchto znaků v řetězci

def retezec_v_slovnik():
    """fce převede vepsaný řetězec do slovníku, kde klíče jsou znaky a hodnoty jejich výskyty"""
    retezec = input("Vypiš řetězec, ze kterého chceš mít slovník: ")
    slovnik_retezce = {}
    delka_retezce = len(retezec)
    seznam_retezce = list(retezec)
    for znak in seznam_retezce:
        slovnik_retezce[znak] = retezec.count(znak)
    print(slovnik_retezce)

retezec_v_slovnik()
