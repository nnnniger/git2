import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QGraphicsScene, QGraphicsView, \
    QGraphicsEllipseItem
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import random


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Random Circles')

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.view)

        self.addButton = QPushButton('добавить жёлтый круг', self)
        self.addButton.clicked.connect(self.addCircle)
        self.layout.addWidget(self.addButton)

    def newCircle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)

        # color = QColor(Qt.yellow)
        #
        # self.scene.addEllipse(x, y, diameter, diameter)
        # self.scene.setBrush(color)
        color = QColor(Qt.yellow)
        ellipse = QGraphicsEllipseItem(x, y, diameter, diameter)
        ellipse.setBrush(color)
        self.scene.addItem(ellipse)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CircleWidget()
    ex.show()
    sys.exit(app.exec_())