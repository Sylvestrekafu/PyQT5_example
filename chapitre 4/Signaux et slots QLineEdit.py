import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class FenetreSimple(QWidget):

    def __init__(self):
        super().__init__()
        self.execute()

    def exempleSlot(self):
        texteCourant = self.edition.text()
        self.editionCopie.setText(texteCourant)

    def execute(self):
        self.disposition = QVBoxLayout()

        self.resize(250, 300)
        self.move(50, 500)
        self.setWindowTitle("Signaux et slots")

        self.edition = QLineEdit()
        self.disposition.addWidget(self.edition)

        self.editionCopie = QLineEdit()
        self.disposition.addWidget(self.editionCopie)

        self.edition.textChanged.connect(self.exempleSlot)

        self.setLayout(self.disposition)
        self.show()

if __name__ == '__main__':
    application = QApplication(sys.argv)
    fenetre = FenetreSimple()
    sys.exit(application.exec_())