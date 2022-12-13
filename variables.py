import random
import math
from decimal import Decimal

# l'operateur d'affectation = permet d'injecter une valeur a une variable

# Intenger
# my_number1 = 123
# my_number2 = -42

# # String "" ou ''
# # \ caracthere d'echapement  \\ pour mettre le "\" (Permet de mettre les "" dans un str)
# #  \n saut de ligne 
# # """ Pour faire plusieur ligne de str

# my_text = 'chaine de caractères'
# my_text2 = 'Autre chaine de caractères'
# my_text3 = "abc\ndef\nghi"
# my_text4 = "John \"Foo\" Doe"
# my_text6 = """abc
# def
# ghi
# """

# print(my_text6) 
# print(type(my_text6))


# print(type(my_text + ' ' + my_text2))
# print(my_number1 + my_number2)
# print(type(my_number1 + my_number2))
# print(my_text4)


# # Float
# my_number3 = 3.14
# my_number4 = -2.71
# my_number5 = 0.0

# print(my_number3)
# print(type(my_number3))
# print(my_number4)
# print(my_number5)
# print(my_number5)
# print(float(my_number1))


# # bool, booléen 
# my_boolean1 = True
# my_boolean2 = False
# print(my_boolean1)
# print(my_boolean2)
# print(type(my_boolean1))


# # None , valeur nule

# my_none = None
# print(my_none)
# print(type(my_none))


# r, pi = 12, 3.14159
# s = pi * r**2
# print(s)
# # print(type(r), type(pi), type(s))
# a = 123
# b = 42

# a,b = b, a 

# c = a
# print(c,b)
# #variantes 
# # marque que avec des nombes
# c = a + b
# a = c - b 
# b = c - a
# print(a,b)

# transtypage
# foo = "123"
# foo = int(foo)   
# # str vers int
# foo = float(foo)
# # str vers float 
# foo = 3.14
# # float vers int suprime tout ce qui a apres la virgule
# foo = int(foo)
# # float en str
# foo = 3.14
# foo = str(foo)

# foo = 2.71
# # recuperer la partie entiere (2)
# a = int(foo)
# # recuperer la partie apres les virgules (0.71)
# b = foo - a
# # print(a, b)


# d = random.uniform(1, 1000)
# print(format(d, '.2f'))
# # number3_rounded = round(number3, 2)
# print(format(Decimal.from_float(d), '.3'))


# # Typecasting == transtyage == conversion d'un type de donées

# # 0 donne false et tout les autres nombres donnent True
# my_number = 0.1
# #Conversion explicite en booleen
# print(bool(my_number))

# #Conversion implicite en booleen
# if bool(my_number):
#     print("User put something other than 0")
# else:
#     print("User put 0")


# my_text = ''
# print(bool(my_text))

# if bool(my_text):
#     print("User write")
# else:
#     print("User didn't write")


# #Listes 
# fruits = ['ananas', 'banane' , 'cerise']

# #operateur d'inclusion
# result = 'ananas' in fruits
# print(result)
# result = 'fraise' in fruits
# print(result)

# # Conversion explisite en booleen 
# result = bool(fruits)
# print(result)


# if fruits:
#   print("La liste contient des element")
# else:
#     print("La liste ne contient pas d'élement")

