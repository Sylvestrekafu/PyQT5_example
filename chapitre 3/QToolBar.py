import sys
from PyQt5.QtWidgets import *

def boutonPresse(a):
    print("Le bouton pressé est le suivant :", a.text())

def principal():

    application = QApplication(sys.argv)

    fenetre = QMainWindow()

    fenetre.setGeometry(100, 100, 350, 100)
    fenetre.setWindowTitle("QToolBar")

    barre = fenetre.addToolBar("Barre d'outils d'exemple")

    action1 = QAction("Créer")
    barre.addAction(action1)

    action2 = QAction("Ouvrir")
    barre.addAction(action2)

    action3 = QAction("Copier")
    barre.addAction(action3)

    action4 = QAction("Coller")
    barre.addAction(action4)

    barre.actionTriggered[QAction].connect(boutonPresse)

    fenetre.show()

    application.exec_()

if __name__ == '__main__':
    principal()