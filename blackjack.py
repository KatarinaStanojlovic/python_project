import random

class Karta:
    def __init__(self, znak, vrednost):
        self.znak = znak
        self.vrednost = vrednost

        if vrednost in ['J', 'Q', 'K']:
            self.poeni = 10
        elif vrednost == 'A':
            self.poeni = 11
        else:
            self.poeni = int(vrednost)

    def __str__(self):
        rez_znak = ''
        match self.znak:
            case 'DIAMONDS':
                rez_znak = '♦'
            case 'CLUBS':
                rez_znak = '♣'
            case 'HEARTS':
                rez_znak = '♥'
            case 'SPADES':
                rez_znak = '♠'

        return f'{self.vrednost}{rez_znak}'  # formatiranje u string

class Spil:
    def __init__(self):
        self.karte = []
        for vrednost in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            for znak in ['DIAMONDS', 'CLUBS', 'HEARTS', 'SPADES']:

                self.karte.append(Karta(znak, vrednost))

        random.shuffle(self.karte)

    def deli(self):
        return  self.karte.pop()

class BlackjackGame:
    def __init__(self):
        self.spil = Spil()  # konstruktor
        self.igrac = []
        self.diler = []
        self.igracStandovao = False

    def zapocni_igru(self):
        self.spil = Spil()
        self.igrac = [self.spil.deli(), self.spil.deli()]
        self.diler = [self.spil.deli()]
        self.igracStandovao = False

        # vraca stanje na nulu


    def get_karte_igrac(self):
        return [f'{karta.vrednost}{karta.znak}'for karta in self.igrac]

    def get_karte_diler(self):
        return [f'{karta.vrednost}{karta.znak}'for karta in self.diler]

    def igrac_hit(self):
        self.igrac.append(self.spil.deli())
          # izvlacenje nove karte

    def diler_hit(self):
        self.diler.append(self.spil.deli())

    def igrac_stand(self):
          self.igracStandovao = True
          # zaustavlja, ne uzima vise karata

    def get_zbir_igrac(self):
        return self.izracunaj_zbir(self.igrac)

    def get_zbir_diler(self):
        return self.izracunaj_zbir(self.diler)

    def izracunaj_zbir(self, ruka):
        suma = 0
        br_keceva = 0
        for karta in ruka:
            suma += karta.poeni
            if karta.poeni == 11:
                br_keceva += 1

        while suma > 21 and br_keceva > 0:
            suma -= 10
            br_keceva -= 1

        return suma

    def igrac_izgubio(self):
        if self.get_zbir_igrac() > 21:
            return True
        else:
            return False

    def diler_izgubio(self):
        return self.get_zbir_diler() > 21  # isto kao i za igrac_izgubio

    def racunaj_predikciju(self):
        if self.get_zbir_igrac() == 0:
            return ''
        if self.get_zbir_igrac() <= 11:
            return 'Predikcija: Hit'
        elif self.get_zbir_igrac() < 17:

            if int(self.diler[0].poeni) <= 6:
                return 'Predikcija: Stand'
            else:
                return 'Predikcija: Hit'
        else:
            return 'Predikcija: Stand'
