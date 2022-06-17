import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from functools import partial

class FenetreSimple(QWidget):

    def __init__(self):
        super().__init__()
        self.execute()

    def slot(self, str):
        print("Le bouton appuyé est le suivant : " + str)

    def execute(self):
        self.disposition = QVBoxLayout()

        self.resize(100, 300)
        self.move(50, 500)
        self.setWindowTitle("Lambda et partial")

        self.boutonPlus = QPushButton("+")
        self.disposition.addWidget(self.boutonPlus)
        self.boutonPlus.clicked.connect(lambda: self.slot("+"))

        self.boutonFois = QPushButton("*")
        self.disposition.addWidget(self.boutonFois)
        self.boutonFois.clicked.connect(lambda: self.slot("*"))

        self.boutonMoins = QPushButton("-")
        self.disposition.addWidget(self.boutonMoins)
        self.boutonMoins.clicked.connect(partial(self.slot, "-"))

        self.boutonDiviser = QPushButton("/")
        self.disposition.addWidget(self.boutonDiviser)
        self.boutonDiviser.clicked.connect(partial(self.slot, "/"))

        self.setLayout(self.disposition)
        self.show()

if __name__ == '__main__':
    application = QApplication(sys.argv)
    fenetre = FenetreSimple()
    sys.exit(application.exec_())