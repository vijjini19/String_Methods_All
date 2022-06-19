'''1.capitalize()'''
# a="world"
# print(a.capitalize())  #World
# b="cOMPUTER"
# print(b.capitalize())  #Computer

'''2.casefold()'''
# a='PYTHON PROGRAM'
# print(a.casefold())  #python program

'''3.center()'''
# a='movie'
# print(a.center(9,'0'))  #00movie00
# b='serial'
# print(b.center(15,'3'))   #33333serial3333

'''4.count()'''
# a="73637777777836"
# print(a.count('7'))  #8
# a="hhhddukskkkk"
# print(a.count('k'))  #5

'''5.encode()'''
# a="awesomeprogram"
# print(a.encode())  #b'awesomeprogram'
# a='55667'
# print(a.encode())  #b'55667'

'''6.endswith()'''
# n="abc5"
# print(n.endswith('5'))  #True
# m="hey9"
# print(m.endswith('9'))  #True
# print(m.endswith('5'))  #False 

'''7.find()'''
# x='87123456'
# print(x.find('4'))  #5
# print(x.find('7'))  #1
# print(x.find('6'))  #7

'''8.index()'''
# y="im writing python program"
# print(y.index('python')) #11

'''9.isalnum()'''
# z="1a2b3c4d"
# print(z.isalnum())  #True

'''10.isalpha()'''
# n="abcdefg"
# print(n.isalpha())  #True
# m="d576dd98"
# print(m.isalpha())  #False

'''11.isdecimal()'''
# a="00032"
# print(a.isdecimal())  #True

'''12.isdigit()'''
# b="37353902"
# print(b.isdigit())  #True
# c="swbhjs78y"
# print(c.isdigit())  #False

'''13.isidentifier()'''
# a="hello"
# print(a.isidentifier())  #True
# b="3hey"
# print(b.isidentifier())  #False
# c="_fine33"
# print(c.isidentifier())  #True

'''14.islower()'''
# x="clock"
# print(x.islower())  #True
# y="DIRECTIOn"
# print(y.islower())  #False

'''15.isnumeric()'''
# p="2456256256"
# print(p.isnumeric())  #True

'''16.isprintable()'''
# q="im doing well"
# print(q.isprintable())  #True

'''17.isupper()'''
# z="SINDHU"
# print(z.isupper())  #True
# n="sindhu"
# print(n.isupper())  #False

'''18.lower()'''
# a="WELCOME"
# print(a.lower())  #welcome

'''19.upper()'''
# b="hyderabad"
# print(b.upper())  #HYDERABAD

'''20.title()'''
# c="how are you doing"
# print(c.title())  #How Are You Doing

'''21.expandtabs()'''
# a="w\te\tl\tc\to\tm\te"
# print(a.expandtabs())  #w  e  l  c  o  m  e

'''22.format'''
# a="i am having bank balance of {price} rupee"
# print(a.format(price=20000))  #i am having bank balance of 20000 rupee

'''23.format_map()'''
# b="my sister is having bank balance of {price} rupee"
# print(b.format_map(price=30000))

'''24.isspace()'''
# c="she is playing"
# print(c.isspace())  #False

'''25.join()'''
# x='sindhu','bindhu','indu'
# print('hello'.join(x))  #sindhuhellobindhuhelloindu

'''26.ljust()'''
# y="hello"
# print(y.ljust(7,"0"))  #hello00

'''27.lstrip()'''
# abc="  program"
# print(abc.lstrip())  #program

'''28.maketrans'''
# ss="hello program"  
# print(ss.maketrans('e','w'))  #{101: 119}

'''29.partition'''
# w="how can i help you"
# print(w.partition("6"))  #('how can i help you', '', '')

'''30.replace'''
# a="python is a programming language"
# print(a.replace("python","java"))  #java is a programming language

'''31.rfind'''
# w="how may i help you"
# print(w.rfind('may',2))  #4

'''32.rindex'''
# abc="hello,welcome to my world"
# print(abc.rindex('o'))  #21

'''33.rjust'''
# y="hello"
# print(y.rjust(8,"0"))  #000hello

'''34.rpartition'''
# w="how may i help you"
# print(w.rpartition("14"))  #('', '', 'how may i help you')

'''35.rsplit'''
# x="apple,banana, cherry"
# print(x.rsplit())  #['apple,banana,', 'cherry']

'''36.rstrip'''
# y="hello  "
# print(y.rstrip())  #hello

'''37.split'''
# y="apple,banana,  cherry"
# print(y.split())  #['apple,banana,', 'cherry']

'''38.splitlines'''
# z="hello,hai,  hey"
# print(z.splitlines())  #[['hello,hai,  hey']

'''39.startswith'''
# abc="56fghg"
# print(abc.startswith('5'))  #True

'''40.strip'''
# a='    hello     '
# print(a.strip())  #hello

'''41.swapcase'''
# b="aAbBcCdD"
# print(b.swapcase())  #AaBbCcDd

'''42.transalte'''
# x="python"
# y="program"
# print(y.translate("x"))  #program

'''43.zfill'''
# a="sindhu"
# print(a.zfill(9))  #000sindhu






































