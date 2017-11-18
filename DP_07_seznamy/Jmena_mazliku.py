#0 seznam zvířat
dom_zvirata = ['pes','kočka','kralík','had']
#4 jména zvířat
moji_mazlicci = ['Chula', 'Gordo', 'Bondy', 'Alan', 'Sancho']
vasi_mazlicci = ['Chula', 'Gordo', 'Brok', 'Alfonso', 'Silák']
spolecni_mazlicci = []
jen_moji = []
jen_vasi = []
for jmena_1 in moji_mazlicci:
    for jmena_2 in vasi_mazlicci:
        if jmena_1 == jmena_2:
            spolecni_mazlicci.append(jmena_1)
        elif jmena_1 not in vasi_mazlicci:
            jen_moji.append(jmena_1)
        elif jmena_2 not in moji_mazlicci:
            jen_vasi.append(jmena_2)

print("Společní mazličci jsou", spolecni_mazlicci)
print("Tohle jsou jen vaši mazlové: ", jen_vasi)
print("Tohle jsou jen moji mazlové: ", jen_moji)

#5. funkce, která seřadí mazlíky dle abecedy
def seradi_abeceda(seznam):
    """Seřadí daný seznam dle abecedy"""
    print(sorted(seznam))

seradi_abeceda (dom_zvirata)

#6.priletela andulka
dom_zvirata.append("andulka")
print(dom_zvirata)
seznam_dvojic = []
dom_zvirata_nove = []
for zvire in dom_zvirata:
    seznam_dvojic.append([zvire[1:], zvire])
print(sorted(seznam_dvojic))
for podseznamy in sorted(seznam_dvojic):
    dom_zvirata_nove.append(podseznamy[1])
print(dom_zvirata_nove)
