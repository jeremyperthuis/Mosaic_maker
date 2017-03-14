import os, sys
from PIL import Image
from math import *
from mosaic_fonctions import *


print"******************************************************************"
print"                           PERTHUISOFT"
print"    _  _ ____ ____ ____ _ ____    _  _ ____ _  _ ____ ____ "
print"    |\/| |  | [__  |__| | |       |\/| |__| |_/  |___ |__/ "
print"    |  | |__| ___] |  | | |___    |  | |  | | \_ |___ |  \  v 1.0\n\n"
print"******************************************************************\n"


path = raw_input("Saisir le chemin du dossier d'images : ")
imgliste= os.listdir(path)
print "\n\n>>> Nombre de fichiers trouves : "+str(len(imgliste))

TestDimensionImages(path,imgliste)	


grid = Choix_Proportions(imgliste)

new_image = Image.new('RGB', (int(grid[0])*70, int(grid[1])*70))

x=0
y=0

for file in imgliste :
	adr = path+"/"+str(file)
	image_courrante= Image.open(adr)
	print adr
	new_image.paste(image_courrante,(x,y))
	x+=70
	if x == grid[0]*70 :
		x = 0
		y +=70

nom = raw_input("Saisir un nom pour sauvegarder l'image : ")+".jpg"	
new_image.save(nom)
print ("\nImage Sauvegardee !")
