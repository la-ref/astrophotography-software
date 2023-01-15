from PyQt6.QtWidgets import (QVBoxLayout, QWidget,QApplication)
from Interface_front import Interface_front


class Logiciel(QWidget):
    def __init__(self,folder):
        super().__init__()
        self.setWindowTitle("Logiciel d'édition profesionnel d'image")
        self.verticalLayout = QVBoxLayout()
        self.widgetinterface = Interface_front(folder)
        self.verticalLayout.addWidget(self.widgetinterface)
        self.setLayout(self.verticalLayout)
        self.show()

if __name__ == "__main__" :
    import sys
    from PyQt6.QtWidgets import QApplication
    from astropy.visualization import simple_norm

    app = QApplication(sys.argv)
    fv = Logiciel('./img/M13_blue')

    sys.exit(app.exec())