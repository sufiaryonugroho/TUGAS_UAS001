NAMA = raw_input("MASUKKAN NAMA ANDA :")
NIM = raw_input("MASUKKAN NIM ANDA :")
UTS = int(raw_input("MASUKKAN NILAI UTS ANDA :"))
UAS = int(raw_input("MASUKKAN NILAI UAS ANDA :"))
TUGAS = int(raw_input("MASUKAN NILAI TUGAS ANDA :"))
akhir = (UTS+UAS+TUGAS)/3
print"=================================="
print " NILAI AKHIR ANDA :", akhir
print "*****************************"

if akhir >=70 :
    print "A"
    print "LULUS"


elif akhir >=60 :
    print "B"
    print "LULUS"

elif akhir >=55 :
    print "C"
    print "TIDAK LULUS"

elif akhir <= 30 :
    print "D"
    print "TIDAK LULUS"

elif akhir <= 0 :
    print "E"
    print "TIDAK LULUS"

print "================================================================="
print "| Nama | NIM | Tugas | UTS | UAS | Akhir "
print "================================================================="
print "| Sufi Aryo Nugroho | 311710097 | 80 | 80 | 80 | 80 " 

