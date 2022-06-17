import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox
from PyQt5.QtWidgets import QFormLayout, QLabel, QLineEdit, QComboBox, QRadioButton

from PyQt5.QtCore import QRect, QPropertyAnimation


class FenetreSimple(QWidget):
    def __init__(self):
        super().__init__()
        self.execute()

    def execute(self):
        self.resize(250, 300)
        self.move(50, 500)
        self.setWindowTitle(" Exemple Animation")

        self.label = QLabel("Un label", self)
        self.label.move(5, 5)

        self.line_edit = QLineEdit(self)
        self.line_edit.move(5, 30)
        self.line_edit.resize(150, 20)
        self.line_edit.setText("Une zone de texte")

        self.bouton = QPushButton(self)
        self.bouton.move(5, 60)
        self.bouton.setText("Cliquez")

        self.animation = QPropertyAnimation(self.bouton, b"geometry")
        self.animation.setDuration(3000)
        self.animation.setLoopCount(2)
        self.animation.setStartValue(QRect(5, 60, 100, 100))
        self.animation.setEndValue(QRect(5, 60, 110, 150))
        self.animation.start()
        self.show()


if __name__ == '__main__':
    application = QApplication(sys.argv)
    fenetre = FenetreSimple()
    sys.exit(application.exec_())