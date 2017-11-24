#Úkolem je vytvořit známou skautskou hru „Kdo? S kým? Co dělali?“. Hra se hráče zeptá postupně na
#různé otázky, například „Kdo?“, „S kým?“, „Co dělali?“, „Kde?“, „Kdy?“, a nakonec „Proč?“, s tím, že
#mu umožní na jednu otázku odpovědět vícekrát a všechny odpovědi si uloží. Na závěr pak hra z každé
#sady odpovědí vybere náhodně jednu odpověď a z takto vybraných odpovědí složí větu, kterou vypíše
#uživateli. Seznam otázek by mělo být možné změnit na jednom místě bez zásahu do logiky programu.
def skautska_hra():
    import random
    seznam_otazek = ["Kdo? ", "S kým? ", "Co dělali? ", "Kde? ", "Kdy? ", "Proč? "]
    seznam_odpovedi = []
    delka_seznam_otazek = len(seznam_otazek)
    print(delka_seznam_otazek)
    zaver = {}
    for sada in range(0,delka_seznam_otazek):
        for dotaz in seznam_otazek:
            odpoved = input(dotaz)
            seznam_odpovedi.append(odpoved)
            vybrana_odpoved = random.choice(seznam_odpovedi)
            zaver[dotaz] = vybrana_odpoved

    print(zaver)

skautska_hra()
