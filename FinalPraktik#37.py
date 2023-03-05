from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QPushButton, QRadioButton, \
    QSpinBox, QWidget, QLCDNumber, QLabel, QGroupBox, QHBoxLayout, QDialog, QMessageBox
from PyQt5.QtCore import pyqtSignal,pyqtSlot,QTimer
import time


#pip install py-trello
#pip install pyqt5
#pip install pyqt5-tools


class Timer(QDialog):
    timeout = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)

        self.spintime = 0
        self.timeInterval = 1000    
        self.chilling = int(900)                                    # По умолчанию секунды
        self.timerDown = QTimer()
        self.timerDown.setInterval(self.timeInterval)
        self.timerDown.timeout.connect(self.updateDowntime)
        self.flag1 = True

        self.initUi()

        self.buttonReset.clicked.connect(self.reset)
        self.buttonReset.clicked.connect(self.timerDown.stop)
        self.buttonCountDown.clicked.connect(self.timerDown.start)
        self.buttonStopAlarm.clicked.connect(self.timerDown.stop)
        self.buttonSkipDown.clicked.connect(self.timerSkip)
        self.buttonCountDown.clicked.connect(self.Rules)
        self.perekur.valueChanged.connect(self.show_perekur)
        self.ycheba.valueChanged.connect(self.show_perekur)


    def initUi(self):
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        self.groupBox = QGroupBox(" Настройки интервалного обучения")
        self.radioButton1 = QLabel("Перерывы")
        self.perekur = QSpinBox()
        self.perekur.setRange(0, 10)  
        self.unitLayout = QHBoxLayout()
        self.unitLayout.addWidget(self.radioButton1)
        self.unitLayout.addWidget(self.perekur)
        self.groupBox.setLayout(self.unitLayout)
        mainLayout.addWidget(self.groupBox)

        self.radioButton2 = QLabel("Секунд для следующего этапа:")
        mainLayout.addWidget(self.radioButton2)

        self.timeViewer = QLCDNumber()
        self.timeViewer.setFixedHeight(45)     
        mainLayout.addWidget(self.timeViewer)

        self.status1 = QLabel()
        mainLayout.addWidget(self.status1)

        self.timeForHuman = QLabel()
        mainLayout.addWidget(self.timeForHuman)

        self.buttonReset = QPushButton(self.tr("Сброс"))
        mainLayout.addWidget(self.buttonReset)

        self.ycheba = QSpinBox()
        self.ycheba.setRange(0, 1000000000)                
        mainLayout.addWidget(self.ycheba)
        
        self.groupBoxCountDown = QGroupBox(" Обратный отсчет ")
        countDown = QVBoxLayout()
        self.buttonCountDown = QPushButton(self.tr("Cтарт"))
        self.buttonStopAlarm = QPushButton(self.tr("Стоп"))
        self.buttonSkipDown = QPushButton(self.tr("Пропустить"))

        countDown.addWidget(self.buttonCountDown)
        countDown.addWidget(self.buttonStopAlarm)
        countDown.addWidget(self.buttonSkipDown)
        self.groupBoxCountDown.setLayout(countDown)
        mainLayout.addWidget(self.groupBoxCountDown)
    
    def show_perekur(self):
  
        # getting current value
        self.perekur1 = self.perekur.value()
        self.perekur0 = self.perekur1 + 1
        self.ycheba1 = self.ycheba.value() * 60
        self.chill = int(round(self.ycheba1 / (self.perekur1 + 1)))
        self.time = self.chill
        self.settimer(self.time)

    def updateDowntime(self):
        if self.perekur0 > 0:
            if self.flag1 == True:
                self.status1.setText("Учёба")
                self.time -= 1
                self.settimer(self.time)
                if self.time == 0:
                    self.flag1 = False
                    self.time = self.chilling
                    self.perekur0 = self.perekur0 - 1
                    if self.perekur0 >0:
                        QMessageBox.about(self, "Конец интервала!", "Молодец, можешь отдохнуть!")
            elif self.flag1 == False and self.perekur0 > 0:
                self.status1.setText("Перерыв")
                self.time -= 1
                self.settimer(self.time)
                if self.time == 0:
                    self.flag1 = True
                    self.time = self.chill
                    QMessageBox.about(self, "Конец Перерыва!", "Пора начинать работать!")
        elif self.flag1 == False and self.perekur0 <= 0:
            QMessageBox.about(self, "Конец обучения!", "Ты хорошо потрудился!")
            self.status1.setText("Всё!!")
            self.flag1 = True
        elif self.perekur0 <= 0 and self.flag1 == True:
            self.time=0
            self.settimer(self.time)

    def settimer(self, int):
        self.time=int
        self.timeViewer.display(self.time)
        self.timeForHuman.setText(
            time.strftime('%H hour %M minute %S second', time.gmtime(self.time/1)))

    def timerSkip(self):
        self.time = 1
        self.settimer(self.time)

    def reset(self):
        self.time=0
        self.settimer(self.time)
        self.flag1 = True

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Вы увеверены что хотите выйти?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def Rules(self):
        QMessageBox.about(self, "Правила обучения", "Во время своего обучения вы должны то то то и это это это")


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)

    timer = Timer()
    def beep():
        print('\a')
    timer.timeout.connect(beep)
    timer.show()
    w = QWidget()
    w.setWindowTitle('Simple')
    sys.exit(app.exec_())

    