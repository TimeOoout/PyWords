import sys
import time

from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,QTextEdit,QLabel,
                             QPushButton, QApplication,QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,QGridLayout,
                             QLineEdit)
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import QCoreApplication, Qt

from PyQt5.QtGui import *
from PyQt5.QtCore import *
import PyQt5.QtWidgets
from PyQt5.QtWidgets import *
import requests
from PyQt5.QtMultimedia import *
from PyQt5 import QtCore


class Start_cartoon(QWidget):
    def __init__(self):
        super(Start_cartoon, self).__init__()
        self.Image=QImage()
        init= \
            {
                # 隐藏标题栏
                self.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint |
                                    QtCore.Qt.ToolTip),
                # 设置大小
                self.resize(1000,600),
                # 窗口定位中心
                self.center(),
                # 设置背景透明
                self.setAttribute(Qt.WA_TranslucentBackground),
            }

        self.Image.load("lib\start\\bg.png")
        self.bg=QLabel(self)
        self.bg.setPixmap(QPixmap.fromImage(self.Image))

        self.up_ct=QPropertyAnimation(self)
        self.down_ct=QPropertyAnimation(self)

        self.turnA_ct=QPropertyAnimation(self)
        self.turnB_ct=QPropertyAnimation(self)
        self.turnC_ct=QPropertyAnimation(self)
        self.turnD_ct=QPropertyAnimation(self)
        self.turnE_ct=QPropertyAnimation(self)



        self.logoUI()

    def logoUI(self):
        self.logoA=QLabel(self)
        self.Image.load("lib\start\logo-A.png")
        self.logoA.setPixmap(QPixmap.fromImage(self.Image))
        self.logoA.setHidden(True)

        self.logoB=QLabel(self)
        self.Image.load("lib\start\logo-B.png")
        self.logoB.setPixmap(QPixmap.fromImage(self.Image))
        self.logoB.setHidden(True)

        self.up_ct.setTargetObject(self.logoA)
        self.up_ct.setPropertyName(b'pos')
        self.up_ct.setStartValue(QPoint(-100,310))
        self.up_ct.setEndValue(QPoint(365,65))
        self.up_ct.setDuration(800)

        self.down_ct.setTargetObject(self.logoB)
        self.down_ct.setPropertyName(b'pos')
        self.down_ct.setStartValue(QPoint(1600,-100))
        self.down_ct.setEndValue(QPoint(425,55))
        self.down_ct.setDuration(800)

        self.nameA=QLabel(self)
        self.Image.load("lib\start\\name-A.png")
        self.nameA.setPixmap(QPixmap.fromImage(self.Image))
        self.nameA.setHidden(True)
        self.nameA.move(360,280)

        self.nameB=QLabel(self)
        self.Image.load("lib\start\\name-B.png")
        self.nameB.setPixmap(QPixmap.fromImage(self.Image))
        self.nameB.move(210,-200)



        self.word=QLabel(self)
        self.Image.load("lib\start\words.png")
        self.word.setPixmap(QPixmap.fromImage(self.Image))
        self.word.move(320,430)
        self.word.setHidden(True)



        self.show()


        self.in_=cartoon(self.bg,self,'bg')
        self.lo_A=cartoon(self.logoA,self,'bg')
        self.lo_B=cartoon(self.logoB,self,'bg')
        self.naA=cartoon(self.nameA,self,'Icon-1')
        self.wo=cartoon(self.word,self,'Icon-2')
        self.p=cartoon(self.nameB,self,'Logo-1')
        self.in_.start()



        self.up_ct.start()
        self.lo_A.start()
        self.down_ct.start()
        self.lo_B.start()
        self.naA.start()
        self.wo.start()
        self.p.start()




    def center(self):

        qr = self.frameGeometry() # 获得主窗口的一个矩形特定几何图形。这包含了窗口的框架。
        cp = QDesktopWidget().availableGeometry().center() # 算出相对于显示器的绝对值。
        # 并且从这个绝对值中，我们获得了屏幕中心点。
        qr.moveCenter(cp) # 矩形已经设置好了它的宽和高。现在我们把矩形的中心设置到屏幕的中间去。
        # 矩形的大小并不会改变。
        self.move(qr.topLeft())




class cartoon(QThread):
    def __init__(self,Qt5,Dad,Type):
        super(cartoon,self).__init__()
        self.op=QGraphicsOpacityEffect()
        self.Qt5=Qt5
        self.dad=Dad
        self.Type=Type
        self.turnA_ct=QPropertyAnimation(self.dad)
        self.turnB_ct=QPropertyAnimation(self.dad)
        self.turnC_ct=QPropertyAnimation(self.dad)
        self.turnD_ct=QPropertyAnimation(self.dad)
        self.turnE_ct=QPropertyAnimation(self.dad)
    def run(self) -> None:
        if self.Type=='bg':
            self.op.setOpacity(0)
            self.Qt5.setGraphicsEffect(self.op)
            self.Qt5.setHidden(False)
            for i in range(50):
                time.sleep(0.01)
                self.op.setOpacity(i/50)
                self.Qt5.setGraphicsEffect(self.op)
                self.dad.update()
                qApp.processEvents()
        elif self.Type=='Icon-1':
            time.sleep(1)
            self.op.setOpacity(0)
            self.Qt5.setGraphicsEffect(self.op)
            self.Qt5.setHidden(False)
            for i in range(50):
                time.sleep(0.01)
                self.op.setOpacity(i/50)
                self.Qt5.setGraphicsEffect(self.op)
                self.dad.update()
                qApp.processEvents()

        elif self.Type=='Icon-2':
            time.sleep(1.3)
            self.op.setOpacity(0)
            self.Qt5.setGraphicsEffect(self.op)
            self.Qt5.setHidden(False)
            for i in range(100):
                time.sleep(0.01)
                self.op.setOpacity(i/100)
                self.Qt5.setGraphicsEffect(self.op)
                self.dad.update()
                qApp.processEvents()

        elif self.Type=='Logo-1':
            i=0
            first=-200
            while i<=470:
                self.Qt5.move(210,first+i)
                self.dad.update()
                qApp.processEvents()
                i+=1
            first=first+i
            print('first')
            i=0
            while i<=70:
                time.sleep(0.001)
                self.Qt5.move(210,first-i)
                self.dad.update()
                qApp.processEvents()
                i+=1
            first=first-i
            time.sleep(0.01)
            i=0
            while i<=60:
                time.sleep(0.001)
                self.Qt5.move(210,first+i)
                self.dad.update()
                qApp.processEvents()
                i+=1
            first=first+i
            i=0
            while i<=30:
                time.sleep(0.001)
                self.Qt5.move(210,first-i)
                self.dad.update()
                qApp.processEvents()
                i+=1
            first=first-i
            time.sleep(0.01)
            i=0
            while i<=20:
                time.sleep(0.001)
                self.Qt5.move(210,first+i)
                self.dad.update()
                qApp.processEvents()
                i+=1
            time.sleep(4)
            print(True)
            sys.exit()


app=QApplication(sys.argv)
a=Start_cartoon()

sys.exit(app.exec_())
