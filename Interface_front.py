from PyQt6.QtCore import (QCoreApplication, QRect, QSize, Qt)
from PyQt6.QtWidgets import (QHBoxLayout, QCheckBox, QGridLayout, QPushButton, QSpinBox, QVBoxLayout, QWidget,QApplication, QLabel, QFileDialog, QComboBox, QSlider, QDoubleSpinBox)
from matplotlib.figure import Figure
from PyQt6.QtCore import pyqtSignal
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.visualization import make_lupton_rgb
from Stacking import *
from Stacking_front import Stacking_front
from os.path import expanduser
import glob
# Set up matplotlib
import matplotlib.pyplot as plt
from scipy.ndimage.interpolation import rotate


from astropy.io import fits
from astropy.utils.data import download_file
from matplotlib.colors import LogNorm

class Interface_front(QWidget):
    
    """Méthode permettant l'initialisation de notre interface d'application

    Args:
        self : Notre application
        folder : Le chemin vers nos fichiers
    """
    def __init__(self,folder):
        super().__init__()
        self.setWindowTitle("Logiciel d'édition profesionnel d'image")
        self.index = 0
        self.minimum = 0
        self.maximum = 0
        self.longueur = 0
        self.hauteur = 0
        self.rotation = 0
        self.nombre_image = 0
        self.valeurprecision = 1
        self.generationtype = "Somme"
        self.sousoptiontype = "Aucun"
        self.optiontypeselect = "Aucun"
        self.scalingvaleur = "Aucun"
        self.cmaptype = "gray"
        self.check = False
        self.rgbimage = False

        self.imagelist_image = []
        self.imagelist_hist = []
        self.moyenne = 0
        self.stddev = 0
        self.coordClick = []
        self.image_list = []
        self.image_list_fini = list[list[int]]

        self.label_3_min_text = QLabel()
        self.label_4_min_valeur = QLabel()

        self.label_5_max_text = QLabel()
        
        self.label_6_max_valeur = QLabel()

        self.label_7_moyenne_text = QLabel()
        self.label_8_moyenne_valeur = QLabel()

        self.label_9_stdev_text = QLabel()
        self.label_10_stdev_valeur = QLabel()

        self.label_11_statistiques_text = QLabel()


        self.label_13_width_text = QLabel()
        self.label_14_height_text = QLabel()

        self.label_15_width_valeur = QLabel()
        self.label_16_height_valeur = QLabel()
        

        self.scaling_text = QLabel()

        self.scalingintervale_text = QLabel()

        self.label_2_scalling = QComboBox()
    
        

        self.pushButton_20_actualiser = QPushButton()
        self.pushButton_21_enregister_png = QPushButton()
        self.pushButton_22_rotation = QPushButton()

        self.max = QDoubleSpinBox()
        self.min = QDoubleSpinBox()
        self.scalingmax_text = QLabel()
        self.scalingmax = QDoubleSpinBox()
        self.scalingmin_text = QLabel()
        self.scalingmin = QDoubleSpinBox()

        self.scalingintervale = QDoubleSpinBox()
        self.scalingintervale2 = QSpinBox()


        

        self.idplot = 1
        self.maxidplot = 4
        self.base_url = folder

        self.figure : Figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.figure.clear()
        self.plot(1)
        self.canvas.draw()

        self.figure2 : Figure = Figure()
        self.canvas2 = FigureCanvas(self.figure2)
        self.canvas2.figure.clear()
        self.plot(2)
        self.canvas2.draw()

        

        self.globalLayout : QHBoxLayout = QHBoxLayout()
        self.setLayout(self.globalLayout)
        self.horizontalLayoutWidget : QWidget = QWidget()
        self.globalLayout.addWidget(self.horizontalLayoutWidget)
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 1081, 1051))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_5 = QVBoxLayout()
        
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_3 = QVBoxLayout()


        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_8 = QHBoxLayout()

        self.verticalLayout = QVBoxLayout()

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.Ouvrirun = QPushButton(self.horizontalLayoutWidget)
        self.Ouvrirun.setObjectName(u"Ouvrirun")
        self.Ouvrirun.setStyleSheet(u"border: 0px solid #fff;\n"
        "background-color: #fff;\n"
        "border-bottom: 1px solid #009BFF;")

        self.horizontalLayout_5.addWidget(self.Ouvrirun)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"border: 0px solid #fff;\n"
        "background-color: #fff;\n"
        "border-bottom: 1px solid #009BFF;")

        self.horizontalLayout_5.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.canvas.setMaximumSize(QSize(16777215, 1050))
        self.canvas.setStyleSheet(u"background-color: #EEEEEE;")

        self.horizontalLayout_7.addWidget(self.canvas)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.horizontalLayout_3.addWidget(self.label)

        self.min.setObjectName(u"min")
        self.min.setMinimum(-1000000000)
        self.min.setMaximum(1000000000)

        self.horizontalLayout_3.addWidget(self.min)

        self.widget = QWidget(self.horizontalLayoutWidget)
        self.widget.setObjectName(u"widget")

        self.horizontalLayout_3.addWidget(self.widget)

        self.max.setObjectName(u"max")
        self.max.setMinimum(-1000000000)
        self.max.setMaximum(1000000000)

        self.horizontalLayout_3.addWidget(self.max)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.horizontalLayout_3.addWidget(self.label_2)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border-radius: 16px;\n"
        "background-color: #fff;\n"
        "border: 1px solid black;\n"
        "height: 25px;\n"
        "margin: 10px;")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.verticalLayout.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_22.addWidget(self.pushButton_21_enregister_png)
        self.horizontalLayout_22.addWidget(self.pushButton_22_rotation)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_900 = QHBoxLayout()
        self.horizontalLayout_900.setObjectName(u"horizontalLayout_900")
        self.horizontalLayout_900.setGeometry(QRect(0, 0, 781, 1000))
        self.canvas2.setStyleSheet(u"background-color: #EEEEEE;")

        self.horizontalLayout_900.addWidget(self.canvas2)


        self.verticalLayout.addLayout(self.horizontalLayout_900)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_2.setSpacing(2)
        self.widgetstacking2 = Stacking_front()

        self.verticalLayout_2.addWidget(self.widgetstacking2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_7.addLayout(self.verticalLayout_3)

        self.verticalLayout_3.addWidget(self.label_11_statistiques_text)
        self.label_11_statistiques_text.setMaximumSize(QSize(999999, 25))

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_4.addWidget(self.label_3_min_text, alignment=Qt.AlignmentFlag.AlignLeft)
        self.label_3_min_text.setFixedWidth(25)

        self.horizontalLayout_4.addWidget(self.label_4_min_valeur)
        self.label_4_min_valeur.setFixedWidth(50)
        self.horizontalLayout_6.addWidget(self.label_5_max_text, alignment=Qt.AlignmentFlag.AlignLeft)
        self.label_5_max_text.setFixedWidth(25)
        self.horizontalLayout_6.addWidget(self.label_6_max_valeur)
        self.label_6_max_valeur.setFixedWidth(50)

        self.horizontalLayout_4.addWidget(self.label_7_moyenne_text, alignment=Qt.AlignmentFlag.AlignLeft)
        self.label_7_moyenne_text.setMaximumSize(QSize(1000000, 25))
        self.horizontalLayout_4.addWidget(self.label_8_moyenne_valeur, alignment=Qt.AlignmentFlag.AlignRight)
        self.label_8_moyenne_valeur.setMaximumSize(QSize(1000000, 25))

        self.horizontalLayout_6.addWidget(self.label_9_stdev_text, alignment=Qt.AlignmentFlag.AlignLeft)
        self.label_9_stdev_text.setMaximumSize(QSize(1000000, 25))
        self.horizontalLayout_6.addWidget(self.label_10_stdev_valeur, alignment=Qt.AlignmentFlag.AlignRight)
        self.label_10_stdev_valeur.setMaximumSize(QSize(1000000, 25))


        self.horizontalLayout_8.addWidget(self.label_13_width_text, alignment=Qt.AlignmentFlag.AlignLeft)
        self.label_13_width_text.setMaximumSize(QSize(1000000, 25))
        self.horizontalLayout_8.addWidget(self.label_15_width_valeur, alignment=Qt.AlignmentFlag.AlignRight)
        self.label_15_width_valeur.setMaximumSize(QSize(1000000, 25))

        self.horizontalLayout_8.addWidget(self.label_14_height_text, alignment=Qt.AlignmentFlag.AlignLeft)
        self.label_14_height_text.setMaximumSize(QSize(1000000, 25))
        self.horizontalLayout_8.addWidget(self.label_16_height_valeur, alignment=Qt.AlignmentFlag.AlignRight)
        self.label_16_height_valeur.setMaximumSize(QSize(1000000, 25))


        self.horizontalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addWidget(self.scaling_text)
        self.scaling_text.setMaximumSize(QSize(999999, 25))
        self.verticalLayout_5.addWidget(self.label_2_scalling)
        self.label_2_scalling.setMaximumSize(QSize(999999, 25))
        self.label_2_scalling.addItems(['Aucun','Linear','Asinh','Sqrt','Histeq'])

        self.verticalLayout_5.addWidget(self.scalingmin_text)
        self.scalingmin_text.setMaximumSize(QSize(999999, 25))
        self.verticalLayout_5.addWidget(self.scalingmin)
        self.scalingmin.setMaximumSize(QSize(999999, 25))

        self.verticalLayout_5.addWidget(self.scalingmax_text)
        self.scalingmax_text.setMaximumSize(QSize(999999, 25))
        self.verticalLayout_5.addWidget(self.scalingmax)
        self.scalingmax.setMaximumSize(QSize(999999, 25))

        self.verticalLayout_5.addWidget(self.scalingintervale_text)
        self.scalingintervale_text.setMaximumSize(QSize(999999, 25))
        self.verticalLayout_5.addWidget(self.scalingintervale)
        self.scalingintervale.setMaximumSize(QSize(999999, 25))
        self.verticalLayout_5.addWidget(self.scalingintervale2)
        self.scalingintervale2.setMaximumSize(QSize(999999, 25))
        
        self.scalingmax_text.setVisible(False)
        self.scalingmax.setVisible(False)
        self.scalingmin_text.setVisible(False)
        self.scalingmin.setVisible(False)
        self.scalingintervale_text.setVisible(False)
        self.scalingintervale.setVisible(False)
        self.scalingintervale2.setVisible(False)

        self.verticalLayout_5.addWidget(self.pushButton_20_actualiser)
        self.min.setValue(self.minimum)
        self.max.setValue(self.maximum)

        self.label_4_min_valeur.setText(f"{self.minimum}")
        self.label_6_max_valeur.setText(f"{self.maximum}")
        self.retranslateUi()

        self.pushButton.clicked.connect(self.actualiser_stats_et_image)
        self.Ouvrirun.clicked.connect(self.openfolder)
        self.pushButton_2.clicked.connect(self.openfichier)
        self.widgetstacking2.optiontypeselect_con.connect(self.optiontypeselect_con)
        self.widgetstacking2.actualisersatking_con.connect(self.actualiserStaking)
        
        self.widgetstacking2.inputfrequence_con.connect(self.inputfrequence_con)
        self.widgetstacking2.inputordre_con.connect(self.inputordre_con)
        self.widgetstacking2.inputSigmaS_con.connect(self.inputSigmaS_con)
        self.widgetstacking2.inputsigma_con.connect(self.inputsigma_con)
        self.widgetstacking2.inputsigmaC_con.connect(self.inputsigmaC_con)
        self.widgetstacking2.inputprecision_con.connect(self.inputprecision_con)
        self.widgetstacking2.inputiteration_con.connect(self.inputiteration_con)
        self.widgetstacking2.inputabsolute_con.connect(self.inputabsolute_con)
        self.widgetstacking2.inputsize_con.connect(self.inputsize_con)
        self.widgetstacking2.selfgenerationtype_con.connect(self.inputsize_con)

        self.widgetstacking2.label_3_couleur_con.connect(self.label_3_couleur_con)
        self.widgetstacking2.combobox_3_con.connect(self.combobox_3_con)
        self.widgetstacking2.combobox_4_con.connect(self.combobox_4_con)
        self.widgetstacking2.combobox_5_con.connect(self.combobox_5_con)
        self.widgetstacking2.label_1_stacking_con.connect(self.label_1_stacking_con)
        self.widgetstacking2.convolutionmatrice_con.connect(self.emitconvolutionmatrice_con)
        self.widgetstacking2.slider_stacking_con.connect(self.inputprecision_con)

        self.pushButton_21_enregister_png.clicked.connect(self.EnregisterPng)
        self.pushButton_22_rotation.clicked.connect(self.rotation_matrice)

        self.label_2_scalling.currentIndexChanged.connect(self.changement_scaling)
        self.pushButton_20_actualiser.clicked.connect(self.actualiserScaling)
        self.inputfrequence = 0
        self.inputordre = 0
        self.inputSigmaS = 0
        self.inputsigma = 0
        self.inputsigmaC = 0
        self.inputprecision = 0.0
        self.inputiteration = 0
        self.inputabsolute = 0
        self.inputsize = 0
        self.convolutionmatrice = np.ndarray(shape=(3,3), dtype=float, order='F')
        # self.widgetstacking.setMaximumSize(QSize(999999, 500))
    def emitconvolutionmatrice_con(self,valeur):
        self.convolutionmatrice = valeur
        print("Change : Matrice :", self.convolutionmatrice)
    def inputfrequence_con(self,valeur):
        self.inputfrequence = valeur
        print("Change : Frequence :", self.inputfrequence)
    def inputordre_con(self,valeur):
        self.inputordre = valeur
        print("Change : Ordre :", self.inputordre)
    def inputSigmaS_con(self,valeur):
        self.inputSigmaS = valeur
        print("Change : Sigma S :", self.inputSigmaS)
    def inputsigma_con(self,valeur):
        self.inputsigma = valeur
        print("Change : Sigma :", self.inputsigma)
    def inputsigmaC_con(self,valeur):
        self.inputsigmaC = valeur
        print("Change : sigma C :", self.inputsigmaC)
    def inputprecision_con(self,valeur):
        self.inputprecision = valeur
        print("Change : precision :", self.inputprecision)
    def inputiteration_con(self,valeur):
        self.inputiteration = valeur
        print("Change : iteration :", self.inputiteration)
    def inputabsolute_con(self,valeur):
        self.inputabsolute = valeur
        print("Change : absolute :", self.inputabsolute)
    def inputsize_con(self,valeur):
        self.inputsize = valeur
        print("Change : taille :", self.inputsize)
    def generationtype_con(self,valeur):
        self.generationtype = valeur
        print("Change : generation type :", self.generationtype)
    def optiontypeselect_con(self,valeur):
        self.optiontypeselect = valeur
        print("Change : option select :", self.optiontypeselect)
    
    def label_3_couleur_con(self,valeur):
        self.cmaptype = valeur
        print("Change : cmap :", self.cmaptype)

    def combobox_3_con(self,valeur):
        self.sousoptiontype = valeur
        print("Change : sous option :", self.sousoptiontype)

    def combobox_4_con(self,valeur):
        self.sousoptiontype = valeur
        print("Change : sous option :", self.sousoptiontype)

    def combobox_5_con(self,valeur):
        self.sousoptiontype = valeur
        print("Change : sous option :", self.sousoptiontype)

    def label_1_stacking_con(self,valeur):
        self.generationtype = valeur
        print("Change : generation type :", self.generationtype)
    
    """Méthode permettent de générer les text de chaque widget

    Args:
        self : Notre application
    """
    def retranslateUi(self):
        self.Ouvrirun.setText("Ouvrir un dossier")
        self.pushButton_2.setText("Ouvrir un fichier")
        self.label.setText("Minimum")
        self.label_2.setText("Maximum")
        self.pushButton.setText("Actualiser")

        self.label_3_min_text.setText("Min")
        self.label_5_max_text.setText("Max")

        self.label_7_moyenne_text.setText("Moyenne")
        self.label_9_stdev_text.setText("Stdev")

        self.label_11_statistiques_text.setText("Statistiques :")


        self.label_13_width_text.setText("Width :")
        self.label_14_height_text.setText("Height :")
        self.scaling_text.setText("Scaling :")
        self.pushButton_20_actualiser.setText("Actualiser")
        self.pushButton_21_enregister_png.setText("Enregistrer (png)")
        self.pushButton_22_rotation.setText("Rotation de 90°")
        
        
    
        self.scalingmax_text.setText("Maximum :")
        self.scalingmin_text.setText("Minimum :")
        self.scalingintervale_text.setText("a :")
    

    """Méthode permettant d'enregister dans le dossier courant l'image dernièrement génrée sous le nom de "image_final.png".

    Args:
        self : Notre application
    """
    def EnregisterPng(self):
        if self.cmaptype == "Aucun":
            plt.imshow(self.generation(self.generationtype), vmin=self.minimum, vmax=self.maximum)
        else:
            plt.imshow(self.generation(self.generationtype), vmin=self.minimum, vmax=self.maximum, cmap=self.cmaptype)
        plt.axis('off')
        plt.savefig("image_final.png", bbox_inches='tight', pad_inches = 0)
    
    
    """Méthode permettant de générer une rotation de notre matrice

    Args:
        self : Notre application
    """
    def rotation_matrice(self):
        self.image_list_fini = self.rotateMatrix(self.image_list_fini)
        self.image(self.image_list_fini)
        print(self.image_list_fini)
    
    """Fonction permettant la génération d'une nouvelle matrice tournée de 90 degré

    Args:
        self : Notre application
    
    Returns:
        list: retourne la nouvelle matrice générée par scipy
    """
    def rotateMatrix(self,mat) -> list:
        from scipy.ndimage.interpolation import rotate
        mat_rotate = rotate(mat, angle=90)
        return mat_rotate

    """Méthode permettant d'actualiser les widget en fonction de notre choix effectué sur notre combo-box des scaling

    Args:
        self : Notre application
    """
    def changement_scaling(self):
        self.scalingvaleur = self.label_2_scalling.currentText()
        print("changement du scaling en : ", self.scalingvaleur)
        self.scalingmax_text.setVisible(False)
        self.scalingmax.setVisible(False)
        self.scalingmin_text.setVisible(False)
        self.scalingmin.setVisible(False)
        self.scalingintervale_text.setVisible(False)
        self.scalingintervale.setVisible(False)
        self.scalingintervale2.setVisible(False)
        self.scalingmax.setValue(self.maximum)
        self.scalingmin.setValue(self.minimum)
        self.scalingmax.setMaximum(self.maximum)
        self.scalingmax.setMinimum(self.minimum)
        self.scalingmin.setMaximum(self.maximum)
        self.scalingmin.setMinimum(self.minimum)
        self.scalingmin.setMaximum(9999999)
        self.scalingmax.setMaximum(9999999)
        if (self.scalingvaleur == "Linear"):
            self.scalingmin.setVisible(True)
            self.scalingmax.setVisible(True)
            self.scalingmax_text.setVisible(True)
            self.scalingmin_text.setVisible(True)
        elif (self.scalingvaleur == "Asinh"):
            self.scalingmax_text.setVisible(True)
            self.scalingmax.setVisible(True)
            self.scalingmin_text.setVisible(True)
            self.scalingmin.setVisible(True)
            self.scalingintervale_text.setVisible(True)
            self.scalingintervale.setVisible(True)
            self.scalingintervale_text.setText("a :")
            self.scalingintervale.setValue(0.5)
            self.scalingintervale.setMaximum(1.0)

        elif (self.scalingvaleur == "Sqrt"):
            self.scalingmax_text.setVisible(True)
            self.scalingmax.setVisible(True)
            self.scalingmin_text.setVisible(True)
            self.scalingmin.setVisible(True)
        elif (self.scalingvaleur == "Histeq"):
            self.scalingmax_text.setVisible(True)
            self.scalingmax.setVisible(True)
            self.scalingmin_text.setVisible(True)
            self.scalingmin.setVisible(True)
            self.scalingintervale_text.setVisible(True)
            self.scalingintervale2.setVisible(True)
            self.scalingintervale2.setValue(256)
            self.scalingintervale2.setMaximum(999999)
            self.scalingintervale_text.setText("bins :")


    """Méthode permettant d'actualiser les valeur statistiques de notre image (et notre image)

    Args:
        self : Notre application
    """
    def actualiser_stats_et_image(self):
        self.minimum = self.min.value()
        self.maximum = self.max.value()
        if self.rgbimage:
            self.imageRGB(self.image_list_fini)
            self.histogrammeRGB(self.image_list_fini)
        else:
            self.image(self.image_list_fini)
            self.histogramme(self.image_list_fini)
        self.canvas.draw()
        self.moyenne = np.mean(self.imagelist_image)
        self.stddev = np.std(self.imagelist_image)
        self.label_6_max_valeur.setText(f"{self.maximum}")
        self.label_4_min_valeur.setText(f"{self.minimum}")
        self.label_8_moyenne_valeur.setText(f"{self.moyenne}")
        self.label_10_stdev_valeur.setText(f"{self.stddev}")
        print("image actualisée en :", self.minimum, "min ", self.maximum, "max ")
    
    """Méthode permettant de générer soit l'histogramme soit l'image de notre application

    Args:
        self : Notre application
        valeur : Notre valeur soit 1 = Image et 2 = Histogramme
    """
    def plot(self, valeur: int):
        print("Affichage en cours...")
        if valeur == 1:
            if self.rgbimage:
                self.imageRGB(self.generation(self.generationtype))
            else:
                self.image(self.generation(self.generationtype))
        if valeur == 2:
            if self.rgbimage:
                self.histogrammeRGB(self.generation(self.generationtype))
            else:
                self.histogramme(self.generation(self.generationtype))
        print("Affichage OK")

    """Méthode permettant de changer l'image affichée sur notre application

    Args:
        self : Notre application
        image : List 
    """
    def image(self, image:list[list[int]]):
        print("Dessin en cours... image")
        self.canvas.figure.clear()
        self.ax = self.figure.add_subplot(111)
        if self.rgbimage:
            self.ax.imshow(image)
        else:
            if self.cmaptype == "Aucun":
                self.ax.imshow(image, vmin=self.minimum, vmax=self.maximum)
            else:
                self.ax.imshow(image, vmin=self.minimum, vmax=self.maximum, cmap=self.cmaptype)
        self.imagelist_image = image

        self.ax.set_axis_off()
        self.canvas.draw()
        print("Dessin OK")
    
    """Méthode permettant de changer l'image affichée sur notre application en format RGB

    Args:
        self : Notre application
        image : Notre image sous le format R G B
    """
    def imageRGB(self, image:list[list[float],list[float],list[float]]):
        print("Dessin en cours... imageRGB")
        self.canvas.figure.clear()
        self.ax = self.figure.add_subplot(111)

        imageoff = make_lupton_rgb((image[0]/self.nombre_image), (image[1]/self.nombre_image), (image[2]/self.nombre_image), stretch=0.5)
        print(imageoff)
        if self.cmaptype == "Aucun":
            self.ax.imshow(imageoff)
        else:
            self.ax.imshow(imageoff, vmin=self.minimum, vmax=self.maximum, cmap=self.cmaptype)
        self.imagelist_image = imageoff

        self.ax.set_axis_off()
        self.canvas.draw()
        print("Dessin OK")
    
    """Méthode permettant de changer l'image avec l'image staking

    Args:
        self : Notre application
    """
    def actualiserStaking(self):
        self.minimum = self.min.value()
        self.maximum = self.max.value()
        print("Affichage en cours...")
        if self.rgbimage:
            self.imageRGB(self.generation(self.generationtype))
            self.histogrammeRGB(self.image_list_fini)
        else:
            self.image(self.generation(self.generationtype))
            self.histogramme(self.image_list_fini)
        print("Affichage OK")
    
    """Méthode permettant de changer l'image avec l'image scaling

    Args:
        self : Notre application
    """
    def actualiserScaling(self):
        self.minimum = self.min.value()
        self.maximum = self.max.value()
        print("Affichage en cours...")
        if self.rgbimage:
            self.imageRGB(self.generation(self.generationtype))
            self.histogrammeRGB(self.image_list_fini)
        else:
            self.image(self.generation(self.generationtype))
            self.histogramme(self.image_list_fini)
        print("Affichage OK")

    """Méthode permettant de changer l'image avec les options chois

    Args:
        self : Notre application
    """
    def actualiserOptions(self):
        self.minimum = self.min.value()
        self.maximum = self.max.value()
        print("Affichage en cours...")
        if self.rgbimage:
            self.imageRGB(self.generationOption())
            self.histogrammeRGB(self.image_list_fini)
        else:
            self.image(self.generationOption())
            self.histogramme(self.image_list_fini)
        print("Affichage OK")
    
    """Méthode permettant de changer l'histogramme

    Args:
        self : Notre application
    """
    def histogramme(self, image:list[list[int]]):
        print("Dessin en cours... hist")
        self.canvas2.figure.clear()
        self.ax2 = self.figure2.add_subplot(111)
        self.imagelist_hist = image
        self.minimum = np.min(image)
        self.maximum = np.max(image)
        self.moyenne = np.mean(image)
        self.stddev = np.std(image)
        self.min.setValue(self.minimum)
        self.max.setValue(self.maximum)
        self.actualiserlabel()
        self.ax2.hist(image.flatten(), bins='auto')
        self.canvas2.draw()
        self.image(image)
        print("Dessin OK")
    
    """Méthode permettant de changer l'histogramme sous format RGB

    Args:
        self : Notre application
    """
    def histogrammeRGB(self, image:list[list[float],list[float],list[float]]):
        print("Dessin en cours... hist")
        self.canvas2.figure.clear()
        self.ax2 = self.figure2.add_subplot(111)
        self.imagelist_hist = make_lupton_rgb(image[0], image[1], image[2], stretch=0.5)

        self.minimum = np.min(image)
        self.maximum = np.max(image)
        self.moyenne = np.mean(image)
        self.stddev = np.std(image)
        self.min.setValue(self.minimum)
        self.max.setValue(self.maximum)
        self.actualiserlabel()
        self.ax2.hist(self.imagelist_hist.flatten(), bins='auto')
        self.canvas2.draw()
        self.imageRGB(image)
        print("Dessin OK")

    """Méthode permettant de générer une nouvelle image avec les options choisis

    Args:
        self : Notre application
    """
    def generationOption(self, list : np.ndarray) -> np.ndarray:
        print("Generation d'une image en cours...")

        print("Generation de l'image OK")
        print("Génération de type : ", self.generationtype)
        if self.optiontypeselect == "Gaussian":
            print("Génération avec filtre Gaussian en cours...")
            if self.sousoptiontype == "Passe haut":
                final_image = Filters.gaussian_highpass_filter(list, self.inputsigma, self.inputsize)
            else:
                final_image = Filters.gaussian_filter(list, self.inputsigma, self.inputsize)
        elif self.optiontypeselect == "Butterworth":
            print("Génération avec filtre Butterworth en cours...")
            # print(list, self.inputfrequence, self.inputordre)
            if self.sousoptiontype == "Passe haut":
                print("Filtre passe haut")
                final_image = Filters.butterworth_highpass_filter(list, self.inputfrequence, self.inputordre)

            else:
                print("Filtre passe bas")
                final_image = Filters.butterworth_lowpass_filter(list, self.inputfrequence, self.inputordre)

            # print(final_image)
        elif self.optiontypeselect == "Valeur abérante":
            print("Génération avec filtre Valeur abérante en cours...")
            if self.sousoptiontype == "Médiane":
                final_image = Filters.medianOutletRemover(list, self.inputprecision)
            elif self.sousoptiontype == "Sigma":
                final_image = Filters.sigmaOutletRemover(list, self.inputprecision)
            else:
                print(self.inputprecision)
                final_image = Filters.meanOutletRemover(list, self.inputprecision)
        else:
            print("Génération avec filtre custom en cours...")
            if self.optiontypeselect == "Moyenne":
                final_image = Filters.mean_filter(list, self.inputsize, self.inputiteration)
            if self.optiontypeselect == "Convolution":
                final_image = Filters.convolution(list, self.convolutionmatrice)
            # ENCORE A FAIRE AVEC LA MATRICE
            if self.optiontypeselect == "Sobel":
                print(self.inputabsolute)
                final_image = Filters.sobel_filter(list, self.inputabsolute)
            if self.optiontypeselect == "Bilateral":
                final_image = Filters.bilateral_filter(list, self.inputsize, self.inputsigmaC, self.inputSigmaS)
            if self.optiontypeselect == "Médiane":
                print("médiane")
                final_image = Filters.median_filter(list, self.inputsize, self.inputiteration)
            if self.optiontypeselect == "Aucun":
                final_image = list
        # self.longueur = len(final_image)
        # self.hauteur = len(final_image[0])
        # self.image_list_fini = final_image
        print("Image avec option créée")
        return final_image
    
    """Méthode permettant de générer une nouvelle image

    Args:
        self : Notre application
    """
    def generation(self,type:str):
        print("Generation de l'image en cours...")
        if self.rgbimage:
            final_image = self.generationRGB(type)
        else:
            if len(self.image_list) < 1:
                base_nonurl = self.base_url + "/*fits"
                self.image_list = glob.glob(base_nonurl)
            image_concat = [fits.getdata(image) for image in self.image_list]
            
            tt = fits.open(self.image_list[0])

            print("Generation de l'image OK")
            print("Génération de type : ", self.generationtype)
            if type == "Somme":
                print("Génération par défaut en cours...")
                final_image = Stacking.addition(image_concat)
            if type == "Moyenne":
                print("Génération par moyenne en cours...")
                final_image = Stacking.mean(image_concat)
            if type == "Mediane":
                print("Génération par médiane en cours...")
                final_image = Stacking.median(image_concat)
            if type == "Sigma":
                print("Génération par Sigma en cours...")
                final_image = Stacking.sigmaOutlet(image_concat,self.valeurprecision)
            
            final_image = self.generationOption(final_image)
            if self.scalingvaleur != "Aucun":
                if self.scalingvaleur == "Linear":
                    final_image = Normalization.linear(final_image,self.scalingmin.value(),self.scalingmax.value())
                if self.scalingvaleur == "Asinh":
                    final_image = Normalization.asinh(final_image,self.scalingmin.value(),self.scalingmax.value(),self.scalingintervale.value())
                if self.scalingvaleur == "Sqrt":
                    final_image = Normalization.sqrt(final_image,self.scalingmin.value(),self.scalingmax.value())
                if self.scalingvaleur == "Histeq":
                    final_image = Normalization.histeq(final_image,self.scalingmin.value(),self.scalingmax.value(),self.scalingintervale2.value())
            self.longueur = len(final_image)
            self.hauteur = len(final_image[0])
            self.image_list_fini = final_image
        return final_image
    
    """Méthode permettant de générer une nouvelle image RGB

    Args:
        self : Notre application
    """
    def generationRGB(self,type:str):

        image_concat_rouge = []
        image_concat_vert = []
        image_concat_bleu = []
        image_concat_list = []
        image_concat_final = []
        for image in self.image_list:
            image_concat_rouge.append(fits.getdata(image)[0])
        for image in self.image_list:
            image_concat_vert.append(fits.getdata(image)[1])
        for image in self.image_list:
            image_concat_bleu.append(fits.getdata(image)[2])
        image_concat_list.append(image_concat_rouge)
        image_concat_list.append(image_concat_vert)
        image_concat_list.append(image_concat_bleu)
        for i in range(3):
            print("Generation de l'image OK")
            print("Génération de type : ", self.generationtype)
            if type == "Somme":
                print("Génération par défaut en cours...")
                image_concat_final.append(Stacking.addition(image_concat_list[i]))
            if type == "Moyenne":
                print("Génération par moyenne en cours...")
                image_concat_final.append(Stacking.mean(image_concat_list[i]))
            if type == "Mediane":
                print("Génération par médiane en cours...")
                image_concat_final.append(Stacking.median(image_concat_list[i]))
            if type == "Sigma":
                print("Génération par Sigma en cours...")
                image_concat_final.append(Stacking.sigmaOutlet(image_concat_list[i],self.valeurprecision))
            image_concat_final[i] = self.generationOption(image_concat_final[i])
            if self.scalingvaleur != "Aucun":
                if self.scalingvaleur == "Linear":
                    image_concat_final[i] = Normalization.linear(image_concat_list[i],self.scalingmin.value(),self.scalingmax.value())
                if self.scalingvaleur == "Asinh":
                    image_concat_final[i] = Normalization.asinh(image_concat_list[i],self.scalingmin.value(),self.scalingmax.value(),self.scalingintervale.value())
                if self.scalingvaleur == "Sqrt":
                    image_concat_final[i] = Normalization.sqrt(image_concat_list[i],self.scalingmin.value(),self.scalingmax.value())
                if self.scalingvaleur == "Histeq":
                    image_concat_final[i] = Normalization.histeq(image_concat_list[i],self.scalingmin.value(),self.scalingmax.value(),self.scalingintervale2.value())
        self.longueur = len(image_concat_list[0])
        self.hauteur = len(image_concat_final[0][0])
        self.image_list_fini = image_concat_final
        return self.image_list_fini

    """Méthode permettant d'ouvrir un fichier et de l'entregistrer dans une liste

    Args:
        self : Notre application
    """
    def openfichier(self):
        path = QFileDialog.getOpenFileName(self, 'Ouvrir un fichier', '', 'Images (*.fits)')
        if path != ('', ''):
            print("Le fichier sélectionné est : ", path[0])
            self.base_url = path[0]
            self.image_list.append(path[0])
            self.nombre_image = 1
            self.update()

    """Méthode permettant d'ouvrir un dossier et de l'entregistrer dans une liste

    Args:
        self : Notre application
    """
    def openfolder(self):
        path = QFileDialog.getExistingDirectory(self,"Ouvrir un dossier", '')
        if path != (''):
            print("Le dossier sélectionné est : ", path)
            print(path)
            self.base_url = path
            base_nonurl = self.base_url + "/*fits"
            self.image_list = glob.glob(base_nonurl)
            if len(self.image_list) > 0:
                self.nombre_image = len(self.image_list)
                self.rgbimage = False
                self.update()
            else:
                self.base_url = path
                base_nonurl = self.base_url + "/*fit"
                self.image_list = glob.glob(base_nonurl)
                if len(self.image_list) > 0:
                    self.nombre_image = len(self.image_list)
                    self.rgbimage = True
                    self.update()

    """Méthode permettant d'actualiser l'image et l'histogramme

    Args:
        self : Notre application
    """
    def update(self):
        self.plot(1)
        self.canvas.draw()
        self.plot(2)
        self.canvas2.draw()

        self.min.setValue(self.minimum)
        self.max.setValue(self.maximum)

    """Méthode permettant d'actualiser les text des statistiques

    Args:
        self : Notre application
    """
    def actualiserlabel(self):
        self.label_6_max_valeur.setText(f"{self.maximum}")
        self.label_4_min_valeur.setText(f"{self.minimum}")
        self.label_8_moyenne_valeur.setText(f"{self.moyenne}")
        self.label_10_stdev_valeur.setText(f"{self.stddev}")
        self.label_15_width_valeur.setText(f"{self.longueur}")
        self.label_16_height_valeur.setText(f"{self.hauteur}")