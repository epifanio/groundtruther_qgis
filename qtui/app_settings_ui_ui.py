/********************************************************************************
** Form generated from reading UI file 'app_settings_ui.ui'
**
** Created by: Qt User Interface Compiler version 5.15.8
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef APP_SETTINGS_UI_UI_H
#define APP_SETTINGS_UI_UI_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_appsettings
{
public:
    QVBoxLayout *verticalLayout_3;
    QScrollArea *scrollArea;
    QWidget *scrollAreaWidgetContents;
    QVBoxLayout *verticalLayout_10;
    QGroupBox *habcam_config_box;
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QLabel *image_path_label;
    QSpacerItem *horizontalSpacer;
    QLineEdit *image_path;
    QToolButton *select_image_path;
    QHBoxLayout *horizontalLayout_2;
    QLabel *metadata_path_label;
    QSpacerItem *horizontalSpacer_2;
    QLineEdit *metadata_path;
    QToolButton *select_metadata_path;
    QHBoxLayout *horizontalLayout_11;
    QLabel *imageannotation_path_label;
    QSpacerItem *horizontalSpacer_11;
    QLineEdit *imageannotation_path;
    QToolButton *select_imageannotation_path;
    QGroupBox *mbes_config_box;
    QVBoxLayout *verticalLayout_2;
    QHBoxLayout *horizontalLayout_3;
    QLabel *mbes_path_label;
    QSpacerItem *horizontalSpacer_3;
    QLineEdit *mbes_path;
    QToolButton *select_mbes_path;
    QGroupBox *export_config_box;
    QVBoxLayout *verticalLayout_5;
    QHBoxLayout *horizontalLayout_5;
    QLabel *label_2;
    QSpacerItem *horizontalSpacer_5;
    QLineEdit *kml_path;
    QToolButton *select_kml_path;
    QHBoxLayout *horizontalLayout_6;
    QLabel *vrt_label;
    QSpacerItem *horizontalSpacer_6;
    QLineEdit *vrt_path;
    QToolButton *select_vrt_path;
    QGroupBox *broadcast_config_box;
    QVBoxLayout *verticalLayout_6;
    QVBoxLayout *verticalLayout_7;
    QHBoxLayout *horizontalLayout_7;
    QLabel *broadcast_IP_label;
    QSpacerItem *horizontalSpacer_7;
    QLineEdit *broadcast_ip;
    QHBoxLayout *horizontalLayout_8;
    QLabel *broadcast_port_label;
    QSpacerItem *horizontalSpacer_8;
    QLineEdit *broadcast_port;
    QGroupBox *groupBox;
    QVBoxLayout *verticalLayout_4;
    QHBoxLayout *horizontalLayout_12;
    QLabel *label;
    QSpacerItem *horizontalSpacer_10;
    QComboBox *gpu_avaibility;
    QHBoxLayout *horizontalLayout_13;
    QLabel *label_4;
    QSpacerItem *horizontalSpacer_12;
    QLineEdit *grass_api_endpoint;
    QGroupBox *filesystem_config_box;
    QVBoxLayout *verticalLayout_9;
    QHBoxLayout *horizontalLayout_9;
    QLabel *filnamager_label;
    QSpacerItem *horizontalSpacer_9;
    QLineEdit *filemanager;
    QSpacerItem *verticalSpacer;
    QHBoxLayout *horizontalLayout_4;
    QPushButton *quit;
    QSpacerItem *horizontalSpacer_4;
    QPushButton *setOption;

    void setupUi(QWidget *appsettings)
    {
        if (appsettings->objectName().isEmpty())
            appsettings->setObjectName(QString::fromUtf8("appsettings"));
        appsettings->resize(502, 580);
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/icons/element-vector.gif"), QSize(), QIcon::Normal, QIcon::Off);
        appsettings->setWindowIcon(icon);
        verticalLayout_3 = new QVBoxLayout(appsettings);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        scrollArea = new QScrollArea(appsettings);
        scrollArea->setObjectName(QString::fromUtf8("scrollArea"));
        scrollArea->setWidgetResizable(true);
        scrollAreaWidgetContents = new QWidget();
        scrollAreaWidgetContents->setObjectName(QString::fromUtf8("scrollAreaWidgetContents"));
        scrollAreaWidgetContents->setGeometry(QRect(0, 0, 468, 680));
        verticalLayout_10 = new QVBoxLayout(scrollAreaWidgetContents);
        verticalLayout_10->setObjectName(QString::fromUtf8("verticalLayout_10"));
        habcam_config_box = new QGroupBox(scrollAreaWidgetContents);
        habcam_config_box->setObjectName(QString::fromUtf8("habcam_config_box"));
        verticalLayout = new QVBoxLayout(habcam_config_box);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        image_path_label = new QLabel(habcam_config_box);
        image_path_label->setObjectName(QString::fromUtf8("image_path_label"));
        image_path_label->setMaximumSize(QSize(90, 16777215));
        QFont font;
        font.setStyleStrategy(QFont::PreferDefault);
        image_path_label->setFont(font);
        image_path_label->setLayoutDirection(Qt::LeftToRight);
        image_path_label->setAutoFillBackground(false);

        horizontalLayout->addWidget(image_path_label);

        horizontalSpacer = new QSpacerItem(37, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);

        image_path = new QLineEdit(habcam_config_box);
        image_path->setObjectName(QString::fromUtf8("image_path"));

        horizontalLayout->addWidget(image_path);

        select_image_path = new QToolButton(habcam_config_box);
        select_image_path->setObjectName(QString::fromUtf8("select_image_path"));

        horizontalLayout->addWidget(select_image_path);


        verticalLayout->addLayout(horizontalLayout);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        metadata_path_label = new QLabel(habcam_config_box);
        metadata_path_label->setObjectName(QString::fromUtf8("metadata_path_label"));
        metadata_path_label->setMaximumSize(QSize(90, 16777215));

        horizontalLayout_2->addWidget(metadata_path_label);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer_2);

        metadata_path = new QLineEdit(habcam_config_box);
        metadata_path->setObjectName(QString::fromUtf8("metadata_path"));

        horizontalLayout_2->addWidget(metadata_path);

        select_metadata_path = new QToolButton(habcam_config_box);
        select_metadata_path->setObjectName(QString::fromUtf8("select_metadata_path"));

        horizontalLayout_2->addWidget(select_metadata_path);


        verticalLayout->addLayout(horizontalLayout_2);

        horizontalLayout_11 = new QHBoxLayout();
        horizontalLayout_11->setObjectName(QString::fromUtf8("horizontalLayout_11"));
        imageannotation_path_label = new QLabel(habcam_config_box);
        imageannotation_path_label->setObjectName(QString::fromUtf8("imageannotation_path_label"));
        imageannotation_path_label->setMaximumSize(QSize(90, 16777215));

        horizontalLayout_11->addWidget(imageannotation_path_label);

        horizontalSpacer_11 = new QSpacerItem(58, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_11->addItem(horizontalSpacer_11);

        imageannotation_path = new QLineEdit(habcam_config_box);
        imageannotation_path->setObjectName(QString::fromUtf8("imageannotation_path"));

        horizontalLayout_11->addWidget(imageannotation_path);

        select_imageannotation_path = new QToolButton(habcam_config_box);
        select_imageannotation_path->setObjectName(QString::fromUtf8("select_imageannotation_path"));

        horizontalLayout_11->addWidget(select_imageannotation_path);


        verticalLayout->addLayout(horizontalLayout_11);


        verticalLayout_10->addWidget(habcam_config_box);

        mbes_config_box = new QGroupBox(scrollAreaWidgetContents);
        mbes_config_box->setObjectName(QString::fromUtf8("mbes_config_box"));
        verticalLayout_2 = new QVBoxLayout(mbes_config_box);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        mbes_path_label = new QLabel(mbes_config_box);
        mbes_path_label->setObjectName(QString::fromUtf8("mbes_path_label"));

        horizontalLayout_3->addWidget(mbes_path_label);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer_3);

        mbes_path = new QLineEdit(mbes_config_box);
        mbes_path->setObjectName(QString::fromUtf8("mbes_path"));

        horizontalLayout_3->addWidget(mbes_path);

        select_mbes_path = new QToolButton(mbes_config_box);
        select_mbes_path->setObjectName(QString::fromUtf8("select_mbes_path"));

        horizontalLayout_3->addWidget(select_mbes_path);


        verticalLayout_2->addLayout(horizontalLayout_3);


        verticalLayout_10->addWidget(mbes_config_box);

        export_config_box = new QGroupBox(scrollAreaWidgetContents);
        export_config_box->setObjectName(QString::fromUtf8("export_config_box"));
        verticalLayout_5 = new QVBoxLayout(export_config_box);
        verticalLayout_5->setObjectName(QString::fromUtf8("verticalLayout_5"));
        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        label_2 = new QLabel(export_config_box);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        horizontalLayout_5->addWidget(label_2);

        horizontalSpacer_5 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_5->addItem(horizontalSpacer_5);

        kml_path = new QLineEdit(export_config_box);
        kml_path->setObjectName(QString::fromUtf8("kml_path"));

        horizontalLayout_5->addWidget(kml_path);

        select_kml_path = new QToolButton(export_config_box);
        select_kml_path->setObjectName(QString::fromUtf8("select_kml_path"));

        horizontalLayout_5->addWidget(select_kml_path);


        verticalLayout_5->addLayout(horizontalLayout_5);

        horizontalLayout_6 = new QHBoxLayout();
        horizontalLayout_6->setObjectName(QString::fromUtf8("horizontalLayout_6"));
        vrt_label = new QLabel(export_config_box);
        vrt_label->setObjectName(QString::fromUtf8("vrt_label"));

        horizontalLayout_6->addWidget(vrt_label);

        horizontalSpacer_6 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_6->addItem(horizontalSpacer_6);

        vrt_path = new QLineEdit(export_config_box);
        vrt_path->setObjectName(QString::fromUtf8("vrt_path"));

        horizontalLayout_6->addWidget(vrt_path);

        select_vrt_path = new QToolButton(export_config_box);
        select_vrt_path->setObjectName(QString::fromUtf8("select_vrt_path"));

        horizontalLayout_6->addWidget(select_vrt_path);


        verticalLayout_5->addLayout(horizontalLayout_6);


        verticalLayout_10->addWidget(export_config_box);

        broadcast_config_box = new QGroupBox(scrollAreaWidgetContents);
        broadcast_config_box->setObjectName(QString::fromUtf8("broadcast_config_box"));
        verticalLayout_6 = new QVBoxLayout(broadcast_config_box);
        verticalLayout_6->setObjectName(QString::fromUtf8("verticalLayout_6"));
        verticalLayout_7 = new QVBoxLayout();
        verticalLayout_7->setObjectName(QString::fromUtf8("verticalLayout_7"));
        horizontalLayout_7 = new QHBoxLayout();
        horizontalLayout_7->setObjectName(QString::fromUtf8("horizontalLayout_7"));
        broadcast_IP_label = new QLabel(broadcast_config_box);
        broadcast_IP_label->setObjectName(QString::fromUtf8("broadcast_IP_label"));

        horizontalLayout_7->addWidget(broadcast_IP_label);

        horizontalSpacer_7 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_7->addItem(horizontalSpacer_7);

        broadcast_ip = new QLineEdit(broadcast_config_box);
        broadcast_ip->setObjectName(QString::fromUtf8("broadcast_ip"));

        horizontalLayout_7->addWidget(broadcast_ip);


        verticalLayout_7->addLayout(horizontalLayout_7);

        horizontalLayout_8 = new QHBoxLayout();
        horizontalLayout_8->setObjectName(QString::fromUtf8("horizontalLayout_8"));
        broadcast_port_label = new QLabel(broadcast_config_box);
        broadcast_port_label->setObjectName(QString::fromUtf8("broadcast_port_label"));

        horizontalLayout_8->addWidget(broadcast_port_label);

        horizontalSpacer_8 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_8->addItem(horizontalSpacer_8);

        broadcast_port = new QLineEdit(broadcast_config_box);
        broadcast_port->setObjectName(QString::fromUtf8("broadcast_port"));
        broadcast_port->setInputMethodHints(Qt::ImhNone);
        broadcast_port->setEchoMode(QLineEdit::Normal);

        horizontalLayout_8->addWidget(broadcast_port);


        verticalLayout_7->addLayout(horizontalLayout_8);


        verticalLayout_6->addLayout(verticalLayout_7);


        verticalLayout_10->addWidget(broadcast_config_box);

        groupBox = new QGroupBox(scrollAreaWidgetContents);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        verticalLayout_4 = new QVBoxLayout(groupBox);
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        horizontalLayout_12 = new QHBoxLayout();
        horizontalLayout_12->setObjectName(QString::fromUtf8("horizontalLayout_12"));
        label = new QLabel(groupBox);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout_12->addWidget(label);

        horizontalSpacer_10 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_12->addItem(horizontalSpacer_10);

        gpu_avaibility = new QComboBox(groupBox);
        gpu_avaibility->addItem(QString());
        gpu_avaibility->addItem(QString());
        gpu_avaibility->setObjectName(QString::fromUtf8("gpu_avaibility"));

        horizontalLayout_12->addWidget(gpu_avaibility);


        verticalLayout_4->addLayout(horizontalLayout_12);

        horizontalLayout_13 = new QHBoxLayout();
        horizontalLayout_13->setObjectName(QString::fromUtf8("horizontalLayout_13"));
        label_4 = new QLabel(groupBox);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        horizontalLayout_13->addWidget(label_4);

        horizontalSpacer_12 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_13->addItem(horizontalSpacer_12);

        grass_api_endpoint = new QLineEdit(groupBox);
        grass_api_endpoint->setObjectName(QString::fromUtf8("grass_api_endpoint"));

        horizontalLayout_13->addWidget(grass_api_endpoint);


        verticalLayout_4->addLayout(horizontalLayout_13);


        verticalLayout_10->addWidget(groupBox);

        filesystem_config_box = new QGroupBox(scrollAreaWidgetContents);
        filesystem_config_box->setObjectName(QString::fromUtf8("filesystem_config_box"));
        verticalLayout_9 = new QVBoxLayout(filesystem_config_box);
        verticalLayout_9->setObjectName(QString::fromUtf8("verticalLayout_9"));
        horizontalLayout_9 = new QHBoxLayout();
        horizontalLayout_9->setObjectName(QString::fromUtf8("horizontalLayout_9"));
        filnamager_label = new QLabel(filesystem_config_box);
        filnamager_label->setObjectName(QString::fromUtf8("filnamager_label"));

        horizontalLayout_9->addWidget(filnamager_label);

        horizontalSpacer_9 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_9->addItem(horizontalSpacer_9);

        filemanager = new QLineEdit(filesystem_config_box);
        filemanager->setObjectName(QString::fromUtf8("filemanager"));

        horizontalLayout_9->addWidget(filemanager);


        verticalLayout_9->addLayout(horizontalLayout_9);


        verticalLayout_10->addWidget(filesystem_config_box);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_10->addItem(verticalSpacer);

        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        quit = new QPushButton(scrollAreaWidgetContents);
        quit->setObjectName(QString::fromUtf8("quit"));

        horizontalLayout_4->addWidget(quit);

        horizontalSpacer_4 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_4->addItem(horizontalSpacer_4);

        setOption = new QPushButton(scrollAreaWidgetContents);
        setOption->setObjectName(QString::fromUtf8("setOption"));

        horizontalLayout_4->addWidget(setOption);


        verticalLayout_10->addLayout(horizontalLayout_4);

        scrollArea->setWidget(scrollAreaWidgetContents);

        verticalLayout_3->addWidget(scrollArea);


        retranslateUi(appsettings);

        QMetaObject::connectSlotsByName(appsettings);
    } // setupUi

    void retranslateUi(QWidget *appsettings)
    {
        appsettings->setWindowTitle(QCoreApplication::translate("appsettings", "Settings", nullptr));
        habcam_config_box->setTitle(QCoreApplication::translate("appsettings", "Habcam", nullptr));
        image_path_label->setText(QCoreApplication::translate("appsettings", "Images            ", nullptr));
        image_path->setText(QCoreApplication::translate("appsettings", "imgs_jpg", nullptr));
        select_image_path->setText(QCoreApplication::translate("appsettings", "...", nullptr));
        metadata_path_label->setText(QCoreApplication::translate("appsettings", "Metadata       ", nullptr));
        metadata_path->setText(QCoreApplication::translate("appsettings", "imagemetadata.pq", nullptr));
        select_metadata_path->setText(QCoreApplication::translate("appsettings", "...", nullptr));
        imageannotation_path_label->setText(QCoreApplication::translate("appsettings", "Annotation   ", nullptr));
        imageannotation_path->setText(QCoreApplication::translate("appsettings", "annotation.csv", nullptr));
        select_imageannotation_path->setText(QCoreApplication::translate("appsettings", "...", nullptr));
        mbes_config_box->setTitle(QCoreApplication::translate("appsettings", "MBES", nullptr));
        mbes_path_label->setText(QCoreApplication::translate("appsettings", "Soundings      ", nullptr));
        mbes_path->setText(QCoreApplication::translate("appsettings", "mbes.pq", nullptr));
        select_mbes_path->setText(QCoreApplication::translate("appsettings", "...", nullptr));
        export_config_box->setTitle(QCoreApplication::translate("appsettings", "Export", nullptr));
        label_2->setText(QCoreApplication::translate("appsettings", "KML                 ", nullptr));
        kml_path->setText(QCoreApplication::translate("appsettings", "kml", nullptr));
        select_kml_path->setText(QCoreApplication::translate("appsettings", "...", nullptr));
        vrt_label->setText(QCoreApplication::translate("appsettings", "VRT                  ", nullptr));
        vrt_path->setText(QCoreApplication::translate("appsettings", "vrt", nullptr));
        select_vrt_path->setText(QCoreApplication::translate("appsettings", "...", nullptr));
        broadcast_config_box->setTitle(QCoreApplication::translate("appsettings", "Broadcast", nullptr));
        broadcast_IP_label->setText(QCoreApplication::translate("appsettings", "IP                  ", nullptr));
        broadcast_ip->setText(QCoreApplication::translate("appsettings", "127.0.0.1", nullptr));
        broadcast_port_label->setText(QCoreApplication::translate("appsettings", "Port             ", nullptr));
        broadcast_port->setText(QCoreApplication::translate("appsettings", "7000", nullptr));
        groupBox->setTitle(QCoreApplication::translate("appsettings", "Processing", nullptr));
        label->setText(QCoreApplication::translate("appsettings", "GPU", nullptr));
        gpu_avaibility->setItemText(0, QCoreApplication::translate("appsettings", "Disabled", nullptr));
        gpu_avaibility->setItemText(1, QCoreApplication::translate("appsettings", "Enabled", nullptr));

        label_4->setText(QCoreApplication::translate("appsettings", "GRASS API", nullptr));
        grass_api_endpoint->setText(QCoreApplication::translate("appsettings", "http://localhost/docs", nullptr));
        filesystem_config_box->setTitle(QCoreApplication::translate("appsettings", "File System", nullptr));
        filnamager_label->setText(QCoreApplication::translate("appsettings", "File Manager", nullptr));
        filemanager->setText(QCoreApplication::translate("appsettings", "/usr/bin/nautilus", nullptr));
        quit->setText(QCoreApplication::translate("appsettings", "Close", nullptr));
        setOption->setText(QCoreApplication::translate("appsettings", "Set", nullptr));
    } // retranslateUi

};

namespace Ui {
    class appsettings: public Ui_appsettings {};
} // namespace Ui

QT_END_NAMESPACE

#endif // APP_SETTINGS_UI_UI_H
