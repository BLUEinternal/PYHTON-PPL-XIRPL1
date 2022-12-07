# def garis1():
#     print ("================================")

# def garis2():
#     print ("--------------------------------")
    
# buku = []

# def show_buku():  
#     if len(buku) <= 0:
#         garis1()
#         print("buku kosong mas")
#         garis1()
#     else:
#         for indeks in range(len(buku)):
#             garis1()
#             print ("[{}] {}". format (indeks,buku [indeks]))
#             garis1()



# class buku:
#     def __init__(self,delete,edit,masukan,perlihatkan):
#         self.delete = delete
#         self.edit = edit
#         self.masukan = masukan
#         self.perlihatkan = perlihatkan;

# buku = buku(0,0,0,0)

# print('------ini adalah Perpustakaan Online Heil Aurora-------')
# print(f'delete = {buku.delete}')
# print(f'edit = {buku.edit}')
# print(f'masukan = {buku.masukan}')
# print(f'perlihatkan = {buku.perlihatkan}')



# class masukan_buku:
#     def masukan_buku():
#         garis1()
#         buku_baru = input("judul buku : ")
#         buku.append(buku_baru)
#         garis1()
#         print("berhasil di tambah")
#         garis1()


# class perlihatkan_buku:
#     def edit_buku():
#         perlihatkan_buku()
#         indeks = int(input("Masukkan ID buku : "))
#         if indeks > len(buku):
#             print("ID Buku Salah")
#             garis2()
#         else:
#             judul_baru = input("Masukkan Judul Buku Baru : ")
#             buku[indeks] = judul_baru
#             garis2()
#             print ("Buku Berhasil Di Ubah")
#             perlihatkan_buku()
#             garis1()    

# class novel(buku):
#     def __init__(self, jenis, total_buku):
#         super().__init__(jenis)
#         self._total_buku = total_buku   

#     def Delete_buku():
#         show_buku()
#         indeks = int(input("inputan id buku : "))
#         if indeks > len(buku):
#             print ("id salah")
#         else:
#             buku.remove(buku[indeks])
#             garis1()
#             print("buku berhasil di apus !")
#             garis2()  

#     def perlihatkan_buku(self):
#         #hak akses mark dari subclass
#         print(f'ini adalah buku {self._jenis}dengan  total buku{self._total_buku}')

#     def perlihatkan_menu():
#         print("\n")
#         print ("---- Selamat Datang Di Perpustakaan Online Heil Aurora----")
#         print ("1. Perlihatkan Buku")
#         print ("2. Tambah Buku")
#         print ("3. Edit Buku")
#         print ("4. Delete Buku")
#         print ("5. Keluar")
        
#         menu = int(input("Silahkan Pilih Menu : > "))
        
#         if menu == 1:
#             perlihatkan_buku()
#         elif menu == 2:
#             masukan_buku()
#         elif menu == 3:
#             show1 = perlihatkan_buku()
#             show1.edit_buku()
#         elif menu == 4:
#             show2 = novel()
#             show2.Delete_buku()
#         elif menu == 5:
#             exit()
#         elif menu == '':
#             print("mohon maaf tolong di isi terlebih dahulu!")
#         else:
#             print("Maaf Salah, Silahkan Ulang Kembali.")
   
    
#         if __name__ == '__main__':
#             while (True):
#                 perlihatkan_buku()

#         show = novel()


#         print (show.perlihatkan_buku) 
#         print (show.masukan_buku)
#         print (show.edit_buku)
#         print (show.delete_buku)
#         print (show.exit)

# start = buku()
# start.perlihatkan_menu()




