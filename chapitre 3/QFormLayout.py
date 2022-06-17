from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFormLayout, QLabel, QLineEdit, QComboBox

app = QApplication([])

fenetre = QWidget()

fenetre.setGeometry(100, 100, 200, 100)
fenetre.setWindowTitle("QFormLayout")
disposition = QFormLayout()

nomLabel = QLabel("Nom : ")
nom = QLineEdit()
disposition.addRow(nomLabel, nom)

prenomLabel = QLabel("Prénom : ")
prenom = QLineEdit()
disposition.addRow(prenomLabel, prenom)

loisirLabel = QLabel("Loisir préféré : ")
loisir = QComboBox()
loisir.addItems(["Pratique sportive", "Pratique artistique", "Programmation informatique", "Voyages"])
disposition.addRow(loisirLabel, loisir)

disposition.addRow(QPushButton("Envoyer"),QPushButton("Annuler"))

fenetre.setLayout(disposition)
fenetre.show()

app.exec_()