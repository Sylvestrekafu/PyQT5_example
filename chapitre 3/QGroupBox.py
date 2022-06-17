import sys
from PyQt5.QtWidgets import *

def principal():

    application = QApplication(sys.argv)

    fenetre = QWidget()

    fenetre.setGeometry(100, 100, 200, 100)
    fenetre.setWindowTitle("QGroupBox")

    disposition = QGridLayout()
    fenetre.setLayout(disposition)

    groupe1 = QGroupBox("Validation")
    groupe1.setCheckable(True)
    disposition.addWidget(groupe1)

    boite1 = QVBoxLayout()
    groupe1.setLayout(boite1)

    boite1.addWidget(QPushButton("Valider"))
    boite1.addWidget(QPushButton("Annuler"))

    groupe2 = QGroupBox("Loisirs sportifs")
    groupe2.setCheckable(True)
    disposition.addWidget(groupe2)

    boite2 = QVBoxLayout()
    groupe2.setLayout(boite2)

    boite2.addWidget(QRadioButton("Cyclisme"))
    boite2.addWidget(QRadioButton("Football"))
    boite2.addWidget(QRadioButton("Rugby"))

    fenetre.setLayout(disposition)
    fenetre.show()

    application.exec_()

if __name__ == '__main__':
    principal()