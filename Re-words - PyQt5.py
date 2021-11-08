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



class MainWin(QWidget):

    #=====应用初始化=====
    def __init__(self):
        super().__init__()
        self.Page="HomePage"
        self.up_ct=QPropertyAnimation(self)
        self.down_ct=QPropertyAnimation(self)
        self.turn_ct=QPropertyAnimation(self)
        self.turn_way=306
        self.mainUI()
        self.tray_Button()


    #=====创建托盘图标=====
    def tray_Button(self):
        self.tray = QSystemTrayIcon()

        # 创建QIcon对象，用于设置图标（图片过大会出错）
        #self.trayIconPix = QIcon(".BG\Simple\LOGO-tray.png")
        #self.trayIconPix.fill(QColor(100,100,100))
        self.Icon = QIcon("lib/skin/LOGO-tray.png")

        # 设置托盘图标（QIcon图标过大或者出错会导致托盘显示不出来）
        self.tray.setIcon(self.Icon)

        # 创建QAction
        showAction = QAction("主界面", self, triggered = self.Show)
        quitAction = QAction("退出", self, triggered = self.close)
        # 创建菜单对象
        self.trayMenu = QMenu(self)
        # 将动作对象添加到菜单
        self.trayMenu.addAction(showAction)

        # 增加分割线
        self.trayMenu.addSeparator()
        self.trayMenu.addAction(quitAction)
        # 将菜单栏加入到右键按钮中
        self.tray.setContextMenu(self.trayMenu)

        self.tray.show()


    #=====主要界面=====
    def mainUI(self):
        # ============窗口初始化======================================
        init=\
        {
            # 隐藏标题栏
        self.setWindowFlags(Qt.FramelessWindowHint),
            # 设置大小
        self.setGeometry(600, 500, 1190, 790),
            # 窗口定位中心
        self.center(),
            # 设置背景透明
        self.setAttribute(Qt.WA_TranslucentBackground),
        }

        self.BG()

        #放置按钮
        self.select_window()

        #展示窗口
        self.show()

    #=====设置背景=====
    def BG(self):
        #------------主要背景部分------------------------------------
        #设置LOGO
        self.setWindowIcon(QIcon("lib/skin/LOGO.png"))
        self.setWindowTitle("PyWord")
        QToolTip.setFont(QFont("微软雅黑",10))

        #设置背景
        self.bg=QImage()
        self.bg.load("lib/skin/small-bg.png")
        self.b=QLabel(self)
        self.b.setPixmap(QPixmap.fromImage(self.bg))
        self.b.resize(1200,800)
        self.b.move(-3,-4)

        #=====设置最大/小化按钮======================
        self.qs=QImage()
        self.qb=QImage()
        self.qs.load("lib/skin/Small-teest.png")
        self.qb.load("lib/skin/Close-test.png")
        self.qsa=QLabel(self)
        self.qba=QLabel(self)
        self.qsa.setPixmap(QPixmap.fromImage(self.qs))
        self.qba.setPixmap(QPixmap.fromImage(self.qb))

        #====设置标签提示框========================
        self.logo = QLabel(self)
        self.logo.resize(300,80)
        self.logo.move(5,15)
        self.logo.setToolTip("一个专注于英语学习的软件！")

        #====设置按钮透明==========================
        self.op=PyQt5.QtWidgets.QGraphicsOpacityEffect()
        self.op.setOpacity(0)
        self.op2=PyQt5.QtWidgets.QGraphicsOpacityEffect()
        self.op2.setOpacity(0)

        #====关闭按钮============================
        self.close_btn = QPushButton(self)             #创建一个按钮
        self.close_btn.setText('X')                    #按钮显示显示文本
        self.close_btn.resize(20, 20)                  #按钮的大小
        self.close_btn.setGraphicsEffect(self.op)
        self.close_btn.setToolTip("退出程序")
        self.close_btn.released.connect(self.close)

        #=====最小化按钮============================
        self.min_btn = QPushButton(self)
        self.min_btn.setText('一')
        self.min_btn.resize(20, 20)
        self.min_btn.setGraphicsEffect(self.op2)
        self.min_btn.setToolTip("最小化")
        self.min_btn.released.connect(self.showMinimized)

    #=====选择功能窗口=====
    def select_window(self):
        #====设置窗口切换按钮=======================
        #-图标选择-
        self.ch_I=QImage()
        self.ch_I.load("lib\skin\choice.png")
        self.ch=QLabel(self)
        self.ch.setPixmap(QPixmap.fromImage(self.ch_I))
        self.ch.move(306,35)

        #---主界面Label---
        self.home_op=QGraphicsOpacityEffect()
        self.home_op.setOpacity(0)

        #-未选中-
        self.home_I=QImage()
        self.home_I.load("lib\skin\H-P_B.png")
        self.home_p_B=QLabel(self)
        self.home_p_B.setPixmap(QPixmap.fromImage(self.home_I))
        self.home_p_B.move(300,10)
        #-已选中-
        self.home_I.load("lib\skin\H-P.png")
        self.home_p=QLabel(self)
        self.home_p.setPixmap(QPixmap.fromImage(self.home_I))
        self.home_p.move(300,10)



        #---主界面Button---
        self.home_b=QPushButton(self)
        self.home_b.resize(50,50)
        self.home_b.move(305,10)
        self.home_b.setGraphicsEffect(self.home_op)
        self.home_b.released.connect(self.home_page)
        self.home_b.setToolTip("主页")

        #---资讯界面---
        #==资讯Label==
        #-未选中-
        self.new_I=QImage()
        self.new_I.load("lib\skin\\news_B.png")
        self.new_p_B=QLabel(self)
        #self.new_p_B.resize(50,50)
        self.new_p_B.setPixmap(QPixmap.fromImage(self.new_I))
        self.new_p_B.move(450,10)
        #-已选中-
        self.new_I.load("lib\skin\\news.png")
        self.new_p=QLabel(self)
        self.new_p.resize(50,50)
        self.new_p.setPixmap(QPixmap.fromImage(self.new_I))
        self.new_p.move(450,10)
        self.new_p.setHidden(True)
        #-资讯Button-
        self.new_op=QGraphicsOpacityEffect()
        self.new_op.setOpacity(0)
        self.new_b=QPushButton(self)
        self.new_b.resize(50,50)
        self.new_b.move(450,10)
        self.new_b.setGraphicsEffect(self.new_op)
        self.new_b.released.connect(self.news_page)
        self.new_b.setToolTip("资讯")

        #---列表界面---
        self.list_I=QImage()
        self.list_I.load("lib\skin\\list_B.png")
        self.list_p_B=QLabel(self)
        self.list_p_B.setPixmap(QPixmap.fromImage(self.list_I))
        self.list_p_B.move(570,10)
        #-已选中-
        self.list_I.load("lib\skin\\list.png")
        self.list_p=QLabel(self)
        self.list_p.resize(50,50)
        self.list_p.setPixmap(QPixmap.fromImage(self.list_I))
        self.list_p.move(570,10)
        self.list_p.setHidden(True)
        #-资讯Button-
        self.list_op=QGraphicsOpacityEffect()
        self.list_op.setOpacity(0)
        self.list_b=QPushButton(self)
        self.list_b.resize(50,50)
        self.list_b.move(570,10)
        self.list_b.setGraphicsEffect(self.list_op)
        self.list_b.released.connect(self.list_page)
        self.list_b.setToolTip("任务列表")

        #---个人中心界面---
        self.UC_I=QImage()
        self.UC_I.load("lib\skin\\U-C_B.png")
        self.UC_p_B=QLabel(self)
        self.UC_p_B.setPixmap(QPixmap.fromImage(self.UC_I))
        self.UC_p_B.move(690,10)
        #-已选中-
        self.UC_I.load("lib\skin\\U-C.png")
        self.UC_p=QLabel(self)
        self.UC_p.resize(50,50)
        self.UC_p.setPixmap(QPixmap.fromImage(self.UC_I))
        self.UC_p.move(690,10)
        self.UC_p.setHidden(True)
        #-资讯Button-
        self.UC_op=QGraphicsOpacityEffect()
        self.UC_op.setOpacity(0)
        self.UC_b=QPushButton(self)
        self.UC_b.resize(50,50)
        self.UC_b.move(690,10)
        self.UC_b.setGraphicsEffect(self.UC_op)
        self.UC_b.released.connect(self.UC_page)
        self.UC_b.setToolTip("个人中心")


    #=====窗口切换操作=====

    #-主界面选择
    def home_page(self):
        if self.Page!="HomePage":
            self.Page="HomePage"
            self.new_p.setHidden(True)
            self.new_p_B.show()
            self.home_p_B.setHidden(True)
            self.home_p.show()
            self.list_p_B.show()
            self.list_p.setHidden(True)
            self.UC_p_B.show()
            self.UC_p.setHidden(True)
            #-起跳-
            self.up_ct.setTargetObject(self.home_p)
            self.up_ct.setPropertyName(b'pos')
            self.up_ct.setStartValue(QPoint(300,10))
            self.up_ct.setEndValue(QPoint(300,3))
            self.up_ct.setDuration(300)
            self.up_ct.start()
            #-选择-
            self.turn_ct.setTargetObject(self.ch)
            self.turn_ct.setPropertyName(b'pos')
            print(self.turn_way)
            self.turn_ct.setStartValue(QPoint(self.turn_way,35))
            self.turn_way=306
            self.turn_ct.setEndValue(QPoint(306,35))
            self.turn_ct.setDuration(100)
            self.turn_ct.start()
            #-落下-
            self.down_ct.setTargetObject(self.home_p)
            self.down_ct.setPropertyName(b'pos')
            self.down_ct.setStartValue(QPoint(300,3))
            self.down_ct.setEndValue(QPoint(300,10))
            self.down_ct.setDuration(100)
            self.down_ct.start()


        print(self.Page)

    #-资讯列表选择
    def news_page(self):
        if self.Page!="NewsPage":
            self.Page="NewsPage"
            self.home_p.setHidden(True)
            self.home_p_B.show()
            self.new_p_B.setHidden(True)
            self.new_p.show()
            self.list_p_B.show()
            self.list_p.setHidden(True)
            self.UC_p_B.show()
            self.UC_p.setHidden(True)

            self.up_ct.setTargetObject(self.new_p)
            self.up_ct.setPropertyName(b'pos')
            print(self.turn_way)
            self.up_ct.setStartValue(QPoint(self.turn_way,10))
            self.up_ct.setEndValue(QPoint(450,3))
            self.up_ct.setDuration(300)
            self.up_ct.start()

            #-选择-
            self.turn_ct.setTargetObject(self.ch)
            self.turn_ct.setPropertyName(b'pos')
            self.turn_ct.setStartValue(QPoint(self.turn_way,35))
            self.turn_way=450
            self.turn_ct.setEndValue(QPoint(451,35))
            self.turn_ct.setDuration(100)
            self.turn_ct.start()

            self.down_ct.setTargetObject(self.new_p)
            self.down_ct.setPropertyName(b'pos')
            self.down_ct.setStartValue(QPoint(450,3))
            self.down_ct.setEndValue(QPoint(450,10))
            self.down_ct.setDuration(100)
            self.down_ct.start()
        print(self.Page)

    #-任务列表选择
    def list_page(self):
        if self.Page!="ListPage":
            self.Page="ListPage"
            self.home_p.setHidden(True)
            self.home_p_B.show()
            self.new_p_B.show()
            self.new_p.setHidden(True)
            self.list_p.show()
            self.list_p_B.setHidden(True)
            self.UC_p_B.show()
            self.UC_p.setHidden(True)

            self.up_ct.setTargetObject(self.list_p)
            self.up_ct.setPropertyName(b'pos')
            print(self.turn_way)
            self.up_ct.setStartValue(QPoint(self.turn_way,10))
            self.up_ct.setEndValue(QPoint(570,3))
            self.up_ct.setDuration(300)
            self.up_ct.start()

            #-选择-
            self.turn_ct.setTargetObject(self.ch)
            self.turn_ct.setPropertyName(b'pos')
            self.turn_ct.setStartValue(QPoint(self.turn_way,35))
            self.turn_way=570
            self.turn_ct.setEndValue(QPoint(572,35))
            self.turn_ct.setDuration(100)
            self.turn_ct.start()

            self.down_ct.setTargetObject(self.list_p)
            self.down_ct.setPropertyName(b'pos')
            self.down_ct.setStartValue(QPoint(570,3))
            self.down_ct.setEndValue(QPoint(570,10))
            self.down_ct.setDuration(100)
            self.down_ct.start()
        print(self.Page)

    #-个人中心选择
    def UC_page(self):
        if self.Page!="UCPage":
            self.Page="UCPage"
            self.home_p.setHidden(True)
            self.home_p_B.show()
            self.new_p_B.show()
            self.new_p.setHidden(True)
            self.list_p_B.show()
            self.list_p.setHidden(True)
            self.UC_p_B.setHidden(True)
            self.UC_p.show()

            self.up_ct.setTargetObject(self.UC_p)
            self.up_ct.setPropertyName(b'pos')
            print(self.turn_way)
            self.up_ct.setStartValue(QPoint(self.turn_way,10))
            self.up_ct.setEndValue(QPoint(690,3))
            self.up_ct.setDuration(300)
            self.up_ct.start()

            #-选择-
            self.turn_ct.setTargetObject(self.ch)
            self.turn_ct.setPropertyName(b'pos')
            self.turn_ct.setStartValue(QPoint(self.turn_way,35))
            self.turn_way=690
            self.turn_ct.setEndValue(QPoint(690,35))
            self.turn_ct.setDuration(100)
            self.turn_ct.start()

            self.down_ct.setTargetObject(self.UC_p)
            self.down_ct.setPropertyName(b'pos')
            self.down_ct.setStartValue(QPoint(690,3))
            self.down_ct.setEndValue(QPoint(690,10))
            self.down_ct.setDuration(100)
            self.down_ct.start()

        print(self.Page)

    #=====定位窗口中心=====
    def center(self):

        qr = self.frameGeometry() # 获得主窗口的一个矩形特定几何图形。这包含了窗口的框架。
        cp = QDesktopWidget().availableGeometry().center() # 算出相对于显示器的绝对值。
        # 并且从这个绝对值中，我们获得了屏幕中心点。
        qr.moveCenter(cp) # 矩形已经设置好了它的宽和高。现在我们把矩形的中心设置到屏幕的中间去。
        # 矩形的大小并不会改变。
        self.move(qr.topLeft())

    #=====关闭事件=====
    def closeEvent(self, event):
        #设置消息提醒框
        reply = QMessageBox.question(self, '提示:',
                                     "要离开我了吗QAQ？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            #self.setHidden(True)
            event.accept()
            sys.exit(app.exec_())
        else:
            event.ignore()

    #=====按钮重新布局=====
    def resizeEvent(self, QResizeEvent):
        # 重新计算三个按钮的位置
        #关闭按钮
        self.close_btn_x = self.width() - self.close_btn.width()-41
        self.close_btn.move(self.close_btn_x, 32)
        #关闭标签
        self.qba.move(self.close_btn_x+1, 33)
        #最小化标签
        self.qsa.move(self.close_btn_x-40, 33)
        #最小化按钮
        self.min_btn_x = self.close_btn_x - self.min_btn.width()
        self.min_btn.move(self.min_btn_x - 21, 32)

    #=====鼠标按下事件=====
    def mousePressEvent(self,evt):
        #鼠标在窗口上按下的位置
        self.globalPos = evt.y()
        #方便调试
        print(self.globalPos)

        if self.globalPos<80:
        # 获取鼠标当前的坐标
            self.mouse_x = evt.globalX()
            self.mouse_y = evt.globalY()

            # 获取窗体当前坐标
            self.origin_x = self.x()
            self.origin_y = self.y()

    #=====鼠标移动事件=====
    def mouseMoveEvent(self,evt):
        # 计算鼠标移动的x，y位移
        if not self.isMaximized() and self.globalPos<80:
            move_x = evt.globalX() - self.mouse_x
            move_y = evt.globalY() - self.mouse_y
                        # 计算窗体更新后的坐标：更新后的坐标 = 原本的坐标 + 鼠标的位移
            dest_x = self.origin_x + move_x
            dest_y = self.origin_y + move_y
                        # 移动窗体
            self.move(dest_x,dest_y)
        elif self.isMaximized() and self.globalPos<80:
            #print(True)
            self.b.setHidden(False)
            self.cb.setHidden(True)
            self.update()
            self.showNormal()

    #=====关闭事件=====
    def Exit(self):
        # 点击关闭按钮或者点击退出事件会出现图标无法消失的bug，需要手动将图标内存清除
        self.close()

    #=====托盘打开事件=====
    def Show(self):
        self.show()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex= MainWin()
    sys.exit(app.exec_())