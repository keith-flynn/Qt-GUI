from PySide6.QtWidgets import QApplication, QWidget
from rock_widget import RockWidget

import sys

app = QApplication(sys.argv)

window = RockWidget()
window.show()

app.exec()