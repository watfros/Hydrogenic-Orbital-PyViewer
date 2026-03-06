import sys
import os  # Library for interacting with the operating system
os.environ['ETS_TOOLKIT'] = 'qt4'
#添加代码,不显示warnings
import warnings
warnings.filterwarnings('ignore')
#代码结束
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

config = {
    "font.family": 'serif',
    "mathtext.fontset": 'stix',
    "font.serif": ['SimSun'],
}
rcParams.update(config)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, p, d, s):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../r2 (2)/ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.p = p
        self.d = d
        self.s = s
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
        theme = ["radial function; ", "radial function squared; ", "radial distribution function;"]
        them = ''
        t = 0
        for pds in [self.p, self.d, self.s]:
            if pds != 0:
                them = them + theme[t] + ' '
            t += 1
        MainWindow.setWindowTitle(_translate("MainWindow", them))
        self.label_3.setText(_translate("MainWindow", "(n): "))
        self.label_4.setText(_translate("MainWindow", "(l): "))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))


class RunThread(QThread):
    msg = pyqtSignal(str)
    def __init__(self, n, l, i, j, k, plt):
        super(RunThread, self).__init__()
        self.n = n
        self.l = l
        self.pi = np.pi
        self.a = 5.291772108e-11

        self.r = np.linspace(0.0, self.a * (5 * self.n ** 1.65), 181)
        self.plt = plt
        self.plt.fig.clear()
        self.ngrid = 100
        self.i = i
        self.j = j
        self.k = k
        self.t = 0

    def run(self):
        for ijk in [self.i, self.j, self.k]:
            if ijk != 0:
                self.t += 1

        print(str(self.t))

        if self.i != 0:
            self.plot_R()
        if self.j != 0:
            self.plot_R2()
        if self.k != 0:
            self.plot_R3()

        self.rd()

    # 空白图片,图片中加入文本说明
    def rd(self):
        ax4 = self.plt.fig.add_subplot(2, self.t, self.t+1)
        # loc只能这三个位置才会‘同时’出现三个title,否则取最后一个
        #    plt.title("right bottom",y=0,loc='right', fontsize = 14, fontweight = 'bold')
        #    plt.title("left top",y=0.8,loc='left', fontsize = 14, fontweight = 'bold')
        #    plt.title("center",y=0.4,loc='center', fontsize = 14, fontweight = 'bold')
        if self.n == 1 and self.l == 0:
            self.equation = r'{R_{1,0}} = 2{\left( {\frac{Z}{{{a_0}}}} \right)^{\frac{3}{2}}}\exp ( - \frac{{Zr}}{{{' \
                            r'a_0}}}) '
        elif self.n == 2 and self.l == 0:
            self.equation = r'{R_{2,0}} = \frac{1}{{2\sqrt {2} }}{\left( {\frac{Z}{{{a_0}}}} \right)^{\frac{3}{' \
                            r'2}}}\left( {2 - \frac{{Zr}}{{{a_0}}}} \right)\exp \left( { - \frac{{Zr}}{{2{a_0}}}} ' \
                            r'\right) '
        elif self.n == 2 and self.l == 1:
            self.equation = r'{R_{2,1}} = \frac{1}{{2\sqrt {6} }}{\left( {\frac{Z}{{{a_0}}}} \right)^{\frac{3}{' \
                            r'2}}}\left( {\frac{{Zr}}{{{a_0}}}} \right)\exp \left( { - \frac{{Zr}}{{2{a_0}}}} \right) '
        elif self.n == 3 and self.l == 0:
            self.equation = r'{R_{3,0}} = \frac{2}{{81\sqrt {3} }}{\left( {\frac{Z}{{{a_0}}}} \right)^{\frac{3}{' \
                            r'2}}}\left( {27 - 18\frac{{Zr}}{{{a_0}}} + 2{{(\frac{{Zr}}{{{a_0}}})}^2}} \right)\exp ( ' \
                            r'- \frac{{Zr}}{{3{a_0}}}) '
        elif self.n == 3 and self.l == 1:
            self.equation = r'{R_{3,1}} = \frac{4}{{81\sqrt {6} }}{\left( {\frac{Z}{{{a_0}}}} \right)^{\frac{3}{2}}}\left( {6\frac{{Zr}}{{{a_0}}} - {{(\frac{{Zr}}{{{a_0}}})}^2}} \right)\exp ( - \frac{{Zr}}{{3{a_0}}})'
        elif self.n == 3 and self.l == 2:
            self.equation = r'{R_{3,2}} = \frac{4}{{81\sqrt {30} }}{\left( {\frac{Z}{{{a_0}}}} \right)^{\frac{3}{' \
                            r'2}}}{\left( {(\frac{{Zr}}{{{a_0}}})} \right)^2}\exp ( - \frac{{Zr}}{{3{a_0}}}) '
        else:
            self.equation = r'{R_{n,l}}(r) = N{e^{ - \frac{\rho }{2}}}{\rho ^l}L_{n + l}^{2l + 1}(\rho ),\rho  = ' \
                            r'\frac{{2Zr}}{{n{a_0}}},N =  - {\left[ {{{(\frac{{2Z}}{{n{a_0}}})}^3} \cdot \frac{{(n - ' \
                            r'l - 1)!}}{{2n{{\left[ {(n + l)!} \right]}^3}}}} \right]^{\frac{1}{2}}},L_{n + l}^{2l + ' \
                            r'1}(\rho ) = \frac{{{d^{2l + 1}}}}{{d{\rho ^{2l + 1}}}}\left[ {{e^\rho }\frac{{{d^{n + ' \
                            r'l}}}}{{d{\rho ^{n + l}}}}({e^{ - \rho }}{\rho ^{n + l}})} \right] '

        # y=0.4,这个数值需要根据输出内容进行调节
        titles = ''
        ax4.set_title(titles + '$%s$' % self.equation, y=0, loc='left',
                      fontsize=11, fontweight='bold', color='blue', verticalalignment='bottom')
        self.plt.axes.spines['right'].set_visible(False)
        self.plt.axes.spines['left'].set_visible(False)
        self.plt.axes.spines['top'].set_visible(False)
        self.plt.axes.spines['bottom'].set_visible(False)
        self.plt.axes.set_xticks([])
        self.plt.axes.set_yticks([])
        ax4.set_xticks([])
        ax4.set_yticks([])
        ax4.plot()
        ax = self.plt.fig.gca()
        ax.spines["right"].set_color("none")
        ax.spines["top"].set_color("none")
        ax.spines["bottom"].set_color("none")
        ax.spines["left"].set_color("none")
        self.plt.draw()

    def plot_R(self):
        # R = np.sqrt(X**2 + Y**2 + Z**2)
        R = np.linspace(0.0, self.a * (5 * self.n ** 1.65), self.n * self.ngrid)
        rho = 2.0 * R / self.n / self.a
        C = np.sqrt((2.0 / self.n / self.a) ** 3 * factorial(self.n - self.l - 1) / (
                    2 * self.n * factorial(self.n + self.l) ** 3))
        f = np.exp(-rho / 2) * rho ** self.l * associatedLaguerre(self.l, self.n, rho)
        f = f * C
        R = R / self.a
        if self.t == 1:
            ax1 = self.plt.fig.add_subplot(2, 1, 1)
        if self.t == 2:
            ax1 = self.plt.fig.add_subplot(2, 2, 1)
        if self.t == 3:
            ax1 = self.plt.fig.add_subplot(2, 3, 1)
        self.equation = r'{R_{(r)}}'
        ax1.set_title('$%s$' % (self.equation), loc='center', fontsize=14, fontweight='bold')
        ax1.set_title('a', loc='left', y=1, fontsize=15, fontweight='bold')
        ax1.plot(R, f, color='red')

        #    只显示两个坐标轴的方法
        #    ax = plt.gca()
        #    ax.spines["right"].set_color("none")
        #    ax.spines["top"].set_color("none")
        #    ax.spines["bottom"].set_position(("data", 0))
        #    ax.spines["left"].set_position(("data", 0))
        ax1.set_xlim(left=0)  # 方框左侧为零点
        if self.n - self.l != 1:
            ax1.axhline(y=0.0, c="blue", ls="--", lw=1)  # 引入参考系
        else:
            ax1.set_ylim(bottom=0)  # 方框底部为零点
        ax1.axhline(y=0.0, c="blue", ls="--", lw=1)  # 引入参考系
        # plt.xticks([])
        ax1.set_yticks([])

    #        plt.show()
    #        plt.close()

    def plot_R2(self):
        #        fig = plt.figure()
        # R = np.sqrt(X**2 + Y**2 + Z**2)
        R = np.linspace(0.0, self.a * (5 * self.n ** 1.65), self.n * self.ngrid)
        rho = 2.0 * R / self.n / self.a
        C = np.sqrt((2.0 / self.n / self.a) ** 3 * factorial(self.n - self.l - 1) / (
                    2 * self.n * factorial(self.n + self.l) ** 3))
        f = np.exp(-rho / 2) * rho ** self.l * associatedLaguerre(self.l, self.n, rho)
        f = f * C
        f = f ** 2
        f_max = np.max(f)
        f = self.n * f / f_max
        R = R / self.a
        if self.t == 1:
            ax2 = self.plt.fig.add_subplot(2, 1, 1)
        if self.t == 2:
            if self.i == 1:
                ax2 = self.plt.fig.add_subplot(2, 2, 2)
            else:
                ax2 = self.plt.fig.add_subplot(2, 2, 1)
        if self.t == 3:
            ax2 = self.plt.fig.add_subplot(2, 3, 2)
        self.equation = r'R_{(r)}^2'
        ax2.set_title('$%s$' % (self.equation), loc='center', fontsize=10, fontweight='bold')
        ax2.set_title('b', loc='left', y=1, fontsize=15, fontweight='bold')

        # 节点的位置需要具体的x数值,等后续添加
        # min_indx=np.argmin(f)/ngrid*10*a#min value index2value
        # max_indx=0.5*np.max(f)
        # plt.annotate('节点',xy=(min_indx,0.0),xytext=(min_indx,max_indx),arrowprops=dict(arrowstyle="simple"))

        ax2.plot(R, f, color='red')
        # plt.axhline(y=0.0, c="blue", ls="--", lw=1)#引入参考系

        #    只显示两个坐标轴的方法
        #    ax = plt.gca()
        #    ax.spines["right"].set_color("none")
        #    ax.spines["top"].set_color("none")
        #    ax.spines["bottom"].set_position(("data", 0))
        #    ax.spines["left"].set_position(("data", 0))
        ax2.set_xlim(left=0)
        ax2.set_ylim(bottom=0)
        if self.l == 0 and self.n != 1:
            ax2.set_ylim(0, 0.2)
        # plt.xticks([])
        self.plt.axes.set_yticks([])
        ax2.set_yticks([])
    #        plt.show()
    #        plt.close()

    def plot_R3(self):
        #        fig = plt.figure()

        # R = np.sqrt(X**2 + Y**2 + Z**2)
        R = np.linspace(0.0, self.a * (5 * self.n ** 1.65), self.n * self.ngrid)
        rho = 2.0 * R / self.n / self.a
        C = np.sqrt((2.0 / self.n / self.a) ** 3 * factorial(self.n - self.l - 1) / (
                    2 * self.n * factorial(self.n + self.l) ** 3))
        f = np.exp(-rho / 2) * rho ** self.l * associatedLaguerre(self.l, self.n, rho)
        f = f * C
        f = R ** 2 * f ** 2
        R = R / self.a
        if self.t == 1:
            ax3 = self.plt.fig.add_subplot(2, 1, 1)
        if self.t == 2:
            ax3 = self.plt.fig.add_subplot(2, 2, 2)
        if self.t == 3:
            ax3 = self.plt.fig.add_subplot(2, 3, 3)
        self.equation = r'{r^2}R_{(r)}^2'
        ax3.set_title('$%s$' % (self.equation), loc='center', fontsize=10, fontweight='bold')
        ax3.set_title('c', loc='left', y=1, fontsize=15, fontweight='bold')

        # 节点的位置需要具体的x数值,等后续添加
        ax3.plot(R, f, color='red')
        # plt.axhline(y=0.0, c="blue", ls="--", lw=1)#引入参考系

        #    只显示两个坐标轴的方法
        #    ax = plt.gca()
        #    ax.spines["right"].set_color("none")
        #    ax.spines["top"].set_color("none")
        #    ax.spines["bottom"].set_position(("data", 0))
        #    ax.spines["left"].set_position(("data", 0))
        ax3.set_xlim(left=0)
        ax3.set_ylim(bottom=0)
        # plt.xticks([])
        ax3.set_yticks([])



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
    def __init__(self, i, j, k, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self, p=i, d=j, s=k)
        self.lineEdit.setPlaceholderText("Principal quantum num")
        self.lineEdit_2.setPlaceholderText("Azimuthal quantum num")
        self.cavas = Mydemo(width=6, height=4, dpi=100)
        self.cavas.axes.set_yticks([])
        self.cavas.axes.set_xticks([])
        self.widget_toolbar = NavigationToolbar(self.cavas, self.widget)
        self.gridLayout.addWidget(self.widget_toolbar)
        self.gridLayout.addWidget(self.cavas)
        self.pushButton.clicked.connect(self.start_counting)
        self.i = i
        self.j = j
        self.k = k

    def start_counting(self):
        self.validationNLM()

    def validationNLM(self):
        n = 0
        l = 0
        s = True
        # Check if n is an integer; if not, show error
        try:
            n = int(self.lineEdit.text())
        except:
            self.msg('Prompt: (n) must be an integer')
            s = False
        # Check if n is greater than 0; if not, show error
        if s == True:
            if (n <= 0):
                self.msg('Prompt: (n) must be greater than 0')
                s = False
        # Check if l is an integer; if not, show error
        if s == True:
            try:
                l = int(self.lineEdit_2.text())
            except:
                self.msg('Prompt: (l) must be an integer')
                s = False
        # Check if l is within valid range; if not, show error
        if s == True:
            if (l >= n) or (l < 0):
                self.msg('Prompt: l must be less than n and >= 0')
                s = False
        # Validation completed, start calculation
        if s == True:
            print(n)
            print(l)
            RunThread(n, l, self.i, self.j, self.k, self.cavas).run()

    def msg(self, msg):
        QMessageBox.about(self, "Error", msg)


def start(i, j, k):
    App = QApplication(sys.argv)
    ex = MainWindow(i, j, k)
    ex.show()
    sys.exit(App.exec_())

if __name__ == "__main__":
    # Configure functions to plot: 1=enable, 0=disable
    start(1, 1, 1)  # Plot all three functions