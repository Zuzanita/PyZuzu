#0. tvorba seznamu
mazlicci = [ 'pes', 'kočka', 'králík','had']

#1. fce, která vybere mazlíky kratší než 5 písmen

def vyber_maz(seznam):
    vyber_mazliku = []
    for zvire in seznam:
        if len(zvire) < 5:
            vyber_mazliku.append(zvire)
    return(vyber_mazliku)

vyber_maz(mazlicci)



#2. fce, která vypíše mazlíky, kteří začínají na k

def k_maz(seznam):
    k_mazel = []
    for zvire in seznam:
        if zvire[0] == 'k':
            k_mazel.append(zvire)
    return(k_mazel)
k_maz(mazlicci)



#3.fce, která potvrdí, že napsané slovo je na seznamu
#def overeni():
#    over_zvire = input("Zadej zvíře, u kterého chceš vědět, zda je na seznamu: ")
#    print(over_zvire in Mazlicci)
#overeni()
