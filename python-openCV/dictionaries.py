#sözlükler "dictionaries"
sozluk={"Ad":"Emir","Yas":"22","Okul":"ERU"}
print(sozluk["Ad"])
print(sozluk["Yas"])
sozluk["Yas"]=23
print(sozluk["Yas"]) #yas 23 e çıktı değişti.
print(sozluk)
sozluk.clear()      #temizler
print(sozluk)
del sozluk
print(sozluk)
