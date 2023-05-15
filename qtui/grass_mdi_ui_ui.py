/********************************************************************************
** Form generated from reading UI file 'grass_mdi_ui.ui'
**
** Created by: Qt User Interface Compiler version 5.15.8
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef GRASS_MDI_UI_UI_H
#define GRASS_MDI_UI_UI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QMdiArea>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_grass_mdi
{
public:
    QVBoxLayout *verticalLayout;
    QFrame *frame;
    QHBoxLayout *horizontalLayout;
    QComboBox *mdi_view;
    QSpacerItem *horizontalSpacer;
    QToolButton *run_geomorphon;
    QToolButton *run_paramscale;
    QToolButton *run_grm_lsi;
    QMdiArea *grassTools;

    void setupUi(QWidget *grass_mdi)
    {
        if (grass_mdi->objectName().isEmpty())
            grass_mdi->setObjectName(QString::fromUtf8("grass_mdi"));
        grass_mdi->resize(236, 179);
        verticalLayout = new QVBoxLayout(grass_mdi);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        frame = new QFrame(grass_mdi);
        frame->setObjectName(QString::fromUtf8("frame"));
        frame->setMaximumSize(QSize(16777215, 40));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        horizontalLayout = new QHBoxLayout(frame);
        horizontalLayout->setSpacing(3);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalLayout->setContentsMargins(3, 3, 3, 3);
        mdi_view = new QComboBox(frame);
        mdi_view->addItem(QString());
        mdi_view->addItem(QString());
        mdi_view->addItem(QString());
        mdi_view->addItem(QString());
        mdi_view->setObjectName(QString::fromUtf8("mdi_view"));

        horizontalLayout->addWidget(mdi_view);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);

        run_geomorphon = new QToolButton(frame);
        run_geomorphon->setObjectName(QString::fromUtf8("run_geomorphon"));
        run_geomorphon->setMaximumSize(QSize(35, 35));

        horizontalLayout->addWidget(run_geomorphon);

        run_paramscale = new QToolButton(frame);
        run_paramscale->setObjectName(QString::fromUtf8("run_paramscale"));
        run_paramscale->setMaximumSize(QSize(35, 35));

        horizontalLayout->addWidget(run_paramscale);

        run_grm_lsi = new QToolButton(frame);
        run_grm_lsi->setObjectName(QString::fromUtf8("run_grm_lsi"));
        run_grm_lsi->setMaximumSize(QSize(35, 35));

        horizontalLayout->addWidget(run_grm_lsi);


        verticalLayout->addWidget(frame);

        grassTools = new QMdiArea(grass_mdi);
        grassTools->setObjectName(QString::fromUtf8("grassTools"));
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(grassTools->sizePolicy().hasHeightForWidth());
        grassTools->setSizePolicy(sizePolicy);
        grassTools->setMinimumSize(QSize(0, 0));
        grassTools->setMaximumSize(QSize(16777215, 16777215));
        grassTools->setContextMenuPolicy(Qt::DefaultContextMenu);
        grassTools->setVerticalScrollBarPolicy(Qt::ScrollBarAsNeeded);
        grassTools->setHorizontalScrollBarPolicy(Qt::ScrollBarAsNeeded);
        grassTools->setActivationOrder(QMdiArea::StackingOrder);
        grassTools->setTabsMovable(true);

        verticalLayout->addWidget(grassTools);


        retranslateUi(grass_mdi);

        QMetaObject::connectSlotsByName(grass_mdi);
    } // setupUi

    void retranslateUi(QWidget *grass_mdi)
    {
        grass_mdi->setWindowTitle(QCoreApplication::translate("grass_mdi", "Form", nullptr));
        mdi_view->setItemText(0, QCoreApplication::translate("grass_mdi", "Tiled", nullptr));
        mdi_view->setItemText(1, QCoreApplication::translate("grass_mdi", "Cascade", nullptr));
        mdi_view->setItemText(2, QCoreApplication::translate("grass_mdi", "Minimize", nullptr));
        mdi_view->setItemText(3, QCoreApplication::translate("grass_mdi", "Close", nullptr));

        run_geomorphon->setText(QString());
        run_paramscale->setText(QString());
        run_grm_lsi->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class grass_mdi: public Ui_grass_mdi {};
} // namespace Ui

QT_END_NAMESPACE

#endif // GRASS_MDI_UI_UI_H
