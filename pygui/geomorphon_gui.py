#!/usr/bin/env python
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from groundtruther.pygui.Ui_geomorphon_ui import Ui_geomorphon


class GeoMorphon(QWidget, Ui_geomorphon):
    def __init__(self, parent=None):
        super(GeoMorphon, self).__init__(parent)
        self.setupUi(self)
