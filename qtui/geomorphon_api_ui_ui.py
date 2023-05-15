/********************************************************************************
** Form generated from reading UI file 'geomorphon_api_ui.ui'
**
** Created by: Qt User Interface Compiler version 5.15.8
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef GEOMORPHON_API_UI_UI_H
#define GEOMORPHON_API_UI_UI_H

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
#include <QtWidgets/QToolButton>
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
    QLineEdit *flat;
    QLabel *label_3;
    QComboBox *elevation;
    QSpinBox *search;
    QSpinBox *skip;
    QLabel *label_6;
    QSpacerItem *verticalSpacer_3;
    QLineEdit *output_suffix;
    QLabel *label_8;
    QLabel *label_5;
    QLabel *label_7;
    QLineEdit *dist;
    QLabel *label_4;
    QWidget *optional;
    QGridLayout *gridLayout_3;
    QCheckBox *flag_m;
    QCheckBox *flag_e;
    QSpacerItem *verticalSpacer_2;
    QCheckBox *overwrite;
    QCheckBox *derivatives;
    QWidget *manual;
    QVBoxLayout *verticalLayout_2;
    QWebView *webView;
    QSpacerItem *verticalSpacer;
    QHBoxLayout *horizontalLayout_2;
    QPushButton *run;
    QSpacerItem *horizontalSpacer_2;
    QToolButton *reload_layers;
    QSpacerItem *horizontalSpacer;
    QPushButton *exit;
    QCheckBox *add_output;

    void setupUi(QWidget *geomorphon)
    {
        if (geomorphon->objectName().isEmpty())
            geomorphon->setObjectName(QString::fromUtf8("geomorphon"));
        geomorphon->resize(398, 373);
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
        flat = new QLineEdit(required);
        flat->setObjectName(QString::fromUtf8("flat"));
        flat->setStyleSheet(QString::fromUtf8(""));

        gridLayout->addWidget(flat, 3, 1, 1, 1);

        label_3 = new QLabel(required);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        gridLayout->addWidget(label_3, 0, 0, 1, 1);

        elevation = new QComboBox(required);
        elevation->setObjectName(QString::fromUtf8("elevation"));

        gridLayout->addWidget(elevation, 0, 1, 1, 1);

        search = new QSpinBox(required);
        search->setObjectName(QString::fromUtf8("search"));
        search->setStyleSheet(QString::fromUtf8(""));
        search->setValue(3);

        gridLayout->addWidget(search, 1, 1, 1, 1);

        skip = new QSpinBox(required);
        skip->setObjectName(QString::fromUtf8("skip"));

        gridLayout->addWidget(skip, 2, 1, 1, 1);

        label_6 = new QLabel(required);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        gridLayout->addWidget(label_6, 3, 0, 1, 1);

        verticalSpacer_3 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_3, 6, 1, 1, 1);

        output_suffix = new QLineEdit(required);
        output_suffix->setObjectName(QString::fromUtf8("output_suffix"));

        gridLayout->addWidget(output_suffix, 5, 1, 1, 1);

        label_8 = new QLabel(required);
        label_8->setObjectName(QString::fromUtf8("label_8"));

        gridLayout->addWidget(label_8, 5, 0, 1, 1);

        label_5 = new QLabel(required);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        gridLayout->addWidget(label_5, 2, 0, 1, 1);

        label_7 = new QLabel(required);
        label_7->setObjectName(QString::fromUtf8("label_7"));

        gridLayout->addWidget(label_7, 4, 0, 1, 1);

        dist = new QLineEdit(required);
        dist->setObjectName(QString::fromUtf8("dist"));

        gridLayout->addWidget(dist, 4, 1, 1, 1);

        label_4 = new QLabel(required);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        gridLayout->addWidget(label_4, 1, 0, 1, 1);

        tabWidget->addTab(required, QString());
        optional = new QWidget();
        optional->setObjectName(QString::fromUtf8("optional"));
        gridLayout_3 = new QGridLayout(optional);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        flag_m = new QCheckBox(optional);
        flag_m->setObjectName(QString::fromUtf8("flag_m"));

        gridLayout_3->addWidget(flag_m, 1, 0, 1, 1);

        flag_e = new QCheckBox(optional);
        flag_e->setObjectName(QString::fromUtf8("flag_e"));

        gridLayout_3->addWidget(flag_e, 2, 0, 1, 1);

        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_3->addItem(verticalSpacer_2, 5, 0, 1, 1);

        overwrite = new QCheckBox(optional);
        overwrite->setObjectName(QString::fromUtf8("overwrite"));

        gridLayout_3->addWidget(overwrite, 3, 0, 1, 1);

        derivatives = new QCheckBox(optional);
        derivatives->setObjectName(QString::fromUtf8("derivatives"));

        gridLayout_3->addWidget(derivatives, 0, 0, 1, 1);

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

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer_2);

        reload_layers = new QToolButton(geomorphon);
        reload_layers->setObjectName(QString::fromUtf8("reload_layers"));
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/fa_solid/qtui/icons/fa_solid/arrows-rotate.svg"), QSize(), QIcon::Normal, QIcon::Off);
        reload_layers->setIcon(icon1);

        horizontalLayout_2->addWidget(reload_layers);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer);

        exit = new QPushButton(geomorphon);
        exit->setObjectName(QString::fromUtf8("exit"));

        horizontalLayout_2->addWidget(exit);


        verticalLayout->addLayout(horizontalLayout_2);

        add_output = new QCheckBox(geomorphon);
        add_output->setObjectName(QString::fromUtf8("add_output"));

        verticalLayout->addWidget(add_output);


        retranslateUi(geomorphon);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(geomorphon);
    } // setupUi

    void retranslateUi(QWidget *geomorphon)
    {
        geomorphon->setWindowTitle(QCoreApplication::translate("geomorphon", "r.geomorphon", nullptr));
        label->setText(QString());
        label_2->setText(QCoreApplication::translate("geomorphon", " Calculates geomorphons (terrain forms) and associated geometry using machine vision approach", nullptr));
        flat->setText(QCoreApplication::translate("geomorphon", "1", nullptr));
        label_3->setText(QCoreApplication::translate("geomorphon", "Name of input elevation raster map:", nullptr));
        label_6->setText(QCoreApplication::translate("geomorphon", "Flatness threshold (degrees):", nullptr));
        output_suffix->setText(QCoreApplication::translate("geomorphon", "geomorphon", nullptr));
        label_8->setText(QCoreApplication::translate("geomorphon", "Output suffix", nullptr));
        label_5->setText(QCoreApplication::translate("geomorphon", "Inner search radius", nullptr));
        label_7->setText(QCoreApplication::translate("geomorphon", "Flatness distance, zero for none:", nullptr));
        dist->setText(QCoreApplication::translate("geomorphon", "0", nullptr));
        label_4->setText(QCoreApplication::translate("geomorphon", "Outer search radius:", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(required), QCoreApplication::translate("geomorphon", "Required", nullptr));
        flag_m->setText(QCoreApplication::translate("geomorphon", "Use meters to define search units (default is cells)", nullptr));
        flag_e->setText(QCoreApplication::translate("geomorphon", "Use extended form correction", nullptr));
        overwrite->setText(QCoreApplication::translate("geomorphon", "Allow output files to overwrite existing files", nullptr));
        derivatives->setText(QCoreApplication::translate("geomorphon", "Derivatives", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(optional), QCoreApplication::translate("geomorphon", "Optional", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(manual), QCoreApplication::translate("geomorphon", "Manual", nullptr));
        run->setText(QCoreApplication::translate("geomorphon", "Run", nullptr));
        reload_layers->setText(QCoreApplication::translate("geomorphon", "...", nullptr));
        exit->setText(QCoreApplication::translate("geomorphon", "Close", nullptr));
        add_output->setText(QCoreApplication::translate("geomorphon", "Add Geomorphic forms into layer tree", nullptr));
    } // retranslateUi

};

namespace Ui {
    class geomorphon: public Ui_geomorphon {};
} // namespace Ui

QT_END_NAMESPACE

#endif // GEOMORPHON_API_UI_UI_H
