from PyQt5.QtGui import QPainter, QPen, QPixmap
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QColor

class SignatureWidget(QWidget):
    def __init__(self, parent=None):
        super(SignatureWidget, self).__init__(parent)
        self.setFixedSize(400, 200)  # Set appropriate size for the signature area
        self.setStyleSheet("background-color: white; border: 1px solid black;")
        self.drawing = False
        self.last_point = QPoint()
        self.image = QPixmap(self.size())  # Initialize the image where the signature will be drawn
        self.image.fill(Qt.white)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and self.drawing:
            painter = QPainter(self.image)
            pen = QPen(Qt.black, 3, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
            painter.setPen(pen)
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()  # Trigger repaint

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvas_painter = QPainter(self)
        canvas_painter.drawPixmap(self.rect(), self.image)

    def clear(self):
        """Clear the signature."""
        self.image.fill(Qt.white)
        self.update()

    def get_signature_image(self):
        """Return the QPixmap image of the signature."""
        return self.image
    
    def is_blank(self):
        # Convert QPixmap to QImage
        image = self.get_signature_image().toImage()

        # Check if the image is null
        if image.isNull():
            return True

        # Check if the entire image is white
        for x in range(image.width()):
            for y in range(image.height()):
                color = QColor(image.pixel(x, y))
                if color != QColor(255, 255, 255):  # Not white
                    return False
        return True