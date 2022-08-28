#!/usr/bin/env python3

from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        
        self.myUi = loader.load('calculator/app.ui')
        self.myUi.show()
        
        self.number = ''
        self.operator = ''
        self.firstSide = ''
        self.secondSide = ''
        
        self.myUi.ButtonNumberOne.clicked.connect(self.setNumberOne)
        self.myUi.ButtonNumberTwo.clicked.connect(self.setNumberTwo)
        self.myUi.ButtonNumberThree.clicked.connect(self.setNumberThree)
        self.myUi.ButtonNumberFour.clicked.connect(self.setNumberFour)
        self.myUi.ButtonNumberFive.clicked.connect(self.setNumberFive)
        self.myUi.ButtonNumberSix.clicked.connect(self.setNumberSix)
        self.myUi.ButtonNumberSeven.clicked.connect(self.setNumberSeven)
        self.myUi.ButtonNumberEight.clicked.connect(self.setNumberEight)
        self.myUi.ButtonNumberNine.clicked.connect(self.setNumberNine)
        self.myUi.ButtonNumberZero.clicked.connect(self.setNumberZero)
        self.myUi.ButtonAdd.clicked.connect(self.addOperator)
        self.myUi.ButtonSub.clicked.connect(self.subOperator)
        self.myUi.ButtonMul.clicked.connect(self.mulOperator)
        self.myUi.ButtonDiv.clicked.connect(self.divOperator)
        self.myUi.ButtonClear.clicked.connect(self.clearOutPut)
        self.myUi.ButtonEqual.clicked.connect(self.showResult)

    def showMessage(self):
        self.myUi.result.setText(self.number)

    def clearOutPut(self):
        self.firstSide  = ''
        self.secondSide = ''
        self.number     = ''
        self.operator   = ''
        self.myUi.result.setText('')    

    
    def setNumberOne(self) :
        self.number += "1"
        self.showMessage()
    
    def setNumberTwo(self) :
        self.number += "2"
        self.showMessage()
    
    def setNumberThree(self) :
        self.number += "3"
        self.showMessage()
    
    def setNumberFour(self) :
        self.number += "4"
        self.showMessage()
    
    def setNumberFive(self) :
        self.number += "5"
        self.showMessage()
    
    def setNumberSix(self) :
        self.number += "6"
        self.showMessage()
    
    def setNumberSeven(self) :
        self.number += "7"
        self.showMessage()
    
    def setNumberEight(self) :
        self.number += "8"
        self.showMessage()
    
    def setNumberNine(self) :
        self.number += "9"
        self.showMessage()
    
    def setNumberZero(self) :
        self.number += "0"
        self.showMessage()


    def addOperator(self) :
        
        if self.number != '' :
            self.operator = '+'
            self.firstSide = int(self.number)
            self.number = self.number + self.operator 
            self.showMessage()
            self.number = ''

    def subOperator(self) :
        
        if self.number != '' :
            self.operator = '-'
            self.firstSide = int(self.number)
            self.number = self.number + self.operator 
            self.showMessage()
            self.number = ''

    def mulOperator(self) :
        
        if self.number != '' :
            self.operator = 'X'
            self.firstSide = int(self.number)
            self.number = self.number + self.operator 
            self.showMessage()
            self.number = ''
            
    def divOperator(self) :
        
        if self.number != '' :
            self.operator = '/'
            self.firstSide = int(self.number)
            self.number = self.number + self.operator 
            self.showMessage()
            self.number = ''       


    def showResult(self):
        
        if self.operator == '+' :
            self.secondSide = int(self.number)
            self.number     = str(self.firstSide + self.secondSide)
            self.showMessage()
            self.firstSide  = ''
            self.secondSide = ''
            self.operator   = ''
        
        if self.operator == '-' :
            self.secondSide = int(self.number)
            self.number = str(self.firstSide - self.secondSide)
            self.showMessage()
            self.firstSide  = ''
            self.secondSide = ''
            self.operator   = ''
        
        if self.operator == 'X' :
            self.secondSide = int(self.number)
            self.number     = str(self.firstSide * self.secondSide)
            self.showMessage()
            self.firstSide  = ''
            self.secondSide = ''
            self.operator   = ''
        
        if self.operator == '/' :
            self.secondSide = int(self.number)
            self.number     = str(int(self.firstSide / self.secondSide))
            self.showMessage()
            self.firstSide  = ''
            self.secondSide = ''
            self.operator   = ''

def run(_):
    app, window = QApplication([]), Calculator()
    app.exec()

try: (run if __name__ == '__main__' else exit)("coded by msfpt")
except Exception as error: ...