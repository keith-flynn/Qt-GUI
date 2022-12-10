from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys

#Setting up global scope

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Our first MainWindow App!")

button = QPushButton()
button.setText("Press Me")

window.setCentralWidget(button)

window.show()
app.exec()