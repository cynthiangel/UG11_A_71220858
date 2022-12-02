print ("======= Program Manipulasi String =======")
print ("Pilihan Menu :")
print ("1. Hitung Kata")
print ("2. Ubah Kata")
pilihan = input ("pilihan anda :")
kata = input("Masukkan sebuah kalimat/kata :")

def hitung_kata():
    a=input("Masukkan kata yang ingin dihitung :")
    al=kata.count(a)
    print ("Terdapat sebanyak",al,"kata",a,"didalam kalimat")

def ubah_kata ():
    b=input("Masukkan kata yang ingin diubah :")
    c=input("Masukkan kata pengganti")
    d=kata.replace(b,c)
    print("string berhasil diubah menjadi :",d)

if pilihan=="1":
    hitung_kata ()

elif pilihan=="2" :
    ubah_kata()
else :
    print("pilihan yang anda ingin input tidak terdaftar di daftar pilihan")
