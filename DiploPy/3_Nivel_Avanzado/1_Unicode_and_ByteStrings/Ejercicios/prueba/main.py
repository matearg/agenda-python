# =================INSTALAR pyqt5 ==============    pip install PyQt5
# ================ Lanzar qt designer ==========    qt5-tools designer
# ================= PYQT5 DESIGNER =============    pip install PyQt5Designer
import sys
from PyQt5 import QtWidgets
import PyQt5 
from PyQt5.QtWidgets import  QApplication, QMainWindow
import os
from PyQt5 import QtCore as core
from PyQt5 import QtWidgets, uic

# IMPORTO VISTAS
from mainwind import Ui_MainWindow
 

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,):
        # ========== DESDE .UI =======================
        #super(MainWindow, self).__init__()
        #uic.loadUi('mainwind.ui', self)
        # ========== DESDE .PY ======================= pyuic5 nombre.ui -o nombre.py
        
        QtWidgets.QMainWindow.__init__(self,)
        Ui_MainWindow.__init__(self, )
        self.setupUi(self,)

        # ===============  ===========================
        self.btn_try.clicked.connect(self.try_connection)
 

    # =================== TRY CONNECTION ============================= 
    def try_connection(self, ): 
        print("dddd")



if __name__ == "__main__":
    dirname = os.path.dirname(PyQt5.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    QtWidgets.QApplication.addLibraryPath(plugin_path)

    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setWindowTitle("PRUEBA")
    widget.setFixedWidth(1290)
    widget.setFixedHeight(650)
    #mainwindow.try_connection()
    widget.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')

