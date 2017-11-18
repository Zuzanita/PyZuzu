from Mazlicci import vyber_maz, k_maz
import pytest

def test_k_maz_kralik_ano():
    zvire = "kralík"
    "králík" in k_mazel #když tam nemám závorky, tak ho to nezná, když mám, tak syntax error....

def test_vyber_maz_kralik_ne():
    zvire = "kralík"
    "kralík" not in vyber_maz

def test_vyber_maz_pes_ano():
    zvire = "pes"
    "pes" in vyber_mazliku
