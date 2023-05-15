/********************************************************************************
** Form generated from reading UI file 'groundtruther_dockwidget_base.ui'
**
** Created by: Qt User Interface Compiler version 5.15.8
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef GROUNDTRUTHER_DOCKWIDGET_BASE_UI_H
#define GROUNDTRUTHER_DOCKWIDGET_BASE_UI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDockWidget>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_GroundTrutherDockWidgetBase
{
public:
    QWidget *dockWidgetContents;
    QGridLayout *gridLayout;
    QLabel *label;

    void setupUi(QDockWidget *GroundTrutherDockWidgetBase)
    {
        if (GroundTrutherDockWidgetBase->objectName().isEmpty())
            GroundTrutherDockWidgetBase->setObjectName(QString::fromUtf8("GroundTrutherDockWidgetBase"));
        GroundTrutherDockWidgetBase->resize(232, 141);
        dockWidgetContents = new QWidget();
        dockWidgetContents->setObjectName(QString::fromUtf8("dockWidgetContents"));
        gridLayout = new QGridLayout(dockWidgetContents);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label = new QLabel(dockWidgetContents);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout->addWidget(label, 0, 0, 1, 1);

        GroundTrutherDockWidgetBase->setWidget(dockWidgetContents);

        retranslateUi(GroundTrutherDockWidgetBase);

        QMetaObject::connectSlotsByName(GroundTrutherDockWidgetBase);
    } // setupUi

    void retranslateUi(QDockWidget *GroundTrutherDockWidgetBase)
    {
        GroundTrutherDockWidgetBase->setWindowTitle(QCoreApplication::translate("GroundTrutherDockWidgetBase", "GroundTruther", nullptr));
        label->setText(QCoreApplication::translate("GroundTrutherDockWidgetBase", "Replace this QLabel\n"
"with the desired\n"
"plugin content.", nullptr));
    } // retranslateUi

};

namespace Ui {
    class GroundTrutherDockWidgetBase: public Ui_GroundTrutherDockWidgetBase {};
} // namespace Ui

QT_END_NAMESPACE

#endif // GROUNDTRUTHER_DOCKWIDGET_BASE_UI_H
