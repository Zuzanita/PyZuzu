#Ukol
# - Zeptej se uzivatele na jmeno, ktere chce vyhledat. Vrat mu prislusne telefonni cislo
#Bonus: Pokud zadane jmeno v seznamu neni, informuj uzivatele a ptej se znovu
zlateStranky = {
    'Alice': '603888921',
    'Bohous':'777891776',
    'Cyril':'602345666',
    'Daniela':'728910000',
    'Eva':'777633798',
    'Filip':'608915433',
}

def nacti_mobil(slovnik):
    jmeno = input("Zadej jméno osoby, u které potřebuješ vědět telefonní číslo: ")
    try:
        jmeno in slovnik
    except KeyError:
        print("Asi sis spletl číslo. Nikoho takového neznám.")
        jmeno = input("Zadej jméno osoby, u které potřebuješ vědět telefonní číslo: ")
    print(slovnik[cislo])

nacti_mobil(zlateStranky)
