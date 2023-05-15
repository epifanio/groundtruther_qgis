# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtui/hbc_browser_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(822, 562)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/epi.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 822, 22))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuWidgets = QtWidgets.QMenu(self.menuView)
        self.menuWidgets.setObjectName("menuWidgets")
        self.menuType_Here = QtWidgets.QMenu(self.menuView)
        self.menuType_Here.setObjectName("menuType_Here")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolWidget = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolWidget.sizePolicy().hasHeightForWidth())
        self.toolWidget.setSizePolicy(sizePolicy)
        self.toolWidget.setMinimumSize(QtCore.QSize(124, 56))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/tools.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolWidget.setWindowIcon(icon1)
        self.toolWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.toolWidget.setObjectName("toolWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tools = QtWidgets.QTabWidget(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tools.sizePolicy().hasHeightForWidth())
        self.tools.setSizePolicy(sizePolicy)
        self.tools.setMinimumSize(QtCore.QSize(100, 0))
        self.tools.setTabPosition(QtWidgets.QTabWidget.North)
        self.tools.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tools.setObjectName("tools")
        self.verticalLayout_3.addWidget(self.tools)
        self.toolWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.toolWidget)
        self.imageBrowsing = QtWidgets.QDockWidget(MainWindow)
        self.imageBrowsing.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.imageBrowsing.setWindowTitle("")
        self.imageBrowsing.setObjectName("imageBrowsing")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.dockWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.annotation_confidence_spinBox_label = QtWidgets.QLabel(self.groupBox_6)
        self.annotation_confidence_spinBox_label.setObjectName("annotation_confidence_spinBox_label")
        self.horizontalLayout.addWidget(self.annotation_confidence_spinBox_label)
        self.annotation_confidence_spinBox = QtWidgets.QDoubleSpinBox(self.groupBox_6)
        self.annotation_confidence_spinBox.setProperty("showGroupSeparator", False)
        self.annotation_confidence_spinBox.setDecimals(2)
        self.annotation_confidence_spinBox.setMaximum(1.0)
        self.annotation_confidence_spinBox.setSingleStep(0.01)
        self.annotation_confidence_spinBox.setProperty("value", 0.6)
        self.annotation_confidence_spinBox.setObjectName("annotation_confidence_spinBox")
        self.horizontalLayout.addWidget(self.annotation_confidence_spinBox)
        self.horizontalLayout_13.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem)
        self.rwd = QtWidgets.QPushButton(self.groupBox_6)
        self.rwd.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rwd.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/fa_solid/qtui/icons/fa_solid/backward.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rwd.setIcon(icon2)
        self.rwd.setAutoRepeat(True)
        self.rwd.setAutoRepeatDelay(500)
        self.rwd.setObjectName("rwd")
        self.horizontalLayout_13.addWidget(self.rwd)
        self.ImageIndexspinBox = QtWidgets.QSpinBox(self.groupBox_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ImageIndexspinBox.setFont(font)
        self.ImageIndexspinBox.setMinimum(0)
        self.ImageIndexspinBox.setProperty("value", 0)
        self.ImageIndexspinBox.setObjectName("ImageIndexspinBox")
        self.horizontalLayout_13.addWidget(self.ImageIndexspinBox)
        self.fwd = QtWidgets.QPushButton(self.groupBox_6)
        self.fwd.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fwd.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/fa_solid/qtui/icons/fa_solid/forward.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fwd.setIcon(icon3)
        self.fwd.setAutoRepeat(True)
        self.fwd.setAutoRepeatDelay(500)
        self.fwd.setAutoDefault(False)
        self.fwd.setObjectName("fwd")
        self.horizontalLayout_13.addWidget(self.fwd)
        self.ImageStepspinBox = QtWidgets.QSpinBox(self.groupBox_6)
        self.ImageStepspinBox.setMinimum(1)
        self.ImageStepspinBox.setMaximum(200)
        self.ImageStepspinBox.setObjectName("ImageStepspinBox")
        self.horizontalLayout_13.addWidget(self.ImageStepspinBox)
        self.zoomto = QtWidgets.QCheckBox(self.groupBox_6)
        self.zoomto.setFocusPolicy(QtCore.Qt.NoFocus)
        self.zoomto.setText("")
        self.zoomto.setObjectName("zoomto")
        self.horizontalLayout_13.addWidget(self.zoomto)
        self.range = QtWidgets.QSpinBox(self.groupBox_6)
        self.range.setAccelerated(True)
        self.range.setMaximum(900000)
        self.range.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.range.setProperty("value", 200)
        self.range.setObjectName("range")
        self.horizontalLayout_13.addWidget(self.range)
        self.gridLayout_8.addLayout(self.horizontalLayout_13, 1, 0, 1, 1)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_4 = QtWidgets.QLabel(self.groupBox_6)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_11.addWidget(self.label_4)
        self.ImageIndexSlider = QtWidgets.QSlider(self.groupBox_6)
        self.ImageIndexSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ImageIndexSlider.setProperty("value", 0)
        self.ImageIndexSlider.setSliderPosition(0)
        self.ImageIndexSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ImageIndexSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.ImageIndexSlider.setTickInterval(500)
        self.ImageIndexSlider.setObjectName("ImageIndexSlider")
        self.horizontalLayout_11.addWidget(self.ImageIndexSlider)
        self.link_to_image_viewer = QtWidgets.QCheckBox(self.groupBox_6)
        self.link_to_image_viewer.setText("")
        self.link_to_image_viewer.setChecked(True)
        self.link_to_image_viewer.setObjectName("link_to_image_viewer")
        self.horizontalLayout_11.addWidget(self.link_to_image_viewer)
        self.verticalLayout_14.addLayout(self.horizontalLayout_11)
        self.gridLayout_8.addLayout(self.verticalLayout_14, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_6)
        self.gisTools_logger = QtWidgets.QLineEdit(self.dockWidgetContents_2)
        self.gisTools_logger.setObjectName("gisTools_logger")
        self.verticalLayout_2.addWidget(self.gisTools_logger)
        self.imageBrowsing.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.imageBrowsing)
        self.gisTools = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gisTools.sizePolicy().hasHeightForWidth())
        self.gisTools.setSizePolicy(sizePolicy)
        self.gisTools.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.gisTools.setObjectName("gisTools")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.dockWidgetContents_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gisToolSplitter = QtWidgets.QSplitter(self.dockWidgetContents_4)
        self.gisToolSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.gisToolSplitter.setObjectName("gisToolSplitter")
        self.horizontalLayout_2.addWidget(self.gisToolSplitter)
        self.gisTools.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.gisTools)
        self.actionWizard = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/fa_solid/qtui/icons/fa_solid/screwdriver-wrench.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionWizard.setIcon(icon4)
        self.actionWizard.setObjectName("actionWizard")
        self.actionTools = QtWidgets.QAction(MainWindow)
        self.actionTools.setCheckable(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/fa_solid/qtui/icons/fa_solid/ruler-combined.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTools.setIcon(icon5)
        self.actionTools.setObjectName("actionTools")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/fa_solid/qtui/icons/fa_solid/power-off.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon6)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAnnotation = QtWidgets.QAction(MainWindow)
        self.actionAnnotation.setCheckable(True)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/fa_solid/qtui/icons/fa_solid/pen-to-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAnnotation.setIcon(icon7)
        self.actionAnnotation.setObjectName("actionAnnotation")
        self.actionGisTools = QtWidgets.QAction(MainWindow)
        self.actionGisTools.setCheckable(True)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/fa_regular/qtui/icons/fa_regular/compass.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGisTools.setIcon(icon8)
        self.actionGisTools.setObjectName("actionGisTools")
        self.actionImageBrowser = QtWidgets.QAction(MainWindow)
        self.actionImageBrowser.setCheckable(True)
        self.actionImageBrowser.setChecked(True)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/fa_solid/qtui/icons/fa_solid/image.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImageBrowser.setIcon(icon9)
        self.actionImageBrowser.setObjectName("actionImageBrowser")
        self.actiongrass_settings = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/grass/qtui/icons/grass/grass_bold_dark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiongrass_settings.setIcon(icon10)
        self.actiongrass_settings.setObjectName("actiongrass_settings")
        self.menuSettings.addAction(self.actionWizard)
        self.menuSettings.addAction(self.actionQuit)
        self.menuWidgets.addAction(self.actionTools)
        self.menuWidgets.addAction(self.actionAnnotation)
        self.menuWidgets.addAction(self.actionGisTools)
        self.menuWidgets.addAction(self.actionImageBrowser)
        self.menuView.addAction(self.menuWidgets.menuAction())
        self.menuView.addAction(self.menuType_Here.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.toolBar.addAction(self.actionWizard)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionImageBrowser)
        self.toolBar.addAction(self.actionTools)
        self.toolBar.addAction(self.actionGisTools)
        self.toolBar.addAction(self.actionAnnotation)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionQuit)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actiongrass_settings)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GroundTruther"))
        self.menuSettings.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuWidgets.setTitle(_translate("MainWindow", "Widgets"))
        self.menuType_Here.setTitle(_translate("MainWindow", "Type Here"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolWidget.setWindowTitle(_translate("MainWindow", "Tools"))
        self.annotation_confidence_spinBox_label.setText(_translate("MainWindow", "Detection Confidence"))
        self.annotation_confidence_spinBox.setToolTip(_translate("MainWindow", "Image Annotation Threshold"))
        self.label_4.setText(_translate("MainWindow", "Image Index"))
        self.actionWizard.setText(_translate("MainWindow", "Preferences..."))
        self.actionTools.setText(_translate("MainWindow", "Tools"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAnnotation.setText(_translate("MainWindow", "Image Annotation"))
        self.actionAnnotation.setToolTip(_translate("MainWindow", "Load and display Image object detection"))
        self.actionGisTools.setText(_translate("MainWindow", "GisTools"))
        self.actionGisTools.setToolTip(_translate("MainWindow", "Show GIS tools"))
        self.actionImageBrowser.setText(_translate("MainWindow", "ImageBrowser"))
        self.actiongrass_settings.setText(_translate("MainWindow", "grass_settings"))
import resources_rc
