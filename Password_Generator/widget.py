import sys
import random
import string
import pyperclip
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QTextDocument
from ui_form import Ui_Widget
from PySide6.QtGui import QIcon


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowTitle("Generador de Contraseñas")
        self.setWindowIcon(QIcon("icono.png"))

        self.ui.letras_checkbox.setFocusPolicy(Qt.NoFocus)
        self.ui.contrasena.setTextFormat(Qt.RichText)

        # Configuración del slider
        self.ui.slider.setMinimum(8)
        self.ui.slider.setMaximum(64)
        self.ui.slider.setValue(15)
        self.ui.slider.setTickInterval(1)

        self.ui.sliderL.setText(f"{self.ui.slider.value()}")
        self.ui.slider.valueChanged.connect(self.actualizar_sliderL)

        # Generar contraseña
        self.ui.generarB.clicked.connect(self.mostrar_contrasena)
        self.ui.contrasena.setTextInteractionFlags(Qt.TextSelectableByMouse)

        # Copiar contraseña
        self.ui.copiar.clicked.connect(self.copiar_texto)
        self.ui.copiar.setToolTip("Copiar")

    # Métodos
    def actualizar_sliderL(self, valor):
        self.ui.sliderL.setText(f"{valor}")

    def generar_contrasena(self, longitud):
        psw = ""
        if self.ui.letras_checkbox.isChecked():
            psw += string.ascii_letters
        if self.ui.numeros_checkbox.isChecked():
            psw += string.digits
        if self.ui.caracteres_checkbox.isChecked():
            psw += "@-!$_"
        if not psw:
            psw = "ERROR"

        return ''.join(random.choice(psw) for _ in range(longitud))

    def mostrar_contrasena(self):
        longitud = self.ui.slider.value()
        contrasena = self.generar_contrasena(longitud)

        # Crear el HTML para estilizar el texto
        contrasena_html = ""

        for char in contrasena:
            if char.isdigit():
                contrasena_html += f'<span style="color: red;">{char}</span>'
            elif char in "@-!$_":
                contrasena_html += f'<span style="color: blue;">{char}</span>'
            else:
                contrasena_html += f'<span style="color: black;">{char}</span>'

        self.ui.contrasena.setText(f'<html><head/><body>{contrasena_html}</body></html>')

    def copiar_texto(self):
        doc = QTextDocument()
        doc.setHtml(self.ui.contrasena.text())
        texto_sin_html = doc.toPlainText()
        pyperclip.copy(texto_sin_html)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
