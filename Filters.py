from Calculation import *
from Normalization import *
import numpy as np

class Filters:
	"""Classe contenant des méthodes statiques contenant les différentes méthodes de filtrage sur une image
	"""
	
	@staticmethod
	def createEmptyImage(image : np.ndarray) -> np.ndarray:
		"""Méthode statique permettant de créer un tableau 2d représentant une image vide

		Args:
			image (np.ndarray): image de base représenté sous un tableau 2d

		Returns:
			np.ndarray: image vide représenté sous un tableau 2d
		"""
		return(np.zeros(shape=image.shape))
	
	@staticmethod
	def removeOutletMedian(liste : list[float], precision : float = 1.5) -> list[float]:
		"""Méthode statique permettant de remplacer les valeurs abérantes par la médiane, d'une liste de nombre
		en fonction de l'écart/dispersion autour de la médiane de Q1 et de Q3 avec l'écart interquartile

		Args:
			liste (list[float]): liste de nombre non triée
			precision (float, optional):IQR précision de la mesure de dispersion, valeur par défaut à 1.5.

		Returns:
			list[float]: liste de nombre avec le remplacement des valeurs abérantes par la médiane
		"""
		val : tuple[float,float,float] = Calculation.findQ1Q3Value(liste)
		ecart : float = (val[2]-val[0])*precision
		new : list[float] = []
		for v in liste:
			if v >= (val[0]-ecart) and v <= (val[2]+ecart):
				new.append(v)
			else:
				new.append(val[1])  
		return new

	@staticmethod
	def removeOutletAvg(liste : list[float], precision : float =1.5) -> list[float]:
		"""Méthode statique permettant de remplacer les valeurs abérantes par la moyenne, d'une liste de nombre
		en fonction de l'écart/dispersion autour de la médiane de Q1 et de Q3 avec l'écart interquartile

		Args:
			liste (list[float]): liste de nombre non triée
			precision (float, optional):IQR précision de la mesure de dispersion, valeur par défaut à 1.5.

		Returns:
			list[float]: liste de nombre avec le remplacement des valeurs abérantes par la moyenne
		"""
		val : tuple[float,float,float]= Calculation.findQ1Q3Value(liste)
		ecart : float = (val[2]-val[0])*precision
		new : list[float] = []
		avg : float = np.mean(val)
		for v in liste:
			if v >= (val[0]-ecart) and v <= (val[2]+ecart):
				new.append(v)
			else:
				new.append(avg)  
		return new

	@staticmethod
	def removeOutletSigma(liste : list[float], precision : float =5) -> list[float]:
		"""Méthode statique permettant de remplacer les valeurs abérantes par l'écart et la dispersion de la médiane, d'une liste de nombre
		en fonction de l'écart/dispersion autour de la médiane de Q1 et de Q3 sans l'écart interquartile

		Args:
			liste (list[float]): liste de nombre non triée
			precision (float, optional):IQR précision de la mesure de dispersion, valeur par défaut à 5.

		Returns:
			list[float]: liste de nombre avec le remplacement des valeurs abérantes par l'écart et la dispersion de la médiane
		"""
		val : tuple[float,float,float] = Calculation.findQ1Q3Value(liste)
		ecart : float = (val[2]-val[0])
		new : list[float] = []
		for v in liste:
			if v >= (val[0]-ecart) and v <= (val[2]+ecart):
				new.append(v)
			else:
				new.append(val[1]+precision*ecart)  
		return new

	@staticmethod
	def sigmaOutletRemover(data : list, précision : float = 5) -> list:
		"""Méthode statique permettant de retirer les valeurs abérantes de chaque image d'une liste comportant plusieurs images 
		et de remplacer les valeurs abérantes par l'écart et la dispersion de la médiane en fonction de l'écart/dispersion 
		autour de la médiane de Q1 et de Q3 avec l'écart interquartile

		Voir méthode : removeOutletSigma
		Args:
			data (list): liste comportant plusieurs images
			precision (float, optional): IQR précision de la mesure de dispersion, valeur par défaut à 1.5.

		Returns:
			list:  liste comportant plusieurs images avec le remplacement des valeurs abérantes par l'écart et la dispersion de la médiane pour chaque image
		"""
		image_out : list = []
		liste : np.ndarray = np.copy(data)
		for i in range(len(liste)):
			value : list = []
			for y in range(len(liste[i])):
				for z in range(len(liste[i][y])):
					value.append(liste[i][y][z])
			value = Filters.removeOutletSigma(value,précision)
			counter : int= 0        
			for y in range(len(liste[i])):
				for z in range(len(liste[i][y])):
					liste[i][y][z] = value[counter]
					counter+=1
			image_out.append(liste[i])
		return image_out

	@staticmethod
	def medianOutletRemover(data : list, precision : float = 1.5) -> list:
		"""Méthode statique permettant de retirer les valeurs abérantes de chaque image d'une liste comportant plusieurs images 
		et de remplacer les valeurs abérantes par la médiane en fonction de l'écart/dispersion 
		autour de la médiane de Q1 et de Q3 avec l'écart interquartile

		Voir méthode : removeOutletMedian
		Args:
			data (list): liste comportant plusieurs images
			precision (float, optional): IQR précision de la mesure de dispersion, valeur par défaut à 1.5.

		Returns:
			list:  liste comportant plusieurs images avec le remplacement des valeurs abérantes par la médiane pour chaque image
		"""
		image_out : list =[]
		liste : np.ndarray = np.copy(data)
		for i in range(len(liste)):
			value : list = []
			for y in range(len(liste[i])):
				for z in range(len(liste[i][y])):
					value.append(liste[i][y][z])
			value = Filters.removeOutletMedian(value,precision)
			counter : int = 0        
			for y in range(len(liste[i])):
				for z in range(len(liste[i][y])):
					liste[i][y][z] = value[counter]
					counter+=1
			image_out.append(liste[i])
		return image_out

	@staticmethod
	def meanOutletRemover(data : list, precision : float = 1.5) :
		"""Méthode statique permettant de retirer les valeurs abérantes de chaque image d'une liste comportant plusieurs images 
		et de remplacer les valeurs abérantes par la moyenne en fonction de l'écart/dispersion 
		autour de la médiane de Q1 et de Q3 avec l'écart interquartile

		Voir méthode : removeOutletAvg
		Args:
			data (list): liste comportant plusieurs images
			precision (float, optional): IQR précision de la mesure de dispersion, valeur par défaut à 1.5.

		Returns:
			list:  liste comportant plusieurs images avec le remplacement des valeurs abérantes par la moyenne pour chaque image
		"""
		image_out : list =[]
		liste : np.ndarray = np.copy(data)
		for i in range(len(liste)):
			value : list = []
			for y in range(len(liste[i])):
				for z in range(len(liste[i][y])):
					value.append(liste[i][y][z])
			value = Filters.removeOutletAvg(value,precision)
			counter : int = 0        
			for y in range(len(liste[i])):
				for z in range(len(liste[i][y])):
					liste[i][y][z] = value[counter]
					counter+=1
			image_out.append(liste[i])
		return image_out
	
	@staticmethod
	def checkPixel(data: np.ndarray,i: int,y: int):
		"""Méthode statique permettant d'obtenir un pixel à une position x y en vérifiant
		si la position du pixel est compris dans l'image

		Args:
			data (np.ndarray): image représenté sous un tableau 2d
			i (int): position du pixel en x
			y (int): position du pixel en y

		Returns:
			float/np.nan: si les coordonnées sont valides cela retourne la valeur pixel sinon cela retourne nan
		"""
		if i >= 0 and i < len(data) and (y >= 0 and y < len(data[0])):
			return data[i][y]
		return np.nan

	@staticmethod
	def checkLimit(data: np.ndarray,i:int,y:int) -> bool:
		"""Méthode statique permettant de vérifier si un pixel à une position x y
		est compris dans l'image

		Args:
			data (np.ndarray): image représenté sous un tableau 2d
			i (int): position du pixel en x
			y (int): position du pixel en y

		Returns:
			bool: vrai si les coordonnées du pixel son valide sinon faux
		"""
		if i >= 0 and i < len(data) and (y >= 0 and y < len(data[0])):
			return True
		return False
		
	@staticmethod
	def median_filter(data: np.ndarray, size : int = 3,iterations : int = 1) -> np.ndarray:
		"""Méthode statique permettant de donner une image filtrer de chaque pixel en les remplaçants par 
		la médiane de chaque pixel voisin à un diamètre choisi 

		Args:
			data (_type_): image représenté sous un tableau 2d
			size (int, optional): Diametre local des pixels voisins,valeur par défaut à 3.
			iterations (int, optional): nombre d'iterations du filtre. valeur par défaut à 1.

		Returns:
			_type_: image représenté sous un tableau 2d filtrer
		"""
		img : np.ndarray = Filters.createEmptyImage(data)
		for nb in range(iterations):
			for i in range(len(data)):
				for j in range(len(data[0])):
					members = []
					for k in range(-(size//2),(size//2)+1):
						for y in range(-(size//2),(size//2)+1):
							members.append(Filters.checkPixel(data,i+k,j+y))
					members = np.array(members)
					members = members[np.logical_not(np.isnan(members))]
					members = np.sort(members)
					img[i][j] = np.median(members)
			data = img
		return img

	@staticmethod
	def mean_filter(data : np.ndarray, size : int = 3, iterations : int = 1) -> np.ndarray:
		"""Méthode statique permettant de donner une image filtrer de chaque pixel en les remplaçants par 
		la moyenne de chaque pixel voisin à un diamètre choisi 

		Args:
			data (_type_): image représenté sous un tableau 2d
			size (int, optional): Diametre local des pixels voisins,valeur par défaut à 3.
			iterations (int, optional): nombre d'iterations du filtre. valeur par défaut à 1.

		Returns:
			_type_: image représenté sous un tableau 2d filtrer
		"""
		img : np.ndarray = Filters.createEmptyImage(data)
		for nb in range(iterations):
			for i in range(len(data)):
				for j in range(len(data[0])):
					members = []
					for k in range(-(size//2),(size//2)+1):
						for y in range(-(size//2),(size//2)+1):
							members.append(Filters.checkPixel(data,i+k,j+y))
					members = np.array(members)
					members = members[np.logical_not(np.isnan(members))]
					img[i][j] = np.mean(members)
			data = img
		return img

	@staticmethod
	def convolution(data : np.ndarray, kernel : np.ndarray) -> np.ndarray:
		"""Méthode statique permettant d'appliquer une matrice de convolution sur un chaque pixel d'une image représenter via un tableau 2d
		La matrice s'applique en fonction des voisins situer en fonction de la taille/diametre de la matrice directements sur les pixels de l'image

		Args:
			data (np.ndarray): image représenté sous un tableau 2d
			kernel (np.ndarray): matrice de convolution

		Returns:
			np.ndarray: image représenté sous un tableau 2d avec la matrice de convolution appliquer sur les pixels
		"""
		img : np.ndarray = Filters.createEmptyImage(data)
		size : int = len(kernel)
		for i in range(len(data)):
			for j in range(len(data[0])):
				val : float = 0
				for k in range(-(size//2),(size//2)+1):
					for y in range(-(size//2),(size//2)+1):
						if (Filters.checkLimit(data,i+k,j+y)):
							val = val+(data[i+k][j+y]*kernel[k+(size//2)][y+(size//2)])
				img[i][j] = val
		return img

	@staticmethod
	def butterworth_lowpass_filter(datas : np.ndarray ,cut : int = 100,n: int =1) -> np.ndarray:
		"""Méthode statique permettant d'appliquer une image représenter via un tableau 2d un filtre passe bas de butterworth
		en convertisant notre image en fréquence via la transformation de fourier et en appliquant le filtre passe bas de butterworth 
		et de la reconvertisant en pixel

		info : https://en.wikipedia.org/wiki/Butterworth_filter

		Args:
			datas (np.ndarray): image représenté sous un tableau 2d
			cut (int, optional): frequence de découpage, Defaults to 100.
			n (int, optional): ordre du filtre, de combien va être couper le filtre. Defaults to 1.

		Returns:
			np.ndarray: image représenté sous un tableau 2d avec les fréquences hautes filtrer 
		"""
		img : np.ndarray = Filters.createEmptyImage(datas)
		data : np.ndarray = np.copy(datas)
		data : np.ndarray = np.fft.fft2(data)
		data = np.fft.fftshift(data)
		for i in range(len(img)):
			for y in range(len(img[0])):
				d = np.sqrt(((i-len(img))/2)**2 + ((y-len(img[0]))/2)**2)
				img[i][y] = (1/(1+(d/cut)**(2*n)))
		new : np.ndarray = data*img
		new : np.ndarray = np.fft.ifftshift(new)
		return np.abs(np.fft.ifft2(new))

	@staticmethod
	def butterworth_highpass_filter(datas: np.ndarray,cut : int = 100,n : int =1):
		"""Méthode statique permettant d'appliquer une image représenter via un tableau 2d un filtre passe haut de butterworth
		en convertisant notre image en fréquence via la transformation de fourier et en appliquant le filtre passe haut de butterworth 
		et de la reconvertisant en pixel

		info : https://en.wikipedia.org/wiki/Butterworth_filter

		Args:
			datas (np.ndarray): image représenté sous un tableau 2d
			cut (int, optional): frequence de découpage, Defaults to 100.
			n (int, optional): ordre du filtre, de combien va être couper le filtre. Defaults to 1.

		Returns:
			np.ndarray: image représenté sous un tableau 2d avec les fréquences basses filtrer 
		"""
		img : np.ndarray = Filters.createEmptyImage(datas)
		data : np.ndarray = np.copy(datas)
		data : np.ndarray = np.fft.fft2(data)
		data = np.fft.fftshift(data)
		for i in range(len(img)):
			for y in range(len(img[0])):
				d = np.sqrt(((i-len(img))/2)**2 + ((y-len(img[0]))/2)**2)
				img[i][y] = (1/(1+(cut/d)**(2*n)))
		new : np.ndarray = data*img
		new : np.ndarray = np.fft.ifftshift(new)
		return np.abs(np.fft.ifft2(new))

	@staticmethod
	def gaussian_filter(datas : np.ndarray ,sigma : float = 1, size : int = 3) -> np.ndarray:
		"""Méthode statique permettant d'appliquer une matrice de convolution gaussienne donnant un effet de flou 
		sur un chaque pixel d'une image représenter via un tableau 2d

		voir : convolution
			   gauss_kernel_normalize

		Args:
			datas (np.ndarray): image représenté sous un tableau 2d
			sigma (float, optional): écart type, valeur par défaut à 1
			size (int, optional): taille de la matrice,valeur par défaut à 3

		Returns:
			np.ndarray: image représenté sous un tableau 2d avec un filtre gaussien
		"""
		
		data : np.ndarray = np.copy(datas)
		gauss : np.ndarray = Calculation.gauss_kernel_normalize(size,sigma)
		data : np.ndarray = Filters.convolution(data,gauss)
		return data

	@staticmethod
	def gaussian_highpass_filter(datas : np.ndarray ,sigma : float = 2, size : int = 5) -> np.ndarray:
		"""Méthode statique permettant d'appliquer un filtre passe haut gaussien qui applique une matrice de convolution gaussienne 
		sur un chaque pixel d'une image représenter via un tableau 2d et la soustrait à l'image de base fessant un high = data-low(gauss)

		voir : gaussian_filter

		Args:
			datas (np.ndarray): image représenté sous un tableau 2d
			sigma (float, optional): écart type, valeur par défaut à 2
			size (int, optional): taille de la matrice,valeur par défaut à 5

		Returns:
			np.ndarray: image représenté sous un tableau 2d avec un filtre passe haut gaussien
		"""
		data : np.ndarray = np.copy(datas)
		low : np.ndarray = Filters.gaussian_filter(data,sigma,size)
		return (np.subtract(data,low))

	@staticmethod
	def sobel_filter(datas : np.ndarray ,absolute: bool =True) -> np.ndarray:
		"""Méthode statique permettant d'appliquer une matrice de convolution de sobel en vertical et en horizontal donnant un effet de accentuation 
		des bords des objets de l'image et s'appliquant sur un chaque pixel d'une image représenter via un tableau 2d

		voir : convolution

		Args:
			datas (np.ndarray): image représenté sous un tableau 2d
			absolute (float, optional): si vrai cela retourne la valeur absolue de l'image sinon l'image de base avec le filtre de sobel

		Returns:
			np.ndarray: image représenté sous un tableau 2d avec un filtre de sobel en absolue si aboslute et vrai sinon l'image de base avec le filtre de sobel
		"""
		data : np.ndarray = np.copy(datas)
		sobelX : np.ndarray = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
		sobelX : np.ndarray = sobelX # /np.sum(sobelX)
		sobelY : np.ndarray = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
		sobelY : np.ndarray = sobelY #/np.sum(sobelY)
		covolveSobelX : np.ndarray = Filters.convolution(data,sobelX)
		covolveSobelY : np.ndarray = Filters.convolution(data, sobelY)
		if absolute: 
			return np.abs((covolveSobelX + covolveSobelY))
		else: 
			return (covolveSobelX + covolveSobelY)
	
	@staticmethod
	def bilateral_filter(data : np.ndarray, size : int = 3, sigmaC : float = 0.5, sigmaS  : float = 20) -> np.ndarray:
		"""Méthode statique permettant d'appliquer un filtre bilateral sur une image donnant un effet de flou/adoucicement
		sur un chaque pixel d'une image représenter via un tableau 2d via la valeur de la distribution gaussienne et la distance
		entre les points dans le diametre de voisin choisi permettant d'avoir une distribution plus équitable qu'un filtre gaussien classique

		voir : https://en.wikipedia.org/wiki/Bilateral_filter

		Args:
			data (np.ndarray): image représenté sous un tableau 2d
			size (int, optional): diametre local des pixels voisins, valeur par défaut à 3.
			sigmaC (float, optional): valeur du sigma dans l'espace de couleur/gris, représente le mélange des couleurs/gris, valeur par défaut à 0.5.
			sigmaS (float, optional): valeur du sigma dans l'espace de coordonnées, représente l'influence des pixels éloignées, valeur par défaut à 20.

		Returns:
			np.ndarray: image représenté sous un tableau 2d avec un filtre bilateral
		"""
		img : np.ndarray = Filters.createEmptyImage(data)
		for i in range(len(data)):
			for j in range(len(data[0])):
				wpTotal : float = 0
				filtrer : float = 0
				for k in range(-(size//2),(size//2)+1):
					for y in range(-(size//2),(size//2)+1):
						index1 = ((i+k)%(len(data)))
						index2 = ((j+y)%(len(data[0])))
						gr : float = Calculation.gauss(data[index1][index2] - data[i][j],0, sigmaC)
						gs : float = Calculation.gauss(Calculation.distance(index1, index2, i, j),0, sigmaS)
						wp : float = gr * gs
						filtrer += (data[index1][index2] * wp)
						wpTotal += wp
				if wpTotal != 0:
					filtrer = filtrer // wpTotal
				img[i][j] = np.round(filtrer)
		return img