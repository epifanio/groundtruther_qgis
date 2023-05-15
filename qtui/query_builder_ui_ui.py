/********************************************************************************
** Form generated from reading UI file 'query_builder_ui.ui'
**
** Created by: Qt User Interface Compiler version 5.15.8
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef QUERY_BUILDER_UI_UI_H
#define QUERY_BUILDER_UI_UI_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTableView>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Form
{
public:
    QVBoxLayout *verticalLayout_3;
    QSplitter *splitter;
    QWidget *verticalLayoutWidget;
    QVBoxLayout *verticalLayout_2;
    QScrollArea *query_builder_tools;
    QWidget *scrollAreaWidgetContents_2;
    QGridLayout *gridLayout_5;
    QGroupBox *groupBox_4;
    QVBoxLayout *verticalLayout;
    QGridLayout *gridLayout_6;
    QLineEdit *qb_longitude;
    QLabel *qb_latlabel;
    QLineEdit *qb_imageindex;
    QLabel *qb_lonlabel;
    QSpinBox *qb_imagebuffer;
    QLabel *image_index_label;
    QSpacerItem *horizontalSpacer_6;
    QLabel *image_buffer_label;
    QLineEdit *qb_latitude;
    QCheckBox *lock_location;
    QGroupBox *groupBox_3;
    QVBoxLayout *verticalLayout_5;
    QGridLayout *gridLayout_4;
    QLabel *qb_minoraxis_lablel;
    QSpacerItem *horizontalSpacer_5;
    QLineEdit *qb_ellipsemajoraxis;
    QComboBox *qb_shapeselection;
    QSpinBox *qb_ellipseorientation;
    QLabel *qb_ellipseorientation_label;
    QLabel *qb_rectangle_l1_label;
    QLabel *qb_majoraxis_label;
    QLineEdit *qb_ellipseminoraxis;
    QLabel *Iconlabel;
    QLabel *qb_rectangle_l2_label;
    QLineEdit *qb_rectangle_l1;
    QLineEdit *qb_rectangle_l2;
    QGroupBox *groupBox;
    QVBoxLayout *verticalLayout_4;
    QGridLayout *gridLayout_2;
    QLabel *label;
    QLabel *label_8;
    QLabel *label_5;
    QLabel *label_4;
    QLabel *label_3;
    QLineEdit *yutm;
    QLineEdit *utmzone;
    QHBoxLayout *horizontalLayout_3;
    QComboBox *qb_pointdatasource;
    QToolButton *reload_settings;
    QSpacerItem *horizontalSpacer_4;
    QLabel *label_9;
    QLineEdit *logitude;
    QLineEdit *xutm;
    QLineEdit *latitude;
    QLabel *label_6;
    QHBoxLayout *horizontalLayout_4;
    QComboBox *set_backscatter_field;
    QSpacerItem *horizontalSpacer_7;
    QSpacerItem *verticalSpacer;
    QGroupBox *groupBox_2;
    QVBoxLayout *verticalLayout_14;
    QTabWidget *tabWidget;
    QWidget *tab;
    QVBoxLayout *verticalLayout_6;
    QTableView *tableView;
    QWidget *tab_2;
    QVBoxLayout *verticalLayout_7;
    QVBoxLayout *verticalLayout_11;
    QGroupBox *groupBox_6;
    QGridLayout *gridLayout_7;
    QGridLayout *gridLayout_3;
    QLabel *label_2;
    QSpinBox *fitting_degree;
    QGridLayout *gridLayout;
    QRadioButton *right_beam;
    QRadioButton *fold_beam;
    QRadioButton *left_beam;
    QRadioButton *raw_beam;
    QSpacerItem *horizontalSpacer_10;
    QHBoxLayout *horizontalLayout;
    QSpacerItem *horizontalSpacer_2;
    QPushButton *draw_graph;
    QSpacerItem *horizontalSpacer;
    QPushButton *clean_graph;
    QSpacerItem *horizontalSpacer_8;
    QPushButton *add_graph;
    QSpacerItem *horizontalSpacer_9;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName(QString::fromUtf8("Form"));
        Form->resize(426, 661);
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(Form->sizePolicy().hasHeightForWidth());
        Form->setSizePolicy(sizePolicy);
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/icons/element-vector.gif"), QSize(), QIcon::Normal, QIcon::Off);
        Form->setWindowIcon(icon);
        Form->setLayoutDirection(Qt::LeftToRight);
        verticalLayout_3 = new QVBoxLayout(Form);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        splitter = new QSplitter(Form);
        splitter->setObjectName(QString::fromUtf8("splitter"));
        splitter->setOrientation(Qt::Vertical);
        verticalLayoutWidget = new QWidget(splitter);
        verticalLayoutWidget->setObjectName(QString::fromUtf8("verticalLayoutWidget"));
        verticalLayout_2 = new QVBoxLayout(verticalLayoutWidget);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        verticalLayout_2->setContentsMargins(0, 0, 0, 10);
        query_builder_tools = new QScrollArea(verticalLayoutWidget);
        query_builder_tools->setObjectName(QString::fromUtf8("query_builder_tools"));
        QSizePolicy sizePolicy1(QSizePolicy::Expanding, QSizePolicy::MinimumExpanding);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(query_builder_tools->sizePolicy().hasHeightForWidth());
        query_builder_tools->setSizePolicy(sizePolicy1);
        query_builder_tools->setWidgetResizable(true);
        scrollAreaWidgetContents_2 = new QWidget();
        scrollAreaWidgetContents_2->setObjectName(QString::fromUtf8("scrollAreaWidgetContents_2"));
        scrollAreaWidgetContents_2->setGeometry(QRect(0, -129, 390, 718));
        gridLayout_5 = new QGridLayout(scrollAreaWidgetContents_2);
        gridLayout_5->setObjectName(QString::fromUtf8("gridLayout_5"));
        groupBox_4 = new QGroupBox(scrollAreaWidgetContents_2);
        groupBox_4->setObjectName(QString::fromUtf8("groupBox_4"));
        verticalLayout = new QVBoxLayout(groupBox_4);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        gridLayout_6 = new QGridLayout();
        gridLayout_6->setObjectName(QString::fromUtf8("gridLayout_6"));
        qb_longitude = new QLineEdit(groupBox_4);
        qb_longitude->setObjectName(QString::fromUtf8("qb_longitude"));
        qb_longitude->setMinimumSize(QSize(160, 0));
        qb_longitude->setMaximumSize(QSize(180, 16777215));
        qb_longitude->setStyleSheet(QString::fromUtf8(""));
        qb_longitude->setAlignment(Qt::AlignCenter);

        gridLayout_6->addWidget(qb_longitude, 2, 1, 1, 1);

        qb_latlabel = new QLabel(groupBox_4);
        qb_latlabel->setObjectName(QString::fromUtf8("qb_latlabel"));
        qb_latlabel->setMinimumSize(QSize(100, 0));
        qb_latlabel->setMaximumSize(QSize(130, 16777215));

        gridLayout_6->addWidget(qb_latlabel, 3, 0, 1, 1);

        qb_imageindex = new QLineEdit(groupBox_4);
        qb_imageindex->setObjectName(QString::fromUtf8("qb_imageindex"));
        qb_imageindex->setMaximumSize(QSize(180, 16777215));
        qb_imageindex->setStyleSheet(QString::fromUtf8(""));
        qb_imageindex->setAlignment(Qt::AlignCenter);

        gridLayout_6->addWidget(qb_imageindex, 0, 1, 1, 1);

        qb_lonlabel = new QLabel(groupBox_4);
        qb_lonlabel->setObjectName(QString::fromUtf8("qb_lonlabel"));
        qb_lonlabel->setMinimumSize(QSize(100, 0));
        qb_lonlabel->setMaximumSize(QSize(130, 16777215));

        gridLayout_6->addWidget(qb_lonlabel, 2, 0, 1, 1);

        qb_imagebuffer = new QSpinBox(groupBox_4);
        qb_imagebuffer->setObjectName(QString::fromUtf8("qb_imagebuffer"));
        qb_imagebuffer->setMinimumSize(QSize(80, 0));
        qb_imagebuffer->setMaximumSize(QSize(120, 16777215));

        gridLayout_6->addWidget(qb_imagebuffer, 1, 1, 1, 1);

        image_index_label = new QLabel(groupBox_4);
        image_index_label->setObjectName(QString::fromUtf8("image_index_label"));
        image_index_label->setMinimumSize(QSize(100, 0));
        image_index_label->setMaximumSize(QSize(130, 16777215));

        gridLayout_6->addWidget(image_index_label, 0, 0, 1, 1);

        horizontalSpacer_6 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_6->addItem(horizontalSpacer_6, 0, 2, 1, 1);

        image_buffer_label = new QLabel(groupBox_4);
        image_buffer_label->setObjectName(QString::fromUtf8("image_buffer_label"));
        image_buffer_label->setMinimumSize(QSize(100, 0));
        image_buffer_label->setMaximumSize(QSize(130, 16777215));

        gridLayout_6->addWidget(image_buffer_label, 1, 0, 1, 1);

        qb_latitude = new QLineEdit(groupBox_4);
        qb_latitude->setObjectName(QString::fromUtf8("qb_latitude"));
        qb_latitude->setMinimumSize(QSize(160, 0));
        qb_latitude->setMaximumSize(QSize(180, 16777215));
        qb_latitude->setStyleSheet(QString::fromUtf8(""));
        qb_latitude->setAlignment(Qt::AlignCenter);

        gridLayout_6->addWidget(qb_latitude, 3, 1, 1, 1);

        lock_location = new QCheckBox(groupBox_4);
        lock_location->setObjectName(QString::fromUtf8("lock_location"));
        lock_location->setMinimumSize(QSize(0, 0));
        lock_location->setMaximumSize(QSize(130, 16777215));
        lock_location->setLayoutDirection(Qt::RightToLeft);

        gridLayout_6->addWidget(lock_location, 4, 0, 1, 1);


        verticalLayout->addLayout(gridLayout_6);


        gridLayout_5->addWidget(groupBox_4, 0, 0, 1, 1);

        groupBox_3 = new QGroupBox(scrollAreaWidgetContents_2);
        groupBox_3->setObjectName(QString::fromUtf8("groupBox_3"));
        verticalLayout_5 = new QVBoxLayout(groupBox_3);
        verticalLayout_5->setObjectName(QString::fromUtf8("verticalLayout_5"));
        gridLayout_4 = new QGridLayout();
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        qb_minoraxis_lablel = new QLabel(groupBox_3);
        qb_minoraxis_lablel->setObjectName(QString::fromUtf8("qb_minoraxis_lablel"));
        qb_minoraxis_lablel->setMinimumSize(QSize(100, 0));
        qb_minoraxis_lablel->setMaximumSize(QSize(130, 16777215));

        gridLayout_4->addWidget(qb_minoraxis_lablel, 2, 0, 1, 1);

        horizontalSpacer_5 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_4->addItem(horizontalSpacer_5, 0, 2, 1, 1);

        qb_ellipsemajoraxis = new QLineEdit(groupBox_3);
        qb_ellipsemajoraxis->setObjectName(QString::fromUtf8("qb_ellipsemajoraxis"));
        qb_ellipsemajoraxis->setMaximumSize(QSize(180, 16777215));
        qb_ellipsemajoraxis->setStyleSheet(QString::fromUtf8(""));

        gridLayout_4->addWidget(qb_ellipsemajoraxis, 1, 1, 1, 1);

        qb_shapeselection = new QComboBox(groupBox_3);
        qb_shapeselection->addItem(QString());
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/custom/qtui/icons/custom/ellipse.png"), QSize(), QIcon::Normal, QIcon::Off);
        qb_shapeselection->addItem(icon1, QString());
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/custom/qtui/icons/custom/rectangle.png"), QSize(), QIcon::Normal, QIcon::Off);
        qb_shapeselection->addItem(icon2, QString());
        qb_shapeselection->setObjectName(QString::fromUtf8("qb_shapeselection"));
        qb_shapeselection->setMaximumSize(QSize(180, 16777215));

        gridLayout_4->addWidget(qb_shapeselection, 0, 1, 1, 1);

        qb_ellipseorientation = new QSpinBox(groupBox_3);
        qb_ellipseorientation->setObjectName(QString::fromUtf8("qb_ellipseorientation"));
        qb_ellipseorientation->setStyleSheet(QString::fromUtf8(""));
        qb_ellipseorientation->setInputMethodHints(Qt::ImhNone);
        qb_ellipseorientation->setMaximum(360);

        gridLayout_4->addWidget(qb_ellipseorientation, 3, 1, 1, 1);

        qb_ellipseorientation_label = new QLabel(groupBox_3);
        qb_ellipseorientation_label->setObjectName(QString::fromUtf8("qb_ellipseorientation_label"));
        qb_ellipseorientation_label->setMinimumSize(QSize(100, 0));
        qb_ellipseorientation_label->setMaximumSize(QSize(130, 16777215));

        gridLayout_4->addWidget(qb_ellipseorientation_label, 3, 0, 1, 1);

        qb_rectangle_l1_label = new QLabel(groupBox_3);
        qb_rectangle_l1_label->setObjectName(QString::fromUtf8("qb_rectangle_l1_label"));

        gridLayout_4->addWidget(qb_rectangle_l1_label, 4, 0, 1, 1);

        qb_majoraxis_label = new QLabel(groupBox_3);
        qb_majoraxis_label->setObjectName(QString::fromUtf8("qb_majoraxis_label"));
        qb_majoraxis_label->setMinimumSize(QSize(100, 0));
        qb_majoraxis_label->setMaximumSize(QSize(130, 16777215));

        gridLayout_4->addWidget(qb_majoraxis_label, 1, 0, 1, 1);

        qb_ellipseminoraxis = new QLineEdit(groupBox_3);
        qb_ellipseminoraxis->setObjectName(QString::fromUtf8("qb_ellipseminoraxis"));
        qb_ellipseminoraxis->setMaximumSize(QSize(180, 16777215));
        qb_ellipseminoraxis->setStyleSheet(QString::fromUtf8(""));

        gridLayout_4->addWidget(qb_ellipseminoraxis, 2, 1, 1, 1);

        Iconlabel = new QLabel(groupBox_3);
        Iconlabel->setObjectName(QString::fromUtf8("Iconlabel"));
        Iconlabel->setMinimumSize(QSize(100, 0));
        Iconlabel->setMaximumSize(QSize(130, 16777215));

        gridLayout_4->addWidget(Iconlabel, 0, 0, 1, 1);

        qb_rectangle_l2_label = new QLabel(groupBox_3);
        qb_rectangle_l2_label->setObjectName(QString::fromUtf8("qb_rectangle_l2_label"));

        gridLayout_4->addWidget(qb_rectangle_l2_label, 5, 0, 1, 1);

        qb_rectangle_l1 = new QLineEdit(groupBox_3);
        qb_rectangle_l1->setObjectName(QString::fromUtf8("qb_rectangle_l1"));

        gridLayout_4->addWidget(qb_rectangle_l1, 4, 1, 1, 1);

        qb_rectangle_l2 = new QLineEdit(groupBox_3);
        qb_rectangle_l2->setObjectName(QString::fromUtf8("qb_rectangle_l2"));

        gridLayout_4->addWidget(qb_rectangle_l2, 5, 1, 1, 1);


        verticalLayout_5->addLayout(gridLayout_4);


        gridLayout_5->addWidget(groupBox_3, 4, 0, 1, 1);

        groupBox = new QGroupBox(scrollAreaWidgetContents_2);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        verticalLayout_4 = new QVBoxLayout(groupBox);
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        gridLayout_2 = new QGridLayout();
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        label = new QLabel(groupBox);
        label->setObjectName(QString::fromUtf8("label"));
        label->setMinimumSize(QSize(100, 0));
        label->setMaximumSize(QSize(130, 16777215));

        gridLayout_2->addWidget(label, 0, 0, 1, 1);

        label_8 = new QLabel(groupBox);
        label_8->setObjectName(QString::fromUtf8("label_8"));
        label_8->setMinimumSize(QSize(100, 0));
        label_8->setMaximumSize(QSize(130, 16777215));

        gridLayout_2->addWidget(label_8, 4, 0, 1, 1);

        label_5 = new QLabel(groupBox);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setMinimumSize(QSize(100, 0));
        label_5->setMaximumSize(QSize(130, 16777215));

        gridLayout_2->addWidget(label_5, 3, 0, 1, 1);

        label_4 = new QLabel(groupBox);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setMinimumSize(QSize(100, 0));
        label_4->setMaximumSize(QSize(130, 16777215));

        gridLayout_2->addWidget(label_4, 2, 0, 1, 1);

        label_3 = new QLabel(groupBox);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setMinimumSize(QSize(100, 0));
        label_3->setMaximumSize(QSize(130, 16777215));

        gridLayout_2->addWidget(label_3, 1, 0, 1, 1);

        yutm = new QLineEdit(groupBox);
        yutm->setObjectName(QString::fromUtf8("yutm"));
        yutm->setMaximumSize(QSize(190, 16777215));

        gridLayout_2->addWidget(yutm, 4, 1, 1, 1);

        utmzone = new QLineEdit(groupBox);
        utmzone->setObjectName(QString::fromUtf8("utmzone"));
        utmzone->setMaximumSize(QSize(40, 16777215));
        utmzone->setInputMethodHints(Qt::ImhDigitsOnly|Qt::ImhFormattedNumbersOnly|Qt::ImhPreferNumbers);

        gridLayout_2->addWidget(utmzone, 5, 1, 1, 1);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        qb_pointdatasource = new QComboBox(groupBox);
        qb_pointdatasource->setObjectName(QString::fromUtf8("qb_pointdatasource"));
        QSizePolicy sizePolicy2(QSizePolicy::Expanding, QSizePolicy::Fixed);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(qb_pointdatasource->sizePolicy().hasHeightForWidth());
        qb_pointdatasource->setSizePolicy(sizePolicy2);
        qb_pointdatasource->setMinimumSize(QSize(155, 0));
        qb_pointdatasource->setMaximumSize(QSize(155, 16777215));

        horizontalLayout_3->addWidget(qb_pointdatasource);

        reload_settings = new QToolButton(groupBox);
        reload_settings->setObjectName(QString::fromUtf8("reload_settings"));
        QIcon icon3;
        icon3.addFile(QString::fromUtf8(":/FA_solid/icons/FA/solid/arrows-rotate.svg"), QSize(), QIcon::Normal, QIcon::Off);
        reload_settings->setIcon(icon3);

        horizontalLayout_3->addWidget(reload_settings);

        horizontalSpacer_4 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer_4);


        gridLayout_2->addLayout(horizontalLayout_3, 0, 1, 1, 1);

        label_9 = new QLabel(groupBox);
        label_9->setObjectName(QString::fromUtf8("label_9"));
        label_9->setMinimumSize(QSize(100, 0));
        label_9->setMaximumSize(QSize(130, 16777215));

        gridLayout_2->addWidget(label_9, 5, 0, 1, 1);

        logitude = new QLineEdit(groupBox);
        logitude->setObjectName(QString::fromUtf8("logitude"));
        logitude->setMaximumSize(QSize(190, 16777215));

        gridLayout_2->addWidget(logitude, 2, 1, 1, 1);

        xutm = new QLineEdit(groupBox);
        xutm->setObjectName(QString::fromUtf8("xutm"));
        xutm->setMaximumSize(QSize(190, 16777215));

        gridLayout_2->addWidget(xutm, 3, 1, 1, 1);

        latitude = new QLineEdit(groupBox);
        latitude->setObjectName(QString::fromUtf8("latitude"));
        latitude->setMaximumSize(QSize(190, 16777215));

        gridLayout_2->addWidget(latitude, 1, 1, 1, 1);

        label_6 = new QLabel(groupBox);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        gridLayout_2->addWidget(label_6, 6, 0, 1, 1);

        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        set_backscatter_field = new QComboBox(groupBox);
        set_backscatter_field->setObjectName(QString::fromUtf8("set_backscatter_field"));

        horizontalLayout_4->addWidget(set_backscatter_field);

        horizontalSpacer_7 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_4->addItem(horizontalSpacer_7);


        gridLayout_2->addLayout(horizontalLayout_4, 6, 1, 1, 1);


        verticalLayout_4->addLayout(gridLayout_2);


        gridLayout_5->addWidget(groupBox, 5, 0, 1, 1);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_5->addItem(verticalSpacer, 6, 0, 1, 1);

        query_builder_tools->setWidget(scrollAreaWidgetContents_2);

        verticalLayout_2->addWidget(query_builder_tools);

        splitter->addWidget(verticalLayoutWidget);
        groupBox_2 = new QGroupBox(splitter);
        groupBox_2->setObjectName(QString::fromUtf8("groupBox_2"));
        verticalLayout_14 = new QVBoxLayout(groupBox_2);
        verticalLayout_14->setObjectName(QString::fromUtf8("verticalLayout_14"));
        tabWidget = new QTabWidget(groupBox_2);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        sizePolicy.setHeightForWidth(tabWidget->sizePolicy().hasHeightForWidth());
        tabWidget->setSizePolicy(sizePolicy);
        tabWidget->setMinimumSize(QSize(100, 100));
        tabWidget->setTabPosition(QTabWidget::North);
        tabWidget->setTabShape(QTabWidget::Rounded);
        tabWidget->setDocumentMode(true);
        tabWidget->setMovable(true);
        tab = new QWidget();
        tab->setObjectName(QString::fromUtf8("tab"));
        verticalLayout_6 = new QVBoxLayout(tab);
        verticalLayout_6->setObjectName(QString::fromUtf8("verticalLayout_6"));
        tableView = new QTableView(tab);
        tableView->setObjectName(QString::fromUtf8("tableView"));
        QSizePolicy sizePolicy3(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy3.setHorizontalStretch(0);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(tableView->sizePolicy().hasHeightForWidth());
        tableView->setSizePolicy(sizePolicy3);

        verticalLayout_6->addWidget(tableView);

        QIcon icon4;
        icon4.addFile(QString::fromUtf8(":/icons/module-db.gif"), QSize(), QIcon::Normal, QIcon::Off);
        tabWidget->addTab(tab, icon4, QString());
        tab_2 = new QWidget();
        tab_2->setObjectName(QString::fromUtf8("tab_2"));
        verticalLayout_7 = new QVBoxLayout(tab_2);
        verticalLayout_7->setObjectName(QString::fromUtf8("verticalLayout_7"));
        verticalLayout_11 = new QVBoxLayout();
        verticalLayout_11->setSpacing(1);
        verticalLayout_11->setObjectName(QString::fromUtf8("verticalLayout_11"));
        groupBox_6 = new QGroupBox(tab_2);
        groupBox_6->setObjectName(QString::fromUtf8("groupBox_6"));
        groupBox_6->setMaximumSize(QSize(16777215, 80));
        gridLayout_7 = new QGridLayout(groupBox_6);
        gridLayout_7->setObjectName(QString::fromUtf8("gridLayout_7"));
        gridLayout_3 = new QGridLayout();
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        label_2 = new QLabel(groupBox_6);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout_3->addWidget(label_2, 0, 0, 1, 1);

        fitting_degree = new QSpinBox(groupBox_6);
        fitting_degree->setObjectName(QString::fromUtf8("fitting_degree"));
        fitting_degree->setMinimum(1);
        fitting_degree->setMaximum(12);

        gridLayout_3->addWidget(fitting_degree, 0, 1, 1, 1);


        gridLayout_7->addLayout(gridLayout_3, 0, 2, 1, 1);

        gridLayout = new QGridLayout();
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        right_beam = new QRadioButton(groupBox_6);
        right_beam->setObjectName(QString::fromUtf8("right_beam"));

        gridLayout->addWidget(right_beam, 0, 2, 1, 1);

        fold_beam = new QRadioButton(groupBox_6);
        fold_beam->setObjectName(QString::fromUtf8("fold_beam"));

        gridLayout->addWidget(fold_beam, 0, 3, 1, 1);

        left_beam = new QRadioButton(groupBox_6);
        left_beam->setObjectName(QString::fromUtf8("left_beam"));

        gridLayout->addWidget(left_beam, 0, 1, 1, 1);

        raw_beam = new QRadioButton(groupBox_6);
        raw_beam->setObjectName(QString::fromUtf8("raw_beam"));
        QFont font;
        font.setStrikeOut(false);
        raw_beam->setFont(font);
        raw_beam->setChecked(true);

        gridLayout->addWidget(raw_beam, 0, 0, 1, 1);


        gridLayout_7->addLayout(gridLayout, 0, 0, 1, 1);

        horizontalSpacer_10 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_7->addItem(horizontalSpacer_10, 0, 1, 1, 1);


        verticalLayout_11->addWidget(groupBox_6);


        verticalLayout_7->addLayout(verticalLayout_11);

        tabWidget->addTab(tab_2, icon, QString());

        verticalLayout_14->addWidget(tabWidget);

        splitter->addWidget(groupBox_2);

        verticalLayout_3->addWidget(splitter);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer_2);

        draw_graph = new QPushButton(Form);
        draw_graph->setObjectName(QString::fromUtf8("draw_graph"));
        draw_graph->setEnabled(false);
        QSizePolicy sizePolicy4(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy4.setHorizontalStretch(0);
        sizePolicy4.setVerticalStretch(0);
        sizePolicy4.setHeightForWidth(draw_graph->sizePolicy().hasHeightForWidth());
        draw_graph->setSizePolicy(sizePolicy4);
        draw_graph->setMaximumSize(QSize(32, 32));
        draw_graph->setStyleSheet(QString::fromUtf8(""));
        QIcon icon5;
        icon5.addFile(QString::fromUtf8(":/fa_solid/qtui/icons/fa_solid/chart-line.svg"), QSize(), QIcon::Normal, QIcon::Off);
        draw_graph->setIcon(icon5);
        draw_graph->setIconSize(QSize(25, 25));

        horizontalLayout->addWidget(draw_graph);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);

        clean_graph = new QPushButton(Form);
        clean_graph->setObjectName(QString::fromUtf8("clean_graph"));
        sizePolicy4.setHeightForWidth(clean_graph->sizePolicy().hasHeightForWidth());
        clean_graph->setSizePolicy(sizePolicy4);
        clean_graph->setMaximumSize(QSize(32, 32));
        clean_graph->setStyleSheet(QString::fromUtf8(""));
        QIcon icon6;
        icon6.addFile(QString::fromUtf8(":/fa_solid/qtui/icons/fa_solid/circle-xmark.svg"), QSize(), QIcon::Normal, QIcon::Off);
        clean_graph->setIcon(icon6);
        clean_graph->setIconSize(QSize(25, 25));

        horizontalLayout->addWidget(clean_graph);

        horizontalSpacer_8 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer_8);

        add_graph = new QPushButton(Form);
        add_graph->setObjectName(QString::fromUtf8("add_graph"));
        add_graph->setMaximumSize(QSize(32, 32));
        QFont font1;
        font1.setBold(false);
        font1.setWeight(50);
        add_graph->setFont(font1);
        QIcon icon7;
        icon7.addFile(QString::fromUtf8(":/fa_solid/qtui/icons/fa_solid/floppy-disk.svg"), QSize(), QIcon::Normal, QIcon::Off);
        add_graph->setIcon(icon7);
        add_graph->setIconSize(QSize(25, 25));

        horizontalLayout->addWidget(add_graph);

        horizontalSpacer_9 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer_9);


        verticalLayout_3->addLayout(horizontalLayout);


        retranslateUi(Form);

        qb_shapeselection->setCurrentIndex(0);
        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(Form);
    } // setupUi

    void retranslateUi(QWidget *Form)
    {
        Form->setWindowTitle(QCoreApplication::translate("Form", "Query_builder", nullptr));
        groupBox_4->setTitle(QCoreApplication::translate("Form", "Positioning", nullptr));
        qb_longitude->setText(QCoreApplication::translate("Form", "0", nullptr));
        qb_latlabel->setText(QCoreApplication::translate("Form", "Latitude", nullptr));
        qb_imageindex->setText(QCoreApplication::translate("Form", "1000", nullptr));
        qb_lonlabel->setText(QCoreApplication::translate("Form", "Longitude", nullptr));
        image_index_label->setText(QCoreApplication::translate("Form", "Image Index", nullptr));
        image_buffer_label->setText(QCoreApplication::translate("Form", "Image Buffer", nullptr));
        qb_latitude->setText(QCoreApplication::translate("Form", "0", nullptr));
        lock_location->setText(QCoreApplication::translate("Form", "Lock             ", nullptr));
        groupBox_3->setTitle(QCoreApplication::translate("Form", "Clipping Area", nullptr));
        qb_minoraxis_lablel->setText(QCoreApplication::translate("Form", "Minor Axis [m]", nullptr));
        qb_ellipsemajoraxis->setText(QCoreApplication::translate("Form", "10", nullptr));
        qb_shapeselection->setItemText(0, QCoreApplication::translate("Form", "- - -", nullptr));
        qb_shapeselection->setItemText(1, QCoreApplication::translate("Form", "Ellipse", nullptr));
        qb_shapeselection->setItemText(2, QCoreApplication::translate("Form", "Rectangle", nullptr));

        qb_ellipseorientation_label->setText(QCoreApplication::translate("Form", "Orientation", nullptr));
        qb_rectangle_l1_label->setText(QCoreApplication::translate("Form", "L1 - x - [m]", nullptr));
        qb_majoraxis_label->setText(QCoreApplication::translate("Form", "Major Axis [m]", nullptr));
        qb_ellipseminoraxis->setText(QCoreApplication::translate("Form", "5", nullptr));
        Iconlabel->setText(QCoreApplication::translate("Form", "Shape", nullptr));
        qb_rectangle_l2_label->setText(QCoreApplication::translate("Form", "L2 - y - [m]", nullptr));
        qb_rectangle_l1->setText(QCoreApplication::translate("Form", "10", nullptr));
        qb_rectangle_l2->setText(QCoreApplication::translate("Form", "5", nullptr));
        groupBox->setTitle(QCoreApplication::translate("Form", "MBES", nullptr));
        label->setText(QCoreApplication::translate("Form", "Point Data Source", nullptr));
        label_8->setText(QCoreApplication::translate("Form", "Northing", nullptr));
        label_5->setText(QCoreApplication::translate("Form", "Easting", nullptr));
        label_4->setText(QCoreApplication::translate("Form", "Longitude", nullptr));
        label_3->setText(QCoreApplication::translate("Form", "Latitude", nullptr));
        yutm->setText(QCoreApplication::translate("Form", "Northing", nullptr));
        utmzone->setText(QCoreApplication::translate("Form", "19", nullptr));
        reload_settings->setText(QString());
        label_9->setText(QCoreApplication::translate("Form", "EPSG", nullptr));
        logitude->setText(QCoreApplication::translate("Form", "Longitude", nullptr));
        xutm->setText(QCoreApplication::translate("Form", "Easting", nullptr));
        latitude->setText(QCoreApplication::translate("Form", "Latitude", nullptr));
        label_6->setText(QCoreApplication::translate("Form", "BS", nullptr));
        groupBox_2->setTitle(QString());
        tabWidget->setTabText(tabWidget->indexOf(tab), QCoreApplication::translate("Form", "Stat", nullptr));
#if QT_CONFIG(tooltip)
        tabWidget->setTabToolTip(tabWidget->indexOf(tab), QCoreApplication::translate("Form", "Statistics on selected pings", nullptr));
#endif // QT_CONFIG(tooltip)
        groupBox_6->setTitle(QCoreApplication::translate("Form", "Data Model", nullptr));
        label_2->setText(QCoreApplication::translate("Form", "Deg", nullptr));
#if QT_CONFIG(tooltip)
        right_beam->setToolTip(QCoreApplication::translate("Form", "render only positive Beams angles", nullptr));
#endif // QT_CONFIG(tooltip)
        right_beam->setText(QCoreApplication::translate("Form", "R", nullptr));
#if QT_CONFIG(tooltip)
        fold_beam->setToolTip(QCoreApplication::translate("Form", "render absolute value of the Beams angles", nullptr));
#endif // QT_CONFIG(tooltip)
        fold_beam->setText(QCoreApplication::translate("Form", "Fold", nullptr));
#if QT_CONFIG(tooltip)
        left_beam->setToolTip(QCoreApplication::translate("Form", "render only negative Beams angles", nullptr));
#endif // QT_CONFIG(tooltip)
        left_beam->setText(QCoreApplication::translate("Form", "L", nullptr));
#if QT_CONFIG(tooltip)
        raw_beam->setToolTip(QCoreApplication::translate("Form", "render both positiveand negative Beams angles", nullptr));
#endif // QT_CONFIG(tooltip)
        raw_beam->setText(QCoreApplication::translate("Form", "Raw", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab_2), QCoreApplication::translate("Form", "ARA", nullptr));
#if QT_CONFIG(tooltip)
        tabWidget->setTabToolTip(tabWidget->indexOf(tab_2), QCoreApplication::translate("Form", "Scatterplot selected pings - Angle vs BS", nullptr));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        draw_graph->setToolTip(QCoreApplication::translate("Form", "Draw Graph", nullptr));
#endif // QT_CONFIG(tooltip)
        draw_graph->setText(QString());
#if QT_CONFIG(tooltip)
        clean_graph->setToolTip(QCoreApplication::translate("Form", "Clean Outupt", nullptr));
#endif // QT_CONFIG(tooltip)
        clean_graph->setText(QString());
#if QT_CONFIG(tooltip)
        add_graph->setToolTip(QCoreApplication::translate("Form", "Add Graph", nullptr));
#endif // QT_CONFIG(tooltip)
        add_graph->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui

QT_END_NAMESPACE

#endif // QUERY_BUILDER_UI_UI_H
