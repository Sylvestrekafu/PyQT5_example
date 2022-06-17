import sys
from PyQt5.QtWidgets import *

class MyQTabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(MyQTabWidget, self).__init__(parent)
        self.onglet1 = QWidget()
        self.onglet2 = QWidget()
        self.onglet3 = QWidget()

        self.addTab(self.onglet1, "Données générales")
        self.addTab(self.onglet2, "Sports préférés")
        self.addTab(self.onglet3, "Loisirs culturels préférés")
        self.creationOnglet1()
        self.creationOnglet2()
        self.creationOnglet3()
        self.setWindowTitle("QTabWidget")

    def creationOnglet1(self):
        disposition = QFormLayout()
        disposition.addRow("Nom", QLineEdit())
        disposition.addRow("Prénom", QLineEdit())
        disposition.addRow("Ville", QLineEdit())
        self.setTabText(0, "Données générales")
        self.onglet1.setLayout(disposition)

    def creationOnglet2(self):
        disposition = QVBoxLayout()
        disposition.addWidget(QCheckBox("Football"))
        disposition.addWidget(QCheckBox("Cyclisme"))
        disposition.addWidget(QCheckBox("Tennis"))
        self.setTabText(1, "Sports préférés")
        self.onglet2.setLayout(disposition)

    def creationOnglet3(self):
        disposition = QHBoxLayout()
        disposition.addWidget(QCheckBox("Visite de musées"))
        disposition.addWidget(QCheckBox("Musique"))
        disposition.addWidget(QCheckBox("Dessin et arts graphiques"))
        self.setTabText(2, "Loisirs culturels préférés")
        self.onglet3.setLayout(disposition)


def principal():
    application = QApplication(sys.argv)
    composant = MyQTabWidget()
    composant.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    principal()