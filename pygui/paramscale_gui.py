#!/usr/bin/env python
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from groundtruther.pygui.Ui_paramscale_ui import Ui_paramscale


class ParamScale(QWidget, Ui_paramscale):
    def __init__(self, parent=None):
        super(ParamScale, self).__init__(parent)
        self.setupUi(self)
