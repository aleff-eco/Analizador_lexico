from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from analizador import analisis

class MiVentana(QMainWindow):
    def __init__(self):
        super(MiVentana, self).__init__()
        loadUi('interfaz.ui', self)

        self.pushButton.clicked.connect(self.verificar)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["Token", "Dato", "Posicion", "Status"])
        self.tableWidget.setColumnWidth(0, 180)
        self.tableWidget.setColumnWidth(1, 220)
        self.tableWidget.setColumnWidth(2, 130)
        self.tableWidget.setColumnWidth(3, 60)

    def verificar(self):
        texto = self.textEdit.toPlainText()
        resultados = analisis(texto)

        error_counter = 0
        self.tableWidget.setRowCount(0)
        self.CC.clear()
        self.CE.clear()

        for resultado in resultados:
            tipo, valor, posicion = resultado
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)

            self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(tipo))
            self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(str(valor)))

            lexpos_value = str(posicion)
            self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(lexpos_value))

            if tipo == "ERROR_LEXICO":
                error_counter += 1
                self.tableWidget.setItem(rowPosition, 3, QTableWidgetItem("     ✕"))

        self.CE.addItem(str(error_counter))
        self.CC.addItem(str(posicion))

if __name__ == '__main__':
    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    app.exec_()
