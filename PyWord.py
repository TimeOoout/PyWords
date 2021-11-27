#@ 版权所有: Dream Studio © 版权所有

#@ 文件名：PyWord.py

#@ 文件功能描述：PyWord主程序

#@ 创建日期：2017年10月1日

#@ 创建人：Dream Studio


import PyTranslator
import os
import sys
import time

from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox, QTextEdit, QLabel,
                             QPushButton, QApplication, QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,
                             QGridLayout,
                             QLineEdit)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication, Qt

from PyQt5.QtGui import *
from PyQt5.QtCore import *
import PyQt5.QtWidgets
from PyQt5.QtWidgets import *
import requests
from PyQt5.QtMultimedia import *
from PyQt5 import QtCore
import sip


# ========主进程
class MainWin(QWidget):

    # =====应用初始化=====
    def __init__(self):
        super().__init__()
        self.Page = "HomePage"
        self.up_ct = QPropertyAnimation(self)
        self.down_ct = QPropertyAnimation(self)
        self.turn_ct = QPropertyAnimation(self)
        self.turn_way = 306
        self.mainUI()
        self.tray_Button()

        self.setFocusPolicy(Qt.ClickFocus)
        self.log_in()

    # =====创建托盘图标=====
    def tray_Button(self):
        self.tray = QSystemTrayIcon()

        # 创建QIcon对象，用于设置图标（图片过大会出错）
        # self.trayIconPix = QIcon(".BG\Simple\LOGO-tray.png")
        # self.trayIconPix.fill(QColor(100,100,100))
        self.Icon = QIcon("lib/tray/LOGO-tray.png")

        # 设置托盘图标（QIcon图标过大或者出错会导致托盘显示不出来）
        self.tray.setIcon(self.Icon)
        self.tray.activated.connect(self.open_tray_menu)

        self.tray.show()

    # =======托盘操作=======
    # ===集合===
    def open_tray_menu(self):
        self.tray_menu = Tray_Menu()
        self.tray_menu.CM_b.clicked.connect(self.Exit)
        self.tray_menu.main_b.clicked.connect(self.tray_h_p)
        self.tray_menu.new_b.clicked.connect(self.tray_n_p)
        self.tray_menu.list_b.clicked.connect(self.tray_l_p)
        self.tray_menu.UC_b.clicked.connect(self.tray_u_p)
        self.tray_menu.show()

    # ===托盘-主页===
    def tray_h_p(self):
        self.show()
        self.showNormal()
        self.home_page()
        self.raise_()

    # ===托盘-资讯===xi
    def tray_n_p(self):
        self.show()
        self.showNormal()
        self.news_page()
        self.raise_()

    # ===托盘-任务列表===
    def tray_l_p(self):
        self.show()
        self.showNormal()
        self.list_page()
        self.raise_()

    # ===托盘-用户中心===
    def tray_u_p(self):
        self.show()
        self.showNormal()
        self.UC_page()
        self.raise_()

    # =====主要界面=====
    def mainUI(self):
        # ============窗口初始化======================================
        init = \
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

        # 放置按钮
        self.select_window()

        # 展示窗口
        self.show()

    # =======设置背景=======
    def BG(self):
        # ------------主要背景部分------------------------------------
        # 设置LOGO
        self.setWindowIcon(QIcon("lib/skin/LOGO.png"))
        self.setWindowTitle("PyWord")
        QToolTip.setFont(QFont("微软雅黑", 10))

        # 设置背景
        self.bg = QImage()
        self.bg.load("lib/skin/small-bg.png")
        self.b = QLabel(self)
        self.b.setPixmap(QPixmap.fromImage(self.bg))
        self.b.resize(1200, 800)
        self.b.move(-3, -4)

        # =====设置最大/小化按钮======================
        self.qs = QImage()
        self.qb = QImage()
        self.qs.load("lib/skin/Small-teest.png")
        self.qb.load("lib/skin/Close-test.png")
        self.qsa = QLabel(self)
        self.qba = QLabel(self)
        self.qsa.setPixmap(QPixmap.fromImage(self.qs))
        self.qba.setPixmap(QPixmap.fromImage(self.qb))

        # ====设置标签提示框========================
        self.logo = QLabel(self)
        self.logo.resize(300, 80)
        self.logo.move(5, 15)
        self.logo.setToolTip("一个专注于英语学习的软件！")

        # ====设置按钮透明==========================
        self.op = PyQt5.QtWidgets.QGraphicsOpacityEffect()
        self.op.setOpacity(0)
        self.op2 = PyQt5.QtWidgets.QGraphicsOpacityEffect()
        self.op2.setOpacity(0)

        # ====关闭按钮============================
        self.close_btn = QPushButton(self)  # 创建一个按钮
        self.close_btn.setText('X')  # 按钮显示显示文本
        self.close_btn.resize(20, 20)  # 按钮的大小
        self.close_btn.setGraphicsEffect(self.op)
        self.close_btn.setToolTip("退出程序")
        self.close_btn.released.connect(self.close)

        # =====最小化按钮============================
        self.min_btn = QPushButton(self)
        self.min_btn.setText('一')
        self.min_btn.resize(20, 20)
        self.min_btn.setGraphicsEffect(self.op2)
        self.min_btn.setToolTip("最小化")
        self.min_btn.released.connect(self.showMinimized)

        # =====搜索栏==============================
        self.search_bar()

    def search_bar(self):
        self.sear_op1=QGraphicsOpacityEffect()
        self.sear_op1.setOpacity(0)
        self.searchbar=QLabel(self)
        self.search=QImage()
        self.search.load("lib\skin\search-bar.png")
        self.searchbar.setPixmap(QPixmap.fromImage(self.search))
        self.searchbar.move(7,88)


        self.search.load("D:\PythonFiles\Myfiles\TestFiles(P)\Words\lib\skin\search_word.png")
        self.search_wordlist=QLabel(self)
        self.search_wordlist.setPixmap(QPixmap.fromImage(self.search))
        self.search_wordlist.move(60,160)
        self.search_wordlist.setHidden(True)


        self.searchicon=QLabel(self)
        self.search.load("lib\skin\search-icon.png")
        self.searchicon.setPixmap(QPixmap.fromImage(self.search))
        self.searchicon.move(730,106)

        self.searchbutton=QPushButton(self)
        self.searchbutton.resize(35,35)
        self.searchbutton.move(725,100)
        self.searchbutton.setGraphicsEffect(self.sear_op1)
        self.searchbutton.clicked.connect(self.Search)

        self.sear_op=QGraphicsOpacityEffect()
        self.sear_op.setOpacity(1)
        self.searchline=QLineEdit(self)
        self.searchline.resize(280,35)
        self.searchline.move(440,101)
        self.Font=QFont()
        #self.Font.setBold(True)
        self.searchline.setFont(self.Font)
        self.searchline.setFont(QFont('微软雅黑',15))
        self.searchline.setStyleSheet('background-color: transparent; border:0px')
        self.searchline.returnPressed.connect(self.Search)

        self.the_word=QLabel(self)
        self.the_word.setFont(QFont('微软雅黑',40))
        self.the_word.resize(550,80)
        self.the_word.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.the_word.setStyleSheet('background-color: transparent; border:0px')
        self.the_word.setHidden(True)
        self.pronounce=QTextEdit(self)
        self.pronounce.setFont(QFont('微软雅黑',10))
        self.pronounce.resize(500,80)

        self.pronounce.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.pronounce.setStyleSheet('background-color: transparent; border:0px')
        self.pronounce.setHidden(True)
        self.pronounceA=QTextEdit(self)
        self.pronounceA.setFont(QFont('微软雅黑',10))
        self.pronounceA.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.pronounceA.setStyleSheet('background-color: transparent; border:0px')
        self.pronounceA.resize(500,80)
        self.pronounceA.setHidden(True)
        self.pronounce.move(130,235)
        self.pronounceA.move(130,250)
        self.simple_meaning=QTextEdit(self)
        self.simple_meaning.move(100,300)
        #self.simple_meaning.setFont(QFont('微软雅黑',13))
        self.simple_meaning.setStyleSheet('background-color: transparent; border:0px')
        #self.simple_meaning.setStyleSheet('QWidget{background-color: dodgerblue; border:0px;border-radius:15px;}')
        self.simple_meaning.resize(480,400)
        #self.simple_meaning.move(-100,-100)
        self.simple_meaning.setHidden(True)
        self.simple_meaning.setTextInteractionFlags(Qt.TextSelectableByMouse)
        #self.simple_meaning.setWordWrapMode()


        self.search.load("lib/skin/play.png")

        self.play_icon=QLabel(self)
        self.play_icon.setPixmap(QPixmap.fromImage(self.search))
        self.play_iconA=QPushButton(self)
        self.play_iconA.resize(20,20)
        self.play_iconA.clicked.connect(self.play_E)
        self.play_iconA.move(100,241)
        #self.play_icon.setHidden(True)
        self.play_icon.move(102,242)

        self.play_icon1=QLabel(self)
        self.play_icon1.setPixmap(QPixmap.fromImage(self.search))


        self.play_iconB=QPushButton(self)
        self.search_op2=QGraphicsOpacityEffect()
        self.search_op2.setOpacity(0)
        self.search_op3=QGraphicsOpacityEffect()
        self.search_op3.setOpacity(0)
        self.play_icon1.setHidden(True)
        self.play_iconA.setHidden(True)
        self.play_icon.setHidden(True)
        self.play_iconB.setHidden(True)
        self.play_iconA.setGraphicsEffect(self.search_op2)
        self.play_iconB.setGraphicsEffect(self.search_op3)
        self.play_iconB.resize(20,20)
        self.play_iconB.clicked.connect(self.play_A)


        self.guess=QTextEdit(self)
        self.guess.resize(450,100)
        self.guess.move(110,650)
        self.guess.setHidden(True)
        self.guess.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.guess.setStyleSheet('''QWidget{background-color: #d2e1f8; border:0px;border-radius:15px;}''')

        self.phrase=QTextEdit(self)
        self.phrase.resize(460,530)
        self.phrase.move(680,235)
        self.phrase.setHidden(True)
        self.phrase.setStyleSheet('''QWidget{background-color: #b4caea; border:0px;border-radius:15px;}''')
        self.phrase.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.search_internet=QPushButton(self)
        self.search.load("lib\skin\search_list.png")
        #self.search_internet.setPixmap(QPixmap.fromImage(self.search))
        self.search_internet.move(680,180)
        self.search_internet.setText('网络释义')
        self.search_internet.setHidden(True)
        self.search_internet.clicked.connect(self.search_inter)







        self.the_word.move(95,150)

    def search_inter(self):
        if self.find_list['Internet-meaning']!=[]:
            self.phrase.setText('')
            self.phrase.append("<font face='微软雅黑' size=6><b>网络释义:</b></font>")
            for i in self.find_list['Internet-meaning']:
                self.phrase.append("<font color=dodgerblue face='微软雅黑' size=4><b>"+i[0]+'</b></font>:<font color=black face="微软雅黑" size=4>'+i[1]+'</font>')

    def play_A(self):
        print(True)
        self.american=Play(self.find_list['Word'],'American')
        self.american.start()

    def play_E(self):
        print(True)
        self.english=Play(self.find_list['Word'],'English')
        self.english.start()

    def Search(self):

        self.init=PyTranslator.Search_words()

        a=self.init.Simple_search(self.searchline.text())
        self.find_list=a
        print(a)

        self.play_icon1.setHidden(True)
        self.play_iconA.setHidden(True)
        self.play_icon.setHidden(True)
        self.play_iconB.setHidden(True)
        self.the_word.setHidden(True)
        self.pronounce.setHidden(True)
        self.pronounceA.setHidden(True)
        self.simple_meaning.setHidden(True)
        self.guess.setHidden(True)
        self.search_internet.setHidden(True)

        self.phrase.setHidden(True)
        self.phrase.setHidden(False)
        self.the_word.setHidden(False)
        self.search_wordlist.setHidden(True)
        self.search_wordlist.setHidden(False)
        self.guess.setText('')
        self.simple_meaning.setText('')
        self.phrase.setText('')

        self.the_word.setText("[ "+a['Word']+" ]")
        if len(a['Word'])>=18:
            b=list(a['Word'])
            b[16:19]='...'
            c=''
            d=0
            for i in b:
                if d==19:
                    break
                c+=i
                d+=1

            self.the_word.setText("[ "+c+" ]")
        self.the_word.show()
        content=[]



        if a['pronounce']!=[]:
            if len(a['pronounce'])==2:
                self.pronounce.setText("<font color=grey>英："+a['pronounce'][0]+'</color>')


                self.pronounceA.setText("<font color=grey>"+'美：'+a['pronounce'][1]+'</color>')
                self.play_iconA.setHidden(False)
                self.play_icon.setHidden(False)
                self.play_iconB.setHidden(False)
                self.play_icon1.setHidden(False)
                self.pronounce.setHidden(False)
                self.pronounceA.setHidden(False)
                self.play_iconB.move(100,270)
                self.play_icon1.move(101,272)
                self.pronounceA.move(130,265)

                content.append('Pronounce')
                content.append('PronounceA')
            else:
                self.pronounceA.setText("<font color=grey>"+a['pronounce'][0]+'</color>')
                self.play_iconB.setHidden(False)
                self.play_icon1.setHidden(False)
                self.pronounceA.setHidden(False)
                self.play_iconB.move(100,270)
                self.play_icon1.move(101,272)
                self.pronounceA.move(120,265)
                content.append('Pronounce')
                #self.pronounce.show()
        elif a['Pin-Yin']!=[]:
            self.pronounce.setText("<font color=grey>"+a['Pin-Yin'][0]+'</color>')
            self.pronounce.setHidden(False)
            content.append('Pronounce')
        if a['Simple-meaning']!=[]:


            n_num=0
            for i in a['Simple-meaning']:
                simple=''
                simple+='    '+i+';\n'
                self.simple_meaning.append('<font color=black face="微软雅黑" size=5><b>    '+simple+'</b></font>')
                n_num+=1
            self.simple_meaning.append('')
            self.simple_meaning.append('<font color=grey face="黑体" size=4>'+a['Others']+'</font>')
            self.simple_meaning.setHidden(False)




        elif a['Chinese-meaning']!=[]:
            simple=''
            n_num=0
            for i in a['Chinese-meaning']:
                simple=''
                simple+='    '+i+';\n'
                self.simple_meaning.append('<font color=black face="微软雅黑" size=5><b>    '+simple+'</b></font>')
                n_num+=1
            self.simple_meaning.append('')
            self.simple_meaning.append('<font color=grey face="黑体" size=4>'+a['Others']+'</font>')
            self.simple_meaning.setHidden(False)



        if a['Guess']!=[]:
            self.guess.append("<font color=black face='黑体' size=6><b>猜你想搜：</b></font>")
            for i in a['Guess']:
                self.guess.append("<font color=dodgerblue face='黑体' size=4><b>"+i[0]+'</b></font>:<font color=black face="黑体" size=4>'+i[1]+'</font>')
            self.guess.setHidden(False)

        if a['Internet-meaning']!=[]:
            self.search_internet.setHidden(False)
            self.phrase.append("<font face='微软雅黑' size=6><b>网络释义:</b></font>")
            for i in a['Internet-meaning']:
                self.phrase.append("<font color=dodgerblue face='微软雅黑' size=4><b>"+i[0]+'</b></font>:<font color=black face="微软雅黑" size=4>'+i[1]+'</font>')
            self.phrase.setHidden(False)










    # =====选择功能窗口=====
    def select_window(self):
        # ====设置窗口切换按钮=======================
        # -图标选择-
        self.ch_I = QImage()
        self.ch_I.load("lib\skin\choice.png")
        self.ch = QLabel(self)
        self.ch.setPixmap(QPixmap.fromImage(self.ch_I))
        self.ch.move(306, 35)

        # ---主界面Label---
        self.home_op = QGraphicsOpacityEffect()
        self.home_op.setOpacity(0)

        # -未选中-
        self.home_I = QImage()
        self.home_I.load("lib\skin\H-P_B.png")
        self.home_p_B = QLabel(self)
        self.home_p_B.setPixmap(QPixmap.fromImage(self.home_I))
        self.home_p_B.move(300, 10)
        # -已选中-
        self.home_I.load("lib\skin\H-P.png")
        self.home_p = QLabel(self)
        self.home_p.setPixmap(QPixmap.fromImage(self.home_I))
        self.home_p.move(300, 10)

        # ---主界面Button---
        self.home_b = QPushButton(self)
        self.home_b.resize(50, 50)
        self.home_b.move(305, 10)
        self.home_b.setGraphicsEffect(self.home_op)
        self.home_b.released.connect(self.home_page)
        self.home_b.setToolTip("主页")

        # ---资讯界面---
        # ==资讯Label==
        # -未选中-
        self.new_I = QImage()
        self.new_I.load("lib\skin\\news_B.png")
        self.new_p_B = QLabel(self)
        # self.new_p_B.resize(50,50)
        self.new_p_B.setPixmap(QPixmap.fromImage(self.new_I))
        self.new_p_B.move(450, 10)
        # -已选中-
        self.new_I.load("lib\skin\\news.png")
        self.new_p = QLabel(self)
        self.new_p.resize(50, 50)
        self.new_p.setPixmap(QPixmap.fromImage(self.new_I))
        self.new_p.move(450, 10)
        self.new_p.setHidden(True)
        # -资讯Button-
        self.new_op = QGraphicsOpacityEffect()
        self.new_op.setOpacity(0)
        self.new_b = QPushButton(self)
        self.new_b.resize(50, 50)
        self.new_b.move(450, 10)
        self.new_b.setGraphicsEffect(self.new_op)
        self.new_b.released.connect(self.news_page)
        self.new_b.setToolTip("资讯")

        # ---列表界面---
        self.list_I = QImage()
        self.list_I.load("lib\skin\\list_B.png")
        self.list_p_B = QLabel(self)
        self.list_p_B.setPixmap(QPixmap.fromImage(self.list_I))
        self.list_p_B.move(570, 10)
        # -已选中-
        self.list_I.load("lib\skin\\list.png")
        self.list_p = QLabel(self)
        self.list_p.resize(50, 50)
        self.list_p.setPixmap(QPixmap.fromImage(self.list_I))
        self.list_p.move(570, 10)
        self.list_p.setHidden(True)
        # -资讯Button-
        self.list_op = QGraphicsOpacityEffect()
        self.list_op.setOpacity(0)
        self.list_b = QPushButton(self)
        self.list_b.resize(50, 50)
        self.list_b.move(570, 10)
        self.list_b.setGraphicsEffect(self.list_op)
        self.list_b.released.connect(self.list_page)
        self.list_b.setToolTip("任务列表")

        # ---个人中心界面---
        self.UC_I = QImage()
        self.UC_I.load("lib\skin\\U-C_B.png")
        self.UC_p_B = QLabel(self)
        self.UC_p_B.setPixmap(QPixmap.fromImage(self.UC_I))
        self.UC_p_B.move(690, 10)
        # -已选中-
        self.UC_I.load("lib\skin\\U-C.png")
        self.UC_p = QLabel(self)
        self.UC_p.resize(50, 50)
        self.UC_p.setPixmap(QPixmap.fromImage(self.UC_I))
        self.UC_p.move(690, 10)
        self.UC_p.setHidden(True)
        # -资讯Button-
        self.UC_op = QGraphicsOpacityEffect()
        self.UC_op.setOpacity(0)
        self.UC_b = QPushButton(self)
        self.UC_b.resize(50, 50)
        self.UC_b.move(690, 10)
        self.UC_b.setGraphicsEffect(self.UC_op)
        self.UC_b.released.connect(self.UC_page)
        self.UC_b.setToolTip("个人中心")

    # =====窗口切换操作=====

    # -主界面选择
    def home_page(self):
        if self.Page != "HomePage":
            self.Page = "HomePage"
            self.new_p.setHidden(True)
            self.new_p_B.show()
            self.home_p_B.setHidden(True)
            self.home_p.show()
            self.list_p_B.show()
            self.list_p.setHidden(True)
            self.UC_p_B.show()
            self.UC_p.setHidden(True)
            # -起跳-
            self.up_ct.setTargetObject(self.home_p)
            self.up_ct.setPropertyName(b'pos')
            self.up_ct.setStartValue(QPoint(300, 10))
            self.up_ct.setEndValue(QPoint(300, 1))
            self.up_ct.setDuration(500)
            self.up_ct.start()
            # -选择-
            self.turn_ct.setTargetObject(self.ch)
            self.turn_ct.setPropertyName(b'pos')
            print(self.turn_way)
            self.turn_ct.setStartValue(QPoint(self.turn_way, 35))
            self.turn_way = 306
            self.turn_ct.setEndValue(QPoint(306, 35))
            self.turn_ct.setDuration(100)
            self.turn_ct.start()
            # -落下-
            self.down_ct.setTargetObject(self.home_p)
            self.down_ct.setPropertyName(b'pos')
            self.down_ct.setStartValue(QPoint(300, 1))
            self.down_ct.setEndValue(QPoint(300, 10))
            self.down_ct.setDuration(100)
            self.down_ct.start()

        print(self.Page)

    # -资讯列表选择
    def news_page(self):
        if self.Page != "NewsPage":
            self.Page = "NewsPage"
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
            self.up_ct.setStartValue(QPoint(self.turn_way, 10))
            self.up_ct.setEndValue(QPoint(450, 1))
            self.up_ct.setDuration(300)
            self.up_ct.start()

            # -选择-
            self.turn_ct.setTargetObject(self.ch)
            self.turn_ct.setPropertyName(b'pos')
            self.turn_ct.setStartValue(QPoint(self.turn_way, 35))
            self.turn_way = 450
            self.turn_ct.setEndValue(QPoint(451, 35))
            self.turn_ct.setDuration(100)
            self.turn_ct.start()

            self.down_ct.setTargetObject(self.new_p)
            self.down_ct.setPropertyName(b'pos')
            self.down_ct.setStartValue(QPoint(450, 1))
            self.down_ct.setEndValue(QPoint(450, 10))
            self.down_ct.setDuration(100)
            self.down_ct.start()
        print(self.Page)

    # -任务列表选择
    def list_page(self):
        if self.Page != "ListPage":
            self.Page = "ListPage"
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
            self.up_ct.setStartValue(QPoint(self.turn_way, 10))
            self.up_ct.setEndValue(QPoint(570, 1))
            self.up_ct.setDuration(300)
            self.up_ct.start()

            # -选择-
            self.turn_ct.setTargetObject(self.ch)
            self.turn_ct.setPropertyName(b'pos')
            self.turn_ct.setStartValue(QPoint(self.turn_way, 35))
            self.turn_way = 570
            self.turn_ct.setEndValue(QPoint(572, 35))
            self.turn_ct.setDuration(100)
            self.turn_ct.start()

            self.down_ct.setTargetObject(self.list_p)
            self.down_ct.setPropertyName(b'pos')
            self.down_ct.setStartValue(QPoint(570, 1))
            self.down_ct.setEndValue(QPoint(570, 10))
            self.down_ct.setDuration(100)
            self.down_ct.start()
        print(self.Page)

    # -个人中心选择
    def UC_page(self):
        if self.Page != "UCPage":
            self.Page = "UCPage"
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
            self.up_ct.setStartValue(QPoint(self.turn_way, 10))
            self.up_ct.setEndValue(QPoint(690, 1))
            self.up_ct.setDuration(300)
            self.up_ct.start()

            # -选择-
            self.turn_ct.setTargetObject(self.ch)
            self.turn_ct.setPropertyName(b'pos')
            self.turn_ct.setStartValue(QPoint(self.turn_way, 35))
            self.turn_way = 690
            self.turn_ct.setEndValue(QPoint(690, 35))
            self.turn_ct.setDuration(100)
            self.turn_ct.start()

            self.down_ct.setTargetObject(self.UC_p)
            self.down_ct.setPropertyName(b'pos')
            self.down_ct.setStartValue(QPoint(690, 1))
            self.down_ct.setEndValue(QPoint(690, 10))
            self.down_ct.setDuration(100)
            self.down_ct.start()

        print(self.Page)

    # =====定位窗口中心=====
    def center(self):

        qr = self.frameGeometry()  # 获得主窗口的一个矩形特定几何图形。这包含了窗口的框架。
        cp = QDesktopWidget().availableGeometry().center()  # 算出相对于显示器的绝对值。
        # 并且从这个绝对值中，我们获得了屏幕中心点。
        qr.moveCenter(cp)  # 矩形已经设置好了它的宽和高。现在我们把矩形的中心设置到屏幕的中间去。
        # 矩形的大小并不会改变。
        self.move(qr.topLeft())

    # =====关闭事件=====
    def closeEvent(self, event):
        # 设置消息提醒框
        reply = QMessageBox.question(self, '提示:',
                                     "要离开我了吗QAQ？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            sys.exit(app.exec_())
        else:
            event.ignore()

    # =====按钮重新布局=====
    def resizeEvent(self, QResizeEvent):
        # 重新计算三个按钮的位置
        # 关闭按钮
        self.close_btn_x = self.width() - self.close_btn.width() - 41
        self.close_btn.move(self.close_btn_x, 32)
        # 关闭标签
        self.qba.move(self.close_btn_x + 1, 33)
        # 最小化标签
        self.qsa.move(self.close_btn_x - 40, 33)
        # 最小化按钮
        self.min_btn_x = self.close_btn_x - self.min_btn.width()
        self.min_btn.move(self.min_btn_x - 21, 32)

    # =====鼠标按下事件=====
    def mousePressEvent(self, evt):
        # 鼠标在窗口上按下的位置
        self.globalPos = evt.y()
        # 方便调试
        print(self.globalPos)

        if self.globalPos < 80:
            # 获取鼠标当前的坐标
            self.mouse_x = evt.globalX()
            self.mouse_y = evt.globalY()

            # 获取窗体当前坐标
            self.origin_x = self.x()
            self.origin_y = self.y()

    # =====鼠标移动事件=====
    def mouseMoveEvent(self, evt):
        # 计算鼠标移动的x，y位移
        if not self.isMaximized() and self.globalPos < 80:
            move_x = evt.globalX() - self.mouse_x
            move_y = evt.globalY() - self.mouse_y
            # 计算窗体更新后的坐标：更新后的坐标 = 原本的坐标 + 鼠标的位移
            dest_x = self.origin_x + move_x
            dest_y = self.origin_y + move_y
            # 移动窗体
            self.move(dest_x, dest_y)
        elif self.isMaximized() and self.globalPos < 80:
            # print(True)
            self.b.setHidden(False)
            self.cb.setHidden(True)
            self.update()
            self.showNormal()

    # =====关闭事件=====
    def Exit(self):
        # 点击关闭按钮或者点击退出事件会出现图标无法消失的bug，需要手动将图标内存清除
        self.close()

    # =====托盘打开事件=====
    def Show(self):
        self.show()

    # =====内测用户=====
    def log_in(self):
        self.FuZhu = 'J+iClumAuOWHoS1YaWFvWWlmYW4t6IWQ56u5LeaKgOacr+aUr+aMgXzmioDmnK/mjIflr7wnID1hc2RmaGhhbHVlaXNobHFwdzk4dHkgaHBxdnc0IDBwY25tNSA3IDkwXVszcTI1YiUhIDM0dHkgOVs0MHU3ZzggcVs4TlxXRVJUCgkHYVx3ZXJcZSAHIDNccWIIZ3YmJSRAIUAhJCpxYjUzNDtob3JnY3YgbztpNHdlcmdqc3ZjW3UwOTMgZWlvcEpHTERVWTU3ODlUNlE0UEdISUFFXV1d'
        self.XueWei = 'J+WtpuWnlC3mna3lmInlroctSGFuZ0ppYXl1LeaKgOacr+aUr+aMgXznvo7mnK/mlK/mjIEnOXBxMzg0aHV3cmVmOXA4NHlodDN3cnVuLSAgaTMwMTJycUVQRkpRVkVSUSPvv6V2M+S4jXZDM0JWUVYgVjM0UVZRM1Y0VkIzVkJXRVJCd3Yg5paH5peF5reY5a6d572RdjN2I0I1Y3YxJk5eQiRtbjglTkIydmI1YzQzNjklI15WMmMlVlgkI14qTkImJF5AQ1glJE0oXlAqPEMhQCMlMnZjNDV5M2libjc2NHlodDV3'
        self.Youhui = 'J+acieeBsC3lkLTnvr3oj7ItV3VZdUZlaS3nvo7mnK/mjIflr7zigJnllYrlo6vlpKflpKvlkozpmL/mlod15oyW5rOVaGkgduWViuWVinVp5oiR54ix5ZCD5ZKM5a6J5b695oiRdOWFtjR2c3ZyYWV2Y2ZhZXZucnRid0BCXiUkKiglJiRHVlFXVEUkJiNCJSRWR3YxMnYzYjZ3Q0ZnNG4mJUd2Y3k0JVZeTl4kJTduYnY0d2M1NXZiNOWOuzUzNeWJjXY25YW2NDZ25YW2djQ25YW2djY05YW2djQ2cTM0djblhbY0djblhbZ2NDYz5YmNNnY15YW2NGPkuozlhbYyMzU2dg=='
        self.Else = 'J05vLk5pbmUt5Lmd54+tLemYv+iQqHVh5ZOI5ber5p2l54S25ZCO5LmxdWnpmL/mlodJVUVRSFRXNElVSUhVNFE4NzkgQUlVUTRPMzg5N0hPSVHlkozljrvlkoznkLznkLzlgbblk6Yg5YW2NFEj77+lICMlIOKApuKApu+8gSM2IO+8gSPvv6UgZXJ0d3ZAQlZAJUJXdnkyWSVWIyEjJEDvv6UlIFl2b25uZTUx5aW9djIkI2Ix5LiA55m+5LiJ5Y2B5ZubNTF2MyQxMzViNHY257u/6JC8'
        self.user = self.XueWei
        if self.user == self.XueWei:
            self.head = QLabel(self)
            self.h = QImage()
            self.h.load('lib\Icon\Dream-Studio - C.png')
            self.head.setPixmap(QPixmap.fromImage(self.h))
            self.head.move(820, 17)
            self.head.show()

    # def paintEvent(self, a0: QPaintEvent) -> None:
    #     opt = QStyleOption()
    #     opt.initFrom(self)
    #     painter = QPainter(self)
    #     #painter.setRenderHint(QtGui.QPainter.Antialiasing) # 反锯齿
    #     self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)



# =========语音
class Play(QThread):
    def __init__(self, word, r_type):
        super(Play, self).__init__()
        self.word = word
        self.type = r_type

    def run(self) -> None:
        if self.type == "English":
            play = QMediaContent(QUrl("http://dict.youdao.com/dictvoice?audio=" + self.word + "&type=1"))
        elif self.type == "American":
            play = QMediaContent(QUrl("http://dict.youdao.com/dictvoice?audio=" + self.word + "&type=2"))
        self.player = QMediaPlayer()
        self.player.setMedia(play)
        # self.player.setVolume(1000)
        self.player.play()
        # time.sleep(3)


# =========托盘
class Tray_Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.main_ui()

    def main_ui(self):
        self.setFocusPolicy(Qt.ClickFocus)

        self.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint |
                            QtCore.Qt.ToolTip)

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.resize(245, 395)
        self.move(1580, 590)
        self.raise_()

        # 背景
        self.Image = QImage()
        self.Image.load("lib\\tray\Tray_Menu_BG.png")
        self.bg = QLabel(self)
        self.bg.setPixmap(QPixmap.fromImage(self.Image))
        self.bg.move(-2, -2)
        self.bg.show()

        # 标签
        self.home_op = QGraphicsOpacityEffect()
        self.home_op.setOpacity(0)
        self.main = QLabel(self)
        self.main.setFont(QFont("幼圆", 11))
        self.main.setText("主页")
        self.main.move(110, 60)
        self.main_b = QPushButton(self)
        self.main_b.resize(150, 27)
        self.main_b.move(38, 58)
        self.main_op = QGraphicsOpacityEffect()
        self.main_op.setOpacity(0)
        self.main_b.setGraphicsEffect(self.main_op)

        self.home_op = QGraphicsOpacityEffect()
        self.home_op.setOpacity(0)
        self.new = QLabel(self)
        self.new.setFont(QFont("幼圆", 11))
        self.new.setText("资讯")
        self.new.move(110, 95)
        self.new_b = QPushButton(self)
        self.new_b.resize(150, 27)
        self.new_b.move(38, 90)
        self.new_op = QGraphicsOpacityEffect()
        self.new_op.setOpacity(0)
        self.new_b.setGraphicsEffect(self.new_op)

        self.list_op = QGraphicsOpacityEffect()
        self.list_op.setOpacity(0)
        self.list = QLabel(self)
        self.list.setFont(QFont("幼圆", 11))
        self.list.setText("任务列表")
        self.list.move(110, 126)
        self.list_b = QPushButton(self)
        self.list_b.resize(150, 27)
        self.list_b.move(38, 122)
        self.list_op = QGraphicsOpacityEffect()
        self.list_op.setOpacity(0)
        self.list_b.setGraphicsEffect(self.list_op)

        self.UC_op = QGraphicsOpacityEffect()
        self.UC_op.setOpacity(0)
        self.UC = QLabel(self)
        self.UC.setFont(QFont("幼圆", 11))
        self.UC.setText("个人中心")
        self.UC.move(110, 160)
        self.UC_b = QPushButton(self)
        self.UC_b.resize(150, 27)
        self.UC_b.move(38, 155)
        self.UC_b.setGraphicsEffect(self.UC_op)

        self.Image.load("lib\\tray\Close-test.png")
        self.clo = QLabel(self)
        self.clo.setPixmap(QPixmap.fromImage(self.Image))
        self.clo.move(210, 15)
        self.clo_p = QPushButton(self)
        self.clo_p.resize(19, 19)
        self.clo_p.move(209, 14)
        self.clo_p.clicked.connect(self.hide_e)
        self.clo_op = QGraphicsOpacityEffect()
        self.clo_op.setOpacity(0)
        self.clo_p.setGraphicsEffect(self.clo_op)

        self.CM = QLabel(self)
        self.CM.setFont(QFont("幼圆", 11))
        self.CM.setText("退出")
        self.CM.move(110, 326)
        self.CM_b = QPushButton(self)
        self.CM_b.resize(150, 27)
        self.CM_b.move(38, 322)
        self.CM_op = QGraphicsOpacityEffect()
        self.CM_op.setOpacity(0)
        self.CM_b.setGraphicsEffect(self.CM_op)

        self.settings = QLabel(self)
        self.settings.setFont(QFont("幼圆", 11))
        self.settings.setText("设置")
        self.settings.move(110, 356)
        self.settings_b = QPushButton(self)
        self.settings_b.resize(150, 27)
        self.settings_b.move(38, 352)
        self.settings_op = QGraphicsOpacityEffect()
        self.settings_op.setOpacity(0)
        self.settings_b.setGraphicsEffect(self.settings_op)
        self.show()

    def hide_e(self):
        self.setHidden(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mythread = Play('They wore badges with the Chinese characters "Tongzhi Nihao" and a smiling face printed against a rainbow background, symbolizing gay pride.', "American")
    #mythread.start()
    #os.system('python Cartoon.py')
    ex = MainWin()

    sys.exit(app.exec_())
