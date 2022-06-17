import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from functools import partial


class Calculatrice(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Calculatrice")
        self.setFixedSize(235, 235)
        self.disposition = QVBoxLayout()
        self._widget = QWidget(self)
        self.setCentralWidget(self._widget)
        self._widget.setLayout(self.disposition)
        self.creation()
        self.creationBoutons()


    def creation(self):

        self.resultat = QLineEdit()
        self.resultat.setFixedHeight(60)
        self.resultat.setContentsMargins(10, 10, 10, 10)
        self.resultat.setAlignment(Qt.AlignRight)
        self.resultat.setReadOnly(True)
        self.disposition.addWidget(self.resultat)
        self.resultat.setText('')

    def creationBoutons(self):

        self.boutons = {}
        dispositionBoutons = QGridLayout()
        boutons = {
            '7': (0, 0),
            '8': (0, 1),
            '9': (0, 2),
            '/': (0, 3),
            'C': (0, 4),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '*': (1, 3),
            '(': (1, 4),
            '1': (2, 0),
            '2': (2, 1),
            '3': (2, 2),
            '-': (2, 3),
            ')': (2, 4),
            '0': (3, 0),
            '00': (3, 1),
            '.': (3, 2),
            '+': (3, 3),
            '=': (3, 4),
        }

        for btnTexte, pos in boutons.items():
            self.boutons[btnTexte] = QPushButton(btnTexte)
            self.boutons[btnTexte].setFixedSize(40, 40)
            dispositionBoutons.addWidget(self.boutons[btnTexte], pos[0], pos[1])
        self.disposition.addLayout(dispositionBoutons)


    def setAffichage(self, texte):

        self.resultat.setText(texte)
        self.resultat.repaint()


    def getAffichage(self):

        return self.resultat.text()


    def nettoyer(self):

        self.setAffichage('')


def evaluation(expression):

	try:
		resultat = str(eval(expression, {}, {}))
	except Exception:
		print('erreur')
		resultat = 'erreur'
	return resultat


class Controleur:

    def __init__(self, modele, vue):
        self._evaluation = modele
        self._vue = vue
        self.connectionSignaux()


    def calculer(self):

        resultat = self._evaluation(expression=self._vue.getAffichage())
        self._vue.setAffichage(resultat)


    def construireExpression(self, btn):

        expression = self._vue.getAffichage() + btn
        self._vue.setAffichage(expression)


    def connectionSignaux(self):

        self._vue.boutons['0'].clicked.connect(lambda: self.construireExpression('0'))
        self._vue.boutons['1'].clicked.connect(lambda: self.construireExpression('1'))
        self._vue.boutons['2'].clicked.connect(lambda: self.construireExpression('2'))
        self._vue.boutons['3'].clicked.connect(lambda: self.construireExpression('3'))
        self._vue.boutons['4'].clicked.connect(lambda: self.construireExpression('4'))
        self._vue.boutons['5'].clicked.connect(lambda: self.construireExpression('5'))
        self._vue.boutons['6'].clicked.connect(lambda: self.construireExpression('6'))
        self._vue.boutons['7'].clicked.connect(lambda: self.construireExpression('7'))
        self._vue.boutons['8'].clicked.connect(lambda: self.construireExpression('8'))
        self._vue.boutons['9'].clicked.connect(lambda: self.construireExpression('9'))
        self._vue.boutons['00'].clicked.connect(lambda: self.construireExpression('00'))

        self._vue.boutons['+'].clicked.connect(lambda: self.construireExpression('+'))
        self._vue.boutons['*'].clicked.connect(lambda: self.construireExpression('*'))
        self._vue.boutons['/'].clicked.connect(lambda: self.construireExpression('/'))
        self._vue.boutons['-'].clicked.connect(lambda: self.construireExpression('-'))
        self._vue.boutons['.'].clicked.connect(lambda: self.construireExpression('.'))

        self._vue.boutons['('].clicked.connect(lambda: self.construireExpression('('))
        self._vue.boutons[')'].clicked.connect(lambda: self.construireExpression(')'))

        self._vue.boutons['='].clicked.connect(self.calculer)
        self._vue.boutons['C'].clicked.connect(self._vue.nettoyer)


if __name__ == "__main__":
    pycalc = QApplication(sys.argv)
    vue = Calculatrice()
    Controleur(modele=evaluation, vue=vue)
    vue.show()
    sys.exit(pycalc.exec_())
