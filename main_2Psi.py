#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sys
import os
os.environ['ETS_TOOLKIT'] = 'qt4'
import warnings
warnings.filterwarnings('ignore')
from mayavi import mlab
from traits.api import HasTraits, Instance
import numpy as np
from calculate_psi import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from pyface.qt import QtGui, QtCore
from traitsui.api import View, Item
from mayavi.core.ui.api import MayaviScene, SceneEditor, MlabSceneModel
from mayavi.core.api import PipelineBase


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

        # 波函数参数输入框
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(990, 100, 221, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_n1 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_n1.setObjectName("label_n1")
        self.horizontalLayout_2.addWidget(self.label_n1)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setMaximumSize(QtCore.QSize(243, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(990, 150, 221, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_l1 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_l1.setObjectName("label_l1")
        self.horizontalLayout_3.addWidget(self.label_l1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(243, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)

        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(990, 200, 221, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_m1 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_m1.setObjectName("label_m1")
        self.horizontalLayout_4.addWidget(self.label_m1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(243, 16777215))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)

        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(990, 250, 221, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_n2 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_n2.setObjectName("label_n2")
        self.horizontalLayout_5.addWidget(self.label_n2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(243, 16777215))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_5.addWidget(self.lineEdit_4)

        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(990, 300, 221, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_l2 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_l2.setObjectName("label_l2")
        self.horizontalLayout_6.addWidget(self.label_l2)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.lineEdit_5.setMaximumSize(QtCore.QSize(243, 16777215))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_6.addWidget(self.lineEdit_5)

        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(990, 350, 221, 31))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_m2 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_m2.setObjectName("label_m2")
        self.horizontalLayout_7.addWidget(self.label_m2)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.lineEdit_6.setMaximumSize(QtCore.QSize(243, 16777215))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_7.addWidget(self.lineEdit_6)

        # 添加posx', posy', posz', coef输入框
        self.horizontalLayoutWidget_posx = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_posx.setGeometry(QtCore.QRect(990, 400, 221, 31))
        self.horizontalLayoutWidget_posx.setObjectName("horizontalLayoutWidget_posx")
        self.horizontalLayout_posx = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_posx)
        self.horizontalLayout_posx.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_posx.setObjectName("horizontalLayout_posx")
        self.label_posx = QtWidgets.QLabel(self.horizontalLayoutWidget_posx)
        self.label_posx.setObjectName("label_posx")
        self.horizontalLayout_posx.addWidget(self.label_posx)
        self.lineEdit_posx = QtWidgets.QLineEdit(self.horizontalLayoutWidget_posx)
        self.lineEdit_posx.setMaximumSize(QtCore.QSize(243, 16777215))
        self.lineEdit_posx.setObjectName("lineEdit_posx")
        self.horizontalLayout_posx.addWidget(self.lineEdit_posx)

        self.horizontalLayoutWidget_posy = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_posy.setGeometry(QtCore.QRect(990, 450, 221, 31))
        self.horizontalLayoutWidget_posy.setObjectName("horizontalLayoutWidget_posy")
        self.horizontalLayout_posy = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_posy)
        self.horizontalLayout_posy.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_posy.setObjectName("horizontalLayout_posy")
        self.label_posy = QtWidgets.QLabel(self.horizontalLayoutWidget_posy)
        self.label_posy.setObjectName("label_posy")
        self.horizontalLayout_posy.addWidget(self.label_posy)
        self.lineEdit_posy = QtWidgets.QLineEdit(self.horizontalLayoutWidget_posy)
        self.lineEdit_posy.setMaximumSize(QtCore.QSize(243, 16777215))
        self.lineEdit_posy.setObjectName("lineEdit_posy")
        self.horizontalLayout_posy.addWidget(self.lineEdit_posy)

        self.horizontalLayoutWidget_posz = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_posz.setGeometry(QtCore.QRect(990, 500, 221, 31))
        self.horizontalLayoutWidget_posz.setObjectName("horizontalLayoutWidget_posz")
        self.horizontalLayout_posz = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_posz)
        self.horizontalLayout_posz.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_posz.setObjectName("horizontalLayout_posz")
        self.label_posz = QtWidgets.QLabel(self.horizontalLayoutWidget_posz)
        self.label_posz.setObjectName("label_posz")
        self.horizontalLayout_posz.addWidget(self.label_posz)
        self.lineEdit_posz = QtWidgets.QLineEdit(self.horizontalLayoutWidget_posz)
        self.lineEdit_posz.setMaximumSize(QtCore.QSize(243, 16777215))
        self.lineEdit_posz.setObjectName("lineEdit_posz")
        self.horizontalLayout_posz.addWidget(self.lineEdit_posz)

        self.horizontalLayoutWidget_coef = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_coef.setGeometry(QtCore.QRect(990, 550, 221, 31))
        self.horizontalLayoutWidget_coef.setObjectName("horizontalLayoutWidget_coef")
        self.horizontalLayout_coef = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_coef)
        self.horizontalLayout_coef.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_coef.setObjectName("horizontalLayout_coef")
        self.label_coef = QtWidgets.QLabel(self.horizontalLayoutWidget_coef)
        self.label_coef.setObjectName("label_coef")
        self.horizontalLayout_coef.addWidget(self.label_coef)
        self.lineEdit_coef = QtWidgets.QLineEdit(self.horizontalLayoutWidget_coef)
        self.lineEdit_coef.setMaximumSize(QtCore.QSize(243, 16777215))
        self.lineEdit_coef.setObjectName("lineEdit_coef")
        self.horizontalLayout_coef.addWidget(self.lineEdit_coef)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(990, 600, 221, 41))
        self.pushButton.setObjectName("pushButton")

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
        MainWindow.setWindowTitle(_translate("MainWindow", "Superposition of Two Ψ"))
        self.label_n1.setText(_translate("MainWindow", "(n1)："))
        self.label_l1.setText(_translate("MainWindow", "(l1)："))
        self.label_m1.setText(_translate("MainWindow", "(m1)："))
        self.label_n2.setText(_translate("MainWindow", "(n2)："))
        self.label_l2.setText(_translate("MainWindow", "(l2)："))
        self.label_m2.setText(_translate("MainWindow", "(m2)："))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.label_posx.setText(_translate("MainWindow", "(posx)："))
        self.label_posy.setText(_translate("MainWindow", "(posy)："))
        self.label_posz.setText(_translate("MainWindow", "(posz)："))
        self.label_coef.setText(_translate("MainWindow", "(coef)："))


class Visualization(HasTraits):
    scene = Instance(MlabSceneModel, ())
    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                     height=200, width=300, show_label=False),
                resizable=True)


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
        self.lineEdit.setPlaceholderText("Positive integer")
        self.lineEdit_2.setPlaceholderText("Non-negative integer")
        self.lineEdit_3.setPlaceholderText("Integer")
        self.lineEdit_4.setPlaceholderText("Positive integer")
        self.lineEdit_5.setPlaceholderText("Non-negative integer")
        self.lineEdit_6.setPlaceholderText("Integer")
        self.lineEdit_posx.setPlaceholderText("Position x(0-10)")
        self.lineEdit_posy.setPlaceholderText("Position y(0-10)")
        self.lineEdit_posz.setPlaceholderText("Position z(0-10)")
        self.lineEdit_coef.setPlaceholderText("Coeff (-10 or 10)")

        self.cavas = MayaviQWidget()
        self.gridLayout.addWidget(self.cavas)
        self.pushButton.clicked.connect(self.start_counting)

        self.current_plot = None
        self.current_node_plot = None

    def start_counting(self):
        self.validationNLM()

    def validationNLM(self):
        params = {
            'n': 1, 'l': 0, 'm': 0,
            'n2': 1, 'l2': 0, 'm2': 0,
            'posx': 5.0, 'posy': 0.0, 'posz': 0.0, 'coef': 1.0
        }
        s = True

        try:
            params['n'] = int(self.lineEdit.text())
            params['n2'] = int(self.lineEdit_4.text())
            params['l'] = int(self.lineEdit_2.text())
            params['l2'] = int(self.lineEdit_5.text())
            params['m'] = int(self.lineEdit_3.text())
            params['m2'] = int(self.lineEdit_6.text())
        except ValueError:
            self.msg('Prompt: quantum number must be an integer')
            s = False

        if s:
            try:
                params['posx'] = float(self.lineEdit_posx.text()) if self.lineEdit_posx.text() else 5.0
                params['posy'] = float(self.lineEdit_posy.text()) if self.lineEdit_posy.text() else 0.0
                params['posz'] = float(self.lineEdit_posz.text()) if self.lineEdit_posz.text() else 0.0
                params['coef'] = float(self.lineEdit_coef.text()) if self.lineEdit_coef.text() else 1.0
            except ValueError:
                self.msg('Prompt: positions and coefficient must be numbers')
                s = False

        if s:
            if params['n'] <= 0:
                self.msg('Prompt: (n1) must be greater than 0')
                s = False
            elif params['l'] < 0 or params['l'] >= params['n']:
                self.msg('Prompt: (l1) must < n and >= 0')
                s = False
            elif abs(params['m']) > params['l']:
                self.msg('Prompt: (m1) should be in the range [-l1, l1]')
                s = False
            elif params['n2'] <= 0:
                self.msg('Prompt: (n2) must be greater than 0')
                s = False
            elif params['l2'] < 0 or params['l2'] >= params['n2']:
                self.msg('Prompt: (l2) must < n and >= 0')
                s = False
            elif abs(params['m2']) > params['l2']:
                self.msg('Prompt: (m2) should be in the range [-l2, l2]')
                s = False
            elif not (0 <= params['posx'] <= 10):
                self.msg('Prompt: posx should be in the range [0, 10]')
                s = False
            elif not (0 <= params['posy'] <= 10):
                self.msg('Prompt: posy should be in the range [0, 10]')
                s = False
            elif not (0 <= params['posz'] <= 10):
                self.msg('Prompt: posz should be in the range [0, 10]')
                s = False
            elif not (-10 <= params['coef'] <= 10):
                self.msg('Prompt: coef should be in the range [-10, 10]')
                s = False

        if s:
            self.plot_superposition(params)

    def plot_superposition(self, params):
        scene = self.cavas.visualization.scene
        mlab.figure(figure=scene.mayavi_scene)
        scene.mlab.clf()

        #a0 = 5.291772108e-11
        n1, l1, m1 = params['n'], params['l'], params['m']
        n2, l2, m2 = params['n2'], params['l2'], params['m2']
        posx, posy, posz = params['posx'], params['posy'], params['posz']
        coef = params['coef']

        Rmax = a0 * (5 * n1 ** R_EXP)
        x, y, z = np.mgrid[-2*Rmax:2*Rmax:GRID_3D*1j, -2*Rmax:2*Rmax:GRID_3D*1j, -2*Rmax:2*Rmax:GRID_3D*1j]
        dx = posx * Rmax/5
        dy = posy * Rmax/5
        dz = posz * Rmax/5
        x1 = x - 0.5*dx
        y1 = y - 0.5*dy
        z1 = z - 0.5*dz
        r1, theta1, phi1 = cart2sph(x1, y1, z1)
        psi1 = calc_psi(r1, theta1, phi1, n1, l1, m1)
        x2 = x + 0.5*dx
        y2 = y + 0.5*dy
        z2 = z + 0.5*dz
        r2, theta2, phi2 = cart2sph(x2, y2, z2)
        psi2 = calc_psi(r2, theta2, phi2, n2, l2, m2)

        psi = psi1 + coef * psi2

        maxpsi = np.abs(np.max(psi))
        minpsi = np.abs(np.min(psi))
        limpsi = maxpsi if n1 == 1 else min(maxpsi, minpsi)

        if n1 == 1 and coef >= 0:
            scene.mlab.contour3d(
                x, y, z, psi,
                contours=[0.1 * limpsi],
                transparent=True,
                vmax=0.1 * limpsi,
                vmin=0.001 * limpsi
            )
        else:
            scene.mlab.contour3d(
                x, y, z, psi,
                contours=[-0.1 * limpsi, 0.1 * limpsi],
                transparent=True,
                vmax=0.1 * limpsi,
                vmin=-0.1 * limpsi
            )
        # 创建新的节面（半透明灰色）
        if np.min(psi) <= 0 <= np.max(psi):
            scene.mlab.contour3d(
                x, y, z, psi,
                contours=[0.0],
                opacity=0.2,
                transparent=True,
                color=(0.5, 0.5, 0.0)
            )

        # ========== 新增：标记两个波函数的中心位置 ==========
        # 第一个波函数
        scene.mlab.points3d(-0.5*dx, -0.5*dy, -0.5*dz, scale_factor= Rmax*0.08,
                            color=(0, 0, 0), opacity=0.8, resolution=10)
        # 第二个波函数
        scene.mlab.points3d(0.5*dx, 0.5*dy, 0.5*dz, scale_factor= Rmax*0.08,
                            color=(0, 0, 0), opacity=0.8, resolution=10)


    def msg(self, msg):
        QMessageBox.about(self, "Error", msg)


def start():
    # 获取或创建 QApplication 实例（确保全局唯一）
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    app.exec_()   # 阻塞直到所有窗口关闭，但不调用 sys.exit
    mlab.close(all=True)          # 窗口关闭后再清理一次

if __name__ == "__main__":
    start()