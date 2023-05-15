/********************************************************************************
** Form generated from reading UI file 'grassapi_settings_ui.ui'
**
** Created by: Qt User Interface Compiler version 5.15.8
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef GRASSAPI_SETTINGS_UI_UI_H
#define GRASSAPI_SETTINGS_UI_UI_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_GRASSAPI
{
public:
    QVBoxLayout *verticalLayout_4;
    QScrollArea *scrollArea;
    QWidget *scrollAreaWidgetContents;
    QVBoxLayout *verticalLayout_3;
    QGroupBox *groupBox;
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    QLineEdit *grass_api_endpoint;
    QGroupBox *groupBox_2;
    QGridLayout *gridLayout;
    QLineEdit *grass_gisdb;
    QLabel *label_3;
    QLabel *label_2;
    QHBoxLayout *horizontalLayout_2;
    QToolButton *new_grass_location_dialog;
    QSpacerItem *horizontalSpacer_2;
    QToolButton *reload;
    QSpacerItem *horizontalSpacer;
    QPushButton *set_location;
    QComboBox *grass_location_list;
    QLabel *label_4;
    QComboBox *location_mapset_list;
    QGroupBox *grass_new_location_groupbox;
    QGridLayout *gridLayout_2;
    QHBoxLayout *horizontalLayout_7;
    QComboBox *epsg_code;
    QToolButton *search_epsg;
    QVBoxLayout *verticalLayout_2;
    QHBoxLayout *horizontalLayout_6;
    QLineEdit *georef_file;
    QToolButton *set_georef_file;
    QHBoxLayout *horizontalLayout_5;
    QLabel *label_10;
    QLineEdit *layer_name;
    QLineEdit *new_location_name;
    QLabel *label_5;
    QHBoxLayout *horizontalLayout_3;
    QVBoxLayout *verticalLayout;
    QRadioButton *choice_epsg;
    QRadioButton *choice_georef;
    QSpacerItem *horizontalSpacer_3;
    QPushButton *create_location;
    QLabel *label_6;
    QLabel *label_7;
    QGroupBox *grass_new_mapset_groupbox;
    QGridLayout *gridLayout_3;
    QHBoxLayout *horizontalLayout_4;
    QSpacerItem *horizontalSpacer_4;
    QPushButton *create_mapset;
    QLabel *label_8;
    QLineEdit *new_mapset;
    QLabel *label_9;
    QComboBox *grass_location_list2;
    QSpacerItem *verticalSpacer;
    QTextEdit *command_output;
    QHBoxLayout *horizontalLayout_8;
    QPushButton *show_output_log;
    QFrame *frame;
    QPushButton *exit;

    void setupUi(QWidget *GRASSAPI)
    {
        if (GRASSAPI->objectName().isEmpty())
            GRASSAPI->setObjectName(QString::fromUtf8("GRASSAPI"));
        GRASSAPI->resize(458, 948);
        GRASSAPI->setMinimumSize(QSize(2, 0));
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/GRASS/icons/GRASS/grass-40x40.png"), QSize(), QIcon::Normal, QIcon::Off);
        GRASSAPI->setWindowIcon(icon);
        verticalLayout_4 = new QVBoxLayout(GRASSAPI);
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        scrollArea = new QScrollArea(GRASSAPI);
        scrollArea->setObjectName(QString::fromUtf8("scrollArea"));
        scrollArea->setWidgetResizable(true);
        scrollAreaWidgetContents = new QWidget();
        scrollAreaWidgetContents->setObjectName(QString::fromUtf8("scrollAreaWidgetContents"));
        scrollAreaWidgetContents->setGeometry(QRect(0, 0, 424, 653));
        verticalLayout_3 = new QVBoxLayout(scrollAreaWidgetContents);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        groupBox = new QGroupBox(scrollAreaWidgetContents);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        QSizePolicy sizePolicy(QSizePolicy::Minimum, QSizePolicy::Minimum);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(groupBox->sizePolicy().hasHeightForWidth());
        groupBox->setSizePolicy(sizePolicy);
        groupBox->setMaximumSize(QSize(16777215, 70));
        horizontalLayout = new QHBoxLayout(groupBox);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label = new QLabel(groupBox);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout->addWidget(label);

        grass_api_endpoint = new QLineEdit(groupBox);
        grass_api_endpoint->setObjectName(QString::fromUtf8("grass_api_endpoint"));

        horizontalLayout->addWidget(grass_api_endpoint);


        verticalLayout_3->addWidget(groupBox);

        groupBox_2 = new QGroupBox(scrollAreaWidgetContents);
        groupBox_2->setObjectName(QString::fromUtf8("groupBox_2"));
        sizePolicy.setHeightForWidth(groupBox_2->sizePolicy().hasHeightForWidth());
        groupBox_2->setSizePolicy(sizePolicy);
        groupBox_2->setMaximumSize(QSize(16777215, 170));
        gridLayout = new QGridLayout(groupBox_2);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        grass_gisdb = new QLineEdit(groupBox_2);
        grass_gisdb->setObjectName(QString::fromUtf8("grass_gisdb"));

        gridLayout->addWidget(grass_gisdb, 0, 1, 1, 1);

        label_3 = new QLabel(groupBox_2);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        gridLayout->addWidget(label_3, 4, 0, 1, 1);

        label_2 = new QLabel(groupBox_2);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout->addWidget(label_2, 3, 0, 1, 1);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        new_grass_location_dialog = new QToolButton(groupBox_2);
        new_grass_location_dialog->setObjectName(QString::fromUtf8("new_grass_location_dialog"));

        horizontalLayout_2->addWidget(new_grass_location_dialog);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer_2);

        reload = new QToolButton(groupBox_2);
        reload->setObjectName(QString::fromUtf8("reload"));
        reload->setMinimumSize(QSize(30, 30));
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/QGIS/icons/QGIS_Images/themes/default/mActionReload.svg"), QSize(), QIcon::Normal, QIcon::Off);
        reload->setIcon(icon1);

        horizontalLayout_2->addWidget(reload);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer);

        set_location = new QPushButton(groupBox_2);
        set_location->setObjectName(QString::fromUtf8("set_location"));

        horizontalLayout_2->addWidget(set_location);


        gridLayout->addLayout(horizontalLayout_2, 5, 1, 1, 1);

        grass_location_list = new QComboBox(groupBox_2);
        grass_location_list->setObjectName(QString::fromUtf8("grass_location_list"));

        gridLayout->addWidget(grass_location_list, 3, 1, 1, 1);

        label_4 = new QLabel(groupBox_2);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        gridLayout->addWidget(label_4, 0, 0, 1, 1);

        location_mapset_list = new QComboBox(groupBox_2);
        location_mapset_list->setObjectName(QString::fromUtf8("location_mapset_list"));

        gridLayout->addWidget(location_mapset_list, 4, 1, 1, 1);


        verticalLayout_3->addWidget(groupBox_2);

        grass_new_location_groupbox = new QGroupBox(scrollAreaWidgetContents);
        grass_new_location_groupbox->setObjectName(QString::fromUtf8("grass_new_location_groupbox"));
        sizePolicy.setHeightForWidth(grass_new_location_groupbox->sizePolicy().hasHeightForWidth());
        grass_new_location_groupbox->setSizePolicy(sizePolicy);
        grass_new_location_groupbox->setMaximumSize(QSize(16777215, 240));
        gridLayout_2 = new QGridLayout(grass_new_location_groupbox);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        horizontalLayout_7 = new QHBoxLayout();
        horizontalLayout_7->setObjectName(QString::fromUtf8("horizontalLayout_7"));
        epsg_code = new QComboBox(grass_new_location_groupbox);
        epsg_code->setObjectName(QString::fromUtf8("epsg_code"));

        horizontalLayout_7->addWidget(epsg_code);

        search_epsg = new QToolButton(grass_new_location_groupbox);
        search_epsg->setObjectName(QString::fromUtf8("search_epsg"));
        search_epsg->setMinimumSize(QSize(30, 30));
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/FA_brands/icons/FA/brands/searchengin.svg"), QSize(), QIcon::Normal, QIcon::Off);
        search_epsg->setIcon(icon2);

        horizontalLayout_7->addWidget(search_epsg);


        gridLayout_2->addLayout(horizontalLayout_7, 1, 2, 1, 1);

        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        horizontalLayout_6 = new QHBoxLayout();
        horizontalLayout_6->setObjectName(QString::fromUtf8("horizontalLayout_6"));
        georef_file = new QLineEdit(grass_new_location_groupbox);
        georef_file->setObjectName(QString::fromUtf8("georef_file"));

        horizontalLayout_6->addWidget(georef_file);

        set_georef_file = new QToolButton(grass_new_location_groupbox);
        set_georef_file->setObjectName(QString::fromUtf8("set_georef_file"));
        set_georef_file->setMinimumSize(QSize(30, 30));
        QIcon icon3;
        icon3.addFile(QString::fromUtf8(":/FA_regular/icons/FA/regular/file-image.svg"), QSize(), QIcon::Normal, QIcon::Off);
        set_georef_file->setIcon(icon3);

        horizontalLayout_6->addWidget(set_georef_file);


        verticalLayout_2->addLayout(horizontalLayout_6);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        label_10 = new QLabel(grass_new_location_groupbox);
        label_10->setObjectName(QString::fromUtf8("label_10"));

        horizontalLayout_5->addWidget(label_10);

        layer_name = new QLineEdit(grass_new_location_groupbox);
        layer_name->setObjectName(QString::fromUtf8("layer_name"));

        horizontalLayout_5->addWidget(layer_name);


        verticalLayout_2->addLayout(horizontalLayout_5);


        gridLayout_2->addLayout(verticalLayout_2, 2, 2, 1, 1);

        new_location_name = new QLineEdit(grass_new_location_groupbox);
        new_location_name->setObjectName(QString::fromUtf8("new_location_name"));

        gridLayout_2->addWidget(new_location_name, 0, 2, 1, 1);

        label_5 = new QLabel(grass_new_location_groupbox);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        gridLayout_2->addWidget(label_5, 1, 0, 1, 1);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        choice_epsg = new QRadioButton(grass_new_location_groupbox);
        choice_epsg->setObjectName(QString::fromUtf8("choice_epsg"));
        choice_epsg->setChecked(true);

        verticalLayout->addWidget(choice_epsg);

        choice_georef = new QRadioButton(grass_new_location_groupbox);
        choice_georef->setObjectName(QString::fromUtf8("choice_georef"));

        verticalLayout->addWidget(choice_georef);


        horizontalLayout_3->addLayout(verticalLayout);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer_3);

        create_location = new QPushButton(grass_new_location_groupbox);
        create_location->setObjectName(QString::fromUtf8("create_location"));

        horizontalLayout_3->addWidget(create_location);


        gridLayout_2->addLayout(horizontalLayout_3, 3, 2, 1, 1);

        label_6 = new QLabel(grass_new_location_groupbox);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        gridLayout_2->addWidget(label_6, 2, 0, 1, 1);

        label_7 = new QLabel(grass_new_location_groupbox);
        label_7->setObjectName(QString::fromUtf8("label_7"));

        gridLayout_2->addWidget(label_7, 0, 0, 1, 1);


        verticalLayout_3->addWidget(grass_new_location_groupbox);

        grass_new_mapset_groupbox = new QGroupBox(scrollAreaWidgetContents);
        grass_new_mapset_groupbox->setObjectName(QString::fromUtf8("grass_new_mapset_groupbox"));
        sizePolicy.setHeightForWidth(grass_new_mapset_groupbox->sizePolicy().hasHeightForWidth());
        grass_new_mapset_groupbox->setSizePolicy(sizePolicy);
        grass_new_mapset_groupbox->setMaximumSize(QSize(16777215, 140));
        gridLayout_3 = new QGridLayout(grass_new_mapset_groupbox);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        horizontalSpacer_4 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_4->addItem(horizontalSpacer_4);

        create_mapset = new QPushButton(grass_new_mapset_groupbox);
        create_mapset->setObjectName(QString::fromUtf8("create_mapset"));

        horizontalLayout_4->addWidget(create_mapset);


        gridLayout_3->addLayout(horizontalLayout_4, 2, 1, 1, 1);

        label_8 = new QLabel(grass_new_mapset_groupbox);
        label_8->setObjectName(QString::fromUtf8("label_8"));

        gridLayout_3->addWidget(label_8, 1, 0, 1, 1);

        new_mapset = new QLineEdit(grass_new_mapset_groupbox);
        new_mapset->setObjectName(QString::fromUtf8("new_mapset"));

        gridLayout_3->addWidget(new_mapset, 1, 1, 1, 1);

        label_9 = new QLabel(grass_new_mapset_groupbox);
        label_9->setObjectName(QString::fromUtf8("label_9"));

        gridLayout_3->addWidget(label_9, 0, 0, 1, 1);

        grass_location_list2 = new QComboBox(grass_new_mapset_groupbox);
        grass_location_list2->setObjectName(QString::fromUtf8("grass_location_list2"));

        gridLayout_3->addWidget(grass_location_list2, 0, 1, 1, 1);


        verticalLayout_3->addWidget(grass_new_mapset_groupbox);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_3->addItem(verticalSpacer);

        scrollArea->setWidget(scrollAreaWidgetContents);

        verticalLayout_4->addWidget(scrollArea);

        command_output = new QTextEdit(GRASSAPI);
        command_output->setObjectName(QString::fromUtf8("command_output"));
        QSizePolicy sizePolicy1(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(command_output->sizePolicy().hasHeightForWidth());
        command_output->setSizePolicy(sizePolicy1);

        verticalLayout_4->addWidget(command_output);

        horizontalLayout_8 = new QHBoxLayout();
        horizontalLayout_8->setObjectName(QString::fromUtf8("horizontalLayout_8"));
        show_output_log = new QPushButton(GRASSAPI);
        show_output_log->setObjectName(QString::fromUtf8("show_output_log"));
        show_output_log->setMaximumSize(QSize(90, 16777215));
        show_output_log->setCheckable(false);

        horizontalLayout_8->addWidget(show_output_log);

        frame = new QFrame(GRASSAPI);
        frame->setObjectName(QString::fromUtf8("frame"));
        frame->setMinimumSize(QSize(0, 15));
        frame->setMaximumSize(QSize(16777215, 30));
        frame->setStyleSheet(QString::fromUtf8("QFrame {\n"
"            border: 1px solid black;\n"
"            border-radius: 1px;\n"
"            background-color: rgb(51, 209, 122);\n"
"            }"));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);

        horizontalLayout_8->addWidget(frame);

        exit = new QPushButton(GRASSAPI);
        exit->setObjectName(QString::fromUtf8("exit"));
        exit->setMaximumSize(QSize(90, 16777215));

        horizontalLayout_8->addWidget(exit);


        verticalLayout_4->addLayout(horizontalLayout_8);


        retranslateUi(GRASSAPI);

        QMetaObject::connectSlotsByName(GRASSAPI);
    } // setupUi

    void retranslateUi(QWidget *GRASSAPI)
    {
        GRASSAPI->setWindowTitle(QCoreApplication::translate("GRASSAPI", "GRASS API Settings", nullptr));
        groupBox->setTitle(QCoreApplication::translate("GRASSAPI", "GRASS API", nullptr));
        label->setText(QCoreApplication::translate("GRASSAPI", "Endpoint", nullptr));
        grass_api_endpoint->setText(QCoreApplication::translate("GRASSAPI", "http://localhost", nullptr));
        groupBox_2->setTitle(QCoreApplication::translate("GRASSAPI", "GRASS ENVIRONMENT", nullptr));
        grass_gisdb->setText(QCoreApplication::translate("GRASSAPI", "/tmp", nullptr));
        label_3->setText(QCoreApplication::translate("GRASSAPI", "MAPSET", nullptr));
        label_2->setText(QCoreApplication::translate("GRASSAPI", "LOCATION", nullptr));
        new_grass_location_dialog->setText(QCoreApplication::translate("GRASSAPI", "New", nullptr));
        reload->setText(QCoreApplication::translate("GRASSAPI", "...", nullptr));
        set_location->setText(QCoreApplication::translate("GRASSAPI", "Set", nullptr));
        label_4->setText(QCoreApplication::translate("GRASSAPI", "GISDB", nullptr));
        grass_new_location_groupbox->setTitle(QCoreApplication::translate("GRASSAPI", "NEW LOCATION", nullptr));
        search_epsg->setText(QString());
        set_georef_file->setText(QCoreApplication::translate("GRASSAPI", "...", nullptr));
        label_10->setText(QCoreApplication::translate("GRASSAPI", "Layer name", nullptr));
        label_5->setText(QCoreApplication::translate("GRASSAPI", "EPSG", nullptr));
        choice_epsg->setText(QCoreApplication::translate("GRASSAPI", "epsg", nullptr));
        choice_georef->setText(QCoreApplication::translate("GRASSAPI", "georef", nullptr));
        create_location->setText(QCoreApplication::translate("GRASSAPI", "ADD", nullptr));
        label_6->setText(QCoreApplication::translate("GRASSAPI", "Georef File", nullptr));
        label_7->setText(QCoreApplication::translate("GRASSAPI", "NAME", nullptr));
        grass_new_mapset_groupbox->setTitle(QCoreApplication::translate("GRASSAPI", "NEW MAPSET", nullptr));
        create_mapset->setText(QCoreApplication::translate("GRASSAPI", "ADD", nullptr));
        label_8->setText(QCoreApplication::translate("GRASSAPI", "NAME", nullptr));
        label_9->setText(QCoreApplication::translate("GRASSAPI", "LOCATION", nullptr));
        show_output_log->setText(QCoreApplication::translate("GRASSAPI", "output log", nullptr));
        exit->setText(QCoreApplication::translate("GRASSAPI", "Exit", nullptr));
    } // retranslateUi

};

namespace Ui {
    class GRASSAPI: public Ui_GRASSAPI {};
} // namespace Ui

QT_END_NAMESPACE

#endif // GRASSAPI_SETTINGS_UI_UI_H
