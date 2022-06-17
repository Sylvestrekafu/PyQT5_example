import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QFormLayout

from PyQt5.QtGui import QFont, QFontInfo
from PyQt5.QtGui import QPixmap, QIcon


class Fenetre(QWidget):


    def __init__(self):

        super().__init__()

        self.setGeometry(100, 100, 300, 100)
        self.setWindowTitle(" QIcon")
        self.disposition = QFormLayout()

        self.iconeCollection = QIcon()

        self.icone1 = QPixmap('gras.png')
        self.iconeCollection.addPixmap(self.icone1, QIcon.Disabled)

        self.icone2 = QPixmap('italique.png')
        self.iconeCollection.addPixmap(self.icone2, QIcon.Active)

        self.boutonTest = QPushButton("Test")
        self.boutonTest.setIcon(self.iconeCollection)

        self.boutonTest2 = QPushButton("Test2")
        self.boutonTest2.setIcon(self.iconeCollection)
        self.boutonTest2.setDisabled(True)

        self.disposition.addRow(self.boutonTest, self.boutonTest2)
        self.setLayout(self.disposition)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = Fenetre()
    fenetre.show()
    sys.exit(app.exec_())