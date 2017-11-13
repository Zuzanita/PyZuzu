#tah_hrace - všude je input nebo print, jediné, co mohu je else
# test - když zadáné číslo bude mezi 0-19 a políčko není obsazené
#
#import Piskvorky
#def test_tah_hrace_zapis_tahu():
#    herni_pole = 20*"-"
#    cislo_policka = 2
#    expected_herni_pole = 2*"-"+"x"+17*"x"

#    actual_tah = Piskvorky.tah_hrace(
#        herni_pole
#        )

#    assert actual_tah == expected_herni_pole

def test_vyhodnot_vyhra_clovek():
    pole = "xoxooxx---o-ox------"
    na_tahu = "x"
    cislo_policka = 7
    assert vyhodnot(pole) == "x"
