from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtGui import (QCursor, QFont, QIcon, QPixmap)
from PySide6.QtWidgets import (QCheckBox, QLabel, QPushButton, QToolButton)


class Ui_Form(object):
    def __init__(self):
        self.label_2 = None
        self.label_1 = None
        self.toolButton = None
        self.pushButton1 = None
        self.pushButton2 = None
        self.pushButton3 = None
        self.pushButton4 = None
        self.imageLabel = None

    def setupUi(self, Form):  # Form是QWidget对象，通常是个window
        if not Form.objectName():
            Form.setObjectName(u"Form")
            Form.setWindowTitle(QCoreApplication.translate("Form",
                                                           u"\u4eca\u5929\u7d22\u8fbe\u80fd\u4e3a\u4e3b\u4eba\u505a\u4ec0\u4e48\uff1f\u2764",
                                                           None))

        # 将 Form 的窗口模态性设置为非模态，这意味着用户可以与其他窗口进行交互。
        Form.setWindowModality(Qt.NonModal)
        Form.resize(572, 512)

        # 将 Form 设置字体为 ADOBE ARABIC 9 号
        font = QFont()
        font.setFamilies([u"Adobe Arabic"])
        font.setPointSize(9)
        Form.setFont(font)

        # 定义一个图标，并将其添加到窗口中
        icon = QIcon()
        icon.addFile(u"./icon.ico")
        Form.setWindowIcon(icon)

        self.label_1 = QLabel(Form)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(349, 30, 303, 21))

        # 创建一个按钮1并设置其属性（start）
        self.pushButton1 = QPushButton(Form)
        self.pushButton1.setObjectName(u"pushButton1")
        self.pushButton1.setGeometry(QRect(379, 80, 101, 51))
        font1 = QFont()
        font1.setFamilies([u"Adobe Arabic"])
        self.pushButton1.setFont(font1)
        self.pushButton1.setText(QCoreApplication.translate("Form", u"Home", None))

        self.pushButton2 = QPushButton(Form)
        self.pushButton2.setObjectName(u"pushButton2")
        self.pushButton2.setGeometry(QRect(379, 150, 101, 51))
        font1 = QFont()
        font1.setFamilies([u"Adobe Arabic"])
        self.pushButton2.setFont(font1)
        self.pushButton2.setText(QCoreApplication.translate("Form", u"Base", None))

        self.pushButton3 = QPushButton(Form)
        self.pushButton3.setObjectName(u"pushButton3")
        self.pushButton3.setGeometry(QRect(379, 220, 101, 51))
        font1 = QFont()
        font1.setFamilies([u"Adobe Arabic"])
        self.pushButton3.setFont(font1)
        self.pushButton3.setText(QCoreApplication.translate("Form", u"Ark", None))

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(319, 340, 303, 21))

        # 创建一个Dialog按钮并设置其属性（What do you need）
        self.toolButton = QToolButton(Form)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(329, 380, 202, 26))
        self.toolButton.setText(QCoreApplication.translate("Form", u"Please choose what you need", None))

        self.pushButton4 = QPushButton(Form)
        self.pushButton4.setObjectName(u"pushButton4")
        self.pushButton4.setGeometry(QRect(379, 410, 101, 51))
        font1 = QFont()
        font1.setFamilies([u"Adobe Arabic"])
        self.pushButton4.setFont(font1)
        self.pushButton4.setText(QCoreApplication.translate("Form", u"Start", None))

        # 添加图片
        self.imageLabel = QLabel(Form)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setGeometry(QRect(0, 0, 286, 512))  # 设置图片位置和大小
        pixmap = QPixmap("./image/soda.jpg")
        self.imageLabel.setPixmap(pixmap)
        self.imageLabel.setScaledContents(True)  # 使图片适应标签大小

        QMetaObject.connectSlotsByName(Form)


class Ui_Dialog(object):
    def __init__(self):
        self.checkBox_0 = None
        self.checkBox_1 = None
        self.checkBox_2 = None
        self.imageLabel = None

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
            Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"What do you want?Darling~\u2764", None))

        # 添加图表到对话框中，并设置icon属性和dialog属性
        icon = QIcon()
        icon.addFile(u"./icon.ico")
        Dialog.setWindowIcon(icon)
        Dialog.resize(440, 341)

        self.checkBox_0 = QCheckBox(Dialog)
        self.checkBox_0.setObjectName(u"checkBox_0")
        self.checkBox_0.setGeometry(QRect(300, 70, 79, 19))
        self.checkBox_0.setText(QCoreApplication.translate("Dialog", u"Home", None))
        self.checkBox_1 = QCheckBox(Dialog)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setGeometry(QRect(300, 170, 79, 19))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"Base", None))
        self.checkBox_2 = QCheckBox(Dialog)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(300, 270, 79, 19))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Ark", None))

        self.imageLabel = QLabel(Dialog)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setGeometry(QRect(0, 0, 220, 341))  # 设置图片位置和大小
        pixmap = QPixmap("./image/viper.jpg")
        self.imageLabel.setPixmap(pixmap)
        self.imageLabel.setScaledContents(True)  # 使图片适应标签大小

        QMetaObject.connectSlotsByName(Dialog)
