import sys
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox
from PyQt5.QtWidgets import QFormLayout, QLabel, QLineEdit, QComboBox

from PyQt5.QtGui import QFont, QPalette, QColor

maFont = QFont('Chalkduster', 18, QFont.Bold)
maFont.setItalic(True)

maFont2 = QFont()
maFont2.setFamily('Futura')
maFont2.setPointSize(15)
maFont2.setCapitalization(QFont.Capitalize)
maFont2.setWeight(QFont.Medium)
maFont2.setUnderline(True)

palette = QPalette()
palette.setColor(QPalette.ButtonText, QColor(0, 0, 255))

palette2 = QPalette()
palette2.setColor(QPalette.ButtonText, Qt.red)


class Fenetre(QWidget):

    def __init__(self):

        super().__init__()

        self.setGeometry(300, 200, 250, 200)
        self.setWindowTitle(" Formulaire")
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

        self.prenomLabel.setFont(maFont2)
        self.loisirLabel.setFont(maFont2)
        self.veloLabel.setFont(maFont2)

        self.boutonEnvoyer.setPalette(palette)
        self.boutonAnnuler.setPalette(palette2)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    fenetre = Fenetre()
    fenetre.show()
    sys.exit(app.exec_())