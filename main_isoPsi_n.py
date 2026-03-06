import sys
import os  # Library for interacting with the operating system
os.environ['ETS_TOOLKIT'] = 'qt4'
#Add code to suppress warnings
import warnings
warnings.filterwarnings('ignore')
#End of code
from wsgiref.validate import validator
import matplotlib.pyplot as plts
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
from pyface.qt import QtGui, QtCore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/新前缀/ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(940, 10, 31, 701))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(990, 180, 221, 31))
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
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(990, 240, 221, 31))
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
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(990, 300, 221, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(243, 16777215))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(990, 440, 221, 41))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(990, 360, 221, 32))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setMinimumSize(QtCore.QSize(30, 30))
        self.label_6.setMaximumSize(QtCore.QSize(90, 30))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 921, 681))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Isosurfaces of Psi, Multiple Isosurfaces of Wave Function"))
        self.label_3.setText(_translate("MainWindow", "(n)："))
        self.label_4.setText(_translate("MainWindow", "(l)："))
        self.label_5.setText(_translate("MainWindow", "(m)："))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))


class RunThread(QThread):
    msg = pyqtSignal(str)

    def __init__(self, n, l, m):
        super(RunThread, self).__init__()
        self.n = n
        self.l = l
        self.m = m
        self.pi = np.pi
        self.a = 5.291772108e-11  # Bohr radius

    def run(self):
        mlab.clf(figure=None)
        # Calculate coordinates and wave function values (maintain original logic)
        x, y, z = np.ogrid[-self.a * (5 * self.n ** 1.65):self.a * (5 * self.n ** 1.65):168j, 
                          -self.a * (5 * self.n ** 1.65):self.a * (5 * self.n ** 1.65):168j,
                          -self.a * (5 * self.n ** 1.65):self.a * (5 * self.n ** 1.65):168j]
        r, Theta, Phi = cart2sph(x, y, z)
        x, y, z = sph2cart(r, Theta, Phi)  # Maintain dimensional consistency

        scalars = calc_psi(r, Theta, Phi, self.n, self.l, self.m)

        # Determine wave function value range
        maxpsi = np.abs(np.max(scalars))
        minpsi = np.abs(np.min(scalars))
        limpsi = maxpsi if self.n == 1 else np.minimum(maxpsi, minpsi)

        # Plot 6 isosurfaces with annotations (offset along x-axis)
        for nth_psi in range(1, 6):
            threshold = 0.1 * nth_psi * limpsi
            # X-axis offset value (staggered display along x-axis)
            x_offset = self.a * (10 * nth_psi * self.n ** 1.65)
            
            # Plot isosurfaces (modify x to x + x_offset)
            if self.n == 1 and self.l == 0:
                contour = mlab.contour3d(
                    x + x_offset,  # X-axis offset
                    y, 
                    z, 
                    scalars, 
                    contours=[threshold],
                    transparent=False,
                    vmax=0.1 * limpsi,
                    vmin=-0.1 * limpsi
                )
                values = [threshold]
            else:
                contour = mlab.contour3d(
                    x + x_offset,  # X-axis offset
                    y, 
                    z, 
                    scalars,
                    contours=[-threshold, threshold],
                    transparent=False,
                    vmax=0.1 * limpsi,
                    vmin=-0.1 * limpsi
                )
                values = [-threshold, threshold]

            # Add annotations for each isosurface value (adjust position to x-offset)
            for val in values:
                # Keep positive values (take absolute value) and format
                abs_val = abs(val)  # Take absolute value to display only positive values
                # Format value to 3 decimal places, use scientific notation if necessary
                if abs_val < 1e-3 or abs_val > 1e5:
                    label_text = f"{abs_val:.3e}"
                else:
                    label_text = f"{abs_val:.3f}"
                
                # Fixed offset (adjust values based on actual display)
                fixed_left_offset = self.a * self.n ** 1.65  # Fixed length offset
                mlab.text3d(
                    x_offset - fixed_left_offset,  # Fixed left offset
                    y.max() * 1.1,
                    0,
                    label_text,
                    scale=0.5 * self.a * self.n ** 1.65,
                    color=(0, 0, 0)
                )
        mlab.show()


class Visualization(HasTraits):
    scene = Instance(MlabSceneModel, ())

    @on_trait_change('scene.activated')
    def update_plot(self):
        # This function is called when the view is opened. We don't
        # populate the scene when the view is not yet open, as some
        # VTK features require a GLContext.
        # We can do normal mlab calls on the embedded scene.

        # self.scene.mlab.pipeline.surface(self.scene.mlab.pipeline.open("cylinder.vtk"))
        # self.scene.mlab.test_mesh()
        pass

    # The layout of the dialog created
    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                     height=200, width=300, show_label=False),
                resizable=True  # We need this to resize with the parent widget
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
        # QApplication.setStyle(QStyleFactory.create('Fusion'))
        self.lineEdit.setPlaceholderText("Positive integer")
        self.lineEdit_2.setPlaceholderText("Non-negative integer")
        self.lineEdit_3.setPlaceholderText("Integer")
        self.cavas = MayaviQWidget()
        self.gridLayout.addWidget(self.cavas)
        self.pushButton.clicked.connect(self.start_counting)

    def start_counting(self):
        self.validationNLM()

    def validationNLM(self):
        n = 0
        l = 0
        m = 0
        s = True
        try:
            n = int(self.lineEdit.text())
        except:
            self.msg('Prompt: (n) must be an integer')
            s = False
        if s == True:
            try:
                l = int(self.lineEdit_2.text())
            except:
                self.msg('Prompt: (l) must be an integer')
                s = False
        if s == True:
            try:
                m = int(self.lineEdit_3.text())
            except:
                self.msg('Prompt: (m) must be an integer')
                s = False
        if s == True:
            if n <= 0:
                self.msg('Prompt: (n) must be greater than 0')
            elif l < 0 or l >= n:
                self.msg('Prompt: (l) must be >= 0 and < n')
            elif (m > l) or (m < -l):
                self.msg('Prompt: (m) must be in range [-l, l]')
            else:
                self.run = RunThread(n, l, m)
                self.run.run()

    def msg(self, msg):
        QMessageBox.about(self, "Error", msg)


def start():
    App = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(App.exec_())
if __name__ == "__main__":
    start()