import sys
from PyQt5.QtWidgets import * #QApplication, QWidget

class FenetreSimple(QWidget):

    def __init__(self):
        super().__init__()
        self.execute()

    def execute(self):

        self.resize(250, 300)
        self.move(50, 500)
        self.setWindowTitle("Exemple QComboBox")

        self.label = QLabel("Utilisation de QComboBox", self)
        self.label.move(5, 5)

        self.cb = QComboBox(self)
        self.cb.addItem("TOGO")
        self.cb.addItem("GHANA")
        self.cb.addItems(["France", "Allemagne", "Belgique"])
        self.cb.setWindowTitle("QComboBox")
        self.cb.move(5, 30)
        self.cb.currentIndexChanged.connect(self.selectionchange)
        self.show()

        for ii in range(self.cb.count()):
            print(self.cb.itemText(ii))

    def selectionchange(self, i):

        self.label.setText(self.cb.currentText())

if __name__ == '__main__':
    application = QApplication(sys.argv)
    fenetre = FenetreSimple()
    sys.exit(application.exec_())