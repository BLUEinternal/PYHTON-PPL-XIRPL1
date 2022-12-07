class Agama:
    def __init__(self, nama, agama):
        self.nama = nama
        self.agama = agama

        
    def perkenalan(self):
        print(self.nama, "Beragama", self.agama )



class Islam(Agama):
    def __init__(self, nama, agama, sholat):
        super().__init__( nama, agama)
        self.sholat = sholat



class kristen(Agama):
    def __init__(self, nama, agama, sembahyang):
        super().__init__(nama, agama)
        self.sembahyang = sembahyang


hisyam = Islam('Hisyam', 'Islam', 'Sholat \n')
hisyam.perkenalan()
print(f'{hisyam.nama} beribadah dengan melakukan {hisyam.sholat}')

abraham = kristen('Abraham', 'kristen', 'Sembahyang \n')
abraham.perkenalan()
print(f'{abraham.nama} beribadah dengan melakukan{abraham.sembahyang}')