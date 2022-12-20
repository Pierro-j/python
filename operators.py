# Librairies 
import random
import math

# opérateurs :
# = affectation 
foo = 123
# + addition 
foo = 123 + 42
foo = foo + 42
# += opérateur d'incrémentation
foo += 42

#foo++ équivlant de foo +=1  // Existe pas en python
# - soustraction 
foo = 123 - 42
# += opérateur d'décrémentation
foo -= 42
#oo-- équivlant de foo -=1  // Existe pas en python
# / division 
foo = 123/42
foo /= 42

# // division entière
foo = 123//42
foo //= 42
# % modulo 
foo = 4 % 3
#TODO 
foo = random.randint(1, 100)
# print(foo)
# print(foo % 2)
# #Si reste = nb impair

# # * multiplication 
# foo = 123 * 10
# foo *= 10
# # ** puissance 
# foo = 2 ** 2
# foo = foo ** 2
# foo = 2 ** 3
# foo = 2 ** 4
# foo = 2 ** 5
# foo = 2 ** 6
# print(foo)
# # ^ puissance mais pas en python 
# foo = 123 ^ 10
# foo ^= 10
# # sqrt() racine carré 
# # 0.5 racine carré
# #Les parrenthèses sont neccesaire 
# foo = math.sqrt(4)
# foo = 4 ** 0.5
# foo = 4 ** (1/2)
# print(foo)
# #racine cubique
# foo = 8 ** (1/3)
# print(foo)

# # les operateur de commparaison 

# # l'egalité ==
# # ne pas confondre avec l'afectation =
# # ne pas confondre avec l'identiter ===  // extiste pas en python
# result = 1 == "1"
# print(result)

# # les grandeurs 
# # plus petits
# result = 123 < 42
# print(result)
# # plus grnad
# result = 123 > 42
# print(result)

# # plus petit ou egal à 
# result = 123 >= 42
# print(result)

# # l'inégalité
# result = 123 != 42
# print(result)

# Les encadrement  < > <= >=

# my_number = random.randint(0, 100)
# print(my_number)
# result = 0 <= my_number < 50
# print(result)
# result = 50 < my_number <= 100
# print(result)

# # Utilisation un peu 'speciales' des comparaisons de grandeur
# result = "abc" < "bcd"
# print(result)


# operateur "and"

# result = True and False # False
# print(result)
# result = False and True # False
# print(result)
# result = True and True # True
# print(result)
# result = False and False # False
# print(result)


# # Operateur "or"
# result = True or False # True
# print(result)
# result = False or True # True
# print(result)
# result = True or True # True
# print(result)
# result = False or False # False
# print(result)


# # on peut utiliser d'autre types de donnés que l'on converti en booleen avec les operateur booleen
# a = random.randint(0,1)
# b = random.randint(0,1)
# result = bool(a) and bool(b) 
# print(a,b)
# print(result)

#operateur "not"
# result = not True
# print(result)
# result = not False
# print(result)



#! in renvoie un resultat boolean
fruits = ['abricot' ,'banana', 'apple']
result = 'ananas' in fruits
print(result)
result = 'apple' in fruits
print(result)
