#Ukol
# - nacti JSON retezec nize jako Python Slovnik
# - zmen polozku 'Skladem' na False
# - pridej polozku 'Dopravne' s hodnotou 199
# - preved vysledny slovnik na JSON retezec a vypis ho do konzole

import json
jsonRetezecZEshopu = """
{
    "JménoProduktu": "Kosmodisk",
    "Cena": 2999,
    "Skladem": true,
}
"""
nactenyJsonZEshopu = json.loads(jsonRetezecZEshopu)

print(nactenyJsonZEshopu)
