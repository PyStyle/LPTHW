




from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap
import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle('A First Window')
        # A button
        self.mybutton = QPushButton(self)
        self.mybutton.setText("OK!")
        # A text field
        self.mytext = QLineEdit(self)
        self.mytext.setText("Welcome")
        # An Image
        filepath = "media/qt-logo.png" # A relative path of you Image filepathself.mypixmap = QPixmao(filepath)
        self.myimg = QPixmap(filepath)
        self.myimg = QLabel(self)
        self.myimg.setPixmap(self.mypixmap)

        # Set uop the window and arrange all the widgets
        pixrect = self.mypixmap.rect()
        self.setGeometry(10, 10, pixrect.width(), pixrect.height() + 50)
        self.mytext.move(20, pixrect.height() + 20)
        self.mybutton.move(150, pixrect.height() +15)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv) # create an application
    mywindow1 = MyWindow() # create an INstance of your window
    mywindow2 = MyWindow() # create an insatnce of your windowmywindow2
    mywindow2.move(20, 500)
    sys.exit(app.exec_()) # start the event loop
