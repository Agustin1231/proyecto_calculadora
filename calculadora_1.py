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
        self.resultado.style_sheet = """
            color: black; 
            font-size: 20px;
        """
        self.resultado.text = ""
        self.lista_1 = [] # Lista donde se guarda el primer numero a operar
        self.lita_2 = [] # Lista donde se guarda el segundo numero a operar
        self.numero_1 = 0 
        self.numero_2 = 0
        
    def __init__(self):
        
        super().__init__() 
        # Botones
        self.boton_1 = QPushButton("1",self)
        self.boton_1.geometry = QRect(10,230,70,70)
        self.boton_1.clicked.connect(self.agregar)
        self.boton_1.style_sheet = "background: #B3B6B7;"

        self.boton_2 = QPushButton("2",self)
        self.boton_2.geometry = QRect(90,230,70,70)
        self.boton_2.clicked.connect(self.agregar)
        self.boton_2.style_sheet = "background: #B3B6B7;"

        self.boton_3 = QPushButton("3",self)
        self.boton_3.geometry = QRect(170,230,70,70)
        self.boton_3.clicked.connect(self.agregar)
        self.boton_3.style_sheet = "background: #B3B6B7;"

        self.boton_4 = QPushButton("4",self)
        self.boton_4.geometry = QRect(10,150,70,70)
        self.boton_4.clicked.connect(self.agregar)
        self.boton_4.style_sheet = "background: #B3B6B7;"

        self.boton_5 = QPushButton("5",self)
        self.boton_5.geometry = QRect(90,150,70,70)
        self.boton_5.clicked.connect(self.agregar)
        self.boton_5.style_sheet = "background: #B3B6B7;"

        self.boton_6 = QPushButton("6",self)
        self.boton_6.geometry = QRect(170,150,70,70)
        self.boton_6.clicked.connect(self.agregar)
        self.boton_6.style_sheet = "background: #B3B6B7;"

        self.boton_7 = QPushButton("7",self)
        self.boton_7.geometry = QRect(10,70,70,70)
        self.boton_7.clicked.connect(self.agregar)
        self.boton_7.style_sheet = "background: #B3B6B7;"

        self.boton_8 = QPushButton("8",self)
        self.boton_8.geometry = QRect(90,70,70,70)
        self.boton_8.clicked.connect(self.agregar)
        self.boton_8.style_sheet = "background: #B3B6B7;"

        self.boton_9 = QPushButton("9",self)
        self.boton_9.geometry = QRect(170,70,70,70)
        self.boton_9.clicked.connect(self.agregar)
        self.boton_9.style_sheet = "background: #B3B6B7;"

        self.boton_0 = QPushButton("0",self)
        self.boton_0.geometry = QRect(10,310,150,70)
        self.boton_0.clicked.connect(self.agregar)
        self.boton_0.style_sheet = "background: #B3B6B7;"

        self.boton_punto = QPushButton(".",self)
        self.boton_punto.geometry = QRect(170,310,70,70)
        self.boton_punto.clicked.connect(self.agregar)
        self.boton_punto.style_sheet = "background: #B3B6B7;"

        self.boton_ce = QPushButton("CE",self)
        self.boton_ce.geometry = QRect(260,70,70,70)
        self.boton_ce.clicked.connect(self.operaciones)
        self.boton_ce.style_sheet = "background: #1F618D;"

        self.boton_dividir = QPushButton("/",self)
        self.boton_dividir.geometry = QRect(260,150,70,70)
        self.boton_dividir.clicked.connect(self.operaciones)
        self.boton_dividir.style_sheet = "background: #B3B6B7;"

        self.boton_resta = QPushButton("-",self)
        self.boton_resta.geometry = QRect(260,230,70,70)
        self.boton_resta.clicked.connect(self.operaciones)
        self.boton_resta.style_sheet = "background: #B3B6B7;"

        self.boton_total = QPushButton("=",self)
        self.boton_total.geometry = QRect(260,310,70,70)
        self.boton_total.clicked.connect(self.operaciones)
        self.boton_total.style_sheet = "background: #B3B6B7;"


        self.boton_c = QPushButton("C",self)
        self.boton_c.geometry = QRect(340,70,70,70)
        self.boton_c.clicked.connect(self.operaciones)
        self.boton_c.style_sheet = "background: #B03A2E;"

        self.boton_multiplicar = QPushButton("*",self)
        self.boton_multiplicar.geometry = QRect(340,150,70,70)
        self.boton_multiplicar.clicked.connect(self.operaciones)
        self.boton_multiplicar.style_sheet = "background: #B3B6B7;"

        self.boton_suma = QPushButton("+",self)
        self.boton_suma.geometry = QRect(340,230,70,150)
        self.boton_suma.clicked.connect(self.operaciones)
        self.boton_suma.style_sheet = "background: #239B56;"

   
    def agregar(self):
        boton = self.sender()
        if boton == self.boton_1:
            self.resultado.text = self.resultado.text+"1"
            self.lista_1.append(1)
            self.numero_1 = float("".join(map(str, self.lista_1))) # Utilizamos map() para convertir los elementos de una lista en una cadena y utilizamos join() para unirla en una sola cadena, despues float para decir que es una cadena decimal

        elif boton == self.boton_2:
            self.resultado.text = self.resultado.text+"2"
            self.lista_1.append(2)
            self.numero_1 = float("".join(map(str, self.lista_1))) # Utilizamos map() para convertir los elementos de una lista en una cadena y utilizamos join() para unirla en una sola cadena, despues float para decir que es una cadena decimal

        elif boton == self.boton_3:
            self.resultado.text = self.resultado.text+"3"
            self.lista_1.append(3)
            self.numero_1 = float("".join(map(str, self.lista_1))) # Utilizamos map() para convertir los elementos de una lista en una cadena y utilizamos join() para unirla en una sola cadena, despues float para decir que es una cadena decimal

        elif boton == self.boton_4:
            self.resultado.text = self.resultado.text+"4"
            self.lista_1.append(4)
            self.numero_1 = float("".join(map(str, self.lista_1))) # Utilizamos map() para convertir los elementos de una lista en una cadena y utilizamos join() para unirla en una sola cadena, despues float para decir que es una cadena decimal

        elif boton == self.boton_5:
            self.resultado.text = self.resultado.text+"5"
            self.lista_1.append(5)
            self.numero_1 = float("".join(map(str, self.lista_1))) # Utilizamos map() para convertir los elementos de una lista en una cadena y utilizamos join() para unirla en una sola cadena, despues float para decir que es una cadena decimal

        elif boton == self.boton_6:
            self.resultado.text = self.resultado.text+"6"
            self.lista_1.append(6)
            self.numero_1 = float("".join(map(str, self.lista_1))) # Utilizamos map() para convertir los elementos de una lista en una cadena y utilizamos join() para unirla en una sola cadena, despues float para decir que es una cadena decimal

        elif boton == self.boton_7:
            self.resultado.text = self.resultado.text+"7"
            self.lista_1.append(7)
            self.numero_1 = float("".join(map(str, self.lista_1))) # Utilizamos map() para convertir los elementos de una lista en una cadena y utilizamos join() para unirla en una sola cadena, despues float para decir que es una cadena decimal

        elif boton == self.boton_8:
            self.resultado.text = self.resultado.text+"8"
            self.lista_1.append(8)
            self.numero_1 = float("".join(map(str, self.lista_1))) # Utilizamos map() para convertir los elementos de una lista en una cadena y utilizamos join() para unirla en una sola cadena, despues float para decir que es una cadena decimal

        elif boton == self.boton_9:
            self.resultado.text = self.resultado.text+"9"
            self.lista_1.append(9)
            self.numero_1 = float("".join(map(str, self.lista_1))) # Utilizamos map() para convertir los elementos de una lista en una cadena y utilizamos join() para unirla en una sola cadena, despues float para decir que es una cadena decimal

        elif boton == self.boton_0:
            self.resultado.text = self.resultado.text+"0"
            self.lista_1.append(0)
            self.numero_1 = float("".join(map(str, self.lista_1))) # Utilizamos map() para convertir los elementos de una lista en una cadena y utilizamos join() para unirla en una sola cadena, despues float para decir que es una cadena decimal

        elif boton == self.boton_punto:
            self.resultado.text = self.resultado.text+"."
            self.lista_1.append(".")
            self.numero_1 = float("".join(map(str, self.lista_1))) # Utilizamos map() para convertir los elementos de una lista en una cadena y utilizamos join() para unirla en una sola cadena, despues float para decir que es una cadena decimal
        print(self.lista_1)
        print(self.numero_1)


    def operaciones(self):
        boton = self.sender()
        if boton == self.boton_suma:
            print("suma")

        elif boton == self.boton_resta:
            print("Resta")
        
        elif boton == self.boton_multiplicar:
            print("multiplicar")
        
        elif boton == self.boton_ce:
            print("CE")

        elif boton == self.boton_c:
            print("C")

        elif boton == self.boton_total:
            print("=")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = calculadora()
    ventana.diseño()
    ventana.show()
    sys.exit(app.exec())
    app.exec_()
