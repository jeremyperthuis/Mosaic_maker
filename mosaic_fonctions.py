import os, sys
from PIL import Image
from math import *

#Module de fonctions pour mosaic_generator.py 

###############################################

# Verifie la taille des images sources et indique celles
#  dont les valeurs sont differentes

# dirpath : chemin du dossier des images (string)
# imgliste : liste des noms des images

# renvoi le nombre de fichiers non conformes

def TestDimensionImages(dirpath,imgliste):
	
	im=Image.open(dirpath+"/"+str(imgliste[0]))
	print">>> Dimensions images sources : "+ str(im.size)+"\n"
	compteur=0
	i=1
	while i<len(imgliste) :
		temp = Image.open(dirpath+"/"+str(imgliste[i]))
		if im.size != temp.size  :
			print " Warning ! image : "+str(imgliste[i])+" -> "+ str(temp.size)
			i+=1
			compteur+=1
		else :
			i+=1
	
	return compteur

###############################################

# Propose different choix de proportions pour l'image de sortie
# Calcul le nombre d'image en hauteur et largeur

# 	imgliste : liste des noms des images	

def Choix_Proportions(imgliste):
	
	print"\n\n 1 : 1/1"
	#print" 2 : 4/3"
	#print" 3 : 16/9"
	arg = raw_input("Choisir la proportion de l'image finale : ")

	#Proportion : carre
	if arg == "1" :
		racine = sqrt(len(imgliste))
		if racine == int(racine) :#si racine est un entier
			grid = [int(racine),int(racine)]
			print ">>> Creation d un carre de "+ str(int(grid[0])) + " images de cote"
			
		else : #sinon on arrondi au superieur
			res=ceil(sqrt(len(imgliste)))
			grid =[res,res]
			print ">>> Creation d un carre de "+ str(int(grid[0])) + " images de cote"
			
	return grid	
			
			
			
			
			

