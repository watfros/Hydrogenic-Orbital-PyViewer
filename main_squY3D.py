import sys
import os  # Library for interacting with the operating system
os.environ['ETS_TOOLKIT'] = 'qt4'
#Add code to suppress warnings
import warnings
warnings.filterwarnings('ignore')
#End of code
from wsgiref.validate import validator
import matplotlib.pyplot as polt
from mayavi import mlab
from traits.api import HasTraits, Instance, Range, on_trait_change
from traitsui.api import View, Item, Group
from mayavi.core.ui.api import MayaviScene, SceneEditor, MlabSceneModel
from mayavi.core.api import PipelineBase
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from math import factorial
import numpy as np
from calculate_psi import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib import rcParams
from traits.api import HasTraits, Instance, on_trait_change
from traitsui.api import View, Item
from mayavi.core.ui.api import MayaviScene, MlabSceneModel, \
    SceneEditor
from pyface.qt import QtGui, QtCore

config = {
    "font.family": 'serif',
    "mathtext.fontset": 'stix',
    "font.serif": ['SimSun'],
}
rcParams.update(config)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("n MainWindow")
        MainWindow.resize(1400, 550)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../r2 (2)/ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(1150, 10, 31, 511))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(1170, 110, 221, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setMaximumSize(QtCore.QSize(243, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(1170, 200, 221, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setObjectName("label_4")

        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(243, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1170, 340, 221, 41))
        self.pushButton.setObjectName("pushButton")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 1141, 491))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-310, 20, 521, 16))
        self.widget.setObjectName("widget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Y², Square of Y"))
        self.label_3.setText(_translate("MainWindow", "(l)："))
        self.label_4.setText(_translate("MainWindow", "(m)："))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))


class RunThread(QThread):
    msg = pyqtSignal(str)

    def __init__(self, m, l, ):
        super(RunThread, self).__init__()
        self.l = l
        self.m = m
        self.pi = np.pi
        self.ngrid = 100

    def run(self):
        self.sph_harm_sq()

    def sph_harm_sq(self):
        mlab.clf(figure=None)
        ngrid = 131
        phi, theta = np.mgrid[0:2 * self.pi:131j, 0:self.pi:131j]
        A = np.sqrt(((2 * self.l + 1) * factorial(self.l - abs(self.m))) / (4 * self.pi * factorial(self.l + abs(self.m))))

        s = calc_Y(theta, phi, self.l, self.m)

        x, y, z = sph2cart(s * s, theta, phi)

        # Handle special case when l=0 (single value needs array conversion)
        if self.l == 0:
            arr = np.ones((ngrid, ngrid), dtype=float)
            s = arr * s

        mlab.mesh(x, y, z, scalars=s / abs(s))
        mlab.show()


class Visualization(HasTraits):
    scene = Instance(MlabSceneModel, ())

    @on_trait_change('scene.activated')
    def update_plot(self):
        # This function is called when the view is opened. We don't
        # populate the scene when the view is not yet open, as some
        # VTK features require a GLContext.
        pass

    # Layout configuration for the visualization scene
    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                     height=200, width=300, show_label=False),
                resizable=True  # Allow resizing with parent widget
                )


class MayaviQWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        layout = QtGui.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.visualization = Visualization()
        self.ui = self.visualization.edit_traits(parent=self, kind='subpanel').control
        layout.addWidget(self.ui)
        self.ui.setParent(self)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.lineEdit.setPlaceholderText("Non-negative integer")
        self.lineEdit_2.setPlaceholderText("Integer")
        self.mayavi_widget = MayaviQWidget()
        self.gridLayout.addWidget(self.mayavi_widget)
        self.pushButton.clicked.connect(self.start_counting)

    def start_counting(self):
        self.validationNLM()

    def validationNLM(self):
        l = 0
        m = 0
        s = True
        # Check if l is an integer; if not, show error
        try:
            l = int(self.lineEdit.text())
        except:
            self.msg('Prompt: (l) must be an integer')
            s = False

        # Check if l is non-negative; if not, show error
        if s == True:
            if (l < 0):
                self.msg('Prompt: (l) must be greater than or equal to 0')
                s = False

        # Check if m is an integer; if not, show error
        if s == True:
            try:
                m = int(self.lineEdit_2.text())
            except:
                self.msg('Prompt: (m) must be an integer')
                s = False

        # Check if m is within valid range; if not, show error
        if s == True:
            if (m > l) or (m < -l):
                self.msg('Prompt: m should be in the range [-l, l]')
                s = False

        # Validation completed, start calculation
        if s == True:
            print(l)
            print(m)
            run = RunThread(m, l)
            run.run()

    def msg(self, msg):
        QMessageBox.about(self, "Error", msg)


def start():
    App = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(App.exec_())

if __name__ == "__main__":
    start()