# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtui/grm_lsi_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_grm_lsi(object):
    def setupUi(self, grm_lsi):
        grm_lsi.setObjectName("grm_lsi")
        grm_lsi.resize(541, 485)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/grass/qtui/icons/grass/grass_location.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        grm_lsi.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(grm_lsi)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(grm_lsi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(40, 40))
        self.label.setMaximumSize(QtCore.QSize(40, 40))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/grass/qtui/icons/grass/grass_location.svg"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(grm_lsi)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(grm_lsi)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 507, 812))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 70))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_32 = QtWidgets.QLabel(self.groupBox)
        self.label_32.setObjectName("label_32")
        self.gridLayout_10.addWidget(self.label_32, 0, 0, 1, 1)
        self.elevation = QtWidgets.QComboBox(self.groupBox)
        self.elevation.setObjectName("elevation")
        self.gridLayout_10.addWidget(self.elevation, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 320))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_8.addWidget(self.label_8, 1, 0, 1, 1)
        self.swc_dist = QtWidgets.QLineEdit(self.groupBox_2)
        self.swc_dist.setObjectName("swc_dist")
        self.gridLayout_8.addWidget(self.swc_dist, 3, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_8.addWidget(self.label_20, 3, 0, 1, 1)
        self.iter_thin = QtWidgets.QLineEdit(self.groupBox_2)
        self.iter_thin.setObjectName("iter_thin")
        self.gridLayout_8.addWidget(self.iter_thin, 4, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout_8.addWidget(self.label_21, 4, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox_2)
        self.label_22.setObjectName("label_22")
        self.gridLayout_8.addWidget(self.label_22, 7, 0, 1, 1)
        self.swc_skip = QtWidgets.QSpinBox(self.groupBox_2)
        self.swc_skip.setProperty("value", 3)
        self.swc_skip.setObjectName("swc_skip")
        self.gridLayout_8.addWidget(self.swc_skip, 1, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.groupBox_2)
        self.label_23.setObjectName("label_23")
        self.gridLayout_8.addWidget(self.label_23, 5, 0, 1, 1)
        self.generalize_method = QtWidgets.QComboBox(self.groupBox_2)
        self.generalize_method.setObjectName("generalize_method")
        self.generalize_method.addItem("")
        self.generalize_method.addItem("")
        self.generalize_method.addItem("")
        self.generalize_method.addItem("")
        self.generalize_method.addItem("")
        self.generalize_method.addItem("")
        self.generalize_method.addItem("")
        self.generalize_method.addItem("")
        self.generalize_method.addItem("")
        self.generalize_method.addItem("")
        self.generalize_method.addItem("")
        self.generalize_method.addItem("")
        self.gridLayout_8.addWidget(self.generalize_method, 6, 1, 1, 1)
        self.swc_search = QtWidgets.QSpinBox(self.groupBox_2)
        self.swc_search.setProperty("value", 9)
        self.swc_search.setObjectName("swc_search")
        self.gridLayout_8.addWidget(self.swc_search, 0, 1, 1, 1)
        self.swc_area_lesser = QtWidgets.QLineEdit(self.groupBox_2)
        self.swc_area_lesser.setObjectName("swc_area_lesser")
        self.gridLayout_8.addWidget(self.swc_area_lesser, 5, 1, 1, 1)
        self.swc_flat = QtWidgets.QLineEdit(self.groupBox_2)
        self.swc_flat.setObjectName("swc_flat")
        self.gridLayout_8.addWidget(self.swc_flat, 2, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox_2)
        self.label_24.setObjectName("label_24")
        self.gridLayout_8.addWidget(self.label_24, 6, 0, 1, 1)
        self.generalize_threshold = QtWidgets.QLineEdit(self.groupBox_2)
        self.generalize_threshold.setObjectName("generalize_threshold")
        self.gridLayout_8.addWidget(self.generalize_threshold, 7, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.groupBox_2)
        self.label_25.setObjectName("label_25")
        self.gridLayout_8.addWidget(self.label_25, 0, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox_2)
        self.label_26.setObjectName("label_26")
        self.gridLayout_8.addWidget(self.label_26, 2, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.groupBox_2)
        self.label_27.setObjectName("label_27")
        self.gridLayout_8.addWidget(self.label_27, 8, 0, 1, 1)
        self.vclean_rmdangle_threshold = QtWidgets.QLineEdit(self.groupBox_2)
        self.vclean_rmdangle_threshold.setObjectName("vclean_rmdangle_threshold")
        self.gridLayout_8.addWidget(self.vclean_rmdangle_threshold, 8, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 220))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.sw_search = QtWidgets.QSpinBox(self.groupBox_3)
        self.sw_search.setProperty("value", 30)
        self.sw_search.setObjectName("sw_search")
        self.gridLayout_11.addWidget(self.sw_search, 0, 1, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.groupBox_3)
        self.label_33.setObjectName("label_33")
        self.gridLayout_11.addWidget(self.label_33, 3, 0, 1, 1)
        self.sw_flat = QtWidgets.QLineEdit(self.groupBox_3)
        self.sw_flat.setObjectName("sw_flat")
        self.gridLayout_11.addWidget(self.sw_flat, 2, 1, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.groupBox_3)
        self.label_34.setObjectName("label_34")
        self.gridLayout_11.addWidget(self.label_34, 2, 0, 1, 1)
        self.sw_skip = QtWidgets.QSpinBox(self.groupBox_3)
        self.sw_skip.setProperty("value", 7)
        self.sw_skip.setObjectName("sw_skip")
        self.gridLayout_11.addWidget(self.sw_skip, 1, 1, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.groupBox_3)
        self.label_35.setObjectName("label_35")
        self.gridLayout_11.addWidget(self.label_35, 0, 0, 1, 1)
        self.sw_area_lesser = QtWidgets.QLineEdit(self.groupBox_3)
        self.sw_area_lesser.setObjectName("sw_area_lesser")
        self.gridLayout_11.addWidget(self.sw_area_lesser, 4, 1, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.groupBox_3)
        self.label_36.setObjectName("label_36")
        self.gridLayout_11.addWidget(self.label_36, 4, 0, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.groupBox_3)
        self.label_37.setObjectName("label_37")
        self.gridLayout_11.addWidget(self.label_37, 1, 0, 1, 1)
        self.sw_dist = QtWidgets.QLineEdit(self.groupBox_3)
        self.sw_dist.setObjectName("sw_dist")
        self.gridLayout_11.addWidget(self.sw_dist, 3, 1, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.groupBox_3)
        self.label_38.setObjectName("label_38")
        self.gridLayout_11.addWidget(self.label_38, 5, 0, 1, 1)
        self.vclean_rmarea_threshold = QtWidgets.QLineEdit(self.groupBox_3)
        self.vclean_rmarea_threshold.setObjectName("vclean_rmarea_threshold")
        self.gridLayout_11.addWidget(self.vclean_rmarea_threshold, 5, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 180))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.point_dmax = QtWidgets.QLineEdit(self.groupBox_4)
        self.point_dmax.setObjectName("point_dmax")
        self.gridLayout_9.addWidget(self.point_dmax, 2, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.groupBox_4)
        self.label_28.setObjectName("label_28")
        self.gridLayout_9.addWidget(self.label_28, 0, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.groupBox_4)
        self.label_29.setObjectName("label_29")
        self.gridLayout_9.addWidget(self.label_29, 1, 0, 1, 1)
        self.transect_split_length = QtWidgets.QLineEdit(self.groupBox_4)
        self.transect_split_length.setObjectName("transect_split_length")
        self.gridLayout_9.addWidget(self.transect_split_length, 1, 1, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.groupBox_4)
        self.label_30.setObjectName("label_30")
        self.gridLayout_9.addWidget(self.label_30, 2, 0, 1, 1)
        self.buffer_distance = QtWidgets.QLineEdit(self.groupBox_4)
        self.buffer_distance.setObjectName("buffer_distance")
        self.gridLayout_9.addWidget(self.buffer_distance, 0, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.groupBox_4)
        self.label_31.setObjectName("label_31")
        self.gridLayout_9.addWidget(self.label_31, 3, 0, 1, 1)
        self.transect_side_distances = QtWidgets.QLineEdit(self.groupBox_4)
        self.transect_side_distances.setObjectName("transect_side_distances")
        self.gridLayout_9.addWidget(self.transect_side_distances, 3, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.run = QtWidgets.QPushButton(grm_lsi)
        self.run.setObjectName("run")
        self.horizontalLayout_2.addWidget(self.run)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.reload_layers = QtWidgets.QToolButton(grm_lsi)
        self.reload_layers.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/fa_solid/qtui/icons/fa_solid/arrows-rotate.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reload_layers.setIcon(icon1)
        self.reload_layers.setObjectName("reload_layers")
        self.horizontalLayout_2.addWidget(self.reload_layers)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.exit = QtWidgets.QPushButton(grm_lsi)
        self.exit.setObjectName("exit")
        self.horizontalLayout_2.addWidget(self.exit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.add_output = QtWidgets.QCheckBox(grm_lsi)
        self.add_output.setObjectName("add_output")
        self.verticalLayout.addWidget(self.add_output)

        self.retranslateUi(grm_lsi)
        QtCore.QMetaObject.connectSlotsByName(grm_lsi)

    def retranslateUi(self, grm_lsi):
        _translate = QtCore.QCoreApplication.translate
        grm_lsi.setWindowTitle(_translate("grm_lsi", "GRM - LSI"))
        self.label_2.setText(_translate("grm_lsi", "Compute metrics for LSI bedforms"))
        self.groupBox.setTitle(_translate("grm_lsi", "Input"))
        self.label_32.setText(_translate("grm_lsi", "Name of input elevation raster map:"))
        self.groupBox_2.setTitle(_translate("grm_lsi", "SWC"))
        self.label_8.setText(_translate("grm_lsi", "Inner search radius"))
        self.swc_dist.setText(_translate("grm_lsi", "0"))
        self.label_20.setText(_translate("grm_lsi", "Flatness distance, zero for none:"))
        self.iter_thin.setText(_translate("grm_lsi", "400"))
        self.label_21.setText(_translate("grm_lsi", "Thinning iterations"))
        self.label_22.setText(_translate("grm_lsi", "v.generalize threshold"))
        self.label_23.setText(_translate("grm_lsi", "Min area threshold"))
        self.generalize_method.setItemText(0, _translate("grm_lsi", "douglas"))
        self.generalize_method.setItemText(1, _translate("grm_lsi", "douglas_reduction"))
        self.generalize_method.setItemText(2, _translate("grm_lsi", "lang"))
        self.generalize_method.setItemText(3, _translate("grm_lsi", "reduction"))
        self.generalize_method.setItemText(4, _translate("grm_lsi", "reumann"))
        self.generalize_method.setItemText(5, _translate("grm_lsi", "boyle"))
        self.generalize_method.setItemText(6, _translate("grm_lsi", "sliding_averaging"))
        self.generalize_method.setItemText(7, _translate("grm_lsi", "chaiken"))
        self.generalize_method.setItemText(8, _translate("grm_lsi", "hermite"))
        self.generalize_method.setItemText(9, _translate("grm_lsi", "snakes"))
        self.generalize_method.setItemText(10, _translate("grm_lsi", "network"))
        self.generalize_method.setItemText(11, _translate("grm_lsi", "displacement"))
        self.swc_area_lesser.setText(_translate("grm_lsi", "70"))
        self.swc_flat.setText(_translate("grm_lsi", "2.0"))
        self.label_24.setText(_translate("grm_lsi", "v.generalize method"))
        self.generalize_threshold.setText(_translate("grm_lsi", "2"))
        self.label_25.setText(_translate("grm_lsi", "Outer search radius:"))
        self.label_26.setText(_translate("grm_lsi", "Flatness threshold (degrees):"))
        self.label_27.setText(_translate("grm_lsi", "v.clean rmdangle threshold"))
        self.vclean_rmdangle_threshold.setText(_translate("grm_lsi", "5,10,20,30"))
        self.groupBox_3.setTitle(_translate("grm_lsi", "SW"))
        self.label_33.setText(_translate("grm_lsi", "Flatness distance, zero for none:"))
        self.sw_flat.setText(_translate("grm_lsi", "3.8"))
        self.label_34.setText(_translate("grm_lsi", "Flatness threshold (degrees):"))
        self.label_35.setText(_translate("grm_lsi", "Outer search radius:"))
        self.sw_area_lesser.setText(_translate("grm_lsi", "1000"))
        self.label_36.setText(_translate("grm_lsi", "Min area threshold"))
        self.label_37.setText(_translate("grm_lsi", "Inner search radius"))
        self.sw_dist.setText(_translate("grm_lsi", "15"))
        self.label_38.setText(_translate("grm_lsi", "v.clean rmarea threshold"))
        self.vclean_rmarea_threshold.setText(_translate("grm_lsi", "10"))
        self.groupBox_4.setTitle(_translate("grm_lsi", "SW Metrics"))
        self.point_dmax.setText(_translate("grm_lsi", "1"))
        self.label_28.setText(_translate("grm_lsi", "Side-split buffer distance"))
        self.label_29.setText(_translate("grm_lsi", "Transect split length"))
        self.transect_split_length.setText(_translate("grm_lsi", "1"))
        self.label_30.setText(_translate("grm_lsi", "Point max distance"))
        self.buffer_distance.setText(_translate("grm_lsi", "1"))
        self.label_31.setText(_translate("grm_lsi", "Transects side distance"))
        self.transect_side_distances.setText(_translate("grm_lsi", "70,70"))
        self.run.setText(_translate("grm_lsi", "Run"))
        self.exit.setText(_translate("grm_lsi", "Close"))
        self.add_output.setText(_translate("grm_lsi", "Add Geomorphic forms into layer tree"))
import resources_rc
