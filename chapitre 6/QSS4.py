import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox
from PyQt5.QtWidgets import QFormLayout, QLabel, QLineEdit, QComboBox

from PyQt5.QtGui import QFont

maFont = QFont('Chalkduster', 18, QFont.Bold)
maFont.setItalic(True)

maFont2 = QFont()
maFont2.setFamily('Futura')
maFont2.setPointSize(15)
maFont2.setCapitalization(QFont.Capitalize)
maFont2.setWeight(QFont.Medium)
maFont2.setUnderline(True)

feuille_de_style = """
.QWidget{ 
  background-color: red; 
}
.fenetre{ 
  background-color: red; 
}
QLabel{ 
  background-color: yellow; 
}
QComboBox{ 
  background-color: transparent;
  font-family:'Verdana';
  color: white;
  font-size: 14pt;
  font-weight: bold; 
}
QCheckBox::indicator::unchecked{
  border: 0px solid transparent;
  background-color: transparent;
}
QCheckBox::indicator::checked{
  border: 5px solid green;
  background-color: lightgreen;
}
#EnvoyerBtn{
  background-color: yellow;
}
"""

class Fenetre(QWidget):

    def __init__(self):

        super().__init__()

        self.setGeometry(100, 100, 250, 100)
        self.setWindowTitle("QSS4")
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
        self.boutonEnvoyer.setObjectName("EnvoyerBtn")

        self.boutonAnnuler = QPushButton("Annuler")
        self.disposition.addRow(self.boutonEnvoyer, self.boutonAnnuler)

        self.setLayout(self.disposition)

        self.nomLabel.setFont(maFont)

        self.prenomLabel.setFont(maFont2)
        self.loisirLabel.setFont(maFont2)
        self.veloLabel.setFont(maFont2)

        self.setStyleSheet(feuille_de_style)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    fenetre = Fenetre()
    fenetre.show()
    sys.exit(app.exec_())