# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PeliasTools/gui/PeliasMainUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PeliasMainDialog(object):
    def setupUi(self, PeliasMainDialog):
        PeliasMainDialog.setObjectName("PeliasMainDialog")
        PeliasMainDialog.resize(502, 824)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PeliasMainDialog.sizePolicy().hasHeightForWidth())
        PeliasMainDialog.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(PeliasMainDialog)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout.setObjectName("gridLayout")
        self.search_tab = QtWidgets.QTabWidget(PeliasMainDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_tab.sizePolicy().hasHeightForWidth())
        self.search_tab.setSizePolicy(sizePolicy)
        self.search_tab.setObjectName("search_tab")
        self.free_tab = QtWidgets.QWidget()
        self.free_tab.setObjectName("free_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.free_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.search_free_text = QgsFilterLineEdit(self.free_tab)
        self.search_free_text.setProperty("qgisRelation", "")
        self.search_free_text.setObjectName("search_free_text")
        self.verticalLayout.addWidget(self.search_free_text)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.search_tab.addTab(self.free_tab, "")
        self.struc_tab = QtWidgets.QWidget()
        self.struc_tab.setObjectName("struc_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.struc_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(self.struc_tab)
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.search_struc_layers_group = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_struc_layers_group.sizePolicy().hasHeightForWidth())
        self.search_struc_layers_group.setSizePolicy(sizePolicy)
        self.search_struc_layers_group.setMinimumSize(QtCore.QSize(180, 0))
        self.search_struc_layers_group.setObjectName("search_struc_layers_group")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.search_struc_layers_group)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.search_struc_layers_text = QgsFilterLineEdit(self.search_struc_layers_group)
        self.search_struc_layers_text.setProperty("qgisRelation", "")
        self.search_struc_layers_text.setObjectName("search_struc_layers_text")
        self.verticalLayout_2.addWidget(self.search_struc_layers_text)
        self.label = QtWidgets.QLabel(self.search_struc_layers_group)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.search_struc_layers_combo = QtWidgets.QComboBox(self.search_struc_layers_group)
        self.search_struc_layers_combo.setObjectName("search_struc_layers_combo")
        self.search_struc_layers_combo.addItem("")
        self.search_struc_layers_combo.addItem("")
        self.search_struc_layers_combo.addItem("")
        self.search_struc_layers_combo.addItem("")
        self.search_struc_layers_combo.addItem("")
        self.search_struc_layers_combo.addItem("")
        self.search_struc_layers_combo.addItem("")
        self.search_struc_layers_combo.addItem("")
        self.verticalLayout_2.addWidget(self.search_struc_layers_combo)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout_4.addWidget(self.search_struc_layers_group, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.search_struc_add = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_struc_add.sizePolicy().hasHeightForWidth())
        self.search_struc_add.setSizePolicy(sizePolicy)
        self.search_struc_add.setMinimumSize(QtCore.QSize(30, 0))
        self.search_struc_add.setObjectName("search_struc_add")
        self.verticalLayout_3.addWidget(self.search_struc_add)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.gridLayout_4.addWidget(self.widget_2, 0, 1, 1, 1)
        self.search_struc_list = QtWidgets.QListWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_struc_list.sizePolicy().hasHeightForWidth())
        self.search_struc_list.setSizePolicy(sizePolicy)
        self.search_struc_list.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.search_struc_list.setObjectName("search_struc_list")
        self.gridLayout_4.addWidget(self.search_struc_list, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        self.search_tab.addTab(self.struc_tab, "")
        self.gridLayout.addWidget(self.search_tab, 0, 0, 1, 2)
        self.search_filters_group = QgsCollapsibleGroupBox(PeliasMainDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_filters_group.sizePolicy().hasHeightForWidth())
        self.search_filters_group.setSizePolicy(sizePolicy)
        self.search_filters_group.setCollapsed(False)
        self.search_filters_group.setObjectName("search_filters_group")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.search_filters_group)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_8 = QtWidgets.QLabel(self.search_filters_group)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.search_filters_sources_combo = QgsCheckableComboBox(self.search_filters_group)
        self.search_filters_sources_combo.setCurrentText("")
        self.search_filters_sources_combo.setObjectName("search_filters_sources_combo")
        self.search_filters_sources_combo.addItem("")
        self.search_filters_sources_combo.addItem("")
        self.search_filters_sources_combo.addItem("")
        self.search_filters_sources_combo.addItem("")
        self.gridLayout_3.addWidget(self.search_filters_sources_combo, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.search_filters_group)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)
        self.search_filters_layer_combo = QgsCheckableComboBox(self.search_filters_group)
        self.search_filters_layer_combo.setCurrentText("")
        self.search_filters_layer_combo.setObjectName("search_filters_layer_combo")
        self.search_filters_layer_combo.addItem("")
        self.search_filters_layer_combo.addItem("")
        self.search_filters_layer_combo.addItem("")
        self.search_filters_layer_combo.addItem("")
        self.search_filters_layer_combo.addItem("")
        self.search_filters_layer_combo.addItem("")
        self.search_filters_layer_combo.addItem("")
        self.search_filters_layer_combo.addItem("")
        self.search_filters_layer_combo.addItem("")
        self.search_filters_layer_combo.addItem("")
        self.search_filters_layer_combo.addItem("")
        self.search_filters_layer_combo.addItem("")
        self.search_filters_layer_combo.addItem("")
        self.gridLayout_3.addWidget(self.search_filters_layer_combo, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.search_filters_group, 3, 0, 1, 2)
        self.search_rest_group = QgsCollapsibleGroupBox(PeliasMainDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_rest_group.sizePolicy().hasHeightForWidth())
        self.search_rest_group.setSizePolicy(sizePolicy)
        self.search_rest_group.setCollapsed(False)
        self.search_rest_group.setObjectName("search_rest_group")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.search_rest_group)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_3 = QtWidgets.QLabel(self.search_rest_group)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 2, 0, 1, 1)
        self.search_rest_country = QgsFilterLineEdit(self.search_rest_group)
        self.search_rest_country.setProperty("qgisRelation", "")
        self.search_rest_country.setObjectName("search_rest_country")
        self.gridLayout_5.addWidget(self.search_rest_country, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 2, 2, 1, 1)
        self.search_rest_circle_group = QtWidgets.QGroupBox(self.search_rest_group)
        self.search_rest_circle_group.setObjectName("search_rest_circle_group")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.search_rest_circle_group)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_12 = QtWidgets.QLabel(self.search_rest_circle_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.gridLayout_7.addWidget(self.label_12, 0, 3, 1, 1)
        self.search_rest_circle_label = QtWidgets.QLabel(self.search_rest_circle_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_rest_circle_label.sizePolicy().hasHeightForWidth())
        self.search_rest_circle_label.setSizePolicy(sizePolicy)
        self.search_rest_circle_label.setObjectName("search_rest_circle_label")
        self.gridLayout_7.addWidget(self.search_rest_circle_label, 0, 1, 1, 1)
        self.search_rest_circle_x = QgsFilterLineEdit(self.search_rest_circle_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_rest_circle_x.sizePolicy().hasHeightForWidth())
        self.search_rest_circle_x.setSizePolicy(sizePolicy)
        self.search_rest_circle_x.setMaximumSize(QtCore.QSize(120, 25))
        self.search_rest_circle_x.setProperty("qgisRelation", "")
        self.search_rest_circle_x.setObjectName("search_rest_circle_x")
        self.gridLayout_7.addWidget(self.search_rest_circle_x, 0, 2, 1, 1)
        self.search_rest_circle_y = QgsFilterLineEdit(self.search_rest_circle_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_rest_circle_y.sizePolicy().hasHeightForWidth())
        self.search_rest_circle_y.setSizePolicy(sizePolicy)
        self.search_rest_circle_y.setMaximumSize(QtCore.QSize(120, 25))
        self.search_rest_circle_y.setProperty("qgisRelation", "")
        self.search_rest_circle_y.setObjectName("search_rest_circle_y")
        self.gridLayout_7.addWidget(self.search_rest_circle_y, 0, 4, 1, 1)
        self.search_rest_circle_button = QtWidgets.QPushButton(self.search_rest_circle_group)
        self.search_rest_circle_button.setObjectName("search_rest_circle_button")
        self.gridLayout_7.addWidget(self.search_rest_circle_button, 0, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.search_rest_circle_group)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.search_rest_circle_value = QtWidgets.QSpinBox(self.widget_3)
        self.search_rest_circle_value.setMaximum(100)
        self.search_rest_circle_value.setObjectName("search_rest_circle_value")
        self.horizontalLayout_2.addWidget(self.search_rest_circle_value)
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.gridLayout_7.addWidget(self.widget_3, 1, 0, 1, 5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem6, 0, 5, 1, 1)
        self.gridLayout_5.addWidget(self.search_rest_circle_group, 1, 0, 1, 3)
        self.search_rest_rect_group = QtWidgets.QGroupBox(self.search_rest_group)
        self.search_rest_rect_group.setObjectName("search_rest_rect_group")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.search_rest_rect_group)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_10 = QtWidgets.QLabel(self.search_rest_rect_group)
        self.label_10.setObjectName("label_10")
        self.gridLayout_6.addWidget(self.label_10, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.search_rest_rect_group)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 0, 3, 1, 1)
        self.search_rest_rect_xmin = QgsFilterLineEdit(self.search_rest_rect_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_rest_rect_xmin.sizePolicy().hasHeightForWidth())
        self.search_rest_rect_xmin.setSizePolicy(sizePolicy)
        self.search_rest_rect_xmin.setMaximumSize(QtCore.QSize(120, 25))
        self.search_rest_rect_xmin.setProperty("qgisRelation", "")
        self.search_rest_rect_xmin.setObjectName("search_rest_rect_xmin")
        self.gridLayout_6.addWidget(self.search_rest_rect_xmin, 0, 2, 1, 1)
        self.search_rest_rect_label = QtWidgets.QLabel(self.search_rest_rect_group)
        self.search_rest_rect_label.setObjectName("search_rest_rect_label")
        self.gridLayout_6.addWidget(self.search_rest_rect_label, 0, 1, 1, 1)
        self.search_rest_rect_ymin = QgsFilterLineEdit(self.search_rest_rect_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_rest_rect_ymin.sizePolicy().hasHeightForWidth())
        self.search_rest_rect_ymin.setSizePolicy(sizePolicy)
        self.search_rest_rect_ymin.setMaximumSize(QtCore.QSize(120, 25))
        self.search_rest_rect_ymin.setProperty("qgisRelation", "")
        self.search_rest_rect_ymin.setObjectName("search_rest_rect_ymin")
        self.gridLayout_6.addWidget(self.search_rest_rect_ymin, 0, 4, 1, 1)
        self.search_rest_rect_xmax = QgsFilterLineEdit(self.search_rest_rect_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_rest_rect_xmax.sizePolicy().hasHeightForWidth())
        self.search_rest_rect_xmax.setSizePolicy(sizePolicy)
        self.search_rest_rect_xmax.setMaximumSize(QtCore.QSize(120, 25))
        self.search_rest_rect_xmax.setProperty("qgisRelation", "")
        self.search_rest_rect_xmax.setObjectName("search_rest_rect_xmax")
        self.gridLayout_6.addWidget(self.search_rest_rect_xmax, 1, 2, 1, 1)
        self.search_rest_rect_ymax = QgsFilterLineEdit(self.search_rest_rect_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_rest_rect_ymax.sizePolicy().hasHeightForWidth())
        self.search_rest_rect_ymax.setSizePolicy(sizePolicy)
        self.search_rest_rect_ymax.setMaximumSize(QtCore.QSize(120, 25))
        self.search_rest_rect_ymax.setProperty("qgisRelation", "")
        self.search_rest_rect_ymax.setObjectName("search_rest_rect_ymax")
        self.gridLayout_6.addWidget(self.search_rest_rect_ymax, 1, 4, 1, 1)
        self.search_rest_rect_button = QtWidgets.QPushButton(self.search_rest_rect_group)
        self.search_rest_rect_button.setObjectName("search_rest_rect_button")
        self.gridLayout_6.addWidget(self.search_rest_rect_button, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.search_rest_rect_group)
        self.label_11.setObjectName("label_11")
        self.gridLayout_6.addWidget(self.label_11, 1, 3, 1, 1)
        self.gridLayout_5.addWidget(self.search_rest_rect_group, 0, 0, 1, 3)
        self.gridLayout.addWidget(self.search_rest_group, 2, 0, 1, 2)
        self.help_button = QtWidgets.QPushButton(PeliasMainDialog)
        self.help_button.setText("")
        self.help_button.setObjectName("help_button")
        self.gridLayout.addWidget(self.help_button, 5, 0, 1, 1)
        self.search_focus_group = QgsCollapsibleGroupBox(PeliasMainDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_focus_group.sizePolicy().hasHeightForWidth())
        self.search_focus_group.setSizePolicy(sizePolicy)
        self.search_focus_group.setCollapsed(False)
        self.search_focus_group.setObjectName("search_focus_group")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.search_focus_group)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_focus_button = QtWidgets.QPushButton(self.search_focus_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_focus_button.sizePolicy().hasHeightForWidth())
        self.search_focus_button.setSizePolicy(sizePolicy)
        self.search_focus_button.setObjectName("search_focus_button")
        self.horizontalLayout.addWidget(self.search_focus_button)
        self.label_2 = QtWidgets.QLabel(self.search_focus_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.search_focus_x = QgsFilterLineEdit(self.search_focus_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_focus_x.sizePolicy().hasHeightForWidth())
        self.search_focus_x.setSizePolicy(sizePolicy)
        self.search_focus_x.setMaximumSize(QtCore.QSize(120, 25))
        self.search_focus_x.setProperty("qgisRelation", "")
        self.search_focus_x.setObjectName("search_focus_x")
        self.horizontalLayout.addWidget(self.search_focus_x)
        self.label_4 = QtWidgets.QLabel(self.search_focus_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.search_focus_y = QgsFilterLineEdit(self.search_focus_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_focus_y.sizePolicy().hasHeightForWidth())
        self.search_focus_y.setSizePolicy(sizePolicy)
        self.search_focus_y.setMaximumSize(QtCore.QSize(120, 25))
        self.search_focus_y.setProperty("qgisRelation", "")
        self.search_focus_y.setObjectName("search_focus_y")
        self.horizontalLayout.addWidget(self.search_focus_y)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.gridLayout.addWidget(self.search_focus_group, 1, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(PeliasMainDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 1, 1, 1)

        self.retranslateUi(PeliasMainDialog)
        self.search_tab.setCurrentIndex(0)
        self.buttonBox.accepted.connect(PeliasMainDialog.accept)
        self.buttonBox.rejected.connect(PeliasMainDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PeliasMainDialog)

    def retranslateUi(self, PeliasMainDialog):
        _translate = QtCore.QCoreApplication.translate
        PeliasMainDialog.setWindowTitle(_translate("PeliasMainDialog", "Dialog"))
        self.search_tab.setTabText(self.search_tab.indexOf(self.free_tab), _translate("PeliasMainDialog", "Free Text"))
        self.search_struc_layers_group.setTitle(_translate("PeliasMainDialog", "Add layers"))
        self.label.setText(_translate("PeliasMainDialog", "Add to layer"))
        self.search_struc_layers_combo.setItemText(0, _translate("PeliasMainDialog", "address"))
        self.search_struc_layers_combo.setItemText(1, _translate("PeliasMainDialog", "neighbourhood"))
        self.search_struc_layers_combo.setItemText(2, _translate("PeliasMainDialog", "borough"))
        self.search_struc_layers_combo.setItemText(3, _translate("PeliasMainDialog", "locality"))
        self.search_struc_layers_combo.setItemText(4, _translate("PeliasMainDialog", "county"))
        self.search_struc_layers_combo.setItemText(5, _translate("PeliasMainDialog", "region"))
        self.search_struc_layers_combo.setItemText(6, _translate("PeliasMainDialog", "postalcode"))
        self.search_struc_layers_combo.setItemText(7, _translate("PeliasMainDialog", "country"))
        self.search_struc_add.setText(_translate("PeliasMainDialog", ">"))
        self.pushButton.setText(_translate("PeliasMainDialog", "<"))
        self.search_tab.setTabText(self.search_tab.indexOf(self.struc_tab), _translate("PeliasMainDialog", "Structured"))
        self.search_filters_group.setTitle(_translate("PeliasMainDialog", "Filters"))
        self.label_8.setText(_translate("PeliasMainDialog", "Sources"))
        self.search_filters_sources_combo.setItemText(0, _translate("PeliasMainDialog", "osm"))
        self.search_filters_sources_combo.setItemText(1, _translate("PeliasMainDialog", "oa"))
        self.search_filters_sources_combo.setItemText(2, _translate("PeliasMainDialog", "wof"))
        self.search_filters_sources_combo.setItemText(3, _translate("PeliasMainDialog", "gn"))
        self.label_9.setText(_translate("PeliasMainDialog", "Layers"))
        self.search_filters_layer_combo.setItemText(0, _translate("PeliasMainDialog", "venue"))
        self.search_filters_layer_combo.setItemText(1, _translate("PeliasMainDialog", "address"))
        self.search_filters_layer_combo.setItemText(2, _translate("PeliasMainDialog", "street"))
        self.search_filters_layer_combo.setItemText(3, _translate("PeliasMainDialog", "neighbourhood"))
        self.search_filters_layer_combo.setItemText(4, _translate("PeliasMainDialog", "borough"))
        self.search_filters_layer_combo.setItemText(5, _translate("PeliasMainDialog", "localadmin"))
        self.search_filters_layer_combo.setItemText(6, _translate("PeliasMainDialog", "locality"))
        self.search_filters_layer_combo.setItemText(7, _translate("PeliasMainDialog", "county"))
        self.search_filters_layer_combo.setItemText(8, _translate("PeliasMainDialog", "macrocounty"))
        self.search_filters_layer_combo.setItemText(9, _translate("PeliasMainDialog", "region"))
        self.search_filters_layer_combo.setItemText(10, _translate("PeliasMainDialog", "macroregion"))
        self.search_filters_layer_combo.setItemText(11, _translate("PeliasMainDialog", "country"))
        self.search_filters_layer_combo.setItemText(12, _translate("PeliasMainDialog", "coarse"))
        self.search_rest_group.setTitle(_translate("PeliasMainDialog", "Restrictions"))
        self.label_3.setText(_translate("PeliasMainDialog", "Country"))
        self.search_rest_circle_group.setTitle(_translate("PeliasMainDialog", "Circle"))
        self.label_12.setText(_translate("PeliasMainDialog", "Y"))
        self.search_rest_circle_label.setText(_translate("PeliasMainDialog", "X"))
        self.search_rest_circle_button.setText(_translate("PeliasMainDialog", "Map!"))
        self.label_6.setText(_translate("PeliasMainDialog", "Radius"))
        self.label_7.setText(_translate("PeliasMainDialog", "km"))
        self.search_rest_rect_group.setTitle(_translate("PeliasMainDialog", "Rectangle"))
        self.label_10.setText(_translate("PeliasMainDialog", "Xmax"))
        self.label_5.setText(_translate("PeliasMainDialog", "Ymin"))
        self.search_rest_rect_label.setText(_translate("PeliasMainDialog", "Xmin"))
        self.search_rest_rect_button.setText(_translate("PeliasMainDialog", "Map!"))
        self.label_11.setText(_translate("PeliasMainDialog", "Ymax"))
        self.search_focus_group.setTitle(_translate("PeliasMainDialog", "Focus Point"))
        self.search_focus_button.setText(_translate("PeliasMainDialog", "Map!"))
        self.label_2.setText(_translate("PeliasMainDialog", "X"))
        self.label_4.setText(_translate("PeliasMainDialog", "Y"))

from qgscheckablecombobox import QgsCheckableComboBox
from qgscollapsiblegroupbox import QgsCollapsibleGroupBox
from qgsfilterlineedit import QgsFilterLineEdit