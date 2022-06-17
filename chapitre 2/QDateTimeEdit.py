import sys
from PyQt5.QtWidgets import * #QApplication, QWidget
from PyQt5.QtCore import *

class FenetreSimple(QWidget):

    def __init__(self):

        super().__init__()
        self.execute()

    def execute(self):

        self.resize(250, 300)
        self.move(50, 500)
        self.setWindowTitle("Exemple QDateTimeEdit")

        self.dt = QDateTimeEdit(self)
        self.dt.move(5, 35)
        self.dt.setDate(QDate.currentDate())

        self.show()


if __name__ == '__main__':

    application = QApplication(sys.argv)
    fenetre = FenetreSimple()
    sys.exit(application.exec_())