#praktekan ENKAPULASI
#buatlah masing prameter:
#siswa - public
#guru - protected
#kepsek - private

#tampilakn
#1.siswa kami bernama euroski
#
#


class siswa:
    def __init__(self, siswa ):
        self.siswa = siswa
       

#instansiasi

nama_siswa = siswa('euroski')


#print
print('ini adalah public class')
print(f'1. siswa kami bernama {nama_siswa.siswa} \n')


 

class gurujp1 : #class induk
    def __init__(self,guru):
        self._guru = guru   #protrcted class declaration

class guru(gurujp1):
    def __init__(self, guru):
        super().__init__(guru)
          

    def nama_guru(self):
        #hak akses mark dari subclass
        print(f'2.nama guru saya yg baik adalah{self._guru}\n')

print('ini adalah protected class')

output = guru('bu anita')
output.nama_guru()


class kepsek:
    def __init__(self, kepsek):
        self.__kepsek = kepsek #private class declaration
    def nama_kepsek(self):
        print(f'3.ini adalah kepsek kami {self.__kepsek} \n')  
        #pangil private disini


#instansiasi
print('ini adalah private class')
moge = kepsek ('pak lili bintoro') 
moge.nama_kepsek()       