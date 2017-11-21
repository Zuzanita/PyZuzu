#Ukol
# - Zeptej se uzivatele na jmeno ktere chce pridat do seznamu
# - Pote se zeptej na telefonni cislo
# - Pridej ziskane polozky do telefoniho seznamu nize
# Bonus: Zkontroluj ze zadane cislo je cele cislo, jinak se ptej znovu
# Bonus: Zkntroluj zda dane jmenu v seznamu uz neni. Pokud tam je, ptej se znovu

zlateStranky = {
    'Alice': '603888921',
    'Bohous':'777891776',
    'Cyril':'602345666',
    'Daniela':'728910000',
    'Eva':'777633798',
    'Filip':'608915433',
}

def pridani_do_slovniku(slovnik):
    """Přidá zvolené jméno a číslo do slovníku. Zkontroluje, zda již daná osoba či číslo ve slovníku není."""
    jmeno = input("Zadej jméno osoby, kterou chceš přidat do Zlatých stránek: ")
    try:
        for klic in slovnik.keys():
            klic != jmeno
    except KeyError:
        print("Takový jedinec už tu je. Zkus zadat někoho nového")
    tel_cislo = input("Zadej telefonní číslo, které patří dané osobě: ")
    try:
        cislo = int(tel_cislo)
    except ValueError:
        print("To nebylo číslo! Zkus to ještě jednou!")
        tel_cislo = input("Zadej telefonní číslo, které patří dané osobě: ")
    slovnik[jmeno] = tel_cislo
    return slovnik
pridani_do_slovniku(zlateStranky)
