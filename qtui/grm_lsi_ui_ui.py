/********************************************************************************
** Form generated from reading UI file 'grm_lsi_ui.ui'
**
** Created by: Qt User Interface Compiler version 5.15.8
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef GRM_LSI_UI_UI_H
#define GRM_LSI_UI_UI_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_grm_lsi
{
public:
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    QLabel *label_2;
    QScrollArea *scrollArea;
    QWidget *scrollAreaWidgetContents_2;
    QVBoxLayout *verticalLayout_2;
    QGroupBox *groupBox;
    QGridLayout *gridLayout_10;
    QLabel *label_32;
    QComboBox *elevation_2;
    QGroupBox *groupBox_2;
    QGridLayout *gridLayout_8;
    QLabel *label_8;
    QLineEdit *dist_3;
    QLabel *label_20;
    QLineEdit *lineEdit_7;
    QLabel *label_21;
    QLabel *label_22;
    QSpinBox *skip_3;
    QLabel *label_23;
    QComboBox *comboBox_2;
    QSpinBox *search_3;
    QLineEdit *lineEdit_8;
    QLineEdit *flat_3;
    QLabel *label_24;
    QLineEdit *lineEdit_9;
    QLabel *label_25;
    QLabel *label_26;
    QLabel *label_27;
    QLineEdit *lineEdit_10;
    QGroupBox *groupBox_3;
    QGridLayout *gridLayout_11;
    QSpinBox *search_4;
    QLabel *label_33;
    QLineEdit *flat_4;
    QLabel *label_34;
    QSpinBox *skip_4;
    QLabel *label_35;
    QLineEdit *lineEdit_15;
    QLabel *label_36;
    QLabel *label_37;
    QLineEdit *dist_4;
    QLabel *label_38;
    QLineEdit *lineEdit_16;
    QGroupBox *groupBox_4;
    QGridLayout *gridLayout_9;
    QLineEdit *lineEdit_11;
    QLabel *label_28;
    QLabel *label_29;
    QLineEdit *lineEdit_12;
    QLabel *label_30;
    QLineEdit *lineEdit_13;
    QLabel *label_31;
    QLineEdit *lineEdit_14;
    QHBoxLayout *horizontalLayout_2;
    QPushButton *pushButton;
    QSpacerItem *horizontalSpacer;
    QPushButton *pushButton_2;
    QCheckBox *checkBox_4;

    void setupUi(QWidget *grm_lsi)
    {
        if (grm_lsi->objectName().isEmpty())
            grm_lsi->setObjectName(QString::fromUtf8("grm_lsi"));
        grm_lsi->resize(571, 454);
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/grass/qtui/icons/grass/grass_location.svg"), QSize(), QIcon::Normal, QIcon::Off);
        grm_lsi->setWindowIcon(icon);
        verticalLayout = new QVBoxLayout(grm_lsi);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label = new QLabel(grm_lsi);
        label->setObjectName(QString::fromUtf8("label"));
        QSizePolicy sizePolicy(QSizePolicy::Minimum, QSizePolicy::Minimum);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(label->sizePolicy().hasHeightForWidth());
        label->setSizePolicy(sizePolicy);
        label->setMinimumSize(QSize(40, 40));
        label->setMaximumSize(QSize(40, 40));
        label->setPixmap(QPixmap(QString::fromUtf8(":/grass/qtui/icons/grass/grass_location.svg")));

        horizontalLayout->addWidget(label);

        label_2 = new QLabel(grm_lsi);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setWordWrap(true);

        horizontalLayout->addWidget(label_2);


        verticalLayout->addLayout(horizontalLayout);

        scrollArea = new QScrollArea(grm_lsi);
        scrollArea->setObjectName(QString::fromUtf8("scrollArea"));
        scrollArea->setWidgetResizable(true);
        scrollAreaWidgetContents_2 = new QWidget();
        scrollAreaWidgetContents_2->setObjectName(QString::fromUtf8("scrollAreaWidgetContents_2"));
        scrollAreaWidgetContents_2->setGeometry(QRect(0, 0, 537, 812));
        verticalLayout_2 = new QVBoxLayout(scrollAreaWidgetContents_2);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        groupBox = new QGroupBox(scrollAreaWidgetContents_2);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        gridLayout_10 = new QGridLayout(groupBox);
        gridLayout_10->setObjectName(QString::fromUtf8("gridLayout_10"));
        label_32 = new QLabel(groupBox);
        label_32->setObjectName(QString::fromUtf8("label_32"));

        gridLayout_10->addWidget(label_32, 0, 0, 1, 1);

        elevation_2 = new QComboBox(groupBox);
        elevation_2->setObjectName(QString::fromUtf8("elevation_2"));

        gridLayout_10->addWidget(elevation_2, 0, 1, 1, 1);


        verticalLayout_2->addWidget(groupBox);

        groupBox_2 = new QGroupBox(scrollAreaWidgetContents_2);
        groupBox_2->setObjectName(QString::fromUtf8("groupBox_2"));
        gridLayout_8 = new QGridLayout(groupBox_2);
        gridLayout_8->setObjectName(QString::fromUtf8("gridLayout_8"));
        label_8 = new QLabel(groupBox_2);
        label_8->setObjectName(QString::fromUtf8("label_8"));

        gridLayout_8->addWidget(label_8, 1, 0, 1, 1);

        dist_3 = new QLineEdit(groupBox_2);
        dist_3->setObjectName(QString::fromUtf8("dist_3"));

        gridLayout_8->addWidget(dist_3, 3, 1, 1, 1);

        label_20 = new QLabel(groupBox_2);
        label_20->setObjectName(QString::fromUtf8("label_20"));

        gridLayout_8->addWidget(label_20, 3, 0, 1, 1);

        lineEdit_7 = new QLineEdit(groupBox_2);
        lineEdit_7->setObjectName(QString::fromUtf8("lineEdit_7"));

        gridLayout_8->addWidget(lineEdit_7, 4, 1, 1, 1);

        label_21 = new QLabel(groupBox_2);
        label_21->setObjectName(QString::fromUtf8("label_21"));

        gridLayout_8->addWidget(label_21, 4, 0, 1, 1);

        label_22 = new QLabel(groupBox_2);
        label_22->setObjectName(QString::fromUtf8("label_22"));

        gridLayout_8->addWidget(label_22, 7, 0, 1, 1);

        skip_3 = new QSpinBox(groupBox_2);
        skip_3->setObjectName(QString::fromUtf8("skip_3"));
        skip_3->setValue(3);

        gridLayout_8->addWidget(skip_3, 1, 1, 1, 1);

        label_23 = new QLabel(groupBox_2);
        label_23->setObjectName(QString::fromUtf8("label_23"));

        gridLayout_8->addWidget(label_23, 5, 0, 1, 1);

        comboBox_2 = new QComboBox(groupBox_2);
        comboBox_2->addItem(QString());
        comboBox_2->addItem(QString());
        comboBox_2->addItem(QString());
        comboBox_2->addItem(QString());
        comboBox_2->addItem(QString());
        comboBox_2->addItem(QString());
        comboBox_2->addItem(QString());
        comboBox_2->addItem(QString());
        comboBox_2->addItem(QString());
        comboBox_2->addItem(QString());
        comboBox_2->addItem(QString());
        comboBox_2->addItem(QString());
        comboBox_2->setObjectName(QString::fromUtf8("comboBox_2"));

        gridLayout_8->addWidget(comboBox_2, 6, 1, 1, 1);

        search_3 = new QSpinBox(groupBox_2);
        search_3->setObjectName(QString::fromUtf8("search_3"));
        search_3->setValue(9);

        gridLayout_8->addWidget(search_3, 0, 1, 1, 1);

        lineEdit_8 = new QLineEdit(groupBox_2);
        lineEdit_8->setObjectName(QString::fromUtf8("lineEdit_8"));

        gridLayout_8->addWidget(lineEdit_8, 5, 1, 1, 1);

        flat_3 = new QLineEdit(groupBox_2);
        flat_3->setObjectName(QString::fromUtf8("flat_3"));

        gridLayout_8->addWidget(flat_3, 2, 1, 1, 1);

        label_24 = new QLabel(groupBox_2);
        label_24->setObjectName(QString::fromUtf8("label_24"));

        gridLayout_8->addWidget(label_24, 6, 0, 1, 1);

        lineEdit_9 = new QLineEdit(groupBox_2);
        lineEdit_9->setObjectName(QString::fromUtf8("lineEdit_9"));

        gridLayout_8->addWidget(lineEdit_9, 7, 1, 1, 1);

        label_25 = new QLabel(groupBox_2);
        label_25->setObjectName(QString::fromUtf8("label_25"));

        gridLayout_8->addWidget(label_25, 0, 0, 1, 1);

        label_26 = new QLabel(groupBox_2);
        label_26->setObjectName(QString::fromUtf8("label_26"));

        gridLayout_8->addWidget(label_26, 2, 0, 1, 1);

        label_27 = new QLabel(groupBox_2);
        label_27->setObjectName(QString::fromUtf8("label_27"));

        gridLayout_8->addWidget(label_27, 8, 0, 1, 1);

        lineEdit_10 = new QLineEdit(groupBox_2);
        lineEdit_10->setObjectName(QString::fromUtf8("lineEdit_10"));

        gridLayout_8->addWidget(lineEdit_10, 8, 1, 1, 1);


        verticalLayout_2->addWidget(groupBox_2);

        groupBox_3 = new QGroupBox(scrollAreaWidgetContents_2);
        groupBox_3->setObjectName(QString::fromUtf8("groupBox_3"));
        gridLayout_11 = new QGridLayout(groupBox_3);
        gridLayout_11->setObjectName(QString::fromUtf8("gridLayout_11"));
        search_4 = new QSpinBox(groupBox_3);
        search_4->setObjectName(QString::fromUtf8("search_4"));
        search_4->setValue(30);

        gridLayout_11->addWidget(search_4, 0, 1, 1, 1);

        label_33 = new QLabel(groupBox_3);
        label_33->setObjectName(QString::fromUtf8("label_33"));

        gridLayout_11->addWidget(label_33, 3, 0, 1, 1);

        flat_4 = new QLineEdit(groupBox_3);
        flat_4->setObjectName(QString::fromUtf8("flat_4"));

        gridLayout_11->addWidget(flat_4, 2, 1, 1, 1);

        label_34 = new QLabel(groupBox_3);
        label_34->setObjectName(QString::fromUtf8("label_34"));

        gridLayout_11->addWidget(label_34, 2, 0, 1, 1);

        skip_4 = new QSpinBox(groupBox_3);
        skip_4->setObjectName(QString::fromUtf8("skip_4"));
        skip_4->setValue(7);

        gridLayout_11->addWidget(skip_4, 1, 1, 1, 1);

        label_35 = new QLabel(groupBox_3);
        label_35->setObjectName(QString::fromUtf8("label_35"));

        gridLayout_11->addWidget(label_35, 0, 0, 1, 1);

        lineEdit_15 = new QLineEdit(groupBox_3);
        lineEdit_15->setObjectName(QString::fromUtf8("lineEdit_15"));

        gridLayout_11->addWidget(lineEdit_15, 4, 1, 1, 1);

        label_36 = new QLabel(groupBox_3);
        label_36->setObjectName(QString::fromUtf8("label_36"));

        gridLayout_11->addWidget(label_36, 4, 0, 1, 1);

        label_37 = new QLabel(groupBox_3);
        label_37->setObjectName(QString::fromUtf8("label_37"));

        gridLayout_11->addWidget(label_37, 1, 0, 1, 1);

        dist_4 = new QLineEdit(groupBox_3);
        dist_4->setObjectName(QString::fromUtf8("dist_4"));

        gridLayout_11->addWidget(dist_4, 3, 1, 1, 1);

        label_38 = new QLabel(groupBox_3);
        label_38->setObjectName(QString::fromUtf8("label_38"));

        gridLayout_11->addWidget(label_38, 5, 0, 1, 1);

        lineEdit_16 = new QLineEdit(groupBox_3);
        lineEdit_16->setObjectName(QString::fromUtf8("lineEdit_16"));

        gridLayout_11->addWidget(lineEdit_16, 5, 1, 1, 1);


        verticalLayout_2->addWidget(groupBox_3);

        groupBox_4 = new QGroupBox(scrollAreaWidgetContents_2);
        groupBox_4->setObjectName(QString::fromUtf8("groupBox_4"));
        gridLayout_9 = new QGridLayout(groupBox_4);
        gridLayout_9->setObjectName(QString::fromUtf8("gridLayout_9"));
        lineEdit_11 = new QLineEdit(groupBox_4);
        lineEdit_11->setObjectName(QString::fromUtf8("lineEdit_11"));

        gridLayout_9->addWidget(lineEdit_11, 2, 1, 1, 1);

        label_28 = new QLabel(groupBox_4);
        label_28->setObjectName(QString::fromUtf8("label_28"));

        gridLayout_9->addWidget(label_28, 0, 0, 1, 1);

        label_29 = new QLabel(groupBox_4);
        label_29->setObjectName(QString::fromUtf8("label_29"));

        gridLayout_9->addWidget(label_29, 1, 0, 1, 1);

        lineEdit_12 = new QLineEdit(groupBox_4);
        lineEdit_12->setObjectName(QString::fromUtf8("lineEdit_12"));

        gridLayout_9->addWidget(lineEdit_12, 1, 1, 1, 1);

        label_30 = new QLabel(groupBox_4);
        label_30->setObjectName(QString::fromUtf8("label_30"));

        gridLayout_9->addWidget(label_30, 2, 0, 1, 1);

        lineEdit_13 = new QLineEdit(groupBox_4);
        lineEdit_13->setObjectName(QString::fromUtf8("lineEdit_13"));

        gridLayout_9->addWidget(lineEdit_13, 0, 1, 1, 1);

        label_31 = new QLabel(groupBox_4);
        label_31->setObjectName(QString::fromUtf8("label_31"));

        gridLayout_9->addWidget(label_31, 3, 0, 1, 1);

        lineEdit_14 = new QLineEdit(groupBox_4);
        lineEdit_14->setObjectName(QString::fromUtf8("lineEdit_14"));

        gridLayout_9->addWidget(lineEdit_14, 3, 1, 1, 1);


        verticalLayout_2->addWidget(groupBox_4);

        scrollArea->setWidget(scrollAreaWidgetContents_2);

        verticalLayout->addWidget(scrollArea);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        pushButton = new QPushButton(grm_lsi);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));

        horizontalLayout_2->addWidget(pushButton);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer);

        pushButton_2 = new QPushButton(grm_lsi);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));

        horizontalLayout_2->addWidget(pushButton_2);


        verticalLayout->addLayout(horizontalLayout_2);

        checkBox_4 = new QCheckBox(grm_lsi);
        checkBox_4->setObjectName(QString::fromUtf8("checkBox_4"));

        verticalLayout->addWidget(checkBox_4);


        retranslateUi(grm_lsi);

        QMetaObject::connectSlotsByName(grm_lsi);
    } // setupUi

    void retranslateUi(QWidget *grm_lsi)
    {
        grm_lsi->setWindowTitle(QCoreApplication::translate("grm_lsi", "GRM - LSI", nullptr));
        label->setText(QString());
        label_2->setText(QCoreApplication::translate("grm_lsi", "Compute metrics for LSI bedforms", nullptr));
        groupBox->setTitle(QCoreApplication::translate("grm_lsi", "Input", nullptr));
        label_32->setText(QCoreApplication::translate("grm_lsi", "Name of input elevation raster map:", nullptr));
        groupBox_2->setTitle(QCoreApplication::translate("grm_lsi", "SWC", nullptr));
        label_8->setText(QCoreApplication::translate("grm_lsi", "Inner search radius", nullptr));
        dist_3->setText(QCoreApplication::translate("grm_lsi", "0", nullptr));
        label_20->setText(QCoreApplication::translate("grm_lsi", "Flatness distance, zero for none:", nullptr));
        lineEdit_7->setText(QCoreApplication::translate("grm_lsi", "400", nullptr));
        label_21->setText(QCoreApplication::translate("grm_lsi", "Thinning iterations", nullptr));
        label_22->setText(QCoreApplication::translate("grm_lsi", "v.generalize threshold", nullptr));
        label_23->setText(QCoreApplication::translate("grm_lsi", "Min area threshold", nullptr));
        comboBox_2->setItemText(0, QCoreApplication::translate("grm_lsi", "douglas", nullptr));
        comboBox_2->setItemText(1, QCoreApplication::translate("grm_lsi", "douglas_reduction", nullptr));
        comboBox_2->setItemText(2, QCoreApplication::translate("grm_lsi", "lang", nullptr));
        comboBox_2->setItemText(3, QCoreApplication::translate("grm_lsi", "reduction", nullptr));
        comboBox_2->setItemText(4, QCoreApplication::translate("grm_lsi", "reumann", nullptr));
        comboBox_2->setItemText(5, QCoreApplication::translate("grm_lsi", "boyle", nullptr));
        comboBox_2->setItemText(6, QCoreApplication::translate("grm_lsi", "sliding_averaging", nullptr));
        comboBox_2->setItemText(7, QCoreApplication::translate("grm_lsi", "chaiken", nullptr));
        comboBox_2->setItemText(8, QCoreApplication::translate("grm_lsi", "hermite", nullptr));
        comboBox_2->setItemText(9, QCoreApplication::translate("grm_lsi", "snakes", nullptr));
        comboBox_2->setItemText(10, QCoreApplication::translate("grm_lsi", "network", nullptr));
        comboBox_2->setItemText(11, QCoreApplication::translate("grm_lsi", "displacement", nullptr));

        lineEdit_8->setText(QCoreApplication::translate("grm_lsi", "70", nullptr));
        flat_3->setText(QCoreApplication::translate("grm_lsi", "2.0", nullptr));
        label_24->setText(QCoreApplication::translate("grm_lsi", "v.generalize method", nullptr));
        lineEdit_9->setText(QCoreApplication::translate("grm_lsi", "2", nullptr));
        label_25->setText(QCoreApplication::translate("grm_lsi", "Outer search radius:", nullptr));
        label_26->setText(QCoreApplication::translate("grm_lsi", "Flatness threshold (degrees):", nullptr));
        label_27->setText(QCoreApplication::translate("grm_lsi", "v.clean rmdangle threshold", nullptr));
        lineEdit_10->setText(QCoreApplication::translate("grm_lsi", "5,10,20,30", nullptr));
        groupBox_3->setTitle(QCoreApplication::translate("grm_lsi", "SW", nullptr));
        label_33->setText(QCoreApplication::translate("grm_lsi", "Flatness distance, zero for none:", nullptr));
        flat_4->setText(QCoreApplication::translate("grm_lsi", "3.8", nullptr));
        label_34->setText(QCoreApplication::translate("grm_lsi", "Flatness threshold (degrees):", nullptr));
        label_35->setText(QCoreApplication::translate("grm_lsi", "Outer search radius:", nullptr));
        lineEdit_15->setText(QCoreApplication::translate("grm_lsi", "1000", nullptr));
        label_36->setText(QCoreApplication::translate("grm_lsi", "Min area threshold", nullptr));
        label_37->setText(QCoreApplication::translate("grm_lsi", "Inner search radius", nullptr));
        dist_4->setText(QCoreApplication::translate("grm_lsi", "15", nullptr));
        label_38->setText(QCoreApplication::translate("grm_lsi", "v.clean rmarea threshold", nullptr));
        lineEdit_16->setText(QCoreApplication::translate("grm_lsi", "10", nullptr));
        groupBox_4->setTitle(QCoreApplication::translate("grm_lsi", "SW Metrics", nullptr));
        lineEdit_11->setText(QCoreApplication::translate("grm_lsi", "1", nullptr));
        label_28->setText(QCoreApplication::translate("grm_lsi", "Side-split buffer distance", nullptr));
        label_29->setText(QCoreApplication::translate("grm_lsi", "Transect split length", nullptr));
        lineEdit_12->setText(QCoreApplication::translate("grm_lsi", "1", nullptr));
        label_30->setText(QCoreApplication::translate("grm_lsi", "Point max distance", nullptr));
        lineEdit_13->setText(QCoreApplication::translate("grm_lsi", "1", nullptr));
        label_31->setText(QCoreApplication::translate("grm_lsi", "Transects side distance", nullptr));
        lineEdit_14->setText(QCoreApplication::translate("grm_lsi", "70,70", nullptr));
        pushButton->setText(QCoreApplication::translate("grm_lsi", "Run", nullptr));
        pushButton_2->setText(QCoreApplication::translate("grm_lsi", "Close", nullptr));
        checkBox_4->setText(QCoreApplication::translate("grm_lsi", "Add Geomorphic forms into layer tree", nullptr));
    } // retranslateUi

};

namespace Ui {
    class grm_lsi: public Ui_grm_lsi {};
} // namespace Ui

QT_END_NAMESPACE

#endif // GRM_LSI_UI_UI_H
