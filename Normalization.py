import numpy as np
import math

class Normalization:
	"""Classe contenant des méthodes statiques contenant les différentes méthodes de normalisation et de scaling/scretching d'image
	"""
	
	@staticmethod
	def checkInterval(data: np.ndarray, minimun : float|None, maximum : float|None) -> tuple[float,float]:
		"""Méthode statique permettant de vérifier si une valeur minimun et maxiumum sont renseignées, si ce n'est pas le cas
		cela donne les valeurs maximum et miniumum de l'image de base

		Args:
			data (np.ndarray): image représenté sous un tableau 2d
			minimun (float | None): valeur minimum selectionnée pour normalisé
			maximum (float | None): valeur maximum selectionnée pour normalisé

		Returns:
			tuple[float,float]: retourne le minimum ou et le maximum de l'image si il n'y a pas de valeur définie sinon retourne la valeur entrer
		"""
		min,max = 0,0
		if minimun == None : min = np.min(data)
		else: min = minimun
		if maximum == None : max = np.max(data)
		else: max = maximum
		return min,max

	@staticmethod
	def linear(datas : np.ndarray, min : float|None = None, max : float|None = None) -> np.ndarray:
		"""Méthode statique appliquant une normalisation des valeurs entre 0 et 1 et un scaling linéaire sur les pixels d'une intervalle définit
		sur une image représenté sous un tableau 2d

		Args:
			datas (np.ndarray): image non normalisé représenté sous un tableau 2d
			min (float | None, optional): valeur minimum selectionnée pour normalisé,valeur par défaut à None
			max (float | None, optional): valeur maximum selectionnée pour normalisé.valeur par défaut à None

		Returns:
			np.ndarray: image représenté sous un tableau 2d normalisé avec un scaling linéaire sur l'intervalle séléctionnée
		"""
		data : np.ndarray = np.copy(datas)
		min,max = Normalization.checkInterval(data,min,max)
		data = np.clip(data, min, max)
		data : np.ndarray = (data - min) / (max - min)
		return data	

	@staticmethod
	def asinh(datas : np.ndarray, min: float|None =None, max: float|None =None, a : float = 0.5) -> np.ndarray: 
		"""Méthode statique appliquant une normalisation des valeurs entre 0 et 1 et un scaling de sinus hyperbolique inverse 
		sur les pixels d'une intervalle définit sur une image représenté sous un tableau 2d


		voir : https://docs.astropy.org/en/stable/api/astropy.visualization.AsinhStretch.html#astropy.visualization.AsinhStretch

		Args:
			datas (np.ndarray): image non normalisé représenté sous un tableau 2d
			min (float | None, optional): valeur minimum selectionnée pour normalisé,valeur par défaut à None
			max (float | None, optional): valeur maximum selectionnée pour normalisé,valeur par défaut à None
			a (float, optional): valeur d'un comportement linéaire à un comportement logarithmique sur une intervalle normalisé(courbure), valeur par défaut à 0.5.

		Returns:
			np.ndarray: image représenté sous un tableau 2d normalisé avec un scaling de sinus hyperbolique inverse sur l'intervalle séléctionnée
		"""
		data : np.ndarray = np.copy(datas)
		data : np.ndarray = Normalization.linear(data,min,max)
		min,max = Normalization.checkInterval(data,min,max)
		data : np.ndarray = np.clip(data, min, max)
		data : np.ndarray = (np.arcsinh(data/a)/np.arcsinh(1/a))
		return data

	@staticmethod
	def sqrt(datas : np.ndarray, min: float|None =None, max: float|None =None) -> np.ndarray:
		"""Méthode statique appliquant une normalisation des valeurs entre 0 et 1 et un scaling racine carré 
		sur les pixels d'une intervalle définit sur une image représenté sous un tableau 2d

		voir : https://docs.astropy.org/en/stable/api/astropy.visualization.SqrtStretch.html#astropy.visualization.SqrtStretch

		Args:
			datas (np.ndarray): image non normalisé représenté sous un tableau 2d
			min (float | None, optional): valeur minimum selectionnée pour normalisé,valeur par défaut à None
			max (float | None, optional): valeur maximum selectionnée pour normalisé,valeur par défaut à None

		Returns:
			np.ndarray: image représenté sous un tableau 2d normalisé avec un scaling racine carré sur l'intervalle séléctionnée
		"""
		data : np.ndarray = np.copy(datas)
		min,max = Normalization.checkInterval(data,min,max)
		data : np.ndarray = np.clip(data, min, max)
		data : np.ndarray = data - min
		data : np.ndarray = np.where(data<0,0,data)
		data : np.ndarray = (np.sqrt(data) / math.sqrt(max - min))
		return data
	
	@staticmethod
	def histeq(datas : np.ndarray, min: float|None =None, max: float|None =None, bins : int = 256) -> np.ndarray:
		"""Méthode statique appliquant une normalisation des valeurs entre 0 et 1 et un scaling avec de l'equalisation d'histogramme donnant les 
		fréquences cummulées pour élargir le contraste de l'image et en interpolant les valeurs manquantes tout ceci
		sur les pixels d'une intervalle définit sur une image représenté sous un tableau 2d


		voir : https://docs.astropy.org/en/stable/api/astropy.visualization.HistEqStretch.html#astropy.visualization.HistEqStretch
			   https://en.wikipedia.org/wiki/Histogram_equalization

		Args:
			datas (np.ndarray): image non normalisé représenté sous un tableau 2d
			min (float | None, optional): valeur minimum selectionnée pour normalisé,valeur par défaut à None
			max (float | None, optional): valeur maximum selectionnée pour normalisé,valeur par défaut à None
			bins (int, optional): nombre de valeur x de l'histogramme, valeur par défaut à 256.

		Returns:
			np.ndarray: image représenté sous un tableau 2d normalisé avec un scaling d'equalisation d'histogramme sur l'intervalle séléctionnée
		"""
		data : np.ndarray = np.copy(datas)
		data : np.ndarray = Normalization.linear(data,min,max)
		min,max = Normalization.checkInterval(data,min,max)
		data : np.ndarray = np.clip(data, min, max)
		histo, histobins = np.histogram(data.flatten(), bins=bins, range=(0.0,1.0), density=True)
		cumulate : np.ndarray = np.cumsum(histo)
		cumulate : np.ndarray = cumulate / np.max(cumulate)
		interpolation : np.ndarray = np.interp(data.flatten(), histobins[:-1], cumulate)
		return np.reshape(interpolation,data.shape)

	@staticmethod
	def dummyRGB(datas : np.ndarray) -> np.ndarray:
		"""Méthode statique appliquant une normalisation des valeurs entre 0 et 255
		sur les pixels d'une intervalle définit sur une image représenté sous un tableau 2d 
		permettant de convertir en faux rgb (car il n'y a qu'une seule valeur et non 3) pour les valeurs des pixels de l'image

		Args:
			datas (np.ndarray): image non normalisé représenté sous un tableau 2d

		Returns:
			np.ndarray: image représenté sous un tableau 2d normalisé entre 0 et 255 pour un rgb factice 
		"""
		data : np.ndarray = np.copy(datas)
		data : np.ndarray = Normalization.linear(data)
		data = (255*data).astype(np.uint8)
		return data

	@staticmethod
	def blackWhiteLevelDummy(datas : np.ndarray) -> np.ndarray:
		"""Méthode statique appliquant une normalisation des valeurs 0 et 1, (0 -> blanc et 1 -> noir)
		sur les pixels d'une intervalle définit sur une image représenté sous un tableau 2d donnant une image tout en noir et blanc

		Args:
			datas (np.ndarray): image non normalisé représenté sous un tableau 2d

		Returns:
			np.ndarray: image en noir et blanc représenté sous un tableau 2d normalisé des valeurs 0 et 1 (0 -> blanc et 1 -> noir)
		"""
		data : np.ndarray = np.copy(datas)
		max : int = 1
		min : int = 0
		data : np.ndarray = np.clip(data, min, max)
		return data