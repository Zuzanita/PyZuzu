#0. tvorba seznamu
Mazlicci = [ 'pes', 'kočka', 'králík','had']

#1. fce, která vybere mazlíky kratší než 5 písmen
Vyber_mazliku = []
def vyber_maz(seznam):
    for zvire in Mazlicci:
        if len(zvire) < 5:
            Vyber_mazliku.append(zvire)
    print(Vyber_mazliku)

vyber_maz(Mazlicci)



#2. fce, která vypíše mazlíky, kteří začínají na k
K_mazel = []
def k_maz(seznam):
    for zvire in Mazlicci:
        if zvire[0] == 'k':
            K_mazel.append(zvire)
    print(K_mazel)
k_maz(Mazlicci)



#3.fce, která potvrdí, že napsané slovo je na seznamu
#def overeni():
#    over_zvire = input("Zadej zvíře, u kterého chceš vědět, zda je na seznamu: ")
#    print(over_zvire in Mazlicci)
#overeni()
