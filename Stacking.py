import numpy as np
from Calculation import *
from Filters import *

class Stacking:
    """Classe contenant des méthodes statiques contenant les différentes méthodes de stacking de plusieurs images
    """

    @staticmethod
    def createEmptyImage(image) -> np.ndarray:
        """Méthode statique permettant de créer un tableau 2d représentant une image vide

		Args:
			image (np.ndarray): image de base représenté sous un tableau 2d

		Returns:
			np.ndarray: image vide représenté sous un tableau 2d
		"""
        return(np.zeros(shape=image.shape))
    
    @staticmethod
    def median(list_median: list) -> np.ndarray:
        """Méthode statique réalisant un assemblage de plusieurs images en déterminant la mediane de chaque pixel des
        différentes images de représentée par un tableau 2d

        Args:
            list_median (list): liste comportant plusieurs images

        Returns:
            np.ndarray: image représentée par un tableau 2d combinée par mediane pour chaque pixels
        """
        final_image = Stacking.createEmptyImage(list_median[0])
        for i in range(len(final_image)):
            for j in range(len(final_image[i])):
                valeur : list[float] = []
                for k in list_median:
                    valeur.append(k[i][j])
                final_image[i][j] = Calculation.findMedianNumber(valeur)
        return final_image

    @staticmethod
    def mean(list_moyenne: list) -> np.ndarray:
        """Méthode statique réalisant un assemblage de plusieurs images en realisant la moyenne de chaque pixel des
        différentes images de représentée par un tableau 2d

        Args:
            list_moyenne (list): liste comportant plusieurs images

        Returns:
            np.ndarray: image représentée par un tableau 2d combinée par moyenne pour chaque pixels
        """
        final_image : np.ndarray = Stacking.createEmptyImage(list_moyenne[0])
        for i in range(len(final_image)):
            for j in range(len(final_image[i])):
                somme : float = 0
                for k in list_moyenne:
                    somme += k[i][j]
                final_image[i][j] = (somme/len(list_moyenne))
        return final_image

    @staticmethod
    def addition(list_addition: list) -> np.ndarray :
        """Méthode statique réalisant un assemblage de plusieurs images en additionnant les pixels de chaque images représentée par un
        tableau 2d

        Args:
            list_addition (list): liste comportant plusieurs images

        Returns:
            np.ndarray: image représentée par un tableau 2d combinée par addition 
        """
        final_image : np.ndarray = Stacking.createEmptyImage(list_addition[0])
        for i in range(len(final_image)):
            for j in range(len(final_image[i])):
                somme : float = 0
                for k in list_addition:
                    somme += k[i][j]
                final_image[i][j] = somme
        return final_image
    
    @staticmethod
    def sigmaOutlet(data, precision : float = 5) -> np.ndarray:
        """Méthode statique réalisant un assemblage par addition de plusieurs images en ajoutant chaque image avec leur valeurs
        abérantes filtrer par l'écart et la dispersion de la médiane pour les différentes images de représentée par un tableau 2d

        voir : sigmaOutletRemover

        Args:
            data (list): liste comportant plusieurs images
            precision (float, optional): IQR précision de la mesure de dispersion, valeur par défaut à 5.

        Returns:
            np.ndarray: image représentée par un tableau 2d combinée par addition des images filtrer de leur valeur abérante par l'écart et la dispersion de la médiane pour chaque pixels
        """
        final_images : list = Filters.sigmaOutletRemover(data,precision)
        return np.copy(Stacking.addition(final_images))
    
    @staticmethod
    def medianOutlet(data, precision : float = 1.5) -> np.ndarray:
        """Méthode statique réalisant un assemblage par addition de plusieurs images  en ajoutant chaque image avec leur valeurs
        abérantes filtrer par mediane pour les différentes images de représentée par un tableau 2d

        voir : medianOutletRemover

        Args:
            data (list): liste comportant plusieurs images
            precision (float, optional): IQR précision de la mesure de dispersion, valeur par défaut à 1.5.

        Returns:
            np.ndarray: image représentée par un tableau 2d combinée par addition des images filtrer de leur valeur abérante par mediane pour chaque pixels
        """
        final_images : list = Filters.medianOutletRemover(data,precision)
        return np.copy(Stacking.addition(final_images))

    @staticmethod
    def meanOutlet(data, precision : float = 1.5) -> np.ndarray:
        """Méthode statique réalisant un assemblage par addition de plusieurs images en ajoutant chaque image avec leur valeurs
        abérantes filtrer par moyenne pour les différentes images de représentée par un tableau 2d

        voir : meanOutletRemover

        Args:
            data (list): liste comportant plusieurs images
            precision (float, optional): IQR précision de la mesure de dispersion, valeur par défaut à 1.5.

        Returns:
            np.ndarray: image représentée par un tableau 2d combinée par addition des images filtrer de leur valeur abérante par moyenne pour chaque pixels
        """
        final_images : list = Filters.meanOutletRemover(data,precision)
        return np.copy(Stacking.addition(final_images))