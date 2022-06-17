import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox
from PyQt5.QtWidgets import QFormLayout, QLabel, QLineEdit, QComboBox

from PyQt5.QtGui import QFont, QFontInfo

maFont = QFont()
maFont.setFamily('LA_POLICE_INCONNUE')
maFont.setPointSize(15)
maFont.setCapitalization(QFont.Capitalize)
maFont.setWeight(QFont.Medium)

maFont.setStyleHint(QFont.Cursive)

# testFont = QFontInfo(maFont)
# print('Police par défaut ? => ' + testFont.family())

class Fenetre(QWidget):

    def __init__(self):

        super().__init__()

        self.setGeometry(100, 100, 250, 100)
        self.setWindowTitle(" QFontInfo")
        self.disposition = QFormLayout()

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