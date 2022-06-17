import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class FenetreSimple(QWidget):

    def __init__(self):
        super().__init__()
        self.execute()

    def exempleSlot(self):
        print("Le bouton a été appuyé.")

    def execute(self):
        self.disposition = QVBoxLayout()

        self.resize(250, 300)
        self.move(50, 500)
        self.setWindowTitle("Signaux et slots")

        self.fermer = QPushButton("Fermer", clicked=self.exempleSlot)
        self.disposition.addWidget(self.fermer)

        self.setLayout(self.disposition)
        self.show()

if __name__ == '__main__':
    application = QApplication(sys.argv)
    fenetre = FenetreSimple()
    sys.exit(application.exec_())