import random
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_file import Ui_MainWindow
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtCore import QPoint


class FirstWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.qp = QPainter()
        self.show()

        self.flag = False

        self.ok.clicked.connect(self.begin)

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def begin(self):
        self.flag = True
        self.repaint()

    def draw(self):
        color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        self.qp.setBrush(QColor(*color))
        a = random.randint(0, 100)
        self.qp.drawEllipse((QPoint(self.width() // 2, self.height() // 2)), a, a)


if __name__ == '__main__':
    ex = QApplication(sys.argv)
    am = FirstWindow()
    sys.exit(ex.exec())
