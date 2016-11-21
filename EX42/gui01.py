





from PyQt5.QtWidgets import QApplication, Widget
import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle('A First Window')
        self.resize(250. 150)

if __name__ == "__main__":
    app = QApplication(sys.argv) # create the application
    mywindow = MyWindow() # create an Instance of your Window
    mywindow.move(0, 0)
    mywindow.show() # tell Qt to make your window visible
    sys.exit(app.exec_() # start the event loop!
