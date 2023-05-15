/********************************************************************************
** Form generated from reading UI file 'hbc_browser_ui.ui'
**
** Created by: Qt User Interface Compiler version 5.15.8
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef HBC_BROWSER_UI_UI_H
#define HBC_BROWSER_UI_UI_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QDockWidget>
#include <QtWidgets/QDoubleSpinBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSlider>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionWizard;
    QAction *actionTools;
    QAction *actionQuit;
    QAction *actionAnnotation;
    QAction *actionGisTools;
    QAction *actionImageBrowser;
    QAction *actiongrass_settings;
    QWidget *centralwidget;
    QMenuBar *menubar;
    QMenu *menuSettings;
    QMenu *menuView;
    QMenu *menuWidgets;
    QMenu *menuType_Here;
    QStatusBar *statusbar;
    QToolBar *toolBar;
    QDockWidget *toolWidget;
    QWidget *dockWidgetContents;
    QVBoxLayout *verticalLayout_3;
    QTabWidget *tools;
    QDockWidget *imageBrowsing;
    QWidget *dockWidgetContents_2;
    QVBoxLayout *verticalLayout_2;
    QGroupBox *groupBox_6;
    QGridLayout *gridLayout_8;
    QHBoxLayout *horizontalLayout_13;
    QHBoxLayout *horizontalLayout;
    QLabel *annotation_confidence_spinBox_label;
    QDoubleSpinBox *annotation_confidence_spinBox;
    QSpacerItem *horizontalSpacer;
    QPushButton *rwd;
    QSpinBox *ImageIndexspinBox;
    QPushButton *fwd;
    QSpinBox *ImageStepspinBox;
    QCheckBox *zoomto;
    QSpinBox *range;
    QVBoxLayout *verticalLayout_14;
    QHBoxLayout *horizontalLayout_11;
    QLabel *label_4;
    QSlider *ImageIndexSlider;
    QCheckBox *link_to_image_viewer;
    QLineEdit *gisTools_logger;
    QDockWidget *gisTools;
    QWidget *dockWidgetContents_4;
    QHBoxLayout *horizontalLayout_2;
    QSplitter *gisToolSplitter;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(822, 562);
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/icons/epi.gif"), QSize(), QIcon::Normal, QIcon::Off);
        MainWindow->setWindowIcon(icon);
        actionWizard = new QAction(MainWindow);
        actionWizard->setObjectName(QString::fromUtf8("actionWizard"));
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/fa_solid/qtui/icons/fa_solid/screwdriver-wrench.svg"), QSize(), QIcon::Normal, QIcon::Off);
        actionWizard->setIcon(icon1);
        actionTools = new QAction(MainWindow);
        actionTools->setObjectName(QString::fromUtf8("actionTools"));
        actionTools->setCheckable(true);
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/fa_solid/qtui/icons/fa_solid/ruler-combined.svg"), QSize(), QIcon::Normal, QIcon::Off);
        actionTools->setIcon(icon2);
        actionQuit = new QAction(MainWindow);
        actionQuit->setObjectName(QString::fromUtf8("actionQuit"));
        QIcon icon3;
        icon3.addFile(QString::fromUtf8(":/fa_solid/qtui/icons/fa_solid/power-off.svg"), QSize(), QIcon::Normal, QIcon::Off);
        actionQuit->setIcon(icon3);
        actionAnnotation = new QAction(MainWindow);
        actionAnnotation->setObjectName(QString::fromUtf8("actionAnnotation"));
        actionAnnotation->setCheckable(true);
        QIcon icon4;
        icon4.addFile(QString::fromUtf8(":/fa_solid/qtui/icons/fa_solid/pen-to-square.svg"), QSize(), QIcon::Normal, QIcon::Off);
        actionAnnotation->setIcon(icon4);
        actionGisTools = new QAction(MainWindow);
        actionGisTools->setObjectName(QString::fromUtf8("actionGisTools"));
        actionGisTools->setCheckable(true);
        QIcon icon5;
        icon5.addFile(QString::fromUtf8(":/fa_regular/qtui/icons/fa_regular/compass.svg"), QSize(), QIcon::Normal, QIcon::Off);
        actionGisTools->setIcon(icon5);
        actionImageBrowser = new QAction(MainWindow);
        actionImageBrowser->setObjectName(QString::fromUtf8("actionImageBrowser"));
        actionImageBrowser->setCheckable(true);
        actionImageBrowser->setChecked(true);
        QIcon icon6;
        icon6.addFile(QString::fromUtf8(":/fa_solid/qtui/icons/fa_solid/image.svg"), QSize(), QIcon::Normal, QIcon::Off);
        actionImageBrowser->setIcon(icon6);
        actiongrass_settings = new QAction(MainWindow);
        actiongrass_settings->setObjectName(QString::fromUtf8("actiongrass_settings"));
        QIcon icon7;
        icon7.addFile(QString::fromUtf8(":/grass/qtui/icons/grass/grass_bold_dark.png"), QSize(), QIcon::Normal, QIcon::Off);
        actiongrass_settings->setIcon(icon7);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 822, 22));
        menuSettings = new QMenu(menubar);
        menuSettings->setObjectName(QString::fromUtf8("menuSettings"));
        menuView = new QMenu(menubar);
        menuView->setObjectName(QString::fromUtf8("menuView"));
        menuWidgets = new QMenu(menuView);
        menuWidgets->setObjectName(QString::fromUtf8("menuWidgets"));
        menuType_Here = new QMenu(menuView);
        menuType_Here->setObjectName(QString::fromUtf8("menuType_Here"));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);
        toolBar = new QToolBar(MainWindow);
        toolBar->setObjectName(QString::fromUtf8("toolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, toolBar);
        toolWidget = new QDockWidget(MainWindow);
        toolWidget->setObjectName(QString::fromUtf8("toolWidget"));
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::MinimumExpanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(toolWidget->sizePolicy().hasHeightForWidth());
        toolWidget->setSizePolicy(sizePolicy);
        toolWidget->setMinimumSize(QSize(124, 56));
        QIcon icon8;
        icon8.addFile(QString::fromUtf8(":/icons/tools.png"), QSize(), QIcon::Normal, QIcon::Off);
        toolWidget->setWindowIcon(icon8);
        toolWidget->setLayoutDirection(Qt::LeftToRight);
        toolWidget->setFeatures(QDockWidget::DockWidgetFloatable|QDockWidget::DockWidgetMovable);
        dockWidgetContents = new QWidget();
        dockWidgetContents->setObjectName(QString::fromUtf8("dockWidgetContents"));
        verticalLayout_3 = new QVBoxLayout(dockWidgetContents);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        tools = new QTabWidget(dockWidgetContents);
        tools->setObjectName(QString::fromUtf8("tools"));
        QSizePolicy sizePolicy1(QSizePolicy::MinimumExpanding, QSizePolicy::Preferred);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(tools->sizePolicy().hasHeightForWidth());
        tools->setSizePolicy(sizePolicy1);
        tools->setMinimumSize(QSize(100, 0));
        tools->setTabPosition(QTabWidget::North);
        tools->setTabShape(QTabWidget::Rounded);

        verticalLayout_3->addWidget(tools);

        toolWidget->setWidget(dockWidgetContents);
        MainWindow->addDockWidget(Qt::RightDockWidgetArea, toolWidget);
        imageBrowsing = new QDockWidget(MainWindow);
        imageBrowsing->setObjectName(QString::fromUtf8("imageBrowsing"));
        imageBrowsing->setFeatures(QDockWidget::DockWidgetFloatable|QDockWidget::DockWidgetMovable);
        dockWidgetContents_2 = new QWidget();
        dockWidgetContents_2->setObjectName(QString::fromUtf8("dockWidgetContents_2"));
        verticalLayout_2 = new QVBoxLayout(dockWidgetContents_2);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        groupBox_6 = new QGroupBox(dockWidgetContents_2);
        groupBox_6->setObjectName(QString::fromUtf8("groupBox_6"));
        QSizePolicy sizePolicy2(QSizePolicy::Preferred, QSizePolicy::Fixed);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(groupBox_6->sizePolicy().hasHeightForWidth());
        groupBox_6->setSizePolicy(sizePolicy2);
        gridLayout_8 = new QGridLayout(groupBox_6);
        gridLayout_8->setObjectName(QString::fromUtf8("gridLayout_8"));
        horizontalLayout_13 = new QHBoxLayout();
        horizontalLayout_13->setObjectName(QString::fromUtf8("horizontalLayout_13"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        annotation_confidence_spinBox_label = new QLabel(groupBox_6);
        annotation_confidence_spinBox_label->setObjectName(QString::fromUtf8("annotation_confidence_spinBox_label"));

        horizontalLayout->addWidget(annotation_confidence_spinBox_label);

        annotation_confidence_spinBox = new QDoubleSpinBox(groupBox_6);
        annotation_confidence_spinBox->setObjectName(QString::fromUtf8("annotation_confidence_spinBox"));
        annotation_confidence_spinBox->setProperty("showGroupSeparator", QVariant(false));
        annotation_confidence_spinBox->setDecimals(2);
        annotation_confidence_spinBox->setMaximum(1.000000000000000);
        annotation_confidence_spinBox->setSingleStep(0.010000000000000);
        annotation_confidence_spinBox->setValue(0.600000000000000);

        horizontalLayout->addWidget(annotation_confidence_spinBox);


        horizontalLayout_13->addLayout(horizontalLayout);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_13->addItem(horizontalSpacer);

        rwd = new QPushButton(groupBox_6);
        rwd->setObjectName(QString::fromUtf8("rwd"));
        rwd->setFocusPolicy(Qt::NoFocus);
        QIcon icon9;
        icon9.addFile(QString::fromUtf8(":/fa_solid/qtui/icons/fa_solid/backward.svg"), QSize(), QIcon::Normal, QIcon::Off);
        rwd->setIcon(icon9);
        rwd->setAutoRepeat(true);
        rwd->setAutoRepeatDelay(500);

        horizontalLayout_13->addWidget(rwd);

        ImageIndexspinBox = new QSpinBox(groupBox_6);
        ImageIndexspinBox->setObjectName(QString::fromUtf8("ImageIndexspinBox"));
        QFont font;
        font.setBold(true);
        font.setWeight(75);
        ImageIndexspinBox->setFont(font);
        ImageIndexspinBox->setMinimum(0);
        ImageIndexspinBox->setValue(0);

        horizontalLayout_13->addWidget(ImageIndexspinBox);

        fwd = new QPushButton(groupBox_6);
        fwd->setObjectName(QString::fromUtf8("fwd"));
        fwd->setFocusPolicy(Qt::NoFocus);
        QIcon icon10;
        icon10.addFile(QString::fromUtf8(":/fa_solid/qtui/icons/fa_solid/forward.svg"), QSize(), QIcon::Normal, QIcon::Off);
        fwd->setIcon(icon10);
        fwd->setAutoRepeat(true);
        fwd->setAutoRepeatDelay(500);
        fwd->setAutoDefault(false);

        horizontalLayout_13->addWidget(fwd);

        ImageStepspinBox = new QSpinBox(groupBox_6);
        ImageStepspinBox->setObjectName(QString::fromUtf8("ImageStepspinBox"));
        ImageStepspinBox->setMinimum(1);
        ImageStepspinBox->setMaximum(200);

        horizontalLayout_13->addWidget(ImageStepspinBox);

        zoomto = new QCheckBox(groupBox_6);
        zoomto->setObjectName(QString::fromUtf8("zoomto"));
        zoomto->setFocusPolicy(Qt::NoFocus);

        horizontalLayout_13->addWidget(zoomto);

        range = new QSpinBox(groupBox_6);
        range->setObjectName(QString::fromUtf8("range"));
        range->setAccelerated(true);
        range->setMaximum(900000);
        range->setStepType(QAbstractSpinBox::AdaptiveDecimalStepType);
        range->setValue(200);

        horizontalLayout_13->addWidget(range);


        gridLayout_8->addLayout(horizontalLayout_13, 1, 0, 1, 1);

        verticalLayout_14 = new QVBoxLayout();
        verticalLayout_14->setObjectName(QString::fromUtf8("verticalLayout_14"));
        horizontalLayout_11 = new QHBoxLayout();
        horizontalLayout_11->setObjectName(QString::fromUtf8("horizontalLayout_11"));
        label_4 = new QLabel(groupBox_6);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        horizontalLayout_11->addWidget(label_4);

        ImageIndexSlider = new QSlider(groupBox_6);
        ImageIndexSlider->setObjectName(QString::fromUtf8("ImageIndexSlider"));
        ImageIndexSlider->setFocusPolicy(Qt::NoFocus);
        ImageIndexSlider->setValue(0);
        ImageIndexSlider->setSliderPosition(0);
        ImageIndexSlider->setOrientation(Qt::Horizontal);
        ImageIndexSlider->setTickPosition(QSlider::TicksBelow);
        ImageIndexSlider->setTickInterval(500);

        horizontalLayout_11->addWidget(ImageIndexSlider);

        link_to_image_viewer = new QCheckBox(groupBox_6);
        link_to_image_viewer->setObjectName(QString::fromUtf8("link_to_image_viewer"));
        link_to_image_viewer->setChecked(true);

        horizontalLayout_11->addWidget(link_to_image_viewer);


        verticalLayout_14->addLayout(horizontalLayout_11);


        gridLayout_8->addLayout(verticalLayout_14, 0, 0, 1, 1);


        verticalLayout_2->addWidget(groupBox_6);

        gisTools_logger = new QLineEdit(dockWidgetContents_2);
        gisTools_logger->setObjectName(QString::fromUtf8("gisTools_logger"));

        verticalLayout_2->addWidget(gisTools_logger);

        imageBrowsing->setWidget(dockWidgetContents_2);
        MainWindow->addDockWidget(Qt::BottomDockWidgetArea, imageBrowsing);
        gisTools = new QDockWidget(MainWindow);
        gisTools->setObjectName(QString::fromUtf8("gisTools"));
        QSizePolicy sizePolicy3(QSizePolicy::Maximum, QSizePolicy::Maximum);
        sizePolicy3.setHorizontalStretch(0);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(gisTools->sizePolicy().hasHeightForWidth());
        gisTools->setSizePolicy(sizePolicy3);
        gisTools->setFeatures(QDockWidget::DockWidgetFloatable|QDockWidget::DockWidgetMovable);
        dockWidgetContents_4 = new QWidget();
        dockWidgetContents_4->setObjectName(QString::fromUtf8("dockWidgetContents_4"));
        horizontalLayout_2 = new QHBoxLayout(dockWidgetContents_4);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        gisToolSplitter = new QSplitter(dockWidgetContents_4);
        gisToolSplitter->setObjectName(QString::fromUtf8("gisToolSplitter"));
        gisToolSplitter->setOrientation(Qt::Horizontal);

        horizontalLayout_2->addWidget(gisToolSplitter);

        gisTools->setWidget(dockWidgetContents_4);
        MainWindow->addDockWidget(Qt::LeftDockWidgetArea, gisTools);

        menubar->addAction(menuSettings->menuAction());
        menubar->addAction(menuView->menuAction());
        menuSettings->addAction(actionWizard);
        menuSettings->addAction(actionQuit);
        menuView->addAction(menuWidgets->menuAction());
        menuView->addAction(menuType_Here->menuAction());
        menuWidgets->addAction(actionTools);
        menuWidgets->addAction(actionAnnotation);
        menuWidgets->addAction(actionGisTools);
        menuWidgets->addAction(actionImageBrowser);
        toolBar->addAction(actionWizard);
        toolBar->addSeparator();
        toolBar->addAction(actionImageBrowser);
        toolBar->addAction(actionTools);
        toolBar->addAction(actionGisTools);
        toolBar->addAction(actionAnnotation);
        toolBar->addSeparator();
        toolBar->addAction(actionQuit);
        toolBar->addSeparator();
        toolBar->addAction(actiongrass_settings);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "GroundTruther", nullptr));
        actionWizard->setText(QCoreApplication::translate("MainWindow", "Preferences...", nullptr));
        actionTools->setText(QCoreApplication::translate("MainWindow", "Tools", nullptr));
        actionQuit->setText(QCoreApplication::translate("MainWindow", "Quit", nullptr));
        actionAnnotation->setText(QCoreApplication::translate("MainWindow", "Image Annotation", nullptr));
#if QT_CONFIG(tooltip)
        actionAnnotation->setToolTip(QCoreApplication::translate("MainWindow", "Load and display Image object detection", nullptr));
#endif // QT_CONFIG(tooltip)
        actionGisTools->setText(QCoreApplication::translate("MainWindow", "GisTools", nullptr));
#if QT_CONFIG(tooltip)
        actionGisTools->setToolTip(QCoreApplication::translate("MainWindow", "Show GIS tools", nullptr));
#endif // QT_CONFIG(tooltip)
        actionImageBrowser->setText(QCoreApplication::translate("MainWindow", "ImageBrowser", nullptr));
        actiongrass_settings->setText(QCoreApplication::translate("MainWindow", "grass_settings", nullptr));
        menuSettings->setTitle(QCoreApplication::translate("MainWindow", "File", nullptr));
        menuView->setTitle(QCoreApplication::translate("MainWindow", "View", nullptr));
        menuWidgets->setTitle(QCoreApplication::translate("MainWindow", "Widgets", nullptr));
        menuType_Here->setTitle(QCoreApplication::translate("MainWindow", "Type Here", nullptr));
        toolBar->setWindowTitle(QCoreApplication::translate("MainWindow", "toolBar", nullptr));
        toolWidget->setWindowTitle(QCoreApplication::translate("MainWindow", "Tools", nullptr));
        imageBrowsing->setWindowTitle(QString());
        groupBox_6->setTitle(QString());
        annotation_confidence_spinBox_label->setText(QCoreApplication::translate("MainWindow", "Detection Confidence", nullptr));
#if QT_CONFIG(tooltip)
        annotation_confidence_spinBox->setToolTip(QCoreApplication::translate("MainWindow", "Image Annotation Threshold", nullptr));
#endif // QT_CONFIG(tooltip)
        rwd->setText(QString());
        fwd->setText(QString());
        zoomto->setText(QString());
        label_4->setText(QCoreApplication::translate("MainWindow", "Image Index", nullptr));
        link_to_image_viewer->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // HBC_BROWSER_UI_UI_H
