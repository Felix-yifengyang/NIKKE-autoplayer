import sys, time

import pyautogui
import auto_task

from ui import Ui_Form, Ui_Dialog

from PySide6 import QtWidgets, QtCore

auto_task_list = [True, True, True]


class TaskThread(QtCore.QThread):  # 每个 TaskThread 对象都代表一个独立的线程
    def __init__(self, task_number, parent=None):
        super().__init__(parent)
        self.task_number = task_number
        self.start_time = None

    def run(self):
        if self.task_number == 0:
            auto_task.home()
        elif self.task_number == 1:
            auto_task.base()
        elif self.task_number == 2:
            auto_task.ark()
        elif self.task_number == 3:
            while True:
                auto_task.auto_all(auto_task_list)
                time.sleep(1)


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.current_task = None
        self.current_thread = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # 设置 UI
        self.ui.label_1.setText("You can click 'task Button' :")
        self.ui.label_2.setText("Or you can choose task then click 'Start' :")
        self.ui.toolButton.clicked.connect(self.auto_all_settings)
        self.ui.pushButton1.clicked.connect(lambda: self.run_task(0, "Home"))
        self.ui.pushButton2.clicked.connect(lambda: self.run_task(1, "Base"))
        self.ui.pushButton3.clicked.connect(lambda: self.run_task(2, "Ark"))
        self.ui.pushButton4.clicked.connect(lambda: self.run_task(3, "Start"))

        self.task0_thread = TaskThread(0)
        self.task1_thread = TaskThread(1)
        self.task2_thread = TaskThread(2)
        self.task3_thread = TaskThread(3)

    def run_task(self, task_number, task_name):
        if self.current_thread:
            self.stop_task()
        self.current_task = task_name
        self.current_thread = getattr(self, f"task{task_number}_thread")
        self.current_thread.start()

    def stop_task(self):
        if self.current_thread:
            self.current_thread.terminate()

    def auto_all_settings(self):
        dialog = Dialog()
        dialog.exec()


class Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.checkBox_0.setChecked(auto_task_list[0])
        self.ui.checkBox_1.setChecked(auto_task_list[1])
        self.ui.checkBox_2.setChecked(auto_task_list[2])

        self.ui.checkBox_0.stateChanged.connect(lambda state, index=0: self.auto_task_change(index))
        self.ui.checkBox_1.stateChanged.connect(lambda state, index=1: self.auto_task_change(index))
        self.ui.checkBox_2.stateChanged.connect(lambda state, index=2: self.auto_task_change(index))

    def auto_task_change(self, index):
        auto_task_list[index] = not auto_task_list[index]
        check_change = getattr(self.ui, f"checkBox_{index}")
        check_change.setChecked(auto_task_list[index])
        print(auto_task_list)


if __name__ == "__main__":
    pyautogui.FAILSAFE = False
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()  # 显示窗口
    sys.exit(app.exec())  # 运行应用程序
