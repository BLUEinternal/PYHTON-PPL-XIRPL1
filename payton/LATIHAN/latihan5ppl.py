#buat 3 objek orang ,pelajar , pekerja
#orang = kelas induk
#pelajar , pekerja = kelas turunan

class orang:
    def __init__(self, nama, asal):
        self.nama = nama 
        self .asal = asal
        print("fungsi di eksekusi")
     

    def perkenalan(self):
        print("hallo nama saya ",self.nama,"dari",self.asal)


class pelajar(orang):
    def __init__(self, nama, asal,sekolah):
        orang.__init__(self,nama,asal,)
        self.sekolah = sekolah
       
       
class pekerja(orang):
    def __init__(self, nama, asal,kantor):
        super().__init__(nama,asal)
        self.kantor = kantor
       

andi = orang('andi','jakarta\n')
andi.perkenalan()

tito = pelajar('tito','subang','smk jp1\n')
tito.perkenalan()
print(f'saya sekolah di{tito.sekolah}\n')

cahyo = pekerja('cahyo','bandung','smk p1')
cahyo.perkenalan()
print(f'asal kerja di{cahyo.kantor}\n')





        
