import random

class Arazi:
    def __init__(self, en=500, boy=500):
        self.en = en
        self.boy = boy

class Hayvan:
    def __init__(self, x, y, tur, birim, cinsiyet=None):
        self.x = x
        self.y = y
        self.tur = tur
        self.birim = birim
        self.cinsiyet = cinsiyet

    def hareket_et(self, arazi):
        self.x = max(0, min(arazi.en, self.x + random.randint(-1, 1)))
        self.y = max(0, min(arazi.boy, self.y + random.randint(-1, 1)))

    def mesafe_hesapla(self, diger_hayvan):
        return ((self.x - diger_hayvan.x) ** 2 + (self.y - diger_hayvan.y) ** 2) ** 0.5

class Koyun(Hayvan):
    def __init__(self, x, y, cinsiyet=None):
        super().__init__(x, y, tur="Koyun", birim=2, cinsiyet=cinsiyet)

class Kurt(Hayvan):
    def __init__(self, x, y, cinsiyet=None):
        super().__init__(x, y, tur="Kurt", birim=3, cinsiyet=cinsiyet)

    def avla(self, hayvanlar):
        for hayvan in hayvanlar:
            if hayvan.tur != "Kurt" and self.mesafe_hesapla(hayvan) <= 4:
                print(f"{self.tur} yakınındaki {hayvan.tur} avlandı!")
                hayvanlar.remove(hayvan)
                return

class Inek(Hayvan):
    def __init__(self, x, y, cinsiyet=None):
        super().__init__(x, y, tur="Inek", birim=2, cinsiyet=cinsiyet)

class Tavuk(Hayvan):
    def __init__(self, x, y, cinsiyet=None):
        super().__init__(x, y, tur="Tavuk", birim=1, cinsiyet=cinsiyet)

class Horoz(Hayvan):
    def __init__(self, x, y, cinsiyet=None):
        super().__init__(x, y, tur="Horoz", birim=1, cinsiyet=cinsiyet)

class Aslan(Hayvan):
    def __init__(self, x, y, cinsiyet=None):
        super().__init__(x, y, tur="Aslan", birim=4, cinsiyet=cinsiyet)

    def avla(self, hayvanlar):
        for hayvan in hayvanlar:
            if hayvan.tur != "Aslan" and self.mesafe_hesapla(hayvan) <= 5:
                print(f"{self.tur} yakınındaki {hayvan.tur} avlandı!")
                hayvanlar.remove(hayvan)
                return

class Avci(Hayvan):
    def __init__(self, x, y,cinsiyet=None):
        super().__init__(x, y, tur="Avci", birim=1, cinsiyet=cinsiyet)

    def avla(self, hayvanlar):
        for hayvan in hayvanlar:
            if hayvan.tur != "Avci" and self.mesafe_hesapla(hayvan) <= 8:
                print(f"{self.tur} yakınındaki {hayvan.tur} avlandı!")
                hayvanlar.remove(hayvan)
                return

class HayvanOlusturma:
    def __init__(self, arazi):
        self.arazi = arazi
        self.hayvanlar = []

    def hayvan_olustur(self, hayvan_sinifi, sayi, cinsiyet=None):
        for _ in range(sayi):
            x = random.randint(0, self.arazi.en)
            y = random.randint(0, self.arazi.boy)
            if cinsiyet is not None and hayvan_sinifi in [Tavuk, Horoz, Avci]:
                hayvan = hayvan_sinifi(x, y)
            else:
                hayvan = hayvan_sinifi(x, y, cinsiyet=random.choice(["Erkek", "Dişi"]) if cinsiyet is None else cinsiyet)
            self.hayvanlar.append(hayvan)

    def hareket_et(self):
        for hayvan in self.hayvanlar:
            hayvan.hareket_et(self.arazi)

    def avlan(self):
        for hayvan in self.hayvanlar:
            if isinstance(hayvan, (Kurt, Aslan, Avci)):
                hayvan.avla(self.hayvanlar)

    def ureme_kontrol(self):
        ciftlesen_hayvanlar = set()  # Çiftleşen hayvanları takip
        for hayvan1 in self.hayvanlar:
            for hayvan2 in self.hayvanlar:
                if hayvan1 != hayvan2 and hasattr(hayvan1, 'cinsiyet') and hasattr(hayvan2, 'cinsiyet'):
                    if hayvan1.cinsiyet != hayvan2.cinsiyet and type(hayvan1) == type(hayvan2):
                        if (hayvan1, hayvan2) in ciftlesen_hayvanlar or (hayvan2, hayvan1) in ciftlesen_hayvanlar:
                            continue # Çiftleşen hayvanlar zaten çiftleşmişse tekrar çiftleşmesin
                        mesafe = hayvan1.mesafe_hesapla(hayvan2)
                        if mesafe <= 3:
                            ciftlesen_hayvanlar.add((hayvan1, hayvan2)) 
                            self.ureme_gercekles(hayvan1, hayvan2)

    def ureme_gercekles(self, hayvan1, hayvan2):
        yeni_hayvan = type(hayvan1)(random.randint(0, self.arazi.en), random.randint(0, self.arazi.boy))
        yeni_hayvan.cinsiyet = random.choice([hayvan1.cinsiyet, hayvan2.cinsiyet])
        self.hayvanlar.append(yeni_hayvan)
        print(f"Yeni bir {yeni_hayvan.cinsiyet} {yeni_hayvan.tur} doğdu!")

    def hayvan_sayisini_yazdir(self):
        sayac = {}
        for hayvan in self.hayvanlar:
            sayac[hayvan.tur] = sayac.get(hayvan.tur, 0) + 1
        print("\n1000 adım sonrasında\nKalan Hayvanların Sayısı:")
        for tur, sayi in sayac.items():
            print(f"{tur}: {sayi}")

arazi = Arazi()
hayvan_olusturucu = HayvanOlusturma(arazi)
hayvan_olusturucu.hayvan_olustur(Koyun, 15, cinsiyet="Erkek")
hayvan_olusturucu.hayvan_olustur(Koyun, 15, cinsiyet="Dişi")
hayvan_olusturucu.hayvan_olustur(Kurt, 5, cinsiyet="Erkek")
hayvan_olusturucu.hayvan_olustur(Kurt, 5, cinsiyet="Dişi")
hayvan_olusturucu.hayvan_olustur(Inek, 5, cinsiyet="Erkek")
hayvan_olusturucu.hayvan_olustur(Inek, 5, cinsiyet="Dişi")
hayvan_olusturucu.hayvan_olustur(Tavuk, 10 )
hayvan_olusturucu.hayvan_olustur(Horoz, 10 )
hayvan_olusturucu.hayvan_olustur(Aslan, 4, cinsiyet="Erkek")
hayvan_olusturucu.hayvan_olustur(Aslan, 4, cinsiyet="Dişi")
hayvan_olusturucu.hayvan_olustur(Avci, 1)

for _ in range(1000):
    hayvan_olusturucu.hareket_et()
    hayvan_olusturucu.avlan()
    hayvan_olusturucu.ureme_kontrol()

hayvan_olusturucu.hayvan_sayisini_yazdir()
