import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox
from PyQt5.QtWidgets import QFormLayout, QLabel, QLineEdit, QComboBox

from PyQt5.QtGui import QFont, QFontInfo
from PyQt5.QtGui import QPixmap


maFont = QFont()
maFont.setFamily('Arial Black')
maFont.setPointSize(15)
maFont.setCapitalization(QFont.Capitalize)
maFont.setWeight(QFont.Medium)


class Fenetre(QWidget):

    def __init__(self):

        super().__init__()

        self.setGeometry(100, 100, 300, 100)
        self.setWindowTitle(" QPixmap")
        self.disposition = QFormLayout()

        self.logoLabel = QLabel("Logo : ")
        self.logo = QLabel()
        self.image = QPixmap('pyqt.png')
        self.logo.setPixmap(self.image)
        self.disposition.addRow(self.logoLabel, self.logo)

        self.nomLabel = QLabel("Nom : ")
        self.nom = QLineEdit()
        self.disposition.addRow(self.nomLabel, self.nom)

        self.prenomLabel = QLabel("Prénom : ")
        self.prenom = QLineEdit()
        self.disposition.addRow(self.prenomLabel, self.prenom)

        self.loisirLabel = QLabel("Loisir préféré : ")
        self.loisir = QComboBox()
        self.loisir.addItems(["Pratique sportive", "Pratique artistique", "Programmation informatique", "Voyages"])
        self.disposition.addRow(self.loisirLabel, self.loisir)

        self.veloLabel = QLabel("Possède un vélo ?")
        self.velo = QCheckBox()
        self.velo.setChecked(True)
        self.disposition.addRow(self.veloLabel, self.velo)

        self.boutonEnvoyer = QPushButton("Envoyer")
        self.boutonAnnuler = QPushButton("Annuler")
        self.disposition.addRow(self.boutonEnvoyer, self.boutonAnnuler)

        self.setLayout(self.disposition)

        self.nomLabel.setFont(maFont)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = Fenetre()
    fenetre.show()
    sys.exit(app.exec_())