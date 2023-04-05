"""
Created on Tue Apr 16/11/2022

@author: Maxime Torre
"""
from re import I
import scipy
import numpy as np
import skimage.io as skio
from os.path import join
import scipy.ndimage as scnd
import skimage.filters as skf
from skimage import color
from skimage import filters

import skimage as sk
import skimage.color as skc
import skimage.data as skd
import matplotlib.pyplot as plt
from skimage import util 
from skimage.util import crop
from skimage import transform
from skimage.util import img_as_ubyte

## 1 - Image sketching -------------------------------------------------------------------------------------------

filename = r'1.jpg'
dirpath = r'/input' 
filepath = join(dirpath, filename)
print(filepath)

img = skio.imread(filepath)
img_3_resize = transform.rescale(img, scale = 0.25, multichannel = True)

fig, axes = plt.subplots(ncols=2,figsize=(8, 4))
axes[0].imshow(img)
axes[0].set_title('Based Image')
axes[1].imshow(img_3_resize)
axes[1].set_title('Resize image')
plt.show()

# Ouvrir chaque image et stocker la valeur moyenne des couleurs de l'image dans une liste ou l'indice correspond au numéro de l'image
taille_bloc = 64
nb_image_data_base = 5
L_color_img_data = []
for j in range (1,nb_image_data_base):
    filename_use = str(j)+'.jpg'
    filepath_use = join(dirpath, filename_use)
    img_use = skio.imread(filepath_use)
    img_use_resize = img_as_ubyte(transform.rescale(img_use, scale = 0.25, multichannel = True)) # float to utin8
    #print(filename_use)
    R = 0
    G = 0
    B = 0
    R_moy = 0
    G_moy = 0
    B_moy = 0
    for k in range(taille_bloc): # colonne
            for i in range(taille_bloc): # ligne
                #print("i = ", i,"k = ",k)
                R = R + img_use_resize[k][i][0]
                G = G + img_use_resize[k][i][1]
                B = B + img_use_resize[k][i][2]
    R_moy = R//(taille_bloc**2)
    G_moy = G//(taille_bloc**2)
    B_moy = B//(taille_bloc**2)
    L_color_img_data.append([R_moy, G_moy, B_moy])

filename_3 = r'Rainbow.jpg'
dirpath_3 = r'/Target_images'
filepath_3 = join(dirpath_3, filename_3)
print(filepath_3)

longueur = 1920
largeur = 1216
nb_bloc = (longueur*largeur)//(taille_bloc**2) # =570

img_2 = skio.imread(filepath_3)
img_3 = img_2

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
        #Regardons quelles images est la plus semblable
        epsilon = img_2[0][0]
        numero_img = 0
        for p in range(len(L_color_img_data)):
            diff_scale = [RGB_moy - RGB_moy_data_base for RGB_moy, RGB_moy_data_base in zip([R_moy, G_moy, B_moy], L_color_img_data[p])]
            diff =  [abs(ele) for ele in diff_scale]
            #diff = abs([R_moy, G_moy, B_moy] - L_color_img_data[p])
            if ((diff[0] < epsilon[0]) & (diff[1] < epsilon[1]) & (diff[2] < epsilon[2])):
                epsilon = diff
                numero_img = p
        # On a trouvé l'image, il faut recopier chaques pixels de l'image sur la nouvelle
        filename_use = str(numero_img+1)+'.jpg'
        filepath_use = join(dirpath, filename_use)
        img_use = skio.imread(filepath_use)
        img_use_resize = img_as_ubyte(transform.rescale(img_use, scale = 0.25, multichannel = True)) # float to utin8
        for k in range(taille_bloc): # colonne
            for i in range(taille_bloc): # ligne
                img_3[k + largeur_bloc*taille_bloc][i + longueur_bloc*taille_bloc] = img_use_resize[k][i]
print("End of job")

img_2 = skio.imread(filepath_3)

fig2, axes2 = plt.subplots(ncols=2,figsize=(8, 4))
axes2[0].imshow(img_2)
axes2[0].set_title('Based Image')
axes2[1].imshow(img_3)
axes2[1].set_title('4px*4px Bloc')

plt.show()
