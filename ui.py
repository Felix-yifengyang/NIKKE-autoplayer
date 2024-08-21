from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QCursor, QFont, QIcon)
from PySide6.QtWidgets import (QCheckBox, QLabel, QPushButton, QSlider, QToolButton, QRadioButton)


class Ui_Form(object):
    def __init__(self):
        self.radioButton_3 = None
        self.radioButton_2 = None
        self.radioButton = None
        self.checkBox_3 = None
        self.checkBox_2 = None
        self.checkBox = None
        self.toolButton = None
        self.pushButton7 = None
        self.pushButton6 = None
        self.pushButton5 = None
        self.initButton = None
        self.label_3 = None
        self.horizontalSlider_2 = None
        self.label_2 = None
        self.horizontalSlider = None
        self.pushButton4 = None
        self.stopButton = None
        self.pushButton3 = None
        self.label = None
        self.pushButton2 = None
        self.pushButton1 = None

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")

        # 将 Form 的窗口模态性设置为非模态，这意味着用户可以与其他窗口进行交互。
        Form.setWindowModality(Qt.NonModal)
        Form.resize(385, 506)

        # 将 Form 设置字体为 ADOBE ARABIC 9 号
        font = QFont()
        font.setFamilies([u"Adobe Arabic"])
        font.setPointSize(9)
        Form.setFont(font)

        # 定义一个图标，并将其添加到窗口中
        icon = QIcon()
        icon.addFile(u"./icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)

        # 创建一个按钮1并设置其属性（收米）
        self.pushButton1 = QPushButton(Form)
        self.pushButton1.setObjectName(u"pushButton1")
        self.pushButton1.setGeometry(QRect(40, 60, 101, 51))
        font1 = QFont()
        font1.setFamilies([u"Adobe Arabic"])
        self.pushButton1.setFont(font1)

        # 创建一个按钮2并设置其属性（连续单抽）
        self.pushButton2 = QPushButton(Form)
        self.pushButton2.setObjectName(u"pushButton2")
        self.pushButton2.setGeometry(QRect(40, 150, 101, 51))
        self.pushButton2.setFont(font1)

        # 创建一个label并设置其属性（？）
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 10, 141, 31))
        font2 = QFont()
        font2.setFamilies([u"Adobe Arabic"])
        font2.setPointSize(15)
        font2.setBold(False)
        self.label.setFont(font2)

        # 创建一个按钮3并设置其属性（模拟室）
        self.pushButton3 = QPushButton(Form)
        self.pushButton3.setObjectName(u"pushButton3")
        self.pushButton3.setGeometry(QRect(40, 240, 101, 51))
        self.pushButton3.setFont(font1)

        # 创建一个停止按钮并设置其属性（终止任务）
        self.stopButton = QPushButton(Form)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setGeometry(QRect(270, 440, 101, 51))
        self.stopButton.setFont(font1)

        # 创建一个按钮4并设置其属性（自动咨询）
        self.pushButton4 = QPushButton(Form)
        self.pushButton4.setObjectName(u"pushButton4")
        self.pushButton4.setGeometry(QRect(40, 330, 101, 51))
        self.pushButton4.setFont(font1)
        self.pushButton4.setCursor(QCursor(Qt.ArrowCursor))  # 将pushButton4的鼠标指针设置为箭头形状

        # 创建一个水平滑块并设置其属性（精确度）
        self.horizontalSlider = QSlider(Form)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(180, 470, 61, 16))
        self.horizontalSlider.setMinimum(4)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setValue(8)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        # 创建一个label2并设置其属性（精确度）
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 440, 61, 21))

        # 创建一个水平滑块2并设置其属性（操作时间间隔）
        self.horizontalSlider_2 = QSlider(Form)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setGeometry(QRect(40, 470, 101, 16))
        self.horizontalSlider_2.setMinimum(20)
        self.horizontalSlider_2.setMaximum(100)
        self.horizontalSlider_2.setValue(25)
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        # 创建一个label3并设置其属性（操作时间间隔）
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 440, 101, 21))

        # 创建一个初始化按钮并设置其属性（矫正窗口）
        self.initButton = QPushButton(Form)
        self.initButton.setObjectName(u"initButton")
        self.initButton.setGeometry(QRect(170, 60, 101, 51))
        self.initButton.setFont(font1)

        # 创建一个按钮5并设置其属性（竞技场）
        self.pushButton5 = QPushButton(Form)
        self.pushButton5.setObjectName(u"pushButton5")
        self.pushButton5.setGeometry(QRect(170, 150, 101, 51))
        self.pushButton5.setFont(font1)

        # 创建一个按钮6并设置其属性（联盟战）
        self.pushButton6 = QPushButton(Form)
        self.pushButton6.setObjectName(u"pushButton6")
        self.pushButton6.setGeometry(QRect(170, 240, 101, 51))
        self.pushButton6.setFont(font1)

        # 创建一个按钮7并设置其属性（一键自动）
        self.pushButton7 = QPushButton(Form)
        self.pushButton7.setObjectName(u"pushButton7")
        self.pushButton7.setGeometry(QRect(170, 330, 101, 51))
        self.pushButton7.setFont(font1)

        # 创建一个工具按钮并设置其属性（...）
        self.toolButton = QToolButton(Form)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(280, 360, 46, 21))
        self.toolButton.setToolButtonStyle(Qt.ToolButtonIconOnly)

        # 创建三个checkbox并设置其属性（竞技场商店，超频，Q键连点）
        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(40, 400, 101, 21))
        self.checkBox_2 = QCheckBox(Form)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(40, 110, 101, 19))
        self.checkBox_3 = QCheckBox(Form)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(40, 290, 79, 19))

        # 创建三个圆点checkbox并设置其属性（单击，双击，按压）
        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(10, 0, 102, 19))
        self.radioButton_2 = QRadioButton(Form)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(70, 0, 102, 19))
        self.radioButton_3 = QRadioButton(Form)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(130, 0, 102, 19))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"NikkeHelper", None))
        self.pushButton1.setText(QCoreApplication.translate("Form", u"\u6536\u7c73", None))
        self.pushButton2.setText(QCoreApplication.translate("Form", u"\u8fde\u7eed\u5355\u62bd", None))
        self.label.setText("")
        self.pushButton3.setText(QCoreApplication.translate("Form", u"\u6a21\u62df\u5ba4", None))
        self.stopButton.setText(QCoreApplication.translate("Form", u"\u7ec8\u6b62\u4efb\u52a1", None))
        self.pushButton4.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u54a8\u8be2", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.initButton.setText(QCoreApplication.translate("Form", u"\u77eb\u6b63\u7a97\u53e3", None))
        self.pushButton5.setText(QCoreApplication.translate("Form", u"\u7ade\u6280\u573a", None))
        self.pushButton6.setText(QCoreApplication.translate("Form", u"\u8054\u76df\u6218", None))
        self.pushButton7.setText(QCoreApplication.translate("Form", u"\u4e00\u952e\u81ea\u52a8", None))
        self.toolButton.setText(QCoreApplication.translate("Form", u"...", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Q\u952e\u8fde\u70b9", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"\u7ade\u6280\u573a\u5546\u5e97", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"\u8d85\u9891", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u5355\u51fb", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u53cc\u51fb", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"\u6309\u538b", None))
    # retranslateUi
