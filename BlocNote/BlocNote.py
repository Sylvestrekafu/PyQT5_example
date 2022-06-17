import sys
import  os
from PyQt5.QtGui import *
from  PyQt5.QtCore import *
from  PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *

class EditeurdeTexte(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(EditeurdeTexte, self).__init__(*args, **kwargs)

        presentation = QVBoxLayout()
        self.editeur = QPlainTextEdit()
        self.path = None
        presentation.addWidget(self.editeur)

        contener = QWidget()
        contener.setLayout(presentation)
        self.setCentralWidget(contener)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        bareOutils = QToolBar("Fichier")
        bareOutils.setIconSize(QSize(20,20))
        self.addToolBar(bareOutils)

        # Menu
        menuFichier = self.menuBar().addMenu("&Fichier")
        ouvrirFichier_action = QAction(QIcon("ouvrir.png"),"Ouvrir Fichier...", self)
        ouvrirFichier_action.setStatusTip("Ouvrir Fichier")
        ouvrirFichier_action.triggered.connect(self.file_open)
        menuFichier.addAction(ouvrirFichier_action)
        bareOutils.addAction(ouvrirFichier_action)

        sauverFicher_action = QAction(QIcon("sauver.png"), "Enregistrer Fichier...",self)
        sauverFicher_action.setStatusTip("Enregistrer")
        sauverFicher_action.triggered.connect(self.SauverFicher)
        menuFichier.addAction(sauverFicher_action)
        bareOutils.addAction(sauverFicher_action)

        sauverFichier_comme_action = QAction(QIcon("sauver_comme.png"),  "Enregistrer comme..", self)
        sauverFichier_comme_action.setStatusTip("Enregistrer comme")
        sauverFichier_comme_action.triggered.connect(self.sauverFichercome)
        menuFichier.addAction(sauverFichier_comme_action)
        bareOutils.addAction(sauverFichier_comme_action)

        imprimer_action = QAction(QIcon("imprimer.png"), "imprimer Fichier...", self)
        imprimer_action.setStatusTip("Imprimer")
        imprimer_action.triggered.connect(self.file_imprimer)
        menuFichier.addAction(imprimer_action)
        bareOutils.addAction(imprimer_action)


        barreOutils_Edition = QToolBar("Edition")
        barreOutils_Edition.setIconSize(QSize(20,20))
        self.addToolBar(barreOutils_Edition)
        menuEdition =  self.menuBar().addMenu("&Edition")

        defaire_action = QAction(QIcon("defaire.png"), "Défaire....",self)
        defaire_action.setStatusTip("defaire le dernier changement")
        defaire_action.triggered.connect(self.editeur.undo)
        barreOutils_Edition.addAction(defaire_action)
        menuEdition.addAction(defaire_action)

        refaire_action = QAction(QIcon("refaire.png"), "Refaire ...",self)
        refaire_action.setStatusTip("Refaire  le derier changement")
        defaire_action.triggered.connect(self.editeur.redo)
        barreOutils_Edition.addAction(refaire_action)
        menuEdition.addAction(refaire_action)

        menuEdition.addSeparator()

        couper_action = QAction(QIcon("couper.png"), "Couper....", self)
        couper_action.setStatusTip("Couper le texte selectionné")
        couper_action.triggered.connect(self.editeur.cut)
        barreOutils_Edition.addAction(couper_action)
        menuEdition.addAction(couper_action)

        copier_action = QAction(QIcon("copier.png"), "Copier ...",self)
        copier_action.setStatusTip("Copier la selection")
        copier_action.triggered.connect(self.editeur.copy)
        barreOutils_Edition.addAction(copier_action)
        menuEdition.addAction(copier_action)

        coller_action = QAction(QIcon("coller.png"), "Coller...", self)
        coller_action.setStatusTip("Coller la selection")
        coller_action.triggered.connect(self.editeur.paste)
        barreOutils_Edition.addAction(coller_action)
        menuEdition.addAction(coller_action)

        self.ModifierTitre()
        self.show()






    def file_open(self):
        path, _= QFileDialog.getOpenFileName(self, "Ouvrir un fichier", "Text  documents (*.txt); All files(*.*)")

        if path:
            try:
                with open(path,"rU") as f:
                    text = f.read()

            except Exception as e:
                self.UiException(str(e))




    def SauverFicher(self):
        if self.path is None:
            return  self.sauverFichercome()
        self.sauverChemin(self.path)



    def sauverFichercome(self):
        path, _= QFileDialog(self, "Enregistrer","", "text documents(*.txt); All files(*.*)")

        if not  path:
            return  self.sauverChemin(path)

    def sauverChemin(self,path):
        text = self.editeur.toPlainText()
        try:
            with open(path, 'w') as  f:
                f.write(text)
        except Exception as e:
            self.UiException(str(e))

        else:
            self.path = path
            self.ModifierTitre()





    def  file_imprimer(self):
        dlg =QPrintDialog()
        if dlg.exec_():
            self.editeur.print(dlg.printer())


    def ModifierTitre(self):
        self.setWindowTitle("%s- Exemple d'éditeur de texte" %(os.path.basename(self.path) if self.path else  "Sans Titre"))

    def PassermodeWrap(self):
        self.editeur.setLineWrapMode(1 if self.editeur.setLineWrapMode()==0 else 0)


    def UiException(self,s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.critical)
        dlg.show()




if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setApplicationName("exemple d'étideur de texte")
    fenetre = EditeurdeTexte()
    app.exec_()

