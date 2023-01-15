import numpy as np
import math

class Calculation:
    """Classe contenant des méthodes statiques contenant les différentes méthodes réalisant des calculs mathématiques
    """
    @staticmethod
    def findMedianNumber(listee : list[float]) -> float:
        """Méthode statique permettant de trouver le nombre médian d'une liste de nombre non triée

        Args:
            liste (list[float]): liste de nombre non triée

        Returns:
            float: médianne de la liste
        """
        liste : np.ndarray = np.array(listee)
        sortedList : np.ndarray = np.sort(liste)
        half : float = len(liste)//2
        if (len(sortedList) % 2 != 1):
            return float(float(sortedList[half - 1]) + float(sortedList[half])) / 2
        return sortedList[half]

    @staticmethod
    def findMedianInfo(liste : list[float]) -> tuple[list[float],list[int],float]:
        """Méthode statique permettant d'obtenir les informations sur le nombre médian 
        avec la position, le nombre médian et la liste triée, d'une liste de nombre non triée

        Args:
            liste (list[float]): liste de nombre non triée

        Returns:
            tuple[list[float],list[int],float]: tuple contenant la liste triée,indices de la position du nombre médian, nombre médian
        """
        sortedList : list[float] = sorted(liste)
        indices : list[int] = []
        half : float = len(liste)//2
        if (len(sortedList) % 2 != 1):
            indices.append(half - 1);indices.append(half)
            return (sortedList,indices, ((sortedList[half - 1] + sortedList[half]) / 2))
        indices.append(half)
        return (sortedList, indices,sortedList[half])

    @staticmethod
    def findQ1Q3List(liste : list[float]) -> tuple[list[float],list[float]]:
        """Méthode statique permettant de retrouver en fonction d'une liste non triée les listes Q1 et Q3
        triée découpé en fonction de la médianne

        Args:
            liste (list[float]): liste de nombre non triée

        Returns:
            tuple[list[float],list[float]]: tuple contenant la liste Q1 et liste Q3 triée
        """
        median = Calculation.findMedianInfo(liste)
        indices : list[int] = median[1]
        listeRange : list[float] = median[0]
        if (len(indices) > 1):
            return (listeRange[:(indices[0]+1)], listeRange[indices[1]:])
        return (listeRange[:(indices[0])], listeRange[(indices[0]+1):])

    @staticmethod
    def findQ1Q3Value(list: list[float]) -> tuple[float,float,float]:
        """Méthode statique permettant de trouver en fonction d'une listes non triée la médianne et le nombre médian
        de Q1 et Q3

        Args:
            list (list[float]): liste de nombre non triée

        Returns:
            tuple[float,float,float]: tuple contenant la médiane de Q1,de la liste et Q3
        """
        val = Calculation.findQ1Q3List(list)
        return(Calculation.findMedianNumber((val[0])),
                Calculation.findMedianNumber(list),
                Calculation.findMedianNumber(val[1]))
    

    @staticmethod
    def gauss(x : float,y : float, sigma : float) -> float :
        """Méthode statique permettant de calculer la fonction gaussienne 2D
        info : https://en.wikipedia.org/wiki/Gaussian_function

        Args:
            x (float): valeur en x 
            y (float): valeur en y/éspérance
            sigma (float): écart type

        Returns:
            float: valeur de la distribution gaussienne
        """
        return (1/(2*math.pi*(sigma**2)))*math.exp(-(((x**2) + (y**2))/(2*(sigma**2))))
    
    @staticmethod 
    def gauss_kernel_normalize(size : int = 3 ,sigma : float = 1) -> np.ndarray:
        """Méthode statique permettant de trouvé la matrice de convolution gaussienne

        Args:
            size (int,optional): taille de la matrice,valeur par défaut à 3
            sigma (float, optional): écart type, valeur par défaut à 1

        Returns:
            np.ndarray: matrice de convolution gaussienne normalisé
        """
        mean : float = size/2
        kernel : np.ndarray = np.zeros((size,size))
        for i in range(-(size//2), (size//2)+1):
            for j in range(-(size//2), (size//2)+1):
                kernel[i+(size//2)][j+(size//2)] = Calculation.gauss(i,j,sigma)
        return kernel/np.sum(kernel)

    @staticmethod
    def distance(x1:float,y1:float,x2:float,y2:float) -> float:
        """Méthode statique permettant de trouvé la distance entre 2 points

        Args:
            x1 (float): valeur en x du 1er point
            y1 (float): valeur en y du 1er point
            x2 (float): valeur en x du 2eme point
            y2 (float): valeur en y du 2eme point

        Returns:
            float: distance entre les 2 points
        """
        return math.sqrt(np.abs((x1-x2)**2-(y1-y2)**2))