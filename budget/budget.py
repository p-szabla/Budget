class NowyWydatek(object):
    def __init__(self):
        pass

    def add(kwota,kategoria,komentarz):
        return f"dodano{kwota}"

class NowyPrzychod(object):
    def __init__(self, miesiac, osoba, kwota):

        self.Lista_M =["nic","Styczen"]

        self.miesiac = miesiac
        self.osoba = osoba
        self.kwota = kwota
    def add(self):
        return f"{self.Lista_M[self.miesiac]} {self.kwota}" 
