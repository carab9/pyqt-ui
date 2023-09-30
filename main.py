#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 00:00:00 2023

@author: caraburgess
"""


import sys

#%% Question 1
# https://doc.qt.io/qt-5/qcolordialog.html
# https://doc.qt.io/qt-5/qcolordialog.html#signals
# https://doc.qt.io/qt-5/qcolordialog.html#colorSelected
# since QColorDialog inherits from QWidget, it has a show method

from PyQt5.QtWidgets import QApplication, QWidget, QColorDialog
from PyQt5.QtGui import QPainter, QColor
from random import randint

class MyWidget(QWidget):
    def __init__(self, rgb):
        super().__init__()
        self.l = 50
        self.x = randint(0, 600-self.l-1)
        self.y = randint(0, 400-self.l-1)
        # Mouse location
        self.mx = 0
        self.my = 0
        # red
        self.color = QColor(rgb[0], rgb[1], rgb[2])
        self.dialog = QColorDialog(self.color, parent=self)
        self.dialog.colorSelected.connect(self.colorSelectedProc)
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 600, 400)
        self.show()

    def colorSelectedProc(self):
        self.color = self.dialog.selectedColor()
        self.update()

    def paintEvent(self, e):
        qp = QPainter(self)
        # white background
        qp.fillRect(self.rect(), QColor(255, 255, 255))
        # color square
        qp.fillRect(self.x, self.y, self.l, self.l, self.color)
        qp.end()

    def mousePressEvent(self, e):
        x = e.pos().x()
        y = e.pos().y()
        if self.x <= x <= self.x + self.l and self.y <= y <= self.y + self.l:
            self.mx = x
            self.my = y

    def mouseMoveEvent(self, e):
        x = e.pos().x()
        y = e.pos().y()
        if self.x <= x <= self.x + self.l and self.y <= y <= self.y + self.l:
            new_x = self.x + x - self.mx
            new_y = self.y + y - self.my
            rect = self.rect()
            if rect.x() <= new_x <= rect.x()+rect.width()-self.l-1 and rect.y() <= new_y <= rect.y()+rect.height()-self.l-1:
                self.x = new_x
                self.y = new_y
                self.mx = x
                self.my = y
                self.update()

    def mouseDoubleClickEvent(self, e):
        x = e.pos().x()
        y = e.pos().y()
        if self.x <= x <= self.x + self.l and self.y <= y <= self.y + self.l:
            # Bind a procedure (colorSelectedProc) to color dialog's signal colorSelected
            self.dialog.show()

def main(rgb):
    app = QApplication([])
    w = MyWidget(rgb)
    app.exec_()

if len(sys.argv) == 2 and sys.argv[1] == '1':
    main([255, 0, 0])
elif len(sys.argv) == 5 and sys.argv[1] == '1':
    main([eval(i) for i in sys.argv[2:]])

#%% Question 2
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QTimer, QThread

class MyWidget(QWidget):
    def __init__(self, rgb):
        super().__init__()
        self.d = 30
        self.x = self.d
        self.y = self.d
        self.vx = 1
        self.vy = 1
        self.color = QColor(rgb[0], rgb[1], rgb[2])
        self.thread = MyThread(self)
        self.thread.start()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 600, 400)
        self.show()

    def paintEvent(self, e):
        qp = QPainter(self)
        # white background
        qp.fillRect(self.rect(), QColor(255, 255, 255))
        # color ball without black border
        qp.setPen(self.color)
        qp.setBrush(self.color)
        qp.drawEllipse(self.x, self.y, self.d, self.d)
        qp.end()

    def animate(self):
        self.checkCollision()
        self.update()

    def checkCollision(self):
        self.x += self.vx
        self.y += self.vy
        rect = self.rect()
        if self.x <= rect.x() and self.vx < 0:
            self.vx = -self.vx
        elif self.x >= rect.width() - self.d - 1 and self.vx > 0:
            self.vx = -self.vx
        if self.y <= rect.y() and self.vy < 0:
            self.vy = -self.vy
        elif self.y >= rect.height() - self.d - 1 and self.vy > 0:
            self.vy = -self.vy

class MyThread(QThread):
    def __init__(self, widget):
        super().__init__()
        self.widget = widget

    def work(self):
         self.widget.animate()

    # Begins execution of the thread by calling run()
    def run(self):
        timer = QTimer()
        timer.timeout.connect(self.work)
        timer.start(25)
        self.exec_()

def main(rgb):
    app = QApplication([])
    w = MyWidget(rgb)
    app.exec_()

if len(sys.argv) == 2 and sys.argv[1] == '2':
    main([255,0,0])
elif len(sys.argv) == 5 and sys.argv[1] == '2':
    main([eval(i) for i in sys.argv[2:]])