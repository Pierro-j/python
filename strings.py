my_text = """Texte
multi-ligne
abc
foo
bar"""

# print(my_text)
my_text2 = "oui\nnon\noui"
# print(my_text2)

my_number = 123
#!interpolation avec f-string
my_text3 = f"Nombre = {my_number}"
#!interpolation avec une heredoc f-string

my_text4 = f"""le nombre 
est
{my_number}
foo
"""
# print(my_text4)

#!afficher des accolades dans une heredoc f-string
my_text5 = f"""
{{
    foo
}}
[
    bar
]
"""
# print(my_text5)

my_number2 = 3.14
#! concaténation de chaînes de caractères
my_text6 = "le nombre PI est " + str(my_number2) + "\nEt le nombre d'or est 1,618"
# print(my_text6)

#! tronquer un float dans une interpolation
#! .4f veut dire 4 chiffres après la virgule
my_number3 = 1/3
my_text7 = f"1/3 ~= {my_number3:.4}"
# print(my_text7)


#! Les interpolation acceptent les expressions
my_text8 = f"1+1 = {1+1}"
# print(my_text8)

#! définition d'une fonction
#!exemple d'ecriture de documentation pour une fonction
def hello(name: str) -> None:
    """Cette fonction dit bonjour à quelqu'un

    name str indique le nom e la personne a saluer
    return None
    """
    print(f"Salut {name}")

#! Appel d'une fonction
# hello("moi")

#! affiche la documentation -> help(hello)

#*
#!
#?
#TODO



my_text9 = "Lorem ipsum dolor sit, amet consectetur ipsum adipisicing elit."
#! Longueur d'une str
my_number4 = len(my_text9)
# print(my_number4)

#! Trouve la position d'une str dans une autre str
my_number5 = my_text9.find("ipsum")
# print(my_number5)

my_number5 = my_text9.find("ipsum", my_number5 + 1) #! mieux utiliser une boucle
# print(my_number5)

#! Compte le nomber d'occurence d'une str dans une autre str
my_number6 = my_text9.count("ipsum")
# print(my_number6)

#! remplacement non permanant
# print(my_text9.replace('ipsum', 'Foo'))
#! remplacement permanant (écrase la variable avec la nouvelle valeur)
my_text9 = my_text9.replace('ipsum', 'Foo')
# print(my_text9)

#! éclate une str en liste en utilisant l'espace comme caractère de séparztion des élements
my_list = my_text9.split()
# print(my_list)
#! La fonction len() peut aussi être utilisée avec des listes pour compter le nombre d'éléments
# print(len(my_list))


#! accèes a la lecture du 0ème caractère de la str
# print(my_text9[0])

#! accèes a la lecture du 0ème au 10ème caractère de la str
# print(my_text9[0:10])

#! accèes a la lecture du 10ème jusqu'au dernier caractère de la str
# print(my_text9[10:])

#! accèes a la lecture par la fin de la str
# print(my_text9[::-1])

#! accès en lecture 1 caractère sur 2 de la str
print(my_text9[::2])



