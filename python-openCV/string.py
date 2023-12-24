Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 'beyaz zambaklar ülkesi'
'beyaz zambaklar ülkesi'
>>> "beyaz zambaklar ülkesi"
'beyaz zambaklar ülkesi'
>>> "zambaklar ülkesi \"grigory petrov\""
'zambaklar ülkesi "grigory petrov"'
>>> "zambaklar ülkesi "grigory petrov""
SyntaxError: invalid syntax
>>> "zambaklar ülkesi "grigory petrov" "
SyntaxError: invalid syntax
>>> "zambaklar ülkesi 'grigory petrov' "
"zambaklar ülkesi 'grigory petrov' "
>>> print(""zambaklar ülkesi "grigory petrov""")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("zambaklar ülkesi "grigory petrov"")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("zambaklar ülkesi \"grigory petrov"\")
SyntaxError: unexpected character after line continuation character
>>> "anne"*2
'anneanne'
>>> 'anne'*2
'anneanne'
>>> 'ba'*2
'baba'
>>> "py"+"thon"
'python'
>>> a="anne"
>>> a*2
'anneanne'
>>> a="eyvallah"
>>> a[0]
'e'
>>> for(int i=0;i<len;i++)print(a[i])
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> i=0
>>> for(int i=0;i<len;i++)print(a[i])
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> a[0:8]
'eyvallah'
>>> a[0:7]
'eyvalla'
>>> a[3:5]
'al'
>>> b="ben"
>>> b[-1:-3]
''
>>> b[-1]
'n'
>>> b[-1:-3]
''
>>> #^yukaridaki örnekte gözüktüğü üzre tersten yazdırma bu şekilde kabul görülmez boş döndürür.
