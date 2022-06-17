from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
import os
import sys


class EditeurDeTexte(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(EditeurDeTexte, self).__init__(*args, **kwargs)

        presentation = QVBoxLayout()
        self.editeur = QPlainTextEdit()
        self.path = None
        presentation.addWidget(self.editeur)

        containeur = QWidget()
        containeur.setLayout(presentation)
        self.setCentralWidget(containeur)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        barreOutils = QToolBar("Fichier")
        barreOutils.setIconSize(QSize(16, 16))
        self.addToolBar(barreOutils)
        menuFichier = self.menuBar().addMenu("&Fichier")

        OuvrirFichier_action = QAction(QIcon('ouvrir.png'), "Ouvrir fichier...", self)
        OuvrirFichier_action.setStatusTip("Ouvrier fichier")
        OuvrirFichier_action.triggered.connect(self.file_open)
        menuFichier.addAction(OuvrirFichier_action)
        barreOutils.addAction(OuvrirFichier_action)

        sauverFichier_action = QAction(QIcon('sauver.png'), "Sauver", self)
        sauverFichier_action.setStatusTip("Sauver la page courante")
        sauverFichier_action.triggered.connect(self.sauverFichier)
        menuFichier.addAction(sauverFichier_action)
        barreOutils.addAction(sauverFichier_action)

        sauverFichier_comme_action = QAction(QIcon('sauver_comme.png'), "Sauver comme...", self)
        sauverFichier_comme_action.setStatusTip("Sauver la page courante comme...")
        sauverFichier_comme_action.triggered.connect(self.sauverFichier_comme)
        menuFichier.addAction(sauverFichier_comme_action)
        barreOutils.addAction(sauverFichier_comme_action)

        imprimer_action = QAction(QIcon('imprimer.png'), "Imprimer...", self)
        imprimer_action.setStatusTip("Imprimer la page courante")
        imprimer_action.triggered.connect(self.file_imprimer)
        menuFichier.addAction(imprimer_action)
        barreOutils.addAction(imprimer_action)

        barreOutils_Edition = QToolBar("Édition")
        barreOutils_Edition.setIconSize(QSize(16, 16))
        self.addToolBar(barreOutils_Edition)
        menuEdition = self.menuBar().addMenu("&Édition")

        defaire_action = QAction(QIcon('defaire.png'), "Défaire", self)
        defaire_action.setStatusTip("Défaire le dernier changement")
        defaire_action.triggered.connect(self.editeur.undo)
        barreOutils_Edition.addAction(defaire_action)
        menuEdition.addAction(defaire_action)

        refaire_action = QAction(QIcon('refaire.png'), "Refaire", self)
        refaire_action.setStatusTip("Refaire le dernier changement")
        refaire_action.triggered.connect(self.editeur.redo)
        barreOutils_Edition.addAction(refaire_action)
        menuEdition.addAction(refaire_action)

        menuEdition.addSeparator()

        couper_action = QAction(QIcon('couper.png'), "Couper", self)
        couper_action.setStatusTip("Coupe le texte sélectionné")
        couper_action.triggered.connect(self.editeur.cut)
        barreOutils_Edition.addAction(couper_action)
        menuEdition.addAction(couper_action)

        copier_action = QAction(QIcon('copier.png'), "Copier", self)
        copier_action.setStatusTip("Copier le texte sélectionné")
        copier_action.triggered.connect(self.editeur.copy)
        barreOutils_Edition.addAction(copier_action)
        menuEdition.addAction(copier_action)

        coller_action = QAction(QIcon('coller.png'), "Coller", self)
        coller_action.setStatusTip("Coller depuis le presse-papier")
        coller_action.triggered.connect(self.editeur.paste)
        barreOutils_Edition.addAction(coller_action)
        menuEdition.addAction(coller_action)

        self.modifierTitre()
        self.show()

    def UI_Exception(self, s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    def file_open(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.txt);All files (*.*)")

        if path:
            try:
                with open(path, 'rU') as f:
                    text = f.read()

            except Exception as e:
                self.UI_Exception(str(e))

            else:
                self.path = path
                self.editeur.setPlainText(text)
                self.modifierTitre()

    def sauverFichier(self):
        if self.path is None:
            return self.sauverFichier_comme()

        self.sauverChemin(self.path)

    def sauverFichier_comme(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Text documents (*.txt);All files (*.*)")

        if not path:
            return

        self.sauverChemin(path)

    def sauverChemin(self, path):
        text = self.editeur.toPlainText()
        try:
            with open(path, 'w') as f:
                f.write(text)

        except Exception as e:
            self.UI_Exception(str(e))

        else:
            self.path = path
            self.modifierTitre()

    def file_imprimer(self):
        dlg = QPrintDialog()
        if dlg.exec_():
            self.editeur.print(dlg.printer())

    def modifierTitre(self):
        self.setWindowTitle("%s - Le petit éditeur de texte" % (os.path.basename(self.path) if self.path else "Untitled"))

    def passerModeWrap(self):
        self.editeur.setLineWrapMode( 1 if self.editeur.lineWrapMode() == 0 else 0 )


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setApplicationName("Le petit éditeur de texte")

    window = EditeurDeTexte()
    app.exec_()