import random

# if True:
#     print("Ouui c'est vrai")
#     print("Ce code est exécuté")

# if False:
#     print("Non c'est faux")
#     print("Ce code est exécuté")

cd_vente = False

# if cd_vente:
#     print("user agreed to cd_vente")
# else:
#     print("user didn't agreed to cd_vente")

# if not cd_vente:
#     print("user didn't agreed to cd_vente")

# emails = random.randint(0, 3)
# if emails == 1:
#     print("Nouveau mails")
# elif emails > 1:
#     print(f"Vous avez {emails} nouveaux mails")
# else:
#     print("Pas de nouveaux mails")


# windows_closed = bool(random.randint(0, 1))
# electricity_off = bool(random.randint(0, 1))

# print(f'{windows_closed =}')  
# print(f'{electricity_off =}')

# if windows_closed and electricity_off:
#     print("Les fenêtre sont fermées")
#     print("L'électricité est coupé")
# elif not windows_closed and electricity_off:
#     print("Les fenêtre ne sont pas fermées")
#     print("L'électricité est coupé")
# elif windows_closed and not electricity_off:
#     print("Les fenêtre sont fermées")
#     print("L'électricité n'est pas coupé")
# else:
#     print("Les fenêtre ne sont pas fermées")
#     print("L'électricité n'est pas coupé")


bank_card = True
cash = True

print(f'{bank_card =}')
print(f'{cash =}')

if bank_card or cash:
    print("On a un moyen de payement")
else:
    print("Aucun moyen de payement")


