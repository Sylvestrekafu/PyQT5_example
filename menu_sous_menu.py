import  sys
from PyQt5.QtWidgets import *

class MesMenus(QTabWidget):
    def __init__(self, parent=None):
        super(MesMenus, self).__init__(parent)
        self.menu1 = QWidget()
        self.menu2 = QWidget()
        self.menu3 = QWidget()

        self.addTab(self.menu1, "Menu génrales")
        self.addTab(self.menu2, "Options")
        self.addTab(self.menu3, "Facultatif")

        self.onglet1()
        self.onglet2()
        self.onglet3()

        self.setWindowTitle("Multimenus")




    def onglet1(self):

        disposition = QFormLayout()
        disposition.addRow("Nom", QLineEdit())
        disposition.addRow("prenom", QLineEdit())
        disposition.addRow("Age", QLineEdit())
        self.setTabText(0,"Menu génrales")
        self.menu1.setLayout(disposition)

    def onglet2(self):
        disposition = QVBoxLayout()
        disposition.addWidget(QCheckBox("Foot"))
        disposition.addWidget(QCheckBox("Danse"))
        disposition.addWidget(QCheckBox("Vélo ou course"))
        self.setTabText(1,"Options")
        self.menu2.setLayout(disposition)


    def onglet3(self):
        disposition = QHBoxLayout()
        disposition.addWidget(QCheckBox("Fruit"))
        disposition.addWidget(QCheckBox("Glace"))
        disposition.addWidget((QCheckBox("Rien")))
        self.setTabText(2,"Facultatif")
        self.menu3.setLayout(disposition)




if __name__ == '__main__':

    app =QApplication(sys.argv)
    fenetre = MesMenus()
    fenetre.show()
    app.exec_()

