import io
import random
import sys

from PyQt5 import uic, QtWidgets, Qt
from PyQt5.QtWidgets import QApplication, QGraphicsEllipseItem


class MyWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('ЖЕЛТЫЕ КРУЖКИ')
        self.scene = QtWidgets.QGraphicsScene(self)
        self.view.setScene(self.scene)
        self.newcircleButton.clicked.connect(self.newCircle)

    def newCircle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        ellipse = QGraphicsEllipseItem(x, y, diameter, diameter)
        ellipse.setBrush(Qt.Qt.yellow)
        self.scene.addItem(ellipse)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
