import sys
from PyQt5.QtWidgets import * #QApplication, QWidget

class FenetreSimple(QWidget):
    def __init__(self):
        super().__init__()
        self.execute()

    def execute(self):
        self.resize(320, 300)
        self.move(50, 500)
        self.setWindowTitle("Exemple QTextEdit")

        label = QLabel("Nom : ", self)
        label.move(10, 15)

        text_edit = QTextEdit(self)
        text_edit.move(5, 30)
        text_edit.resize(250, 150)
        text_edit.append(u"<font color='red'><b> rouge et en gras</b></font><br /><font color='blue'><i> bleu et en italique</i></font><br />")
        self.show()

if __name__ == '__main__':
    application = QApplication(sys.argv)
    fenetre = FenetreSimple()
    sys.exit(application.exec_())