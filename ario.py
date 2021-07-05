Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class biodata():
    def __init__(self,nama,nim,kelas):
 
        print "====================INPUT========================"
        print "Silakan masukkan biodata anda:"
 
    def input(self):
        self.nama = raw_input("Nama: ario budiaji           ")
        self.nim = raw_input("NIM:    04114026         ")
        self.kelas = raw_input("kelas:   b       ")

class mahasiswa(biodata):
    def cetak(self):
        print "====================CETAK========================"
        print "Biodata anda:"
        print "Nama:            ",self.nama
        print "NIM:             ",self.nim
        print "Alamat:          ",self.kelas
 
dataMhs = mahasiswa("nama","nim","kelas")
dataMhs.input()
dataMhs.cetak()
