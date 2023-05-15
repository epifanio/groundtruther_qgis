#!/usr/bin/env python
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from groundtruther.pygui.Ui_grm_lsi_ui import Ui_grm_lsi


class GrmLsi(QWidget, Ui_grm_lsi):
    def __init__(self, parent=None):
        super(GrmLsi, self).__init__(parent)
        self.setupUi(self)
