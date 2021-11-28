import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle('YellowCircles')
        self.btn.clicked.connect(self.paint)

    def draw_circles(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        d1 = randint(0, 300)
        qp.drawEllipse(0, 0, d1, d1)
        d2 = randint(0, 300)
        qp.drawEllipse(d1, d1, d2, d2)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
