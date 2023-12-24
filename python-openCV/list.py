Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #listeler
>>> isimler=["Ali","Ayse","Fatma"]
>>> isimler
['Ali', 'Ayse', 'Fatma']
>>> isimler[0]
'Ali'
>>> isimler[1]
'Ayse'
>>> isimler[1:]
['Ayse', 'Fatma']
>>> isimler=["","Ali","Ayse","Fatma"]
>>> isimler[0]
''
>>> yaslar=[19,23,11]
>>> yaslar
[19, 23, 11]
>>> isimler+yaslar
['', 'Ali', 'Ayse', 'Fatma', 19, 23, 11]
>>> isimler=["Ali","Ayse","Fatma"]
>>> isimler+yaslar
['Ali', 'Ayse', 'Fatma', 19, 23, 11]
>>> #listeye eleman ekleme
>>> isimler.append("Mehmet")
>>> isimler
['Ali', 'Ayse', 'Fatma', 'Mehmet']
>>> yaslar.append("33")
>>> yaslar
[19, 23, 11, '33']
>>> isimler+yaslar
['Ali', 'Ayse', 'Fatma', 'Mehmet', 19, 23, 11, '33']
>>> #listenin içini temizleme
>>> isimler=[]
>>> isimler
[]
>>> #liste içinde liste oluşturmak
>>> isimler=["Ali","Ayse","Fatma"]
>>> isimler.append("Mehmet")
>>> kimlik=(isimler,yaslar)
>>> kimlik
(['Ali', 'Ayse', 'Fatma', 'Mehmet'], [19, 23, 11, '33'])
