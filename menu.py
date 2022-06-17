import sys
from PyQt5.QtWidgets import *

def boutonPresse(a):
    print("Bonton presser", a.text())
def fonction():
    app = QApplication(sys.argv)
    fenetre = QMainWindow()
    fenetre.setWindowTitle(" EXEMPLE MENU") # Titre de la fenetre
    fenetre.setGeometry(400,300,400,300) # La résolution  de la fenetre

    menu = fenetre.addToolBar("Exemple Menus")
    menu1= QAction("Nouveau") # création de l'onglet nouveau
    menu.addAction(menu1)

    menu2 =QAction("Ouvrir")
    menu.addAction(menu2)

    menu3 =QAction("Copier")
    menu.addAction(menu3)
    menu4 =QAction("Coller")
    menu.addAction(menu4)
    menu5 =QAction("Enregistrer")
    menu.addAction(menu5)

    menu.actionTriggered[QAction].connect(boutonPresse)
    fenetre.show()
    app.exec_()

if __name__ == '__main__':
    fonction()