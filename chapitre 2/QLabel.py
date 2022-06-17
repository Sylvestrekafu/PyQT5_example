import sys
from PyQt5.QtWidgets import * #QApplication, QWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import * #QPixmap

class FenetreSimple(QWidget):
    def __init__(self):
        super().__init__()
        self.execute()

    def execute(self):
        self.resize(250, 300)
        self.move(50, 500)
        self.setWindowTitle("Bonjour tout le monde ! ")

        label1 = QLabel("PyQt", self)
        label1.setText(label1.text() + "5")
        label1.setMargin(5)
        label1.setIndent(15)

        pic = QPixmap("pyqt.png")
        label2 = QLabel(self)
        label2.setPixmap(pic)
        label2.move(60, 100)

        self.show()

if __name__ == '__main__':
    application = QApplication(sys.argv)
    fenetre = FenetreSimple()
    sys.exit(application.exec_())