import sys
import os  # Library for interacting with the operating system
os.environ['ETS_TOOLKIT'] = 'qt4'
#添加代码,不显示warnings
import warnings
warnings.filterwarnings('ignore')
#代码结束
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
        MainWindow.setWindowTitle(_translate("MainWindow", "2D plots of Y"))
        self.label_3.setText(_translate("MainWindow", "(n)："))
        self.label_4.setText(_translate("MainWindow", "(l)："))
        self.label_5.setText(_translate("MainWindow", "(m)："))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))



class RunThread(QThread):
    msg = pyqtSignal(str)

    def __init__(self, n, l, m, plt):
        super(RunThread, self).__init__()
        self.n = n
        self.l = l
        self.m = m
        # self.planexyz = planexyz
        self.pi = np.pi
        self.a = 5.291772108e-11
        self.A = np.sqrt(
            ((2 * l + 1) * factorial(l - abs(m))) / (4 * self.pi * factorial(l + abs(m))))  # Normalization constant
        self.r = np.linspace(0.0, self.a * (5 * self.n ** 1.65), 181)
        self.plt = plt
        self.plt.axes.clear()

    def run(self):
        self.plt.axes.set_xticks([])  # 关闭x刻度
        self.plt.axes.set_yticks([])  # 关闭y刻度
        self.plt.axes.spines['right'].set_visible(False)
        self.plt.axes.spines['left'].set_visible(False)
        self.plt.axes.spines['top'].set_visible(False)
        self.plt.axes.spines['bottom'].set_visible(False)
        A = np.sqrt(((2 * self.l + 1) * factorial(self.l - abs(self.m))) / (4 * self.pi * factorial(self.l + abs(self.m))))  # Normalization constant
        r = np.linspace(0.0, self.a * (5 * self.n ** 1.65), 181)

        ax1 = self.plt.fig.add_subplot(2, 3, 1, aspect='equal')
        ax2 = self.plt.fig.add_subplot(2, 3, 2, aspect='equal')
        ax3 = self.plt.fig.add_subplot(2, 3, 3, aspect='equal')
        # if planexyz==0 :
        r = np.linspace(0.0, self.a * (5 * self.n ** 1.65), 181)
        theta = self.pi / 2
        phi = np.linspace(0, 2 * self.pi, 181)
        Theta = theta
        R, Phi = np.meshgrid(r, phi)
        f = calc_psi_prof(R,Theta,Phi,self.n,self.l,self.m)
        x, y, z = sph2cart(abs(R), Theta, Phi)
        maxpsi = np.abs(np.max(f))
        minpsi = np.abs(np.min(f))
        limpsi = np.maximum(maxpsi, minpsi)

        # ax1.contour(x,y,f,levels=[0.0], colors=['black'])
        ax1.contour(x, y, f,
                    levels=[-0.8 * limpsi, -0.4 * limpsi, -0.2 * limpsi, -0.1 * limpsi, -0.05 * limpsi, -0.01 * limpsi,
                            0.01 * limpsi, 0.05 * limpsi, 0.1 * limpsi, 0.2 * limpsi, 0.4 * limpsi, 0.8 * limpsi],
                    colors=['black'])

        ax1.set_xlabel("xaxis")  # x轴上的名字
        ax1.set_ylabel("yaxis")  # y轴上的名字
        ax1.set_xticks([])  # 关闭x刻度
        ax1.set_yticks([])  # 关闭y刻度
        ax1.set_title('profile of Psi_xy', fontsize=14, fontweight='bold')

        # if planexyz==1 :
        phi = self.pi / 2
        theta = np.linspace(0, self.pi, 181)
        Phi = phi
        R, Theta = np.meshgrid(r, theta)
        f = calc_psi_prof(R, Theta, Phi, self.n, self.l, self.m)
        x, y, z = sph2cart(abs(R), Theta, Phi)
        maxpsi = np.abs(np.max(f))
        minpsi = np.abs(np.min(f))
        limpsi = np.maximum(maxpsi, minpsi)
        # ax2.contour(y,z,f,levels=[0.0], colors=['black'])
        ax2.contour(y, z, f,
                    levels=[-0.8 * limpsi, -0.4 * limpsi, -0.2 * limpsi, -0.1 * limpsi, -0.05 * limpsi, -0.01 * limpsi,
                            0.01 * limpsi, 0.05 * limpsi, 0.1 * limpsi, 0.2 * limpsi, 0.4 * limpsi, 0.8 * limpsi],
                    colors=['black'])

        phi = self.pi * 3 / 2
        theta = np.linspace(0, self.pi, 181)
        Phi = phi
        R, Theta = np.meshgrid(r, theta)
        f = calc_psi_prof(R, Theta, Phi, self.n, self.l, self.m)
        x, y, z = sph2cart(abs(R), Theta, Phi)
        maxpsi = np.abs(np.max(f))
        minpsi = np.abs(np.min(f))
        limpsi = np.maximum(maxpsi, minpsi)
        # ax2.contour(y,z,f,levels=[0.0], colors=['black'])
        ax2.contour(y, z, f,
                    levels=[-0.8 * limpsi, -0.4 * limpsi, -0.2 * limpsi, -0.1 * limpsi, -0.05 * limpsi, -0.01 * limpsi,
                            0.01 * limpsi, 0.05 * limpsi, 0.1 * limpsi, 0.2 * limpsi, 0.4 * limpsi, 0.8 * limpsi],
                    colors=['black'])

        ax2.set_xlabel("yaxis")  # x轴上的名字
        ax2.set_ylabel("zaxis")  # y轴上的名字
        ax2.set_xticks([])  # 关闭x刻度
        ax2.set_yticks([])  # 关闭y刻度
        ax2.set_title('profile of Psi_yz', fontsize=14, fontweight='bold')
        # if planexyz==2 :
        phi = 0
        theta = np.linspace(0, self.pi, 181)
        Phi = phi
        R, Theta = np.meshgrid(r, theta)
        f = calc_psi_prof(R, Theta, Phi, self.n, self.l, self.m)
        x, y, z = sph2cart(abs(R), Theta, Phi)
        maxpsi = np.abs(np.max(f))
        minpsi = np.abs(np.min(f))
        limpsi = np.maximum(maxpsi, minpsi)
        # ax3.contour(x,z,f,levels=[0.0], colors=['black'])
        ax3.contour(x, z, f,
                    levels=[-0.8 * limpsi, -0.4 * limpsi, -0.2 * limpsi, -0.1 * limpsi, -0.05 * limpsi, -0.01 * limpsi,
                            0.01 * limpsi, 0.05 * limpsi, 0.1 * limpsi, 0.2 * limpsi, 0.4 * limpsi, 0.8 * limpsi],
                    colors=['black'])

        phi = self.pi
        theta = np.linspace(0, self.pi, 181)
        Phi = phi
        R, Theta = np.meshgrid(r, theta)
        f = calc_psi_prof(R, Theta, Phi, self.n, self.l, self.m)
        x, y, z = sph2cart(abs(R), Theta, Phi)
        maxpsi = np.abs(np.max(f))
        minpsi = np.abs(np.min(f))
        limpsi = np.maximum(maxpsi, minpsi)
        # ax3.contour(x,z,f,levels=[0.0], colors=['black'])
        ax3.contour(x, z, f,
                    levels=[-0.8 * limpsi, -0.4 * limpsi, -0.2 * limpsi, -0.1 * limpsi, -0.05 * limpsi, -0.01 * limpsi,
                            0.01 * limpsi, 0.05 * limpsi, 0.1 * limpsi, 0.2 * limpsi, 0.4 * limpsi, 0.8 * limpsi],
                    colors=['black'])

        # plt.clabel(C,inline = True,fontsize = 10) #显示等高线数值
        ax3.set_xlabel("xaxis")  # x轴上的名字
        ax3.set_ylabel("zaxis")  # y轴上的名字
        ax3.set_xticks([])  # 关闭x刻度
        ax3.set_yticks([])  # 关闭y刻度
        ax3.set_title('profile of Psi_xz', fontsize=14, fontweight='bold')
        self.plt.draw()




