#0 seznam zvířat
Dom_zvirata = ['pes','kočka','kralík','had']
#4 jména zvířat
Moji_mazlicci = ['Chula', 'Gordo', 'Bondy', 'Alan', 'Sancho']
Vasi_mazlicci = ['Chula', 'Gordo', 'Brok', 'Alfonso', 'Silák']
Spolecni_mazlicci = []
Jen_moji = []
Jen_vasi = []
for jmena_1 in Moji_mazlicci:
    for jmena_2 in Vasi_mazlicci:
        if jmena_1 == jmena_2:
            Spolecni_mazlicci.append(jmena_1)
        elif jmena_1 not in Vasi_mazlicci:
            Jen_moji.append(jmena_1)
        elif jmena_2 not in Moji_mazlicci:
            Jen_vasi.append(jmena_2)

print("Společní mazličci jsou", Spolecni_mazlicci)
print("Tohle jsou jen vaši mazlové: ", Jen_vasi)
print("Tohle jsou jen moji mazlové: ", Jen_moji)

#5. funkce, která seřadí mazlíky dle abecedy
def seradi_abeceda(seznam):
    """Seřadí daný seznam dle abecedy"""
    print(sorted(seznam))

seradi_abeceda (Dom_zvirata)

#6.priletela andulka
Dom_zvirata.append("andulka")
print(Dom_zvirata)
Seznam_dvojic = []
Dom_zvirata_nove = []
for zvire in Dom_zvirata:
    Seznam_dvojic.append([zvire[1:], zvire])
print(sorted(Seznam_dvojic))
for podseznamy in sorted(Seznam_dvojic):
    Dom_zvirata_nove.append(podseznamy[1])
print(Dom_zvirata_nove)
