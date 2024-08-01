import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Layout Example')

# Vytvoření vertikálního rozložení
layout = QVBoxLayout()

# Přidání tlačítek do rozložení
layout.addWidget(QPushButton('Button 1'))
layout.addWidget(QPushButton('Button 2'))
layout.addWidget(QPushButton('Button 3'))

# Nastavení rozložení pro okno
window.setLayout(layout)

window.show()
sys.exit(app.exec_())
