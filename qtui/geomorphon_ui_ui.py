/********************************************************************************
** Form generated from reading UI file 'geomorphon_ui.ui'
**
** Created by: Qt User Interface Compiler version 5.15.8
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef GEOMORPHON_UI_UI_H
#define GEOMORPHON_UI_UI_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWebKitWidgets/QWebView>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_geomorphon
{
public:
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    QLabel *label_2;
    QTabWidget *tabWidget;
    QWidget *required;
    QGridLayout *gridLayout;
    QLabel *label_5;
    QSpinBox *skip;
    QLabel *label_3;
    QLineEdit *forms;
    QLineEdit *flat;
    QLineEdit *dist;
    QLabel *label_8;
    QLabel *label_6;
    QComboBox *elevation;
    QSpinBox *search;
    QLabel *label_4;
    QLabel *label_7;
    QSpacerItem *verticalSpacer_3;
    QWidget *geometry;
    QGridLayout *gridLayout_2;
    QLabel *label_14;
    QLabel *label_12;
    QLineEdit *elongation;
    QLineEdit *extend;
    QLabel *label_17;
    QLineEdit *exposition;
    QLabel *label_9;
    QLabel *label_10;
    QLineEdit *variance;
    QLineEdit *intensity;
    QLineEdit *range;
    QLabel *label_11;
    QLabel *label_15;
    QLabel *label_16;
    QLabel *label_13;
    QLineEdit *azimuth;
    QLineEdit *width;
    QSpacerItem *verticalSpacer_4;
    QWidget *optional;
    QGridLayout *gridLayout_3;
    QCheckBox *flag_m;
    QCheckBox *flag_e;
    QCheckBox *overwrite;
    QSpacerItem *verticalSpacer_2;
    QWidget *manual;
    QVBoxLayout *verticalLayout_2;
    QWebView *webView;
    QSpacerItem *verticalSpacer;
    QHBoxLayout *horizontalLayout_2;
    QPushButton *run;
    QSpacerItem *horizontalSpacer;
    QPushButton *exit;
    QCheckBox *checkBox_4;

    void setupUi(QWidget *geomorphon)
    {
        if (geomorphon->objectName().isEmpty())
            geomorphon->setObjectName(QString::fromUtf8("geomorphon"));
        geomorphon->resize(576, 456);
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/grass/qtui/icons/grass/grass_location.svg"), QSize(), QIcon::Normal, QIcon::Off);
        geomorphon->setWindowIcon(icon);
        verticalLayout = new QVBoxLayout(geomorphon);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label = new QLabel(geomorphon);
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

        label_2 = new QLabel(geomorphon);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setWordWrap(true);

        horizontalLayout->addWidget(label_2);


        verticalLayout->addLayout(horizontalLayout);

        tabWidget = new QTabWidget(geomorphon);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        required = new QWidget();
        required->setObjectName(QString::fromUtf8("required"));
        gridLayout = new QGridLayout(required);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label_5 = new QLabel(required);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        gridLayout->addWidget(label_5, 2, 0, 1, 1);

        skip = new QSpinBox(required);
        skip->setObjectName(QString::fromUtf8("skip"));

        gridLayout->addWidget(skip, 2, 1, 1, 1);

        label_3 = new QLabel(required);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        gridLayout->addWidget(label_3, 0, 0, 1, 1);

        forms = new QLineEdit(required);
        forms->setObjectName(QString::fromUtf8("forms"));

        gridLayout->addWidget(forms, 5, 1, 1, 1);

        flat = new QLineEdit(required);
        flat->setObjectName(QString::fromUtf8("flat"));
        flat->setStyleSheet(QString::fromUtf8(""));

        gridLayout->addWidget(flat, 3, 1, 1, 1);

        dist = new QLineEdit(required);
        dist->setObjectName(QString::fromUtf8("dist"));

        gridLayout->addWidget(dist, 4, 1, 1, 1);

        label_8 = new QLabel(required);
        label_8->setObjectName(QString::fromUtf8("label_8"));

        gridLayout->addWidget(label_8, 5, 0, 1, 1);

        label_6 = new QLabel(required);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        gridLayout->addWidget(label_6, 3, 0, 1, 1);

        elevation = new QComboBox(required);
        elevation->setObjectName(QString::fromUtf8("elevation"));

        gridLayout->addWidget(elevation, 0, 1, 1, 1);

        search = new QSpinBox(required);
        search->setObjectName(QString::fromUtf8("search"));
        search->setStyleSheet(QString::fromUtf8(""));
        search->setValue(3);

        gridLayout->addWidget(search, 1, 1, 1, 1);

        label_4 = new QLabel(required);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        gridLayout->addWidget(label_4, 1, 0, 1, 1);

        label_7 = new QLabel(required);
        label_7->setObjectName(QString::fromUtf8("label_7"));

        gridLayout->addWidget(label_7, 4, 0, 1, 1);

        verticalSpacer_3 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_3, 6, 1, 1, 1);

        tabWidget->addTab(required, QString());
        geometry = new QWidget();
        geometry->setObjectName(QString::fromUtf8("geometry"));
        gridLayout_2 = new QGridLayout(geometry);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        label_14 = new QLabel(geometry);
        label_14->setObjectName(QString::fromUtf8("label_14"));

        gridLayout_2->addWidget(label_14, 6, 0, 2, 1);

        label_12 = new QLabel(geometry);
        label_12->setObjectName(QString::fromUtf8("label_12"));

        gridLayout_2->addWidget(label_12, 4, 0, 1, 1);

        elongation = new QLineEdit(geometry);
        elongation->setObjectName(QString::fromUtf8("elongation"));

        gridLayout_2->addWidget(elongation, 5, 1, 1, 1);

        extend = new QLineEdit(geometry);
        extend->setObjectName(QString::fromUtf8("extend"));

        gridLayout_2->addWidget(extend, 7, 1, 2, 1);

        label_17 = new QLabel(geometry);
        label_17->setObjectName(QString::fromUtf8("label_17"));

        gridLayout_2->addWidget(label_17, 0, 0, 1, 1);

        exposition = new QLineEdit(geometry);
        exposition->setObjectName(QString::fromUtf8("exposition"));

        gridLayout_2->addWidget(exposition, 2, 1, 1, 1);

        label_9 = new QLabel(geometry);
        label_9->setObjectName(QString::fromUtf8("label_9"));

        gridLayout_2->addWidget(label_9, 1, 0, 1, 1);

        label_10 = new QLabel(geometry);
        label_10->setObjectName(QString::fromUtf8("label_10"));

        gridLayout_2->addWidget(label_10, 2, 0, 1, 1);

        variance = new QLineEdit(geometry);
        variance->setObjectName(QString::fromUtf8("variance"));

        gridLayout_2->addWidget(variance, 4, 1, 1, 1);

        intensity = new QLineEdit(geometry);
        intensity->setObjectName(QString::fromUtf8("intensity"));

        gridLayout_2->addWidget(intensity, 1, 1, 1, 1);

        range = new QLineEdit(geometry);
        range->setObjectName(QString::fromUtf8("range"));

        gridLayout_2->addWidget(range, 3, 1, 1, 1);

        label_11 = new QLabel(geometry);
        label_11->setObjectName(QString::fromUtf8("label_11"));

        gridLayout_2->addWidget(label_11, 3, 0, 1, 1);

        label_15 = new QLabel(geometry);
        label_15->setObjectName(QString::fromUtf8("label_15"));

        gridLayout_2->addWidget(label_15, 8, 0, 1, 1);

        label_16 = new QLabel(geometry);
        label_16->setObjectName(QString::fromUtf8("label_16"));

        gridLayout_2->addWidget(label_16, 9, 0, 1, 1);

        label_13 = new QLabel(geometry);
        label_13->setObjectName(QString::fromUtf8("label_13"));

        gridLayout_2->addWidget(label_13, 5, 0, 1, 1);

        azimuth = new QLineEdit(geometry);
        azimuth->setObjectName(QString::fromUtf8("azimuth"));

        gridLayout_2->addWidget(azimuth, 6, 1, 1, 1);

        width = new QLineEdit(geometry);
        width->setObjectName(QString::fromUtf8("width"));

        gridLayout_2->addWidget(width, 9, 1, 1, 1);

        verticalSpacer_4 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_2->addItem(verticalSpacer_4, 10, 0, 1, 1);

        tabWidget->addTab(geometry, QString());
        optional = new QWidget();
        optional->setObjectName(QString::fromUtf8("optional"));
        gridLayout_3 = new QGridLayout(optional);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        flag_m = new QCheckBox(optional);
        flag_m->setObjectName(QString::fromUtf8("flag_m"));

        gridLayout_3->addWidget(flag_m, 0, 0, 1, 1);

        flag_e = new QCheckBox(optional);
        flag_e->setObjectName(QString::fromUtf8("flag_e"));

        gridLayout_3->addWidget(flag_e, 1, 0, 1, 1);

        overwrite = new QCheckBox(optional);
        overwrite->setObjectName(QString::fromUtf8("overwrite"));

        gridLayout_3->addWidget(overwrite, 2, 0, 1, 1);

        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_3->addItem(verticalSpacer_2, 3, 0, 1, 1);

        tabWidget->addTab(optional, QString());
        manual = new QWidget();
        manual->setObjectName(QString::fromUtf8("manual"));
        verticalLayout_2 = new QVBoxLayout(manual);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        webView = new QWebView(manual);
        webView->setObjectName(QString::fromUtf8("webView"));
        webView->setUrl(QUrl(QString::fromUtf8("about:blank")));

        verticalLayout_2->addWidget(webView);

        tabWidget->addTab(manual, QString());

        verticalLayout->addWidget(tabWidget);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        run = new QPushButton(geomorphon);
        run->setObjectName(QString::fromUtf8("run"));

        horizontalLayout_2->addWidget(run);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer);

        exit = new QPushButton(geomorphon);
        exit->setObjectName(QString::fromUtf8("exit"));

        horizontalLayout_2->addWidget(exit);


        verticalLayout->addLayout(horizontalLayout_2);

        checkBox_4 = new QCheckBox(geomorphon);
        checkBox_4->setObjectName(QString::fromUtf8("checkBox_4"));

        verticalLayout->addWidget(checkBox_4);


        retranslateUi(geomorphon);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(geomorphon);
    } // setupUi

    void retranslateUi(QWidget *geomorphon)
    {
        geomorphon->setWindowTitle(QCoreApplication::translate("geomorphon", "r.geomorphon", nullptr));
        label->setText(QString());
        label_2->setText(QCoreApplication::translate("geomorphon", " Calculates geomorphons (terrain forms) and associated geometry using machine vision approach", nullptr));
        label_5->setText(QCoreApplication::translate("geomorphon", "Inner search radius", nullptr));
        label_3->setText(QCoreApplication::translate("geomorphon", "Name of input elevation raster map:", nullptr));
        flat->setText(QCoreApplication::translate("geomorphon", "1", nullptr));
        dist->setText(QCoreApplication::translate("geomorphon", "0", nullptr));
        label_8->setText(QCoreApplication::translate("geomorphon", "Most common geomorphic forms:", nullptr));
        label_6->setText(QCoreApplication::translate("geomorphon", "Flatness threshold (degrees):", nullptr));
        label_4->setText(QCoreApplication::translate("geomorphon", "Outer search radius:", nullptr));
        label_7->setText(QCoreApplication::translate("geomorphon", "Flatness distance, zero for none:", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(required), QCoreApplication::translate("geomorphon", "Required", nullptr));
        label_14->setText(QCoreApplication::translate("geomorphon", "Local azimuth of the elongation:", nullptr));
        label_12->setText(QCoreApplication::translate("geomorphon", "Variance of form boundary:", nullptr));
        label_17->setText(QCoreApplication::translate("geomorphon", "Raster containing:", nullptr));
        label_9->setText(QCoreApplication::translate("geomorphon", "Mean relative elevation of the form:", nullptr));
        label_10->setText(QCoreApplication::translate("geomorphon", "Maximum difference between extend and central cell:", nullptr));
        label_11->setText(QCoreApplication::translate("geomorphon", "Difference between max and min elevation of the form extend:", nullptr));
        label_15->setText(QCoreApplication::translate("geomorphon", "Local extend (area) of the form:", nullptr));
        label_16->setText(QCoreApplication::translate("geomorphon", "Local width of the form:", nullptr));
        label_13->setText(QCoreApplication::translate("geomorphon", "Local elongation:", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(geometry), QCoreApplication::translate("geomorphon", "Geometry", nullptr));
        flag_m->setText(QCoreApplication::translate("geomorphon", "Use meters to define search units (default is cells)", nullptr));
        flag_e->setText(QCoreApplication::translate("geomorphon", "Use extended form correction", nullptr));
        overwrite->setText(QCoreApplication::translate("geomorphon", "Allow output files to overwrite existing files", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(optional), QCoreApplication::translate("geomorphon", "Optional", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(manual), QCoreApplication::translate("geomorphon", "Manual", nullptr));
        run->setText(QCoreApplication::translate("geomorphon", "Run", nullptr));
        exit->setText(QCoreApplication::translate("geomorphon", "Close", nullptr));
        checkBox_4->setText(QCoreApplication::translate("geomorphon", "Add Geomorphic forms into layer tree", nullptr));
    } // retranslateUi

};

namespace Ui {
    class geomorphon: public Ui_geomorphon {};
} // namespace Ui

QT_END_NAMESPACE

#endif // GEOMORPHON_UI_UI_H
