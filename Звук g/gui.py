#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import PyQt5.QtWidgets as qw
import time

from playsound import playsound


class MainWindow(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 250)
        self.move(300, 300)
        self.setWindowTitle('Play sound')

        self.goBtn = qw.QPushButton('Play', self)
        self.goBtn.move(50, 50)
        self.goBtn.clicked.connect(self.play_song)

        self.quitBtn = qw.QPushButton('Quit', self)
        self.quitBtn.move(50, 100)
        self.quitBtn.clicked.connect(self.close)

    def play_song(self):
        playsound("out.wav")  



if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    w = MainWindow()
    w.show()

    sys.exit(app.exec_())
