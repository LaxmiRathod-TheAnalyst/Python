Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
"hello".count("e")
1
text = "happy birthday"
txt.count("a")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    txt.count("a")
NameError: name 'txt' is not defined. Did you mean: 'text'?
text.count("a")
2
text.count("day")
1
x = "Happy Birthday"
x.lower()
'happy birthday'
x.upper()
'HAPPY BIRTHDAY'
x
'Happy Birthday'
# strings are an immutable data type....they cannot be changed but can be overwritten
x = x.upper()
x
'HAPPY BIRTHDAY'
x = x.lower()
x
'happy birthday'
x.capitalize()
'Happy birthday'
x
'happy birthday'
x.title()
'Happy Birthday'
x = x.title()
x
'Happy Birthday'
x
'Happy Birthday'
x.islower()
False
x.isupper()
False
x.istitle()
True
# to check if it contains letters
x.isalpha()
False
x
'Happy Birthday'
# false ...x has space in between
"abcd"
'abcd'
"abcd".isalpha()
True
x.isdigit()
False
"123".isdigit()
True
y = "happy birthday 123"
y,isalphamnum()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    y,isalphamnum()
NameError: name 'isalphamnum' is not defined
y,isalphanum()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    y,isalphanum()
NameError: name 'isalphanum' is not defined
y.isalphanum()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    y.isalphanum()
AttributeError: 'str' object has no attribute 'isalphanum'. Did you mean: 'isalnum'?
y.isalnum()
False
y = "happybirthday123"
y.isalnum()
True
.lower(),.upper(),.title(),.capitalize()
SyntaxError: invalid syntax
.islower,.isupper(),.istitle()
SyntaxError: invalid syntax
.count("a")
SyntaxError: invalid syntax
.isalpha(),.isdigit(),.isalnum()
SyntaxError: invalid syntax

================================ RESTART: Shell ================================
x = "happy birthday"
x.index("birthday")
6
#h = 0 , a = 1, p =2, p =3, y = 4, space = 5....
x.index("ghggyghjbb")
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    x.index("ghggyghjbb")
ValueError: substring not found
# to find small string inside big string
x.find("birthday")
6
x.find("ghgfgftrtjhjjhjbbvb")
-1
#methods are casesensitive
x.index("Birthday")
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    x.index("Birthday")
ValueError: substring not found
x.find("Birthday)
       
SyntaxError: unterminated string literal (detected at line 1)
x.find("Birthday")
       
-1
y = "000000happybirthday00000")
SyntaxError: unmatched ')'
y = ("000000happybirthday00000")
y.strip("0") # stripoff zero
'happybirthday'
y
'000000happybirthday00000'
y.lstrip("0") # stripoff from left
'happybirthday00000'
y.rstrip("0") # stripoff from right
'000000happybirthday'
'000000happybirthday'
'000000happybirthday'
y.strip()
'000000happybirthday00000'
name = input("What is your name?: ")
What is your name?: lax
print(name)
lax
len(name)
3
name = input("What is your name?: ")
What is your name?: lax   
print(name)
lax   
len(name)
6
# space while entering the name
name = input("What is your name?: ").strip()
What is your name?: lax  
print(name)
lax
len(name)
3
y.strip() # strip aay white spaces
'000000happybirthday00000'
