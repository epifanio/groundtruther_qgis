/********************************************************************************
** Form generated from reading UI file 'kmlsave_ui.ui'
**
** Created by: Qt User Interface Compiler version 5.15.8
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef KMLSAVE_UI_UI_H
#define KMLSAVE_UI_UI_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDoubleSpinBox>
#include <QtWidgets/QFontComboBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Form
{
public:
    QVBoxLayout *verticalLayout_3;
    QScrollArea *scrollArea;
    QWidget *scrollAreaWidgetContents;
    QVBoxLayout *verticalLayout_6;
    QSplitter *splitter;
    QWidget *verticalLayoutWidget;
    QVBoxLayout *verticalLayout_2;
    QScrollArea *scrollArea_2;
    QWidget *scrollAreaWidgetContents_2;
    QVBoxLayout *verticalLayout_5;
    QGroupBox *kml_marker;
    QVBoxLayout *verticalLayout_4;
    QGridLayout *gridLayout;
    QHBoxLayout *horizontalLayout_3;
    QLineEdit *longitude;
    QLineEdit *latitude;
    QSpacerItem *horizontalSpacer_8;
    QCheckBox *lock_location;
    QLineEdit *kmlname;
    QHBoxLayout *horizontalLayout_9;
    QSpinBox *LineWidth;
    QSpacerItem *horizontalSpacer_5;
    QHBoxLayout *horizontalLayout_11;
    QToolButton *polygoncolor;
    QLineEdit *polygoncolorlabel;
    QSpinBox *PolygonAlpha;
    QSpacerItem *horizontalSpacer_7;
    QLabel *label_2;
    QComboBox *SelectIcon;
    QHBoxLayout *horizontalLayout_6;
    QCheckBox *Tessellate;
    QSpacerItem *horizontalSpacer_10;
    QComboBox *altitudeMode;
    QLabel *label;
    QHBoxLayout *horizontalLayout_7;
    QToolButton *labelcolor;
    QLineEdit *labelcolorlabel;
    QSpinBox *LabelAlpha;
    QSpacerItem *horizontalSpacer_3;
    QLabel *Tessellatelabel;
    QLabel *Extrudelabel;
    QLabel *label_5;
    QHBoxLayout *horizontalLayout_4;
    QCheckBox *Extrude;
    QDoubleSpinBox *Offset;
    QSpacerItem *horizontalSpacer_13;
    QHBoxLayout *horizontalLayout_10;
    QToolButton *linecolor;
    QLineEdit *linecolorlabel;
    QSpinBox *LineAlpha;
    QSpacerItem *horizontalSpacer_6;
    QLabel *label_3;
    QLabel *LineWidthlabel;
    QLabel *Iconlabel;
    QLineEdit *kmllabel;
    QHBoxLayout *horizontalLayout_5;
    QLineEdit *Zoom;
    QLineEdit *Range;
    QLineEdit *Roll;
    QLineEdit *Pitch;
    QLineEdit *Head;
    QSpacerItem *horizontalSpacer_9;
    QLabel *label_4;
    QLabel *label_6;
    QLabel *label_8;
    QSpacerItem *verticalSpacer;
    QGroupBox *groupBox_2;
    QVBoxLayout *verticalLayout;
    QLabel *label_7;
    QFrame *line;
    QGridLayout *gridLayout_2;
    QSpacerItem *horizontalSpacer;
    QToolButton *editor_italic;
    QToolButton *editor_align_justify;
    QToolButton *editor_undo;
    QToolButton *editor_redo;
    QToolButton *editor_save;
    QToolButton *editor_paste;
    QToolButton *editor_align_center;
    QToolButton *editor_align_left;
    QToolButton *editor_copy;
    QToolButton *editor_underline;
    QToolButton *editor_bold;
    QToolButton *editor_align_right;
    QToolButton *editor_select_all;
    QToolButton *editor_cut;
    QHBoxLayout *horizontalLayout;
    QFontComboBox *fontComboBox;
    QSpinBox *fontsize;
    QPushButton *addimage;
    QPushButton *addlink;
    QToolButton *get_2dgraph;
    QToolButton *get_3dgraph;
    QToolButton *get_selected_points;
    QPushButton *clean;
    QSpacerItem *horizontalSpacer_2;
    QTextEdit *description;
    QHBoxLayout *horizontalLayout_8;
    QSpacerItem *horizontalSpacer_4;
    QPushButton *update;
    QSpacerItem *horizontalSpacer_16;
    QPushButton *save;
    QSpacerItem *horizontalSpacer_17;
    QPushButton *opendir;
    QSpacerItem *horizontalSpacer_15;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName(QString::fromUtf8("Form"));
        Form->resize(641, 856);
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/icons/element-vector.gif"), QSize(), QIcon::Normal, QIcon::Off);
        Form->setWindowIcon(icon);
        verticalLayout_3 = new QVBoxLayout(Form);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        scrollArea = new QScrollArea(Form);
        scrollArea->setObjectName(QString::fromUtf8("scrollArea"));
        scrollArea->setWidgetResizable(true);
        scrollAreaWidgetContents = new QWidget();
        scrollAreaWidgetContents->setObjectName(QString::fromUtf8("scrollAreaWidgetContents"));
        scrollAreaWidgetContents->setGeometry(QRect(0, 0, 621, 797));
        verticalLayout_6 = new QVBoxLayout(scrollAreaWidgetContents);
        verticalLayout_6->setObjectName(QString::fromUtf8("verticalLayout_6"));
        splitter = new QSplitter(scrollAreaWidgetContents);
        splitter->setObjectName(QString::fromUtf8("splitter"));
        splitter->setOrientation(Qt::Vertical);
        verticalLayoutWidget = new QWidget(splitter);
        verticalLayoutWidget->setObjectName(QString::fromUtf8("verticalLayoutWidget"));
        verticalLayout_2 = new QVBoxLayout(verticalLayoutWidget);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        verticalLayout_2->setContentsMargins(0, 0, 0, 0);
        scrollArea_2 = new QScrollArea(verticalLayoutWidget);
        scrollArea_2->setObjectName(QString::fromUtf8("scrollArea_2"));
        scrollArea_2->setWidgetResizable(true);
        scrollAreaWidgetContents_2 = new QWidget();
        scrollAreaWidgetContents_2->setObjectName(QString::fromUtf8("scrollAreaWidgetContents_2"));
        scrollAreaWidgetContents_2->setGeometry(QRect(0, 0, 585, 521));
        verticalLayout_5 = new QVBoxLayout(scrollAreaWidgetContents_2);
        verticalLayout_5->setObjectName(QString::fromUtf8("verticalLayout_5"));
        kml_marker = new QGroupBox(scrollAreaWidgetContents_2);
        kml_marker->setObjectName(QString::fromUtf8("kml_marker"));
        QFont font;
        font.setBold(false);
        font.setWeight(50);
        kml_marker->setFont(font);
        kml_marker->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);
        kml_marker->setFlat(false);
        verticalLayout_4 = new QVBoxLayout(kml_marker);
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        gridLayout = new QGridLayout();
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        longitude = new QLineEdit(kml_marker);
        longitude->setObjectName(QString::fromUtf8("longitude"));
        longitude->setMaximumSize(QSize(180, 16777215));
        longitude->setStyleSheet(QString::fromUtf8(""));
        longitude->setAlignment(Qt::AlignCenter);

        horizontalLayout_3->addWidget(longitude);

        latitude = new QLineEdit(kml_marker);
        latitude->setObjectName(QString::fromUtf8("latitude"));
        latitude->setMaximumSize(QSize(180, 16777215));
        latitude->setStyleSheet(QString::fromUtf8(""));
        latitude->setAlignment(Qt::AlignCenter);

        horizontalLayout_3->addWidget(latitude);

        horizontalSpacer_8 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer_8);

        lock_location = new QCheckBox(kml_marker);
        lock_location->setObjectName(QString::fromUtf8("lock_location"));

        horizontalLayout_3->addWidget(lock_location);


        gridLayout->addLayout(horizontalLayout_3, 14, 2, 1, 2);

        kmlname = new QLineEdit(kml_marker);
        kmlname->setObjectName(QString::fromUtf8("kmlname"));
        kmlname->setMaximumSize(QSize(290, 16777215));
        kmlname->setStyleSheet(QString::fromUtf8(""));

        gridLayout->addWidget(kmlname, 1, 3, 1, 1);

        horizontalLayout_9 = new QHBoxLayout();
        horizontalLayout_9->setObjectName(QString::fromUtf8("horizontalLayout_9"));
        LineWidth = new QSpinBox(kml_marker);
        LineWidth->setObjectName(QString::fromUtf8("LineWidth"));
        LineWidth->setStyleSheet(QString::fromUtf8(""));

        horizontalLayout_9->addWidget(LineWidth);

        horizontalSpacer_5 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_9->addItem(horizontalSpacer_5);


        gridLayout->addLayout(horizontalLayout_9, 5, 3, 1, 1);

        horizontalLayout_11 = new QHBoxLayout();
        horizontalLayout_11->setObjectName(QString::fromUtf8("horizontalLayout_11"));
        polygoncolor = new QToolButton(kml_marker);
        polygoncolor->setObjectName(QString::fromUtf8("polygoncolor"));
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(polygoncolor->sizePolicy().hasHeightForWidth());
        polygoncolor->setSizePolicy(sizePolicy);
        polygoncolor->setMinimumSize(QSize(60, 0));
        polygoncolor->setMaximumSize(QSize(60, 16777215));
        polygoncolor->setStyleSheet(QString::fromUtf8(""));

        horizontalLayout_11->addWidget(polygoncolor);

        polygoncolorlabel = new QLineEdit(kml_marker);
        polygoncolorlabel->setObjectName(QString::fromUtf8("polygoncolorlabel"));
        sizePolicy.setHeightForWidth(polygoncolorlabel->sizePolicy().hasHeightForWidth());
        polygoncolorlabel->setSizePolicy(sizePolicy);
        polygoncolorlabel->setMinimumSize(QSize(60, 0));
        polygoncolorlabel->setMaximumSize(QSize(80, 16777215));
        polygoncolorlabel->setStyleSheet(QString::fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
""));
        polygoncolorlabel->setReadOnly(true);

        horizontalLayout_11->addWidget(polygoncolorlabel);

        PolygonAlpha = new QSpinBox(kml_marker);
        PolygonAlpha->setObjectName(QString::fromUtf8("PolygonAlpha"));
        sizePolicy.setHeightForWidth(PolygonAlpha->sizePolicy().hasHeightForWidth());
        PolygonAlpha->setSizePolicy(sizePolicy);
        PolygonAlpha->setMinimumSize(QSize(50, 0));
        PolygonAlpha->setMaximumSize(QSize(50, 16777215));
        PolygonAlpha->setStyleSheet(QString::fromUtf8(""));
        PolygonAlpha->setMaximum(255);
        PolygonAlpha->setValue(255);

        horizontalLayout_11->addWidget(PolygonAlpha);

        horizontalSpacer_7 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_11->addItem(horizontalSpacer_7);


        gridLayout->addLayout(horizontalLayout_11, 11, 2, 1, 2);

        label_2 = new QLabel(kml_marker);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout->addWidget(label_2, 2, 2, 1, 1);

        SelectIcon = new QComboBox(kml_marker);
        SelectIcon->addItem(QString());
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/icons/blue_circle.png"), QSize(), QIcon::Normal, QIcon::Off);
        SelectIcon->addItem(icon1, QString());
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/icons/green_circle.png"), QSize(), QIcon::Normal, QIcon::Off);
        SelectIcon->addItem(icon2, QString());
        QIcon icon3;
        icon3.addFile(QString::fromUtf8(":/icons/red_circle.png"), QSize(), QIcon::Normal, QIcon::Off);
        SelectIcon->addItem(icon3, QString());
        QIcon icon4;
        icon4.addFile(QString::fromUtf8(":/icons/yellow_circle.png"), QSize(), QIcon::Normal, QIcon::Off);
        SelectIcon->addItem(icon4, QString());
        SelectIcon->setObjectName(QString::fromUtf8("SelectIcon"));
        sizePolicy.setHeightForWidth(SelectIcon->sizePolicy().hasHeightForWidth());
        SelectIcon->setSizePolicy(sizePolicy);
        SelectIcon->setMinimumSize(QSize(120, 0));
        SelectIcon->setMaximumSize(QSize(120, 16777215));

        gridLayout->addWidget(SelectIcon, 3, 3, 1, 1);

        horizontalLayout_6 = new QHBoxLayout();
        horizontalLayout_6->setObjectName(QString::fromUtf8("horizontalLayout_6"));
        Tessellate = new QCheckBox(kml_marker);
        Tessellate->setObjectName(QString::fromUtf8("Tessellate"));
        Tessellate->setLayoutDirection(Qt::LeftToRight);

        horizontalLayout_6->addWidget(Tessellate);

        horizontalSpacer_10 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_6->addItem(horizontalSpacer_10);


        gridLayout->addLayout(horizontalLayout_6, 7, 3, 1, 1);

        altitudeMode = new QComboBox(kml_marker);
        altitudeMode->addItem(QString());
        altitudeMode->addItem(QString());
        altitudeMode->addItem(QString());
        altitudeMode->setObjectName(QString::fromUtf8("altitudeMode"));
        sizePolicy.setHeightForWidth(altitudeMode->sizePolicy().hasHeightForWidth());
        altitudeMode->setSizePolicy(sizePolicy);
        altitudeMode->setMaximumSize(QSize(120, 16777215));

        gridLayout->addWidget(altitudeMode, 4, 3, 1, 1);

        label = new QLabel(kml_marker);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout->addWidget(label, 1, 2, 1, 1);

        horizontalLayout_7 = new QHBoxLayout();
        horizontalLayout_7->setObjectName(QString::fromUtf8("horizontalLayout_7"));
        labelcolor = new QToolButton(kml_marker);
        labelcolor->setObjectName(QString::fromUtf8("labelcolor"));
        labelcolor->setMinimumSize(QSize(60, 0));
        labelcolor->setMaximumSize(QSize(60, 16777215));
        labelcolor->setStyleSheet(QString::fromUtf8(""));

        horizontalLayout_7->addWidget(labelcolor);

        labelcolorlabel = new QLineEdit(kml_marker);
        labelcolorlabel->setObjectName(QString::fromUtf8("labelcolorlabel"));
        sizePolicy.setHeightForWidth(labelcolorlabel->sizePolicy().hasHeightForWidth());
        labelcolorlabel->setSizePolicy(sizePolicy);
        labelcolorlabel->setMinimumSize(QSize(60, 0));
        labelcolorlabel->setMaximumSize(QSize(80, 16777215));
        labelcolorlabel->setStyleSheet(QString::fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
""));
        labelcolorlabel->setReadOnly(true);

        horizontalLayout_7->addWidget(labelcolorlabel);

        LabelAlpha = new QSpinBox(kml_marker);
        LabelAlpha->setObjectName(QString::fromUtf8("LabelAlpha"));
        sizePolicy.setHeightForWidth(LabelAlpha->sizePolicy().hasHeightForWidth());
        LabelAlpha->setSizePolicy(sizePolicy);
        LabelAlpha->setMinimumSize(QSize(50, 0));
        LabelAlpha->setMaximumSize(QSize(50, 16777215));
        LabelAlpha->setStyleSheet(QString::fromUtf8(""));
        LabelAlpha->setMaximum(255);
        LabelAlpha->setValue(255);

        horizontalLayout_7->addWidget(LabelAlpha);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_7->addItem(horizontalSpacer_3);


        gridLayout->addLayout(horizontalLayout_7, 9, 2, 1, 2);

        Tessellatelabel = new QLabel(kml_marker);
        Tessellatelabel->setObjectName(QString::fromUtf8("Tessellatelabel"));

        gridLayout->addWidget(Tessellatelabel, 7, 2, 1, 1);

        Extrudelabel = new QLabel(kml_marker);
        Extrudelabel->setObjectName(QString::fromUtf8("Extrudelabel"));

        gridLayout->addWidget(Extrudelabel, 6, 2, 1, 1);

        label_5 = new QLabel(kml_marker);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setTextFormat(Qt::RichText);

        gridLayout->addWidget(label_5, 8, 0, 1, 1);

        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        Extrude = new QCheckBox(kml_marker);
        Extrude->setObjectName(QString::fromUtf8("Extrude"));

        horizontalLayout_4->addWidget(Extrude);

        Offset = new QDoubleSpinBox(kml_marker);
        Offset->setObjectName(QString::fromUtf8("Offset"));
        Offset->setStyleSheet(QString::fromUtf8(""));

        horizontalLayout_4->addWidget(Offset);

        horizontalSpacer_13 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_4->addItem(horizontalSpacer_13);


        gridLayout->addLayout(horizontalLayout_4, 6, 3, 1, 1);

        horizontalLayout_10 = new QHBoxLayout();
        horizontalLayout_10->setObjectName(QString::fromUtf8("horizontalLayout_10"));
        linecolor = new QToolButton(kml_marker);
        linecolor->setObjectName(QString::fromUtf8("linecolor"));
        sizePolicy.setHeightForWidth(linecolor->sizePolicy().hasHeightForWidth());
        linecolor->setSizePolicy(sizePolicy);
        linecolor->setMinimumSize(QSize(60, 0));
        linecolor->setAcceptDrops(false);
        linecolor->setAutoFillBackground(false);
        linecolor->setStyleSheet(QString::fromUtf8(""));
        linecolor->setAutoRaise(false);

        horizontalLayout_10->addWidget(linecolor);

        linecolorlabel = new QLineEdit(kml_marker);
        linecolorlabel->setObjectName(QString::fromUtf8("linecolorlabel"));
        sizePolicy.setHeightForWidth(linecolorlabel->sizePolicy().hasHeightForWidth());
        linecolorlabel->setSizePolicy(sizePolicy);
        linecolorlabel->setMinimumSize(QSize(60, 0));
        linecolorlabel->setMaximumSize(QSize(80, 16777215));
        linecolorlabel->setStyleSheet(QString::fromUtf8("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: rgb(231, 231, 231);\n"
" }\n"
""));
        linecolorlabel->setReadOnly(true);

        horizontalLayout_10->addWidget(linecolorlabel);

        LineAlpha = new QSpinBox(kml_marker);
        LineAlpha->setObjectName(QString::fromUtf8("LineAlpha"));
        sizePolicy.setHeightForWidth(LineAlpha->sizePolicy().hasHeightForWidth());
        LineAlpha->setSizePolicy(sizePolicy);
        LineAlpha->setMinimumSize(QSize(50, 0));
        LineAlpha->setMaximumSize(QSize(50, 16777215));
        LineAlpha->setStyleSheet(QString::fromUtf8(""));
        LineAlpha->setMaximum(255);
        LineAlpha->setValue(255);

        horizontalLayout_10->addWidget(LineAlpha);

        horizontalSpacer_6 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_10->addItem(horizontalSpacer_6);


        gridLayout->addLayout(horizontalLayout_10, 10, 2, 1, 2);

        label_3 = new QLabel(kml_marker);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        gridLayout->addWidget(label_3, 4, 2, 1, 1);

        LineWidthlabel = new QLabel(kml_marker);
        LineWidthlabel->setObjectName(QString::fromUtf8("LineWidthlabel"));

        gridLayout->addWidget(LineWidthlabel, 5, 2, 1, 1);

        Iconlabel = new QLabel(kml_marker);
        Iconlabel->setObjectName(QString::fromUtf8("Iconlabel"));

        gridLayout->addWidget(Iconlabel, 3, 2, 1, 1);

        kmllabel = new QLineEdit(kml_marker);
        kmllabel->setObjectName(QString::fromUtf8("kmllabel"));
        kmllabel->setMaximumSize(QSize(290, 16777215));
        kmllabel->setStyleSheet(QString::fromUtf8(""));

        gridLayout->addWidget(kmllabel, 2, 3, 1, 1);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        Zoom = new QLineEdit(kml_marker);
        Zoom->setObjectName(QString::fromUtf8("Zoom"));
        Zoom->setMaximumSize(QSize(180, 16777215));
        Zoom->setStyleSheet(QString::fromUtf8(""));
        Zoom->setAlignment(Qt::AlignCenter);

        horizontalLayout_5->addWidget(Zoom);

        Range = new QLineEdit(kml_marker);
        Range->setObjectName(QString::fromUtf8("Range"));
        Range->setMaximumSize(QSize(180, 16777215));
        Range->setStyleSheet(QString::fromUtf8(""));
        Range->setAlignment(Qt::AlignCenter);

        horizontalLayout_5->addWidget(Range);

        Roll = new QLineEdit(kml_marker);
        Roll->setObjectName(QString::fromUtf8("Roll"));
        sizePolicy.setHeightForWidth(Roll->sizePolicy().hasHeightForWidth());
        Roll->setSizePolicy(sizePolicy);
        Roll->setMinimumSize(QSize(50, 0));
        Roll->setMaximumSize(QSize(50, 16777215));
        Roll->setStyleSheet(QString::fromUtf8(""));
        Roll->setAlignment(Qt::AlignCenter);

        horizontalLayout_5->addWidget(Roll);

        Pitch = new QLineEdit(kml_marker);
        Pitch->setObjectName(QString::fromUtf8("Pitch"));
        sizePolicy.setHeightForWidth(Pitch->sizePolicy().hasHeightForWidth());
        Pitch->setSizePolicy(sizePolicy);
        Pitch->setMinimumSize(QSize(50, 0));
        Pitch->setMaximumSize(QSize(50, 16777215));
        Pitch->setStyleSheet(QString::fromUtf8(""));
        Pitch->setAlignment(Qt::AlignCenter);

        horizontalLayout_5->addWidget(Pitch);

        Head = new QLineEdit(kml_marker);
        Head->setObjectName(QString::fromUtf8("Head"));
        sizePolicy.setHeightForWidth(Head->sizePolicy().hasHeightForWidth());
        Head->setSizePolicy(sizePolicy);
        Head->setMinimumSize(QSize(50, 0));
        Head->setMaximumSize(QSize(50, 16777215));
        Head->setStyleSheet(QString::fromUtf8(""));
        Head->setAlignment(Qt::AlignCenter);

        horizontalLayout_5->addWidget(Head);

        horizontalSpacer_9 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_5->addItem(horizontalSpacer_9);


        gridLayout->addLayout(horizontalLayout_5, 15, 2, 1, 2);

        label_4 = new QLabel(kml_marker);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setTextFormat(Qt::RichText);

        gridLayout->addWidget(label_4, 0, 0, 1, 1);

        label_6 = new QLabel(kml_marker);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        gridLayout->addWidget(label_6, 13, 0, 1, 1);

        label_8 = new QLabel(kml_marker);
        label_8->setObjectName(QString::fromUtf8("label_8"));

        gridLayout->addWidget(label_8, 15, 0, 1, 1);


        verticalLayout_4->addLayout(gridLayout);


        verticalLayout_5->addWidget(kml_marker);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_5->addItem(verticalSpacer);

        scrollArea_2->setWidget(scrollAreaWidgetContents_2);

        verticalLayout_2->addWidget(scrollArea_2);

        splitter->addWidget(verticalLayoutWidget);
        groupBox_2 = new QGroupBox(splitter);
        groupBox_2->setObjectName(QString::fromUtf8("groupBox_2"));
        groupBox_2->setAlignment(Qt::AlignCenter);
        groupBox_2->setFlat(false);
        verticalLayout = new QVBoxLayout(groupBox_2);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        label_7 = new QLabel(groupBox_2);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);

        verticalLayout->addWidget(label_7);

        line = new QFrame(groupBox_2);
        line->setObjectName(QString::fromUtf8("line"));
        line->setFrameShape(QFrame::HLine);
        line->setFrameShadow(QFrame::Sunken);

        verticalLayout->addWidget(line);

        gridLayout_2 = new QGridLayout();
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_2->addItem(horizontalSpacer, 0, 22, 1, 1);

        editor_italic = new QToolButton(groupBox_2);
        editor_italic->setObjectName(QString::fromUtf8("editor_italic"));
        editor_italic->setMinimumSize(QSize(26, 26));
        editor_italic->setMaximumSize(QSize(26, 26));
        QIcon icon5;
        icon5.addFile(QString::fromUtf8(":/editor/qtui/icons/txt_editor/italic.png"), QSize(), QIcon::Normal, QIcon::Off);
        editor_italic->setIcon(icon5);

        gridLayout_2->addWidget(editor_italic, 0, 11, 1, 1);

        editor_align_justify = new QToolButton(groupBox_2);
        editor_align_justify->setObjectName(QString::fromUtf8("editor_align_justify"));
        editor_align_justify->setMinimumSize(QSize(26, 26));
        editor_align_justify->setMaximumSize(QSize(26, 26));
        QIcon icon6;
        icon6.addFile(QString::fromUtf8(":/editor/qtui/icons/txt_editor/align-justify.png"), QSize(), QIcon::Normal, QIcon::Off);
        editor_align_justify->setIcon(icon6);

        gridLayout_2->addWidget(editor_align_justify, 0, 17, 1, 1);

        editor_undo = new QToolButton(groupBox_2);
        editor_undo->setObjectName(QString::fromUtf8("editor_undo"));
        editor_undo->setMinimumSize(QSize(26, 26));
        editor_undo->setMaximumSize(QSize(26, 26));
        QIcon icon7;
        icon7.addFile(QString::fromUtf8(":/editor/qtui/icons/txt_editor/undo.png"), QSize(), QIcon::Normal, QIcon::Off);
        editor_undo->setIcon(icon7);

        gridLayout_2->addWidget(editor_undo, 0, 7, 1, 1);

        editor_redo = new QToolButton(groupBox_2);
        editor_redo->setObjectName(QString::fromUtf8("editor_redo"));
        editor_redo->setMinimumSize(QSize(26, 26));
        editor_redo->setMaximumSize(QSize(26, 26));
        QIcon icon8;
        icon8.addFile(QString::fromUtf8(":/editor/qtui/icons/txt_editor/redo.png"), QSize(), QIcon::Normal, QIcon::Off);
        editor_redo->setIcon(icon8);

        gridLayout_2->addWidget(editor_redo, 0, 8, 1, 1);

        editor_save = new QToolButton(groupBox_2);
        editor_save->setObjectName(QString::fromUtf8("editor_save"));
        editor_save->setMinimumSize(QSize(26, 26));
        editor_save->setMaximumSize(QSize(26, 26));
        QIcon icon9;
        icon9.addFile(QString::fromUtf8(":/editor/qtui/icons/txt_editor/print.png"), QSize(), QIcon::Normal, QIcon::Off);
        editor_save->setIcon(icon9);

        gridLayout_2->addWidget(editor_save, 0, 18, 1, 1);

        editor_paste = new QToolButton(groupBox_2);
        editor_paste->setObjectName(QString::fromUtf8("editor_paste"));
        editor_paste->setMinimumSize(QSize(26, 26));
        editor_paste->setMaximumSize(QSize(26, 26));
        QIcon icon10;
        icon10.addFile(QString::fromUtf8(":/editor/qtui/icons/txt_editor/paste.png"), QSize(), QIcon::Normal, QIcon::Off);
        editor_paste->setIcon(icon10);

        gridLayout_2->addWidget(editor_paste, 0, 2, 1, 1);

        editor_align_center = new QToolButton(groupBox_2);
        editor_align_center->setObjectName(QString::fromUtf8("editor_align_center"));
        editor_align_center->setMinimumSize(QSize(26, 26));
        editor_align_center->setMaximumSize(QSize(26, 26));
        QIcon icon11;
        icon11.addFile(QString::fromUtf8(":/editor/qtui/icons/txt_editor/align-center.png"), QSize(), QIcon::Normal, QIcon::Off);
        editor_align_center->setIcon(icon11);

        gridLayout_2->addWidget(editor_align_center, 0, 16, 1, 1);

        editor_align_left = new QToolButton(groupBox_2);
        editor_align_left->setObjectName(QString::fromUtf8("editor_align_left"));
        editor_align_left->setMinimumSize(QSize(26, 26));
        editor_align_left->setMaximumSize(QSize(26, 26));
        QIcon icon12;
        icon12.addFile(QString::fromUtf8(":/editor/qtui/icons/txt_editor/align-left.png"), QSize(), QIcon::Normal, QIcon::Off);
        editor_align_left->setIcon(icon12);

        gridLayout_2->addWidget(editor_align_left, 0, 14, 1, 1);

        editor_copy = new QToolButton(groupBox_2);
        editor_copy->setObjectName(QString::fromUtf8("editor_copy"));
        editor_copy->setMinimumSize(QSize(26, 26));
        editor_copy->setMaximumSize(QSize(26, 26));
        QIcon icon13;
        icon13.addFile(QString::fromUtf8(":/editor/qtui/icons/txt_editor/copy.png"), QSize(), QIcon::Normal, QIcon::Off);
        editor_copy->setIcon(icon13);

        gridLayout_2->addWidget(editor_copy, 0, 0, 1, 1);

        editor_underline = new QToolButton(groupBox_2);
        editor_underline->setObjectName(QString::fromUtf8("editor_underline"));
        editor_underline->setMinimumSize(QSize(26, 26));
        editor_underline->setMaximumSize(QSize(26, 26));
        QIcon icon14;
        icon14.addFile(QString::fromUtf8(":/editor/qtui/icons/txt_editor/underline.png"), QSize(), QIcon::Normal, QIcon::Off);
        editor_underline->setIcon(icon14);

        gridLayout_2->addWidget(editor_underline, 0, 13, 1, 1);

        editor_bold = new QToolButton(groupBox_2);
        editor_bold->setObjectName(QString::fromUtf8("editor_bold"));
        editor_bold->setMinimumSize(QSize(26, 26));
        editor_bold->setMaximumSize(QSize(26, 26));
        QIcon icon15;
        icon15.addFile(QString::fromUtf8(":/editor/qtui/icons/txt_editor/bold.png"), QSize(), QIcon::Normal, QIcon::Off);
        editor_bold->setIcon(icon15);

        gridLayout_2->addWidget(editor_bold, 0, 10, 1, 1);

        editor_align_right = new QToolButton(groupBox_2);
        editor_align_right->setObjectName(QString::fromUtf8("editor_align_right"));
        editor_align_right->setMinimumSize(QSize(26, 26));
        editor_align_right->setMaximumSize(QSize(26, 26));
        QIcon icon16;
        icon16.addFile(QString::fromUtf8(":/editor/qtui/icons/txt_editor/align-right.png"), QSize(), QIcon::Normal, QIcon::Off);
        editor_align_right->setIcon(icon16);

        gridLayout_2->addWidget(editor_align_right, 0, 15, 1, 1);

        editor_select_all = new QToolButton(groupBox_2);
        editor_select_all->setObjectName(QString::fromUtf8("editor_select_all"));
        editor_select_all->setMinimumSize(QSize(26, 26));
        editor_select_all->setMaximumSize(QSize(26, 26));
        QIcon icon17;
        icon17.addFile(QString::fromUtf8(":/fa_solid/qtui/icons/fa_solid/maximize.svg"), QSize(), QIcon::Normal, QIcon::Off);
        editor_select_all->setIcon(icon17);

        gridLayout_2->addWidget(editor_select_all, 0, 9, 1, 1);

        editor_cut = new QToolButton(groupBox_2);
        editor_cut->setObjectName(QString::fromUtf8("editor_cut"));
        editor_cut->setMinimumSize(QSize(26, 26));
        editor_cut->setMaximumSize(QSize(26, 26));
        QIcon icon18;
        icon18.addFile(QString::fromUtf8(":/editor/qtui/icons/txt_editor/cut.png"), QSize(), QIcon::Normal, QIcon::Off);
        editor_cut->setIcon(icon18);

        gridLayout_2->addWidget(editor_cut, 0, 1, 1, 1);


        verticalLayout->addLayout(gridLayout_2);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        fontComboBox = new QFontComboBox(groupBox_2);
        fontComboBox->setObjectName(QString::fromUtf8("fontComboBox"));
        QSizePolicy sizePolicy1(QSizePolicy::Minimum, QSizePolicy::Minimum);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(fontComboBox->sizePolicy().hasHeightForWidth());
        fontComboBox->setSizePolicy(sizePolicy1);
        fontComboBox->setMinimumSize(QSize(120, 0));
        fontComboBox->setMaximumSize(QSize(240, 16777215));
        QFont font1;
        font1.setBold(false);
        font1.setItalic(false);
        font1.setUnderline(false);
        font1.setWeight(50);
        fontComboBox->setFont(font1);
        fontComboBox->setEditable(false);

        horizontalLayout->addWidget(fontComboBox);

        fontsize = new QSpinBox(groupBox_2);
        fontsize->setObjectName(QString::fromUtf8("fontsize"));
        fontsize->setMinimum(3);
        fontsize->setMaximum(300);
        fontsize->setValue(11);

        horizontalLayout->addWidget(fontsize);

        addimage = new QPushButton(groupBox_2);
        addimage->setObjectName(QString::fromUtf8("addimage"));
        sizePolicy.setHeightForWidth(addimage->sizePolicy().hasHeightForWidth());
        addimage->setSizePolicy(sizePolicy);
        addimage->setMinimumSize(QSize(26, 26));
        addimage->setMaximumSize(QSize(26, 26));
        addimage->setStyleSheet(QString::fromUtf8(""));
        QIcon icon19;
        icon19.addFile(QString::fromUtf8(":/fa_solid/qtui/icons/fa_solid/image.svg"), QSize(), QIcon::Normal, QIcon::Off);
        addimage->setIcon(icon19);

        horizontalLayout->addWidget(addimage);

        addlink = new QPushButton(groupBox_2);
        addlink->setObjectName(QString::fromUtf8("addlink"));
        sizePolicy.setHeightForWidth(addlink->sizePolicy().hasHeightForWidth());
        addlink->setSizePolicy(sizePolicy);
        addlink->setMinimumSize(QSize(26, 26));
        addlink->setMaximumSize(QSize(26, 26));
        addlink->setStyleSheet(QString::fromUtf8(""));
        QIcon icon20;
        icon20.addFile(QString::fromUtf8(":/fa_solid/qtui/icons/fa_solid/link.svg"), QSize(), QIcon::Normal, QIcon::Off);
        addlink->setIcon(icon20);

        horizontalLayout->addWidget(addlink);

        get_2dgraph = new QToolButton(groupBox_2);
        get_2dgraph->setObjectName(QString::fromUtf8("get_2dgraph"));
        get_2dgraph->setMinimumSize(QSize(26, 26));
        get_2dgraph->setMaximumSize(QSize(26, 26));
        QIcon icon21;
        icon21.addFile(QString::fromUtf8(":/fa_solid/qtui/icons/fa_solid/arrow-up-right-dots.svg"), QSize(), QIcon::Normal, QIcon::Off);
        get_2dgraph->setIcon(icon21);

        horizontalLayout->addWidget(get_2dgraph);

        get_3dgraph = new QToolButton(groupBox_2);
        get_3dgraph->setObjectName(QString::fromUtf8("get_3dgraph"));
        get_3dgraph->setMinimumSize(QSize(26, 26));
        get_3dgraph->setMaximumSize(QSize(26, 26));
        QIcon icon22;
        icon22.addFile(QString::fromUtf8(":/fa_solid/qtui/icons/fa_solid/cubes.svg"), QSize(), QIcon::Normal, QIcon::Off);
        get_3dgraph->setIcon(icon22);

        horizontalLayout->addWidget(get_3dgraph);

        get_selected_points = new QToolButton(groupBox_2);
        get_selected_points->setObjectName(QString::fromUtf8("get_selected_points"));
        QIcon icon23;
        icon23.addFile(QString::fromUtf8(":/fa_solid/qtui/icons/fa_solid/table-list.svg"), QSize(), QIcon::Normal, QIcon::Off);
        get_selected_points->setIcon(icon23);

        horizontalLayout->addWidget(get_selected_points);

        clean = new QPushButton(groupBox_2);
        clean->setObjectName(QString::fromUtf8("clean"));
        sizePolicy.setHeightForWidth(clean->sizePolicy().hasHeightForWidth());
        clean->setSizePolicy(sizePolicy);
        clean->setMinimumSize(QSize(26, 26));
        clean->setMaximumSize(QSize(26, 26));
        clean->setStyleSheet(QString::fromUtf8(""));
        QIcon icon24;
        icon24.addFile(QString::fromUtf8(":/fa_solid/qtui/icons/fa_solid/arrow-rotate-left.svg"), QSize(), QIcon::Normal, QIcon::Off);
        clean->setIcon(icon24);

        horizontalLayout->addWidget(clean);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer_2);


        verticalLayout->addLayout(horizontalLayout);

        description = new QTextEdit(groupBox_2);
        description->setObjectName(QString::fromUtf8("description"));
        QSizePolicy sizePolicy2(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(description->sizePolicy().hasHeightForWidth());
        description->setSizePolicy(sizePolicy2);
        description->setMaximumSize(QSize(16777215, 16777215));
        description->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOn);
        description->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOn);
        description->setSizeAdjustPolicy(QAbstractScrollArea::AdjustToContents);
        description->setAutoFormatting(QTextEdit::AutoAll);
        description->setTextInteractionFlags(Qt::LinksAccessibleByKeyboard|Qt::LinksAccessibleByMouse|Qt::TextBrowserInteraction|Qt::TextEditable|Qt::TextEditorInteraction|Qt::TextSelectableByKeyboard|Qt::TextSelectableByMouse);

        verticalLayout->addWidget(description);

        splitter->addWidget(groupBox_2);

        verticalLayout_6->addWidget(splitter);

        scrollArea->setWidget(scrollAreaWidgetContents);

        verticalLayout_3->addWidget(scrollArea);

        horizontalLayout_8 = new QHBoxLayout();
        horizontalLayout_8->setObjectName(QString::fromUtf8("horizontalLayout_8"));
        horizontalSpacer_4 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_8->addItem(horizontalSpacer_4);

        update = new QPushButton(Form);
        update->setObjectName(QString::fromUtf8("update"));
        update->setMinimumSize(QSize(30, 30));
        update->setFont(font);
        QIcon icon25;
        icon25.addFile(QString::fromUtf8(":/fa_solid/qtui/icons/fa_solid/arrows-rotate.svg"), QSize(), QIcon::Normal, QIcon::Off);
        update->setIcon(icon25);
        update->setIconSize(QSize(25, 25));

        horizontalLayout_8->addWidget(update);

        horizontalSpacer_16 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_8->addItem(horizontalSpacer_16);

        save = new QPushButton(Form);
        save->setObjectName(QString::fromUtf8("save"));
        save->setMinimumSize(QSize(30, 30));
        QIcon icon26;
        icon26.addFile(QString::fromUtf8(":/editor/qtui/icons/txt_editor/save.png"), QSize(), QIcon::Normal, QIcon::Off);
        save->setIcon(icon26);
        save->setIconSize(QSize(25, 25));

        horizontalLayout_8->addWidget(save);

        horizontalSpacer_17 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_8->addItem(horizontalSpacer_17);

        opendir = new QPushButton(Form);
        opendir->setObjectName(QString::fromUtf8("opendir"));
        QIcon icon27;
        icon27.addFile(QString::fromUtf8(":/fa_solid/qtui/icons/fa_solid/folder-open.svg"), QSize(), QIcon::Normal, QIcon::Off);
        opendir->setIcon(icon27);
        opendir->setIconSize(QSize(25, 25));

        horizontalLayout_8->addWidget(opendir);

        horizontalSpacer_15 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_8->addItem(horizontalSpacer_15);


        verticalLayout_3->addLayout(horizontalLayout_8);


        retranslateUi(Form);

        SelectIcon->setCurrentIndex(1);


        QMetaObject::connectSlotsByName(Form);
    } // setupUi

    void retranslateUi(QWidget *Form)
    {
        Form->setWindowTitle(QCoreApplication::translate("Form", "Report Builder", nullptr));
        kml_marker->setTitle(QCoreApplication::translate("Form", "KML marker", nullptr));
        lock_location->setText(QCoreApplication::translate("Form", "Lock", nullptr));
        polygoncolor->setText(QCoreApplication::translate("Form", "Polygon", nullptr));
        label_2->setText(QCoreApplication::translate("Form", "Label", nullptr));
        SelectIcon->setItemText(0, QString());
        SelectIcon->setItemText(1, QCoreApplication::translate("Form", "blue_circle", nullptr));
        SelectIcon->setItemText(2, QCoreApplication::translate("Form", "green_circle", nullptr));
        SelectIcon->setItemText(3, QCoreApplication::translate("Form", "red_circle", nullptr));
        SelectIcon->setItemText(4, QCoreApplication::translate("Form", "yellow_circle", nullptr));

        Tessellate->setText(QString());
        altitudeMode->setItemText(0, QCoreApplication::translate("Form", "absolute", nullptr));
        altitudeMode->setItemText(1, QCoreApplication::translate("Form", "clampToGround", nullptr));
        altitudeMode->setItemText(2, QCoreApplication::translate("Form", "relativeToGround", nullptr));

        label->setText(QCoreApplication::translate("Form", "Name", nullptr));
        labelcolor->setText(QCoreApplication::translate("Form", "Label", nullptr));
        Tessellatelabel->setText(QCoreApplication::translate("Form", "Tessellate", nullptr));
        Extrudelabel->setText(QCoreApplication::translate("Form", "Extrude", nullptr));
        label_5->setText(QCoreApplication::translate("Form", "<b>Colors<b>", nullptr));
        Extrude->setText(QString());
        linecolor->setText(QCoreApplication::translate("Form", "Line", nullptr));
        label_3->setText(QCoreApplication::translate("Form", "Altitude Mode", nullptr));
        LineWidthlabel->setText(QCoreApplication::translate("Form", "Line Width", nullptr));
        Iconlabel->setText(QCoreApplication::translate("Form", "Icon", nullptr));
        Zoom->setText(QCoreApplication::translate("Form", "1000", nullptr));
        Range->setText(QCoreApplication::translate("Form", "1000", nullptr));
        Roll->setText(QCoreApplication::translate("Form", "0", nullptr));
        Pitch->setText(QCoreApplication::translate("Form", "0", nullptr));
        Head->setText(QCoreApplication::translate("Form", "0", nullptr));
        label_4->setText(QCoreApplication::translate("Form", "<b>General<b>", nullptr));
        label_6->setText(QCoreApplication::translate("Form", "<b>Position<b>", nullptr));
        label_8->setText(QCoreApplication::translate("Form", "Look At", nullptr));
        groupBox_2->setTitle(QString());
        label_7->setText(QCoreApplication::translate("Form", "KML Description", nullptr));
#if QT_CONFIG(tooltip)
        editor_italic->setToolTip(QCoreApplication::translate("Form", "Set / Un-set selexted text to Bold", nullptr));
#endif // QT_CONFIG(tooltip)
        editor_italic->setText(QString());
#if QT_CONFIG(tooltip)
        editor_align_justify->setToolTip(QCoreApplication::translate("Form", "Justified Alignment for selected text", nullptr));
#endif // QT_CONFIG(tooltip)
        editor_align_justify->setText(QString());
#if QT_CONFIG(tooltip)
        editor_undo->setToolTip(QCoreApplication::translate("Form", "Undo text edit", nullptr));
#endif // QT_CONFIG(tooltip)
        editor_undo->setText(QString());
#if QT_CONFIG(tooltip)
        editor_redo->setToolTip(QCoreApplication::translate("Form", "Redo text editing", nullptr));
#endif // QT_CONFIG(tooltip)
        editor_redo->setText(QString());
#if QT_CONFIG(tooltip)
        editor_save->setToolTip(QCoreApplication::translate("Form", "save editor text to HTML", nullptr));
#endif // QT_CONFIG(tooltip)
        editor_save->setText(QString());
#if QT_CONFIG(tooltip)
        editor_paste->setToolTip(QCoreApplication::translate("Form", "Paste selected text", nullptr));
#endif // QT_CONFIG(tooltip)
        editor_paste->setText(QString());
#if QT_CONFIG(tooltip)
        editor_align_center->setToolTip(QCoreApplication::translate("Form", "Align selected text to the center", nullptr));
#endif // QT_CONFIG(tooltip)
        editor_align_center->setText(QString());
#if QT_CONFIG(tooltip)
        editor_align_left->setToolTip(QCoreApplication::translate("Form", "Align selected text to the left", nullptr));
#endif // QT_CONFIG(tooltip)
        editor_align_left->setText(QString());
#if QT_CONFIG(tooltip)
        editor_copy->setToolTip(QCoreApplication::translate("Form", "Copy selected text", nullptr));
#endif // QT_CONFIG(tooltip)
        editor_copy->setText(QString());
#if QT_CONFIG(tooltip)
        editor_underline->setToolTip(QCoreApplication::translate("Form", "Set / Un-Set selexted text to Underign", nullptr));
#endif // QT_CONFIG(tooltip)
        editor_underline->setText(QString());
#if QT_CONFIG(tooltip)
        editor_bold->setToolTip(QCoreApplication::translate("Form", "Set / Un-Set selexted text to Bold", nullptr));
#endif // QT_CONFIG(tooltip)
        editor_bold->setText(QString());
#if QT_CONFIG(tooltip)
        editor_align_right->setToolTip(QCoreApplication::translate("Form", "Align selected text to the right", nullptr));
#endif // QT_CONFIG(tooltip)
        editor_align_right->setText(QString());
#if QT_CONFIG(tooltip)
        editor_select_all->setToolTip(QCoreApplication::translate("Form", "Select all text", nullptr));
#endif // QT_CONFIG(tooltip)
        editor_select_all->setText(QString());
#if QT_CONFIG(tooltip)
        editor_cut->setToolTip(QCoreApplication::translate("Form", "Cut selected text", nullptr));
#endif // QT_CONFIG(tooltip)
        editor_cut->setText(QString());
#if QT_CONFIG(tooltip)
        fontComboBox->setToolTip(QCoreApplication::translate("Form", "Select Font Family", nullptr));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        fontsize->setToolTip(QCoreApplication::translate("Form", "set font size", nullptr));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        addimage->setToolTip(QCoreApplication::translate("Form", "Add link to current HBC image", nullptr));
#endif // QT_CONFIG(tooltip)
        addimage->setText(QString());
#if QT_CONFIG(tooltip)
        addlink->setToolTip(QCoreApplication::translate("Form", "Add link", nullptr));
#endif // QT_CONFIG(tooltip)
        addlink->setText(QString());
#if QT_CONFIG(tooltip)
        get_2dgraph->setToolTip(QCoreApplication::translate("Form", "Add 2D Graph from query builder", nullptr));
#endif // QT_CONFIG(tooltip)
        get_2dgraph->setText(QString());
#if QT_CONFIG(tooltip)
        get_3dgraph->setToolTip(QCoreApplication::translate("Form", "Add 3D Graph from query builder", nullptr));
#endif // QT_CONFIG(tooltip)
        get_3dgraph->setText(QString());
        get_selected_points->setText(QString());
#if QT_CONFIG(tooltip)
        clean->setToolTip(QCoreApplication::translate("Form", "clean up the editor", nullptr));
#endif // QT_CONFIG(tooltip)
        clean->setText(QString());
#if QT_CONFIG(tooltip)
        update->setToolTip(QCoreApplication::translate("Form", "Reset positioning values", nullptr));
#endif // QT_CONFIG(tooltip)
        update->setText(QString());
        save->setText(QString());
        opendir->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui

QT_END_NAMESPACE

#endif // KMLSAVE_UI_UI_H
