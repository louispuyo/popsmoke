import hashlib
from getpass import getpass

chaine_mot_de_passe = b"popsmoke"
mot_de_passe_chiffre = hashlib.sha1(chaine_mot_de_passe).hexdigest()
print(mot_de_passe_chiffre)

verrouille = True
while verrouille:
    entre = getpass("Tapez le mot de passe : ") # azerty
    # On encode la saisie pour avoir un type bytes
    entre = entre.encode()
    
    entre_chiffre = hashlib.sha1(entre).hexdigest()
    if entre_chiffre == mot_de_passe_chiffre:
        verrouille = False
    else:
        print("Mot de passe incorrect")

print("Mot de passe accepté...")