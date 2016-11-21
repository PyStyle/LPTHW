





from PyQt5.QtWidgets import QApplication, QWidget
import sys

class MyWindow(QWidget): # parent class of all GUI in qt with tons of behaviour
    def __init__(self): # overriding __init__
        super(MyWindow, self).__init__() # gives access to methods of QWidget
        self.initGUI() # command for initialize wanted unique behaviour of QWidget

    def initGUI(self): # definition of parameters unique behaviour 
        self.setWindowTitle('A First Window')
        self.resize(250, 150)

if __name__ == "__main__": # boilerplate code
    app = QApplication(sys.argv) # create the application, brain class (boilerplate code)
    mywindow = MyWindow() # create an Instance of your Window, construction function
    mywindow.move(0, 0) # positioning window at 0,0 == top left corner
    mywindow.show() # tell Qt to make your window visible
    sys.exit(app.exec_()) # start the event (while-)loop!,
    # exec = starting the program, boilerplate code
