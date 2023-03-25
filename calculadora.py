from PySide6.QtWidgets import *
from PySide6.QtCore import *
from __feature__ import snake_case, true_property
import sys

class calculadora(QMainWindow):

    def diseño(self):

        # Fondo calculadora
        self.set_fixed_size(420,390)
        self.style_sheet = ("background: #212F3D;")

        # Contenedor resultado
        self.fr_resultado = QFrame(self)
        self.fr_resultado.geometry = QRect(10,10,400,50)
        self.fr_resultado.style_sheet = "background: white;"

        # Texto resultado
        self.resultado = QLabel(self.fr_resultado)
        self.resultado.geometry = QRect(0.5,0.5,390,40)
        self.resultado.alignment = Qt.AlignCenter
        self.resultado.style_sheet = "font-size: 20px;"
        self.resultado.text = ""

        # Botones

        self.fr_boton_1 = QPushButton(self)
        self.fr_boton_1.geometry = QRect(10,230,70,70)
        self.fr_boton_1.text = "1"
        self.fr_boton_1.style_sheet = "background: #B3B6B7;"

        self.fr_boton_2 = QPushButton(self)
        self.fr_boton_2.geometry = QRect(90,230,70,70)
        self.fr_boton_2.text = "2"
        self.fr_boton_2.style_sheet = "background: #B3B6B7;"

        self.fr_boton_3 = QPushButton(self)
        self.fr_boton_3.geometry = QRect(170,230,70,70)
        self.fr_boton_3.text = "3"
        self.fr_boton_3.style_sheet = "background: #B3B6B7;"

        self.fr_boton_4 = QPushButton(self)
        self.fr_boton_4.geometry = QRect(10,150,70,70)
        self.fr_boton_4.text = "4"
        self.fr_boton_4.style_sheet = "background: #B3B6B7;"

        self.fr_boton_5 = QPushButton(self)
        self.fr_boton_5.geometry = QRect(90,150,70,70)
        self.fr_boton_5.text = "5"
        self.fr_boton_5.style_sheet = "background: #B3B6B7;"

        self.fr_boton_6 = QPushButton(self)
        self.fr_boton_6.geometry = QRect(170,150,70,70)
        self.fr_boton_6.text = "6"
        self.fr_boton_6.style_sheet = "background: #B3B6B7;"

        self.fr_boton_7 = QPushButton(self)
        self.fr_boton_7.geometry = QRect(10,70,70,70)
        self.fr_boton_7.text = "7"
        self.fr_boton_7.style_sheet = "background: #B3B6B7;"

        self.fr_boton_8 = QPushButton(self)
        self.fr_boton_8.geometry = QRect(90,70,70,70)
        self.fr_boton_8.text = "8"
        self.fr_boton_8.style_sheet = "background: #B3B6B7;"

        self.fr_boton_9 = QPushButton(self)
        self.fr_boton_9.geometry = QRect(170,70,70,70)
        self.fr_boton_9.text = "9"
        self.fr_boton_9.style_sheet = "background: #B3B6B7;"

        self.fr_boton_0 = QPushButton(self)
        self.fr_boton_0.geometry = QRect(10,310,150,70)
        self.fr_boton_0.text = "0"
        self.fr_boton_0.style_sheet = "background: #B3B6B7;"

        self.fr_boton_punto = QPushButton(self)
        self.fr_boton_punto.geometry = QRect(170,310,70,70)
        self.fr_boton_punto.text = "."
        self.fr_boton_punto.style_sheet = "background: #B3B6B7;"

        self.fr_boton_ce = QPushButton(self)
        self.fr_boton_ce.geometry = QRect(260,70,70,70)
        self.fr_boton_ce.text = "CE"
        self.fr_boton_ce.style_sheet = "background: #1F618D;"

        self.fr_boton_dividir = QPushButton(self)
        self.fr_boton_dividir.geometry = QRect(260,150,70,70)
        self.fr_boton_dividir.text = "/"
        self.fr_boton_dividir.style_sheet = "background: #B3B6B7;"

        self.fr_boton_resta = QPushButton(self)
        self.fr_boton_resta.geometry = QRect(260,230,70,70)
        self.fr_boton_resta.text = "-"
        self.fr_boton_resta.style_sheet = "background: #B3B6B7;"

        self.fr_boton_total = QPushButton(self)
        self.fr_boton_total.geometry = QRect(260,310,70,70)
        self.fr_boton_total.text = "="
        self.fr_boton_total.style_sheet = "background: #B3B6B7;"


        self.fr_boton_c = QPushButton(self)
        self.fr_boton_c.geometry = QRect(340,70,70,70)
        self.fr_boton_c.text = "C"
        self.fr_boton_c.style_sheet = "background: #B03A2E;"

        self.fr_boton_multipicar = QPushButton(self)
        self.fr_boton_multipicar.geometry = QRect(340,150,70,70)
        self.fr_boton_multipicar.text = "*"
        self.fr_boton_multipicar.style_sheet = "background: #B3B6B7;"

        self.fr_boton_suma = QPushButton(self)
        self.fr_boton_suma.geometry = QRect(340,230,70,150)
        self.fr_boton_suma.text = "+"
        self.fr_boton_suma.style_sheet = "background: #239B56;"

app = QApplication(sys.argv)
window = calculadora()
window.diseño()
window.show()
sys.exit(app.exec())
