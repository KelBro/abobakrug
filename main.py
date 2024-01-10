from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import sys
import random


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("okr.ui", self)
        self.pushButton.clicked.connect(self.sozdanie)
        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.black)
        for circle in self.circles:
            painter.setBrush(QColor("yellow"))
            painter.drawEllipse(circle[0], circle[1], circle[2], circle[2])

    def sozdanie(self):
        diameter = random.randint(50, 300)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter - 200)
        self.circles.append((x, y, diameter))
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.setFixedSize(800, 600)
    window.show()
    sys.exit(app.exec_())
