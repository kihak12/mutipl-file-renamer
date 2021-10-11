import sys
import os
import pathlib
import moviepy
import time
import moviepy.editor

# But du programme : renomer les video présentes dans le dossier sélectionner

# Dossier dans lesquels effectuer la recherche
mains_folders = [str(input("Entrez le dossier des episodes a renommer : "))]


# Fonction redemarrage du programme
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


# Liste des episodes trouver
eps_folders = []

# Recherche des episodes
for s in mains_folders:
    folders = s;
    dirs = os.listdir( folders )

    for f in dirs:
        episode = f;

# Ajout dans la liste
        eps_folders.append( folders + "\\" + episode)

# Listage de la liste
for file in eps_folders:
   print ( file )


Nb_eps = len(eps_folders)
   
# Pause dans le script en Sec
confirm = input("Avez vous entrer le bon chemin Y/N :")

if confirm == "n" :
    restart_program()

else :
    print("demarrage")

# Creation dossier sauvegarde
    save_dir = pathlib.Path( folders + "/Rename/")
    print (save_dir)
    if save_dir.exists ():
        print ("directory exist")
    else:
        os.mkdir(str(mains_folders[0]) + '/Rename/')
        print ("directory created")

# Nouveau nom a appliquer
new_name = input("comment renommer les episodes : ")
number = int(input("Numéro episode du début : "))
ext = "." + input("Type de fichier : ")

i = 0

while Nb_eps > i:
    if dirs[i] == "Rename":
        i = i + 1
    else:
        if i <= 9 and number <= 9:
            print(new_name + "0" + str(i + number))
            os.rename(str(eps_folders[i]), str(save_dir) + "\\" + new_name + "0" + str(i + number) + ext)
            i = i + 1
        else:
            print(new_name + str(i + number))
            os.rename(str(eps_folders[i]), str(save_dir) + "\\" + new_name + str(i + number) + ext)
            i = i + 1


restart = input("Recommencer ?")
if restart == "y" :
    restart_program()



