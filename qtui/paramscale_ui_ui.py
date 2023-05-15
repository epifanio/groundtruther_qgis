/********************************************************************************
** Form generated from reading UI file 'paramscale_ui.ui'
**
** Created by: Qt User Interface Compiler version 5.15.8
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef PARAMSCALE_UI_UI_H
#define PARAMSCALE_UI_UI_H

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

class Ui_paramscale
{
public:
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    QLabel *label_2;
    QTabWidget *tabWidget;
    QWidget *required;
    QGridLayout *gridLayout;
    QLabel *label_3;
    QSpacerItem *verticalSpacer_3;
    QLineEdit *output;
    QComboBox *input;
    QLabel *label_4;
    QWidget *optional;
    QGridLayout *gridLayout_3;
    QLineEdit *curvature_tolerance;
    QSpinBox *size;
    QLabel *label_5;
    QCheckBox *overwrite;
    QSpacerItem *verticalSpacer_2;
    QLineEdit *exponent;
    QLineEdit *zscale;
    QLineEdit *slope_tolerance;
    QComboBox *method;
    QCheckBox *flag_c;
    QLabel *label_6;
    QLabel *label_7;
    QLabel *label_8;
    QLabel *label_9;
    QLabel *label_10;
    QWidget *manual;
    QVBoxLayout *verticalLayout_2;
    QWebView *webView;
    QSpacerItem *verticalSpacer;
    QHBoxLayout *horizontalLayout_2;
    QPushButton *pushButton;
    QSpacerItem *horizontalSpacer;
    QPushButton *pushButton_2;
    QCheckBox *add_output;

    void setupUi(QWidget *paramscale)
    {
        if (paramscale->objectName().isEmpty())
            paramscale->setObjectName(QString::fromUtf8("paramscale"));
        paramscale->resize(574, 455);
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/grass/qtui/icons/grass/grass_location.svg"), QSize(), QIcon::Normal, QIcon::Off);
        paramscale->setWindowIcon(icon);
        verticalLayout = new QVBoxLayout(paramscale);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label = new QLabel(paramscale);
        label->setObjectName(QString::fromUtf8("label"));
        QSizePolicy sizePolicy(QSizePolicy::Minimum, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(label->sizePolicy().hasHeightForWidth());
        label->setSizePolicy(sizePolicy);
        label->setMinimumSize(QSize(40, 40));
        label->setMaximumSize(QSize(40, 40));
        label->setPixmap(QPixmap(QString::fromUtf8(":/grass/qtui/icons/grass/grass_location.svg")));

        horizontalLayout->addWidget(label);

        label_2 = new QLabel(paramscale);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setTextFormat(Qt::PlainText);
        label_2->setScaledContents(false);
        label_2->setWordWrap(true);

        horizontalLayout->addWidget(label_2);


        verticalLayout->addLayout(horizontalLayout);

        tabWidget = new QTabWidget(paramscale);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        required = new QWidget();
        required->setObjectName(QString::fromUtf8("required"));
        gridLayout = new QGridLayout(required);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label_3 = new QLabel(required);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        gridLayout->addWidget(label_3, 0, 0, 1, 1);

        verticalSpacer_3 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_3, 2, 2, 1, 1);

        output = new QLineEdit(required);
        output->setObjectName(QString::fromUtf8("output"));

        gridLayout->addWidget(output, 1, 2, 1, 1);

        input = new QComboBox(required);
        input->setObjectName(QString::fromUtf8("input"));

        gridLayout->addWidget(input, 0, 2, 1, 1);

        label_4 = new QLabel(required);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        gridLayout->addWidget(label_4, 1, 0, 1, 1);

        tabWidget->addTab(required, QString());
        optional = new QWidget();
        optional->setObjectName(QString::fromUtf8("optional"));
        gridLayout_3 = new QGridLayout(optional);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        curvature_tolerance = new QLineEdit(optional);
        curvature_tolerance->setObjectName(QString::fromUtf8("curvature_tolerance"));

        gridLayout_3->addWidget(curvature_tolerance, 4, 1, 1, 1);

        size = new QSpinBox(optional);
        size->setObjectName(QString::fromUtf8("size"));
        size->setMinimum(3);
        size->setMaximum(499);
        size->setSingleStep(2);

        gridLayout_3->addWidget(size, 5, 1, 1, 1);

        label_5 = new QLabel(optional);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        gridLayout_3->addWidget(label_5, 3, 0, 1, 1);

        overwrite = new QCheckBox(optional);
        overwrite->setObjectName(QString::fromUtf8("overwrite"));

        gridLayout_3->addWidget(overwrite, 2, 0, 1, 1);

        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_3->addItem(verticalSpacer_2, 9, 1, 1, 1);

        exponent = new QLineEdit(optional);
        exponent->setObjectName(QString::fromUtf8("exponent"));

        gridLayout_3->addWidget(exponent, 7, 1, 1, 1);

        zscale = new QLineEdit(optional);
        zscale->setObjectName(QString::fromUtf8("zscale"));

        gridLayout_3->addWidget(zscale, 8, 1, 1, 1);

        slope_tolerance = new QLineEdit(optional);
        slope_tolerance->setObjectName(QString::fromUtf8("slope_tolerance"));

        gridLayout_3->addWidget(slope_tolerance, 3, 1, 1, 1);

        method = new QComboBox(optional);
        method->addItem(QString());
        method->addItem(QString());
        method->addItem(QString());
        method->addItem(QString());
        method->addItem(QString());
        method->addItem(QString());
        method->addItem(QString());
        method->addItem(QString());
        method->addItem(QString());
        method->addItem(QString());
        method->setObjectName(QString::fromUtf8("method"));

        gridLayout_3->addWidget(method, 6, 1, 1, 1);

        flag_c = new QCheckBox(optional);
        flag_c->setObjectName(QString::fromUtf8("flag_c"));

        gridLayout_3->addWidget(flag_c, 1, 0, 1, 1);

        label_6 = new QLabel(optional);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        gridLayout_3->addWidget(label_6, 4, 0, 1, 1);

        label_7 = new QLabel(optional);
        label_7->setObjectName(QString::fromUtf8("label_7"));

        gridLayout_3->addWidget(label_7, 5, 0, 1, 1);

        label_8 = new QLabel(optional);
        label_8->setObjectName(QString::fromUtf8("label_8"));

        gridLayout_3->addWidget(label_8, 6, 0, 1, 1);

        label_9 = new QLabel(optional);
        label_9->setObjectName(QString::fromUtf8("label_9"));

        gridLayout_3->addWidget(label_9, 7, 0, 1, 1);

        label_10 = new QLabel(optional);
        label_10->setObjectName(QString::fromUtf8("label_10"));

        gridLayout_3->addWidget(label_10, 8, 0, 1, 1);

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
        pushButton = new QPushButton(paramscale);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));

        horizontalLayout_2->addWidget(pushButton);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer);

        pushButton_2 = new QPushButton(paramscale);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));

        horizontalLayout_2->addWidget(pushButton_2);


        verticalLayout->addLayout(horizontalLayout_2);

        add_output = new QCheckBox(paramscale);
        add_output->setObjectName(QString::fromUtf8("add_output"));

        verticalLayout->addWidget(add_output);


        retranslateUi(paramscale);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(paramscale);
    } // setupUi

    void retranslateUi(QWidget *paramscale)
    {
        paramscale->setWindowTitle(QCoreApplication::translate("paramscale", "r.param.scale", nullptr));
        label->setText(QString());
        label_2->setText(QCoreApplication::translate("paramscale", " Extracts terrain parameters from a DEM. Uses a multi-scale approach by taking fitting quadratic parameters to any size window (via least square)", nullptr));
        label_3->setText(QCoreApplication::translate("paramscale", "Name of input raster map:", nullptr));
        label_4->setText(QCoreApplication::translate("paramscale", "Name for output raster map containing morphometric parameter:", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(required), QCoreApplication::translate("paramscale", "Required", nullptr));
        curvature_tolerance->setText(QCoreApplication::translate("paramscale", "0.0001", nullptr));
        label_5->setText(QCoreApplication::translate("paramscale", "Slope tolerance that defines a 'flat' surface (degrees) ", nullptr));
        overwrite->setText(QCoreApplication::translate("paramscale", "Allow output files to overwrite existing files", nullptr));
        exponent->setText(QCoreApplication::translate("paramscale", "0.0", nullptr));
        zscale->setText(QCoreApplication::translate("paramscale", "1.0", nullptr));
        slope_tolerance->setText(QCoreApplication::translate("paramscale", "1.0", nullptr));
        method->setItemText(0, QCoreApplication::translate("paramscale", "elev", nullptr));
        method->setItemText(1, QCoreApplication::translate("paramscale", "slope", nullptr));
        method->setItemText(2, QCoreApplication::translate("paramscale", "aspect", nullptr));
        method->setItemText(3, QCoreApplication::translate("paramscale", "profc", nullptr));
        method->setItemText(4, QCoreApplication::translate("paramscale", "planc", nullptr));
        method->setItemText(5, QCoreApplication::translate("paramscale", "longc", nullptr));
        method->setItemText(6, QCoreApplication::translate("paramscale", "crossc", nullptr));
        method->setItemText(7, QCoreApplication::translate("paramscale", "minc", nullptr));
        method->setItemText(8, QCoreApplication::translate("paramscale", "maxic", nullptr));
        method->setItemText(9, QCoreApplication::translate("paramscale", "feature", nullptr));

        flag_c->setText(QCoreApplication::translate("paramscale", "Constain model through central window cell", nullptr));
        label_6->setText(QCoreApplication::translate("paramscale", "Curvature tolerance that defines 'planar' surface ", nullptr));
        label_7->setText(QCoreApplication::translate("paramscale", "Size of processing window (odd number only) ", nullptr));
        label_8->setText(QCoreApplication::translate("paramscale", "Morphometric parameter in 'size' window to calculate ", nullptr));
        label_9->setText(QCoreApplication::translate("paramscale", "Exponent for distance weighting (0.0-4.0) ", nullptr));
        label_10->setText(QCoreApplication::translate("paramscale", "Vertical scaling factor ", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(optional), QCoreApplication::translate("paramscale", "Optional", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(manual), QCoreApplication::translate("paramscale", "Manual", nullptr));
        pushButton->setText(QCoreApplication::translate("paramscale", "Run", nullptr));
        pushButton_2->setText(QCoreApplication::translate("paramscale", "Close", nullptr));
        add_output->setText(QCoreApplication::translate("paramscale", "Add Geomorphic forms into layer tree", nullptr));
    } // retranslateUi

};

namespace Ui {
    class paramscale: public Ui_paramscale {};
} // namespace Ui

QT_END_NAMESPACE

#endif // PARAMSCALE_UI_UI_H
