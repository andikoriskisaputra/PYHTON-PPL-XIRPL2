# contoh overloading
# mendefinisikan atau memfungsikan operator sesiau kemauan kita (+)

class angka:
    def __init__(self,angka):
        self.angka = angka
    
    def __add__(self,objek):
        return angka(
            self.angka + objek.angka
        )

# mambuat objek
x1 = angka(10)
x2 = angka(20)
x3 = x1 + x2
print(x3.angka)