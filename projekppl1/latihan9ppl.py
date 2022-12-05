# beberapa yang biasa digunakan untuk ngoding

# magic method init (konstruktor) berfungsi untuk mendahulukan gilira satu sekali jalan codingannya atau looping 
class halodunia:
    def __init__(self):
        print('Halo dunia')

# membuat instansiasi
# a = halodunia()


# magic method str, menampilkan string saat ketika dijadikan parameter
class segitiga:
    def __init__(self, a, t):
        self.a = a
        self.t = t

    def __str__(self):
        luas = 0.5 * self.a * self.t return f'segitiga (alas = {self.a}) (tinggi = {self.t}) (luas = {luas})'

# membuat instansiasinya
# a = segitiga(10,10)
# print(a)

# magic method len, len berfungsi untuk menghitung panjang dari objek yang kita buat

# class siswa
class siswa:
    def __init__(self):
        self.__list_siswa = []
    def tambah_siswa(self, siswa):
        self.__list_siswa.append(siswa)
    def __len__(self):
        return len(self.__list_siswa)

# buat instansiasi
grup1 = siswa()
grup1.tambah_siswa('putra')
grup1.tambah_siswa('boim')  

print(len(grup1))
# ['putra', 'boim']