# l'operateur d'affectation = permet d'injecter une valeur a une variable

# Intenger
my_number1 = 123
my_number2 = -42

# String "" ou ''
# \ caracthere d'echapement  \\ pour mettre le "\" (Permet de mettre les "" dans un str)
#  \n saut de ligne 
# """ Pour faire plusieur ligne de str

my_text = 'chaine de caractères'
my_text2 = 'Autre chaine de caractères'
my_text3 = "abc\ndef\nghi"
my_text4 = "John \"Foo\" Doe"
my_text6 = """abc
def
ghi
"""

print(my_text6) 
print(type(my_text6))


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
# print(type(r), type(pi), type(s))
a = 123
b = 42

a,b = b, a 

c = a
print(c,b)
#variantes 
# marque que avec des nombes
c = a + b
a = c - b 
b = c - a
print(a,b)
