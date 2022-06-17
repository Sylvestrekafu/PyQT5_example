import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class RichEditor(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.filename = ""
        self.UI_Initialization()

    def Menubar(self):
        menubar = self.menuBar()
        file = menubar.addMenu("Fichier")

        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)

    def Toolbar(self):
        self.newAction = QAction("Nouveau", self)
        self.newAction.triggered.connect(self.new)
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.setStatusTip("Créer un document")

        self.openAction = QAction("Ouvrir", self)
        self.openAction.triggered.connect(self.open)
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.setStatusTip("Ouvrir un document existant")

        self.saveAction = QAction("Sauver", self)
        self.saveAction.triggered.connect(self.save)
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.setStatusTip("Sauver le document")

        self.addToolBarBreak()

    def Organize(self):
        fontbox = QFontComboBox(self)
        fontbox.currentFontChanged.connect(lambda font: self.text.setCurrentFont(font))
        fontSize = QSpinBox(self)
        fontSize.setSuffix(" pt")
        fontSize.valueChanged.connect(lambda size: self.text.setFontPointSize(size))
        fontSize.setValue(14)

        fontColor = QAction(QIcon("couleur_police.png"), "Changer la couleur du texte", self)
        fontColor.triggered.connect(self.fontColorChanged)

        backColor = QAction(QIcon("couleur_fond.png"), "Changer la couleur de fond", self)
        backColor.triggered.connect(self.highlight)

        boldAction = QAction(QIcon("gras.png"), "Gras", self)
        boldAction.triggered.connect(self.bold)

        italicAction = QAction(QIcon("italique.png"), "Italique", self)
        italicAction.triggered.connect(self.italic)

        underlAction = QAction(QIcon("souligner.png"), "Souligner", self)
        underlAction.triggered.connect(self.underline)

        strikeAction = QAction(QIcon("rayer.png"), "Rayer", self)
        strikeAction.triggered.connect(self.strike)

        alignLeft = QAction(QIcon("gauche.png"), "A gauche", self)
        alignLeft.triggered.connect(self.alignLeft)

        alignCenter = QAction(QIcon("centre.png"), "Au centre", self)
        alignCenter.triggered.connect(self.alignCenter)

        alignRight = QAction(QIcon("droite.png"), "A droite", self)
        alignRight.triggered.connect(self.alignRight)

        alignJustify = QAction(QIcon("justifier.png"), "Justifier", self)
        alignJustify.triggered.connect(self.alignJustify)

        self.organization = self.addToolBar("Format")
        self.organization.addWidget(fontbox)
        self.organization.addWidget(fontSize)
        self.organization.addSeparator()
        self.organization.addAction(fontColor)
        self.organization.addAction(backColor)

        self.organization.addSeparator()

        self.organization.addAction(boldAction)
        self.organization.addAction(italicAction)
        self.organization.addAction(underlAction)
        self.organization.addAction(strikeAction)

        self.organization.addSeparator()
        self.organization.addAction(alignLeft)
        self.organization.addAction(alignCenter)
        self.organization.addAction(alignRight)
        self.organization.addAction(alignJustify)

    def new(self):
        window = Main(self)
        window.show()

    def open(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open File', ".", "(*.txt)")
        if self.filename:
            with open(self.filename, "txt") as file:
                self.text.setText(file.read())

    def save(self):
        if not self.filename:
            self.filename = QFileDialog.getSaveFileName(self, 'Save File')

        if not self.filename.endswith(".txt"):
            self.filename += ".txt"

        with open(self.filename, "txt") as file:
            file.write(self.text.toHtml())

    def fontColorChanged(self):
        color = QColorDialog.getColor()
        self.text.setTextColor(color)

    def highlight(self):
        color = QColorDialog.getColor()
        self.text.setTextBackgroundColor(color)

    def bold(self):
        if self.text.fontWeight() == QFont.Bold:
            self.text.setFontWeight(QFont.Normal)
        else:
            self.text.setFontWeight(QFont.Bold)

    def italic(self):
        state = self.text.fontItalic()
        self.text.setFontItalic(not state)

    def underline(self):
        state = self.text.fontUnderline()
        self.text.setFontUnderline(not state)

    def strike(self):
        fmt = self.text.currentCharFormat()
        fmt.setFontStrikeOut(not fmt.fontStrikeOut())
        self.text.setCurrentCharFormat(fmt)

    def alignLeft(self):
        self.text.setAlignment(Qt.AlignLeft)

    def alignRight(self):
        self.text.setAlignment(Qt.AlignRight)

    def alignCenter(self):
        self.text.setAlignment(Qt.AlignCenter)

    def alignJustify(self):
        self.text.setAlignment(Qt.AlignJustify)

    def UI_Initialization(self):
        self.text = QTextEdit(self)
        self.Toolbar()
        self.Organize()
        self.Menubar()
        self.setWindowTitle("Editeur de texte ")
        self.text.setTabStopWidth(33)
        self.setCentralWidget(self.text)
        self.statusbar = self.statusBar()
        self.setGeometry(200, 200, 1000, 600)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = RichEditor()
    main.show()
    sys.exit(app.exec_())
