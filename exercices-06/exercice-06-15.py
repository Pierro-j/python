# exo 6.15
# Trouvez la chaîne de caractères la plus longue dans une liste.
# Affichez son index, sa valeur et sa longueur.

my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

# réponse 6.15

longest_string = ''

for i,string in enumerate(my_list):
    if len(string) > len(longest_string):
        longest_string = string

print(f'Index: {my_list.index(longest_string)}')
print(f'Valeur: {longest_string}')
print(f'Longueur: {len(longest_string)}')

