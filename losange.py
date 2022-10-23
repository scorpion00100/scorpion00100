def lit(fichier, position, nb_octets): #lit une suite d'octet et en retourne la liste
    fichier.seek(position)
    return list(fichier.read(nb_octets))

def lit_entier(fichier, position, nb_octets): # lit un entier sur plusieurs octets
    fichier.seek(position)
    return int.from_bytes(fichier.read(nb_octets), byteorder="little", signed=True)

def ecrit(fichier, position, octet) : # ecrit un seul octet
    fichier.seek(position)
    fichier.write(bytes([octet]))

def ecrit_liste(fichier, position, octets) : # ecrit une liste d'octets
    fichier.seek(position)
    fichier.write(bytes(octets))

def ecrit_entier(fichier, position, entier, nb_octets): # ecrit un entier (sur plusieurs octets)
    fichier.seek(position)
    fichier.write(entier.to_bytes(nb_octets, byteorder='little', signed=True))

f = open("formes.bmp", 'r+b')
taille_fichier = lit_entier(f, 2, 4)

debut_image = lit_entier(f, 10, 4)

largeur_image = lit_entier(f, 18, 4)

hauteur_image = -lit_entier(f, 22, 4)

ecrit_liste(f , debut_image, [0xff]*(taille_fichier - debut_image))

for x in range(largeur_image//2):
    ecrit_liste(f, debut_image+(x*(taille_fichier//largeur_image))+(largeur_image*2)-(x*4),([0x00]+[0x00]+[0x00]+[0x00])*(x))
    ecrit_liste(f, debut_image+(x*(taille_fichier//largeur_image))+(largeur_image*2),([0x00]+[0x00]+[0x00]+[0x00])*(x))
    ecrit_liste(f, debut_image+((taille_fichier - debut_image)//2)+(x*(taille_fichier//largeur_image))+(x*4), ([0x00]+[0x00]+[0x00]+[0x00])*((largeur_image//2)-x))
    ecrit_liste(f, debut_image+((taille_fichier - debut_image)//2)+(x*(taille_fichier//largeur_image))+(largeur_image*2), ([0x00]+[0x00]+[0x00]+[0x00])*((largeur_image//2)-x))

f.close()