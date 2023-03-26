"""
Created on Tue Apr 16/11/2022

@author: Maxime Torre
"""
import skimage.io as skio
from os.path import join
import matplotlib.pyplot as plt


filename_2 = r'Rainbow.jpg'
dirpath_2 = r'C:/Users/torre/Documents/2A_Phelma_Partiel_S1/TP_traitement_image/Target_images'
filepath_2 = join(dirpath_2, filename_2)
print(filepath_2)

img_2 = skio.imread(filepath_2)

longueur = 1920
largeur = 1216
taille_bloc = 4 # PGCD(longueur, largeur) et après on peut encore le diviser par un multiple de 4
nb_bloc = (longueur*largeur)//(taille_bloc**2) # =570
L_img = []

img_3 = img_2
print(img_2[1215][1919]) # le maximum que l'on peut avoir !!!
print("longueur max : ",((longueur-(taille_bloc**2)//taille_bloc) -1))
print("largeur max :", ((largeur-(taille_bloc**2)//taille_bloc) - 1))

for largeur_bloc in range(largeur//taille_bloc): # largeur bloc
    #print("largeur bloc =", largeur_bloc)
    for longueur_bloc in range(longueur//taille_bloc):# longueur bloc
        #print("longueur bloc =",longueur_bloc,"largeur bloc =", largeur_bloc)
        R = 0
        G = 0
        B = 0
        R_moy = 0
        G_moy = 0
        B_moy = 0
        for k in range(taille_bloc): # colonne
            for i in range(taille_bloc): # ligne
                #print("i = ", i,"k = ",k)
                R = R + img_2[k + largeur_bloc*taille_bloc][i + longueur_bloc*taille_bloc][0]
                G = G + img_2[k + largeur_bloc*taille_bloc][i + longueur_bloc*taille_bloc][1]
                B = B + img_2[k + largeur_bloc*taille_bloc][i + longueur_bloc*taille_bloc][2]
        R_moy = R//(taille_bloc**2)
        G_moy = G//(taille_bloc**2)
        B_moy = B//(taille_bloc**2)
        #print("RGB moy =:", R_moy ,  G_moy , B_moy )
        for k in range(taille_bloc): # colonne
            for i in range(taille_bloc): # ligne
                img_3[k + largeur_bloc*taille_bloc][i + longueur_bloc*taille_bloc][0] = R_moy
                img_3[k + largeur_bloc*taille_bloc][i + longueur_bloc*taille_bloc][1] = G_moy
                img_3[k + largeur_bloc*taille_bloc][i + longueur_bloc*taille_bloc][2] = B_moy

img_2 = skio.imread(filepath_2)

fig1, axes1 = plt.subplots(ncols=2,figsize=(8, 4))
axes1[0].imshow(img_2)
axes1[0].set_title('Based Image')
axes1[1].imshow(img_3)
axes1[1].set_title('4px*4px Bloc')

plt.show()
