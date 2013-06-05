import sys
from PlotGUI import *
import random
 
class GUIForm(QtGui.QDialog):
 
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'), self.PlotFunc)
 
    def PlotFunc(self):
        randomNumbers = random.sample(range(0, 10), 10)
        print(randomNumbers)
        self.ui.widget.canvas.ax.clear()
        self.ui.widget.canvas.ax.plot(randomNumbers)
        self.ui.widget.canvas.draw()
 
 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = GUIForm()
    myapp.show()
    sys.exit(app.exec_())