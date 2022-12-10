"""
# Version 1
from PySide6.QtWidgets import QApplication, QPushButton

# The slot : responds when something happens
def button_clicked():
    print("You clicked the button, you maverick renegade!")

app = QApplication()
button = QPushButton("Press me.")

# clicked is a signal of QPushButton. It's emitted when you click
# on a button
# You can wire a slot to the signal using this syntax:
button.clicked.connect(button_clicked)

button.show()
app.exec()
"""

# Version 2
"""
from PySide6.QtWidgets import QApplication, QPushButton

# The slot : responds when something happens
def button_clicked(data):
    print("You clicked the button, you maverick renegade! checked : ", data)

app = QApplication()
button = QPushButton("Press me.")
button.setCheckable(True) # Makes button checkable - unchecked by default
# Wire a slot to the signal using this syntax:
button.clicked.connect(button_clicked)

button.show()
app.exec()
"""

# Version 3
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider

# The slot : responds when something happens
def respond_to_slider(data):
    print("slider moved to : ", data)

app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

# You just do the connection. Qt takes care of
# passing the data from signal to slot.
slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()
