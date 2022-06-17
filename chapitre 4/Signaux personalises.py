import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MonWidgetSimple(QWidget):

    simple = pyqtSignal()
    intListe = pyqtSignal(int, list, str)

    def __init__(self, parent=None):

        super(MonWidgetSimple, self).__init__(parent)

        self.resize(250, 300)
        self.move(50, 500)

        self.simple.connect(self.simpleSlot)
        self.intListe.connect(self.intListeSlot)

        self.bouton = QPushButton('Cliquez test', self)
        self.bouton.clicked.connect(self.boutonSlot)

    def boutonSlot(self, checked=False):

        self.simple.emit()
        self.intListe.emit(42, [1, 2, 3], 'coucou')

    @pyqtSlot()
    def simpleSlot(self):

        print("Slot personnalisé sans argument")

    @pyqtSlot(int, list, str)
    def intListeSlot(self, *args):

        print("Slot personnalisé avec arguments")
        print(args[0])
        print(args[1])
        print(args[2])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MonWidgetSimple()
    widget.show()
    app.exec_()