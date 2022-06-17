import sys
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox
from PyQt5.QtWidgets import QFormLayout, QLabel, QLineEdit, QComboBox

from PyQt5.QtGui import QFont, QPalette, QColor, QBrush

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

brush3 = QBrush(Qt.red, Qt.Dense3Pattern)

palette3 = QPalette()
palette3.setBrush(QPalette.Window, brush3)

class Fenetre(QWidget):

    def __init__(self):

        super().__init__()

        self.setGeometry(100, 100, 250, 100)
        self.setWindowTitle("Chapitre 6 - QBrush")
        self.disposition = QFormLayout()

        self.nomLabel = QLabel("Nom : ")
        self.nom = QLineEdit()
        self.disposition.addRow(self.nomLabel, self.nom)

        self.boutonEnvoyer = QPushButton("Envoyer")
        self.boutonAnnuler = QPushButton("Annuler")
        self.disposition.addRow(self.boutonEnvoyer, self.boutonAnnuler)

        self.setLayout(self.disposition)

        self.nomLabel.setFont(maFont)

        self.boutonEnvoyer.setPalette(palette)
        self.boutonAnnuler.setPalette(palette2)
        self.setPalette(palette3)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    fenetre = Fenetre()
    fenetre.show()
    sys.exit(app.exec_())