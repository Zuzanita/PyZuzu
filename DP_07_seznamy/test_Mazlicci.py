from Mazlicci import vyber_maz, k_maz
import pytest

def test_vyber_maz_kralik_ne():
    mazlicci = [ 'pes', 'kočka', 'králík','had']
    zvire = vyber_maz(mazlicci)
    assert "kralík" not in vyber_maz(mazlicci)

def test_vyber_maz_kralik_ano():
    mazlicci = [ 'pes', 'kočka', 'králík','had']
    zvire = k_maz(mazlicci)
    assert "králík" in k_maz(mazlicci)

def test_vyber_maz_pes_ne():
    mazlicci = [ 'pes', 'kočka', 'králík','had']
    zvire = k_maz(mazlicci)
    assert "pes" not in k_maz(mazlicci)

def test_vyber_maz_pes_ano():
    mazlicci = [ 'pes', 'kočka', 'králík','had']
    zvire = vyber_maz(mazlicci)
    assert "pes" in vyber_maz(mazlicci)
