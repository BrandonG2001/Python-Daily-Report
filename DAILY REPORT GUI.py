# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_ui_frontend.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from sys import argv as sys_argv, exit as sys_exit
from PyQt5 import QtCore, QtGui, QtWidgets
from daily_report import main_report
from auto_website_open import open_my_websites
from execute_command import clean_windows_temp_files, clean_cache
from multiprocessing.pool import ThreadPool
from time import sleep

from warnings import filterwarnings
filterwarnings("ignore", category=UserWarning)

from os.path import join
from os import environ

class Ui_Dialog(object):

    buttons_pool = ThreadPool(processes=1)

    buttonStyleSheet = """
        color: white;
        background-color: {};
        border-radius : 5px;
        """

    def setupUi(self, Dialog):
        # all the colors
        if True:
            Dialog.setObjectName("Dialog")
            Dialog.resize(440, 275)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
            Dialog.setSizePolicy(sizePolicy)
            Dialog.setMinimumSize(QtCore.QSize(440, 275))
            Dialog.setMaximumSize(QtCore.QSize(440, 275))   
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(139, 139, 139))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
            brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
            brush = QtGui.QBrush(QtGui.QColor(173, 173, 173))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
            brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
            brush = QtGui.QBrush(QtGui.QColor(93, 93, 93))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(139, 139, 139))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
            brush = QtGui.QBrush(QtGui.QColor(197, 197, 197))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(139, 139, 139))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
            brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
            brush = QtGui.QBrush(QtGui.QColor(173, 173, 173))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
            brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
            brush = QtGui.QBrush(QtGui.QColor(93, 93, 93))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(139, 139, 139))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
            brush = QtGui.QBrush(QtGui.QColor(197, 197, 197))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
            brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(139, 139, 139))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
            brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
            brush = QtGui.QBrush(QtGui.QColor(173, 173, 173))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
            brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
            brush = QtGui.QBrush(QtGui.QColor(93, 93, 93))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
            brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
            brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
            brush = QtGui.QBrush(QtGui.QColor(139, 139, 139))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(139, 139, 139))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
            brush = QtGui.QBrush(QtGui.QColor(139, 139, 139))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
            Dialog.setPalette(palette)
        
        # all the buttons
        if True:
            self.pushButton = QtWidgets.QPushButton(Dialog)
            self.pushButton.setGeometry(QtCore.QRect(270, 90, 111, 31))
            self.pushButton.setObjectName("pushButton")
            self.pushButton_2 = QtWidgets.QPushButton(Dialog)
            self.pushButton_2.setGeometry(QtCore.QRect(270, 150, 111, 31))
            self.pushButton_2.setObjectName("pushButton_2")
            self.checkBox = QtWidgets.QCheckBox(Dialog)
            self.checkBox.setGeometry(QtCore.QRect(50, 30, 200, 17))
            self.checkBox.setChecked(True)
            self.checkBox.setObjectName("checkBox")
            self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
            self.checkBox_2.setGeometry(QtCore.QRect(50, 90, 150, 17))
            self.checkBox_2.setChecked(True)
            self.checkBox_2.setObjectName("checkBox_2")
            self.checkBox_3 = QtWidgets.QCheckBox(Dialog)
            self.checkBox_3.setGeometry(QtCore.QRect(50, 150, 150, 17))
            self.checkBox_3.setChecked(True)
            self.checkBox_3.setObjectName("checkBox_3")
            self.checkBox_4 = QtWidgets.QCheckBox(Dialog)
            self.checkBox_4.setGeometry(QtCore.QRect(50, 210, 150, 17))
            self.checkBox_4.setObjectName("checkBox_4")
            self.checkBox_5 = QtWidgets.QCheckBox(Dialog)
            self.checkBox_5.setGeometry(QtCore.QRect(50, 60, 150, 17))
            self.checkBox_5.setChecked(True)
            self.checkBox_5.setObjectName("checkBox_5")
            self.checkBox_6 = QtWidgets.QCheckBox(Dialog)
            self.checkBox_6.setGeometry(QtCore.QRect(50, 120, 150, 17))
            self.checkBox_6.setChecked(True)
            self.checkBox_6.setObjectName("checkBox_6")
            self.checkBox_7 = QtWidgets.QCheckBox(Dialog)
            self.checkBox_7.setGeometry(QtCore.QRect(50, 180, 150, 17))
            self.checkBox_7.setChecked(True)
            self.checkBox_7.setObjectName("checkBox_7")
            self.checkBox_8 = QtWidgets.QCheckBox(Dialog)
            self.checkBox_8.setGeometry(QtCore.QRect(50, 240, 150, 17))
            self.checkBox_8.setObjectName("checkBox_8")

        try:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(join(environ['UserProfile'], 'Documents', 'Github', 'Python-Daily-Report', 'jarvis image.png')), QtGui.QIcon.Normal, QtGui.QIcon.On)
            Dialog.setWindowIcon(icon)
        except:
            pass

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Python Daily REPORT"))

        self.pushButton.setText(_translate("Dialog", "Run Daily Report"))
        self.pushButton.clicked.connect(self.run_report)

        self.pushButton_2.setText(_translate("Dialog", "Open My Websites"))
        self.pushButton_2.clicked.connect(open_my_websites)

        self.checkBox.setText(_translate("Dialog", "Full Run (w/ update sys)"))
        self.checkBox.stateChanged.connect(self.set_full_run)

        self.checkBox_2.setText(_translate("Dialog", "Check Calendar"))
        self.checkBox_2.toggled.connect(self.toggle_check)

        self.checkBox_3.setText(_translate("Dialog", "Check News"))
        self.checkBox_3.toggled.connect(self.toggle_check)

        self.checkBox_4.setText(_translate("Dialog", "Check Youtube/Twitch"))

        self.checkBox_5.setText(_translate("Dialog", "Check Stardate"))
        self.checkBox_5.toggled.connect(self.toggle_check)

        self.checkBox_6.setText(_translate("Dialog", "Check Weather"))
        self.checkBox_6.toggled.connect(self.toggle_check)

        self.checkBox_7.setText(_translate("Dialog", "Check Space Launches"))
        self.checkBox_7.toggled.connect(self.toggle_check)

        self.checkBox_8.setText(_translate("Dialog", "Clean Windows Files"))

        self.pushButton.setStyleSheet("QPushButton::hover"
                             "{"
                             f'{self.buttonStyleSheet.format("green")}'
                             "}"
                        )
        
        self.pushButton_2.setStyleSheet("QPushButton::hover"
                             "{"
                             f'{self.buttonStyleSheet.format("green")}'
                             "}"
                        )
        

    # check status of all checkboxes
    # run main report with settings
    def run_report(self):
        global my_result
        full_run = self.checkBox.checkState() == 2
        check_calendar = self.checkBox_2.checkState() == 2
        check_news = self.checkBox_3.checkState() == 2
        check_vids = self.checkBox_4.checkState() == 2
        check_stardate = self.checkBox_5.checkState() == 2
        check_weather = self.checkBox_6.checkState() == 2
        check_space_launches = self.checkBox_7.checkState() == 2
        clean_windows = self.checkBox_8.checkState()==2
        get_quote = full_run or check_stardate

        main_pool = ThreadPool(processes=4)
        
        my_result = main_pool.apply_async(main_report, (full_run, check_stardate, get_quote, check_calendar, check_weather, check_news, check_space_launches, check_vids, clean_windows, False) )
        
        self.pushButton.setEnabled(False)
        #self.pushButton_2.setEnabled(False)
        
        self.buttons_pool.apply_async(self.enabling_buttons, (check_vids, my_result))

    def enabling_buttons(self, check_vids, my_result):
        #scaling_factor = 10  # everything is 1/scaling_factor
        for _ in range(1, 60*5):  #5 minutes maximum (my timeout counter) 
            sleep(1)
            try:
                if my_result.ready():
                    break
            except:
                pass
        if check_vids:
            self.check_videos()
        try:
            if my_result.get() == False:
                self.closeIt()
        except:
            pass

        self.pushButton.setEnabled(True)
        #self.pushButton_2.setEnabled(True)

    def closeIt(self):
        QtCore.QCoreApplication.instance().quit()
        
    def run_cleanup(self):
        print('Running Cleanup')
        clean_windows_temp_files()

    # if full run set, select main functions
    # if full run is unselected, unselect all functions
    def set_full_run(self):
        if self.checkBox.checkState() == 2:
            self.checkBox_2.setChecked(True)
            self.checkBox_3.setChecked(True)
            #self.checkBox_4.setChecked(True)
            self.checkBox_5.setChecked(True)
            self.checkBox_6.setChecked(True)
            self.checkBox_7.setChecked(True)
            #self.checkBox_8.setChecked(True)

        else:
            self.checkBox_2.setChecked(False)
            self.checkBox_3.setChecked(False)
            self.checkBox_4.setChecked(False)
            self.checkBox_5.setChecked(False)
            self.checkBox_6.setChecked(False)
            self.checkBox_7.setChecked(False)
            self.checkBox_8.setChecked(False)

    # if full run enabled, prevent main functions from turning off
    # otherwise, we good to toggle
    def toggle_check(self):
        if self.checkBox.checkState() == 2:
            self.checkBox_2.setChecked(True)
            self.checkBox_3.setChecked(True)
            #self.checkBox_4.setChecked(True)
            self.checkBox_5.setChecked(True)
            self.checkBox_6.setChecked(True)
            self.checkBox_7.setChecked(True)
            #self.checkBox_8.setChecked(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys_argv)
 
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
 
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    
    # run cache cleaning
    if not clean_cache():
        print('Unable to Clean Cache')
        input()

    sys_exit()