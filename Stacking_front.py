from PyQt6.QtCore import (QCoreApplication, QRect, QSize, Qt)
from PyQt6.QtWidgets import (QHBoxLayout, QCheckBox, QGridLayout, QPushButton, QSpinBox, QVBoxLayout, QWidget,QApplication, QLabel, QFileDialog, QComboBox, QSlider, QDoubleSpinBox)
from PyQt6.QtCore import pyqtSignal
import numpy as np

class Stacking_front(QWidget):

    optiontypeselect_con : pyqtSignal = pyqtSignal(str)
    inputfrequence_con : pyqtSignal = pyqtSignal(int)
    inputordre_con : pyqtSignal = pyqtSignal(int)
    inputSigmaS_con : pyqtSignal = pyqtSignal(float)
    inputsigma_con : pyqtSignal = pyqtSignal(float)
    inputsigmaC_con : pyqtSignal = pyqtSignal(float)
    inputiteration_con : pyqtSignal = pyqtSignal(int)
    inputabsolute_con : pyqtSignal = pyqtSignal(Qt.CheckState)
    inputsize_con : pyqtSignal = pyqtSignal(int)
    inputprecision_con : pyqtSignal = pyqtSignal(float)
    actualisersatking_con : pyqtSignal = pyqtSignal()
    selfgenerationtype_con : pyqtSignal = pyqtSignal(str)
    slider_stacking_con : pyqtSignal = pyqtSignal(int)
    
    label_3_couleur_con : pyqtSignal = pyqtSignal(str)
    combobox_2_con : pyqtSignal = pyqtSignal(str)
    combobox_3_con : pyqtSignal = pyqtSignal(str)
    combobox_4_con : pyqtSignal = pyqtSignal(str)
    combobox_5_con : pyqtSignal = pyqtSignal(str)
    label_1_stacking_con : pyqtSignal = pyqtSignal(str)
    convolutionmatrice_con : pyqtSignal = pyqtSignal(np.ndarray)

    def __init__(self) -> None:
        super().__init__()
        self.verticalLayout_666 = QVBoxLayout()
        self.verticalWidget_6 = QWidget()
        self.verticalLayout_666.addWidget(self.verticalWidget_6)
        self.setLayout(self.verticalLayout_666)
        self.widgetstacking_con : QWidget = QWidget()
        self.verticalLayout_6 = QVBoxLayout()
        
        self.verticalWidget_6.setLayout(self.verticalLayout_6)
        self.verticalWidget_6.setMaximumSize(QSize(999999, 700))
        self.verticalWidget_6.setStyleSheet("background-color:#fff;")

        self.label_12_stacking_text = QLabel()
        self.verticalLayout_6.addWidget(self.label_12_stacking_text)
        self.label_12_stacking_text.setMaximumSize(QSize(999999, 15))

        self.label_1_stacking = QComboBox()
        self.verticalLayout_6.addWidget(self.label_1_stacking)
        self.label_1_stacking.addItems(["Somme","Moyenne","Mediane","Sigma"])
        self.horizontalLayout_20 = QHBoxLayout()
        self.verticalLayout_6.addLayout(self.horizontalLayout_20)
        self.label_1_stacking.setStyleSheet("background-color:#fff;")

        self.slider_stacking_text = QLabel()
        self.horizontalLayout_20.addWidget(self.slider_stacking_text)
        self.slider_stacking = QSlider(Qt.Orientation.Horizontal)
        self.horizontalLayout_20.addWidget(self.slider_stacking)

        self.valeur_slide = QLabel()
        self.horizontalLayout_20.addWidget(self.valeur_slide)

        self.anti_width = QLabel()
        self.horizontalLayout_20.addWidget(self.anti_width)
        self.horizontalLayout_20.heightForWidth(25)
        self.slider_stacking.setMaximumSize(QSize(999999, 25))
        self.valeur_slide.setMaximumSize(QSize(999999, 25))
        self.anti_width.setMaximumSize(QSize(999999, 25))
        self.slider_stacking.setVisible(False)
        self.valeur_slide.setVisible(False)

        self.verticalLayout_12 = QVBoxLayout()
        self.label_13_options = QLabel()
        self.verticalLayout_12.addWidget(self.label_13_options)
        self.label_13_options.setMaximumSize(QSize(999999, 25))
        
        self.label_12_color_map = QLabel()
        self.verticalLayout_6.addWidget(self.label_12_color_map)
        self.label_12_color_map.setMaximumSize(QSize(999999, 25))
        self.label_3_couleur = QComboBox()
        self.verticalLayout_6.addWidget(self.label_3_couleur)
        self.label_3_couleur.addItems(['gray', 'Aucun', 'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r'])
        
        self.verticalLayout_6.addLayout(self.verticalLayout_12)
        self.combobox_2 = QComboBox()
        self.combobox_3 = QComboBox()
        self.combobox_4 = QComboBox()
        self.combobox_5 = QComboBox()
    
        self.verticalLayout_12.addWidget(self.combobox_2)
        self.combobox_2.addItems(["Aucun","Valeur abérante","Médiane","Moyenne","Convolution", "Butterworth", "Gaussian", "Sobel", "Bilateral"])

        self.verticalLayout_12.addWidget(self.combobox_3)
        self.combobox_3.addItems(["Moyenne","Médiane","Sigma"])

        self.verticalLayout_12.addWidget(self.combobox_4)
        self.combobox_4.addItems(["Passe bas","Passe haut"])

        self.verticalLayout_12.addWidget(self.combobox_5)
        self.combobox_5.addItems(["Simple","Passe haut"])

        self.combobox_3.setVisible(False)
        self.combobox_4.setVisible(False)
        self.combobox_5.setVisible(False)


        self.inputsize_text = QLabel()
        self.inputsize = QSpinBox()
        self.inputprecision_text = QLabel()
        self.inputprecision = QDoubleSpinBox()
        self.inputiteration_text = QLabel()
        self.inputiteration = QSpinBox()

        self.inputabsolute_text = QLabel()
        self.inputabsolute = QCheckBox()

        self.inputfrequence_text = QLabel()
        self.inputfrequence = QSpinBox()

        self.inputSigmaS_text = QLabel()
        self.inputSigmaS = QDoubleSpinBox()

        self.inputsigma_text = QLabel()
        self.inputsigma = QDoubleSpinBox()

        self.inputSigmaC_text = QLabel()
        self.inputsigmaC = QDoubleSpinBox()

        self.inputordre_text = QLabel()
        self.inputordre = QSpinBox()

        self.matrice_convolution_layout = QGridLayout()
        self.inputsize.setMinimum(0)
        self.inputsize.setMaximum(1000000000)

        self.verticalLayout_12.addWidget(self.inputsize_text)
        self.inputsize_text.setMaximumSize(QSize(999999, 25))
        self.verticalLayout_12.addWidget(self.inputsize)

        self.inputprecision.setMinimum(0)
        self.inputprecision.setMaximum(1000000000)

        self.verticalLayout_12.addWidget(self.inputprecision_text)
        self.inputprecision_text.setMaximumSize(QSize(999999, 25))
        self.verticalLayout_12.addWidget(self.inputprecision)

        self.inputiteration.setMinimum(0)
        self.inputiteration.setMaximum(1000000000)

        self.verticalLayout_12.addWidget(self.inputiteration_text)
        self.inputiteration_text.setMaximumSize(QSize(999999, 25))
        self.verticalLayout_12.addWidget(self.inputiteration)


        self.verticalLayout_12.addWidget(self.inputabsolute_text)
        self.inputabsolute_text.setMaximumSize(QSize(999999, 25))
        self.verticalLayout_12.addWidget(self.inputabsolute)

        self.inputfrequence.setMinimum(0)
        self.inputfrequence.setMaximum(1000000000)

        self.verticalLayout_12.addWidget(self.inputfrequence_text)
        self.inputfrequence_text.setMaximumSize(QSize(999999, 25))
        self.verticalLayout_12.addWidget(self.inputfrequence)

        self.inputsigma.setMinimum(0)
        self.inputsigma.setMaximum(1000000000)

        self.verticalLayout_12.addWidget(self.inputsigma_text)
        self.inputsigma_text.setMaximumSize(QSize(999999, 25))
        self.verticalLayout_12.addWidget(self.inputsigma)

        self.inputSigmaS.setMinimum(0)
        self.inputSigmaS.setMaximum(1000000000)

        self.verticalLayout_12.addWidget(self.inputSigmaS_text)
        self.inputSigmaS_text.setMaximumSize(QSize(999999, 25))
        self.verticalLayout_12.addWidget(self.inputSigmaS)

        self.inputsigmaC.setMinimum(0)
        self.inputsigmaC.setMaximum(1000000000)

        self.verticalLayout_12.addWidget(self.inputSigmaC_text)
        self.inputSigmaC_text.setMaximumSize(QSize(999999, 25))
        self.verticalLayout_12.addWidget(self.inputsigmaC)

        self.inputordre.setMinimum(0)
        self.inputordre.setMaximum(1000000000)

        self.verticalLayout_12.addWidget(self.inputordre_text)
        self.inputordre_text.setMaximumSize(QSize(999999, 25))
        self.verticalLayout_12.addWidget(self.inputordre)

        self.verticalLayout_12.addLayout(self.matrice_convolution_layout)
        self.convolutionmatrice = np.ndarray(shape=(3,3), dtype=float, order='F')
        for i in range(3):
            for j in range(3):
                self.convolutionmatrice[i][j] = 0
                self.spin = QDoubleSpinBox() 
                self.spin.setObjectName(f"{i,j}")
                self.matrice_convolution_layout.addWidget(self.spin,i,j)
                self.spin.valueChanged.connect(lambda ____, r=i, c=j, v=self.spin : self.positionchange(r, c, v))
                self.spin.setVisible(False)
        self.emitconvolutionmatrice()
        self.inputsize.setVisible(False)
        self.inputsize_text.setVisible(False)
        self.inputprecision.setVisible(False)
        self.inputprecision_text.setVisible(False)
        self.inputiteration.setVisible(False)
        self.inputiteration_text.setVisible(False)

        self.inputabsolute.setVisible(False)
        self.inputabsolute_text.setVisible(False)

        self.inputfrequence.setVisible(False)
        self.inputfrequence_text.setVisible(False)

        self.inputfrequence.setVisible(False)
        self.inputfrequence_text.setVisible(False)

        self.inputSigmaS.setVisible(False)
        self.inputSigmaS_text.setVisible(False)

        self.inputsigmaC.setVisible(False)
        self.inputSigmaC_text.setVisible(False)

        self.inputsigma.setVisible(False)
        self.inputsigma_text.setVisible(False)

        self.inputordre.setVisible(False)
        self.inputordre_text.setVisible(False)

        self.pushButton_5_actualiser = QPushButton()
        self.verticalLayout_6.addWidget(self.pushButton_5_actualiser)
        self.pushButton_5_actualiser.setStyleSheet("border: 1px solid #009BFF; border-radius: 10px;border-top-left-radius :35px; border-top-right-radius : 20px; border-bottom-left-radius : 50px; border-bottom-right-radius : 10px")
        
        self.label_12_stacking_text.setText("Stacking :")
        self.pushButton_5_actualiser.setText("Actualiser")

        self.label_13_options.setText("Filtrage :")
        self.label_12_color_map.setText("Color Map :")
        self.valeur_slide.setText(f"0")

        self.inputprecision_text.setText("Précision :")
        self.inputsize_text.setText("Taille :")
        self.inputiteration_text.setText("Itération :")

        self.inputabsolute_text.setText("Valeur absolue (True/False) :")
        self.inputfrequence_text.setText("Fréquence :")

        self.inputsigma_text.setText("Sigma :")
        self.inputSigmaC_text.setText("Sigma C :")
        self.inputSigmaS_text.setText("Sigma S :")

        self.slider_stacking_text.setText("Précision : ")

        self.inputordre_text.setText("n :")

        self.combobox_2.currentIndexChanged.connect(self.option_choix_filtre)

        self.combobox_3.currentIndexChanged.connect(self.sousoption_valeur_aberante)
        self.combobox_4.currentIndexChanged.connect(self.sousoption_butterworth)
        self.inputsize.valueChanged.connect(self.checkimpair)
        self.combobox_5.currentIndexChanged.connect(self.sousoption_gaussian)

        self.label_1_stacking.currentIndexChanged.connect(self.selection_stacking_change)
        self.label_3_couleur.currentIndexChanged.connect(self.couleur_change_cmap)
        self.slider_stacking.valueChanged.connect(self.valeur_precision_change)
        
        self.pushButton_5_actualiser.clicked.connect(self.actualiserStaking)

        self.inputsize.valueChanged.connect(self.emitinputSizeValueChange)
        self.inputabsolute.stateChanged.connect(self.emitinputAbsoluteValueChange)
        self.inputprecision.valueChanged.connect(self.emitinputPrecisionValueChange)
        self.inputfrequence.valueChanged.connect(self.emitinputfrequenceValueChange)
        self.inputordre.valueChanged.connect(self.emitinputordreValueChange)
        self.inputsigma.valueChanged.connect(self.emitinputsigmaValueChange)
        self.inputsigmaC.valueChanged.connect(self.emitinputsigmaCValueChange)
        self.inputSigmaS.valueChanged.connect(self.emitinputSigmaSValueChange)
        self.inputiteration.valueChanged.connect(self.emitinputiterationValueChange)
        self.slider_stacking.valueChanged.connect(self.emitslider_stacking)



    """ Ensemble des callback qui envoi les nouvelles informations à l'interface
    """
    def emitslider_stacking(self):
        self.slider_stacking_con.emit(self.slider_stacking.value())
    
    def emitlabel_3_couleur(self):
        self.label_3_couleur_con.emit(self.label_3_couleur.currentText())
    
    def emitcombobox_2(self):
        self.combobox_2_con.emit(self.combobox_2.currentText())
    
    def emitcombobox_3(self):
        self.combobox_3_con.emit(self.combobox_3.currentText())
    
    def emitcombobox_4(self):
        self.combobox_4_con.emit(self.combobox_4.currentText())
    
    def emitcombobox_5(self):
        self.combobox_5_con.emit(self.combobox_5.currentText())
    
    def emitlabel_1_stacking(self):
        self.label_1_stacking_con.emit(self.label_1_stacking.currentText())

    def emitinputfrequenceValueChange(self):
        self.inputfrequence_con.emit(self.inputfrequence.value())
    
    def emitinputordreValueChange(self):
        self.inputordre_con.emit(self.inputordre.value())
    
    def emitinputSigmaSValueChange(self):
        self.inputSigmaS_con.emit(self.inputSigmaS.value())
    
    def emitinputsigmaValueChange(self):
        self.inputsigma_con.emit(self.inputsigma.value())
    
    def emitinputsigmaCValueChange(self):
        self.inputsigmaC_con.emit(self.inputsigmaC.value())
    
    def emitinputPrecisionValueChange(self):
        self.inputprecision_con.emit(self.inputprecision.value())

    def emitinputiterationValueChange(self):
        self.inputiteration_con.emit(self.inputiteration.value())

    def emitinputAbsoluteValueChange(self):
        self.inputabsolute_con.emit(self.inputabsolute.checkState())

    def emitinputSizeValueChange(self):
        self.inputsize_con.emit(self.inputsize.value())

    def emitOptioinTypeSelect(self):
        self.optiontypeselect_con.emit(self.combobox_2.currentText())
    
    def actualiserStaking(self):
        self.actualisersatking_con.emit()

    def generationtype_con(self,valeur):
        self.selfgenerationtype_con.emit(valeur)
    
    def emitconvolutionmatrice(self):
        self.convolutionmatrice_con.emit(self.convolutionmatrice)

    
    """Méthode permettant d'actualiser les widget en fonction de notre choix effectué sur notre combo-box des filtres stacking

    Args:
        self : Notre application
    """
    def option_choix_filtre(self):  
        self.optiontypeselect = self.combobox_2.currentText()
        self.emitOptioinTypeSelect()
        self.inputsize.setVisible(False)
        self.inputsize_text.setVisible(False)
        self.inputprecision.setVisible(False)
        self.inputprecision_text.setVisible(False)
        self.inputiteration.setVisible(False)
        self.inputiteration_text.setVisible(False)
        self.inputabsolute.setVisible(False)
        self.inputabsolute_text.setVisible(False)
        self.inputfrequence.setVisible(False)
        self.inputfrequence_text.setVisible(False)
        self.inputfrequence.setVisible(False)
        self.inputfrequence_text.setVisible(False)
        self.inputSigmaS.setVisible(False)
        self.inputSigmaS_text.setVisible(False)
        self.inputsigmaC.setVisible(False)
        self.inputSigmaC_text.setVisible(False)
        self.inputsigma.setVisible(False)
        self.inputsigma_text.setVisible(False)
        self.inputordre.setVisible(False)
        self.inputordre_text.setVisible(False)
        self.combobox_3.setVisible(False)
        self.combobox_4.setVisible(False)
        self.combobox_5.setVisible(False)
        if self.matrice_convolution_layout.count() > 1:
            for i in range(3):
                for j in range(3):
                    self.matrice_convolution_layout.itemAtPosition(i,j).widget().deleteLater()
                    self.convolutionmatrice[i][j] = 0
        self.emitconvolutionmatrice()
        if (self.optiontypeselect == "Valeur abérante"):
            self.combobox_3.setVisible(True)
            self.inputprecision.setVisible(True)
            self.inputprecision_text.setVisible(True)
            self.inputprecision.setValue(1.5)
        else:
            if (self.optiontypeselect == "Butterworth"):
                self.combobox_4.setVisible(True)
                self.inputordre.setVisible(True)
                self.inputordre_text.setVisible(True)
                self.inputfrequence.setVisible(True)
                self.inputfrequence_text.setVisible(True)
                self.inputfrequence.setValue(100)
                self.inputordre.setValue(1)
            else:
                if (self.optiontypeselect == "Gaussian"):
                    self.widgetstacking_con.setMaximumSize(QSize(999999, 400))
                    self.combobox_5.setVisible(True)
                    self.inputsize.setVisible(True)
                    self.inputsize_text.setVisible(True)
                    self.inputsigma.setVisible(True)
                    self.inputsigma_text.setVisible(True)
                    self.inputsize.setValue(3)
                    self.inputsigma.setValue(1)
                else:
                    if (self.optiontypeselect == "Médiane"):
                        self.widgetstacking_con.setMinimumSize(QSize(300,300))
                        self.widgetstacking_con.setMaximumSize(QSize(999999, 500))
                        self.inputsize.setVisible(True)
                        self.inputsize_text.setVisible(True)
                        self.inputiteration.setVisible(True)
                        self.inputiteration_text.setVisible(True)
                        self.inputsize.setValue(3)
                        self.inputiteration.setValue(1)

                    if (self.optiontypeselect == "Moyenne"):
                        self.widgetstacking_con.setMinimumSize(QSize(300,300))
                        self.widgetstacking_con.setMaximumSize(QSize(999999, 500))
                        self.inputsize.setVisible(True)
                        self.inputsize_text.setVisible(True)
                        self.inputiteration.setVisible(True)
                        self.inputiteration_text.setVisible(True)
                        self.inputsize.setValue(3)
                        self.inputiteration.setValue(1)

                    if (self.optiontypeselect == "Sobel"):
                        self.widgetstacking_con.setMaximumSize(QSize(999999, 300))
                        self.inputabsolute_text.setVisible(True)
                        self.inputabsolute.setVisible(True)
                    if (self.optiontypeselect == "Bilateral"):
                        self.widgetstacking_con.setMaximumSize(QSize(999999, 500))
                        self.inputsize.setVisible(True)
                        self.inputsize_text.setVisible(True)
                        self.inputsigmaC.setVisible(True)
                        self.inputSigmaC_text.setVisible(True)
                        self.inputSigmaS.setVisible(True)
                        self.inputSigmaS_text.setVisible(True)
                        self.inputsize.setValue(3)
                        self.inputsigmaC.setValue(0.5)
                        self.inputSigmaS.setValue(20)
                    
                    if (self.optiontypeselect == "Convolution"):
                        for i in range(3):
                            for j in range(3):
                                self.spin = QDoubleSpinBox() 
                                self.spin.setObjectName(f"{i,j}")
                                self.matrice_convolution_layout.addWidget(self.spin,i,j)
                                self.spin.valueChanged.connect(lambda ____, r=i, c=j, v=self.spin : self.positionchange(r, c, v))
                                self.spin.setVisible(True)
                    self.optiontypeselect = "Aucun"
        self.emitconvolutionmatrice()
        self.emitinputSigmaSValueChange()
        self.emitcombobox_2()
        self.emitcombobox_3()
        self.emitcombobox_4()
        self.emitcombobox_5()
        self.emitinputSizeValueChange()
        self.emitinputAbsoluteValueChange()
        self.emitinputiterationValueChange()
        self.emitinputsigmaCValueChange()
        self.emitinputsigmaValueChange()
        self.emitinputPrecisionValueChange()
        print("Option sélectionnée changée en :", self.combobox_2.currentText())
    
    """Méthode permettant d'actualiser les widget sous-option de notre filtre Gaussian(filtre staking)

    Args:
        self : Notre application
    """
    def sousoption_gaussian(self):  
        self.sousoptiontype = self.combobox_5.currentText()
        self.emitcombobox_5()
        print("Sous-Option changée en :", self.sousoptiontype)
        self.widgetstacking_con.setMaximumSize(QSize(999999, 400))
        self.inputsize.setVisible(True)
        self.inputsize_text.setVisible(True)
        self.inputsigma.setVisible(True)
        self.inputsigma_text.setVisible(True)
        if (self.sousoptiontype == "Simple"):
            self.inputsize.setValue(3)
            self.inputsigma.setValue(1)
        else:
            self.inputsize.setValue(5)
            self.inputsigma.setValue(2)
        self.emitinputsigmaValueChange()
        self.emitinputSizeValueChange()
        self.emitcombobox_5()

    """Méthode permettant d'actualiser la valeur de précision de notre stacking (utilisé dans le stacking avec Sgima)

    Args:
        self : Notre application
    """
    def valeur_precision_change(self):  
        self.valeurprecision = self.slider_stacking.value()
        self.emitcombobox_5()
        self.valeur_slide.setText(f"{self.valeurprecision}")
        print("Valeur précision changée en :", self.slider_stacking.value())
        self.emitinputPrecisionValueChange()
        self.emitslider_stacking()

    """Méthode permettant d'actualiser la méthode de stacking utilisée

    Args:
        self : Notre application
    """
    def selection_stacking_change(self):  
        self.generationtype = self.label_1_stacking.currentText()
        self.generationtype_con(self.generationtype)
        if (self.generationtype == "Valeur abérante") or (self.generationtype == "Sigma"):
            self.slider_stacking_text.setVisible(True)
            self.slider_stacking.setVisible(True)
            self.valeur_slide.setVisible(True)
        else:
            self.slider_stacking_text.setVisible(False)
            self.slider_stacking.setVisible(False)
            self.valeur_slide.setVisible(False)
        print("Staking changé en :", self.label_1_stacking.currentText())
        self.emitlabel_1_stacking()
    
    """Méthode permettant d'actualiser la couleur du cmap de notre image

    Args:
        self : Notre application
    """
    def couleur_change_cmap(self):  
        self.cmaptype = self.label_3_couleur.currentText()
        print("cmap change en :", self.label_3_couleur.currentText())
        self.emitlabel_3_couleur()
    
    """Méthode permettant d'actualiser les widget sous-option de notre passe haut et passe bas (filtre staking)

    Args:
        self : Notre application
    """
    def sousoption_butterworth(self):  
        self.sousoptiontype = self.combobox_4.currentText()
        print("Sous-Option changée en :", self.sousoptiontype)
        self.combobox_4.setVisible(True)
        self.inputordre.setVisible(True)
        self.inputordre_text.setVisible(True)
        self.inputfrequence.setVisible(True)
        self.inputfrequence_text.setVisible(True)
        self.inputfrequence.setValue(100)
        self.inputordre.setValue(1)
        self.widgetstacking_con.setMaximumSize(QSize(999999, 400))
        self.emitcombobox_4()
        self.emitinputordreValueChange()
        self.emitinputfrequenceValueChange()
    
    """Méthode permettant d'actualiser les widget sous-option de notre valeur abérante (filtre staking)

    Args:
        self : Notre application
    """
    def sousoption_valeur_aberante(self):  
        self.sousoptiontype = self.combobox_3.currentText()
        print("Sous-Option changée en :", self.sousoptiontype)
        self.combobox_3.setVisible(True)
        self.inputprecision.setVisible(True)
        self.inputprecision_text.setVisible(True)
        if (self.sousoptiontype == "Sigma"):
            self.inputprecision.setValue(5)
        else:
            self.inputprecision.setValue(1.5)
        self.widgetstacking_con.setMaximumSize(QSize(999999, 400))
        self.emitcombobox_3()
        self.emitinputPrecisionValueChange()
    
    """Méthode permettant d'actualiser la matrice en fonction des "input" mis dans la grille 3x3 de notre matrice de convolution

    Args:
        self : Notre application
        col : La colonne de notre valeur
        row : La colonne de notre ligne
        value : La valeur entrée
    """
    def positionchange(self,col,row,value):
        self.convolutionmatrice[col][row] = value.value()
        print("valeur changée : ", self.convolutionmatrice[col][row])
        self.emitconvolutionmatrice()

    """Méthode permettant de vérifier si la valeur de notre widget "input" est bien impair pour les filtres de stacking

    Args:
        self : Notre application
    """
    def checkimpair(self):
        if ((self.inputsize.value()%2) == 0):
            print("Votre chiffre doit être impair !")
            self.inputsize.setValue(self.inputsize.value()+1)
            self.emitinputSizeValueChange()