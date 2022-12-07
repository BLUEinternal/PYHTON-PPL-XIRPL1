#jenis enkapulasi :public, protectted, prifvate

#membuat public classs

class segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi;


#instansiasi

segitiga_besar = segitiga(100, 80)


#print
print('ini adalah public class')
print(f'alas = {segitiga_besar.alas}')
print(f'tinggi = {segitiga_besar.alas}')
print(f'luas = {segitiga_besar.alas}\n')


#protected class

class mobil : #class induk
    def __init__(self,merk):
        self._merk = merk   #protrcted class declaration

class mobilf1(mobil):
    def __init__(self, merk, total_gear):
        super().__init__(merk)
        self._total_gear = total_gear     

    def pamer(self):
        #hak akses mark dari subclass
        print(f'ini adalah mobil {self._merk}dengan  total  gear nya{self._total_gear}')

print('ini adalah protected class')
ferari = mobilf1('ferari',8)
ferari.pamer()


#membaut private class
class motor:
    def __init__(self, merk):
        self.__merk = merk #private class declaration
    def tampilkan_merk(self):
        print(f'merk motornya : {self.__merk}')  
        #pangil private disini


#instansiasi
print('ini adalah private class')
moge = motor ('harley') 
moge.tampilkan_merk()       
        