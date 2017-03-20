import os, sys
from PIL import Image
from math import *

#Bibliotheque de fonctions pour mosaic_generator.py 

##############################################################################################

#  - Verifie la taille des images sources et indique celles
#    dont les valeurs sont differentes

#  - dirpath : chemin du dossier des images (string)
#  - imgliste : liste de noms des images sources

#  - Renvoi les dimension en pixel de la 1ere image lue  sous la forme d'une liste  (x,y)

def TestDimensionImages(dirpath,imgliste):
	
	im=Image.open(dirpath+"/"+str(imgliste[0]))
	dimensionsrc = im.size
	print">>> Dimensions images sources : "+ str(dimensionsrc)+"\n"
	
	i=1
	while i<len(imgliste) :
		temp = Image.open(dirpath+"/"+str(imgliste[i]))
		if im.size != temp.size  :
			print " Warning ! image : "+str(imgliste[i])+" -> "+ str(temp.size)
			i+=1
		else :
			i+=1
	
	return dimensionsrc

##############################################################################################

#  - Propose different choix de proportions pour l'image de sortie 

#  - imgliste : liste de nom des images sources

#  - Renvoi les valeurs de l'image de sortie sous la forme d'une liste (L,H)

def Choix_Proportions(imgliste):
	
	print"\n\n 1 : 1/1"
	print" 2 : valeurs perso"
	
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
	
	if arg == "2":
		Suggestion_Proportions(imgliste)
		L= input("nombre image longueur : ")
		H= input("nombre image hauteur : ")
		grid = [int(L),int(H)]
		
		
	return grid	

#################################################################################################

#  - Dans le cas d une proportion personnalisee, la fonction calcul toute les combinaisons possibles
#    pour obtenir une image de sortie sans espace perdu

def Suggestion_Proportions(imgliste):
	nbr = len(imgliste)
	L=nbr
	H=1
	print ">>>  Suggestion de proportions : " 
	while L>0:
		H=1
		while H<=nbr:
			temp = L*H
			if temp ==nbr:
				print "     >> "+str(L)+"x"+str(H)
			H+=1
		
		L-=1
	
			
#################################################################################################			
			
			

