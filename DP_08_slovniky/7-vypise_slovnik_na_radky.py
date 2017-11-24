#Napiš funkci, která vypíše obsah slovníku (klíče a k nim náležící hodnoty) na jednotlivé řádky
zkouska = {'Zuzu':'čokoládová', 'Martínek':'pistáciová','Raúl':'citrónová'}

def obsah_slovniku(slovnik):
    """Vypíše obsah slovníku do řádek"""
    for keys, values in slovnik.items():
        print(keys,values)

obsah_slovniku(zkouska)
