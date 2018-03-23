'''
ReadMe:
This program is separated in two processes, one is running the GUI,
and the other is runing a motor(Or just printing ON and OFF in this case),...
GUI process writes value of slider to file when slider is changed, wheter
motor process is reading the same file and apply this value to motor's speed

GUI has only a slider which is for controling the speed of motor
'''


from PyQt5 import QtWidgets,uic, QtCore
from PyQt5.QtWidgets import QMessageBox,QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtCore import QTimer,QTime
from PyQt5.QtGui import QIcon
import time
from multiprocessing import Process, Queue, Value

app = QtWidgets.QApplication([])
dlg = uic.loadUi("Motor.ui")


def startMotor():
    try:
        while True:
            time.sleep(0.01)
            file = open("test.txt", "r") 
            a=file.read()
            file.close()
            if int(a) == 0:
                print("OFF")
            else:
                print("ON, speed is:", a)
    except:
        print("Abort...")
        
def runProgram():
    dlg.show()
    app.exec()


def changeSpeed():
    dlg.label.setText(str(dlg.slider.value()))
    
    file = open("test.txt","w") 
    file.write(str(dlg.slider.value()))
    file.close() 

#when slider's value is changed
dlg.slider.valueChanged.connect(changeSpeed)


if __name__ == '__main__':
    #On Program load    
    p1 = Process(target=startMotor,args=())
    p2 = Process(target=runProgram,args=())
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