class Mydemo(FigureCanvas):
    def __init__(self, parent=None, width=10, height=3, dpi=600):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(1, 1, 1)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.fig.tight_layout()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # QApplication.setStyle(QStyleFactory.create('Fusion'))
        self.lineEdit.setPlaceholderText("Positive integer")
        self.lineEdit_2.setPlaceholderText("Non-negative integer")
        self.lineEdit_3.setPlaceholderText("Integer")
        self.cavas = Mydemo(width=6, height=4, dpi=100)
        self.cavas.axes.set_yticks([])
        self.cavas.axes.set_xticks([])
        self.widget_toolbar = NavigationToolbar(self.cavas, self.widget)
        self.gridLayout.addWidget(self.widget_toolbar)
        self.gridLayout.addWidget(self.cavas)
        self.pushButton.clicked.connect(self.start_counting)

    def start_counting(self):
        self.validationNLM()

    def validationNLM(self):
        n = 0
        l = 0
        m = 0
        s = True
		#检测n是否为整数，如果不是，报错
        try:
            n = int(self.lineEdit.text())
        except:
            self.msg('Prompt: (n) must be an integer')
            s = False
		#判断n是否小于等于0，如果是，报错
        if s == True:
            if (n <= 0):
                self.msg('Prompt: (n) must be greater than 0')
                s = False

		#检测l是否为整数，如果不是，报错
        if s == True:
            try:
                l = int(self.lineEdit_2.text())
            except:
                self.msg('Prompt: (l) must be an integer')
                s = False
		#检测m是否符合范围，如果不是，报错
        if s == True:
            if (l >= n) or (l < 0):
                self.msg('Prompt: (l) must < n and >= 0')
                s = False

		#检测m是否为整数，如果不是，报错
        if s == True:
            try:
                m = int(self.lineEdit_3.text())
            except:
                self.msg('Prompt: (m) must be an integer')
                s = False
		#检测m是否符合范围，如果不是，报错
        if s == True:
            if (m > l) or (m < -l):
                self.msg('Prompt: m should be in the range [-l, l]')
                s = False

        if s == True:
            print(n)
            print(l)
            print(m)
            run = RunThread(n, l, m, self.cavas)
            run.run()

    def msg(self, msg):
        QMessageBox.about(self, "错误", msg)


def start():
    App = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(App.exec_())

if __name__ == "__main__":
    start()