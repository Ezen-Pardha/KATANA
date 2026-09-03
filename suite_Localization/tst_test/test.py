# -*- coding: utf-8 -*-

import names

from openpyxl import load_workbook

def main():
    excelPath = "/home/ezen/Desktop/stringsheet.xlsx"

    workbook = load_workbook(excelPath)  
    sheet = workbook["Sheet8"]
    
    mouseClick(waitForObject(names.wdPopup_lbText_QLabel_5), 55, 8, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))

    mouseClick(waitForObject(names.homeScreen_lbIcon_WdIcon_2), 474, 89, Qt.NoModifier, Qt.LeftButton)
    setWindowState(waitForObject(names.o_ScreenSwitcher), WindowState.Minimize)
    #test.compare(str(waitForObjectExists(names.treatmentScreen_text_QLabel_2).text), "Left Pedal")
    ActulText1=str(waitForObjectExists(names.treatmentScreen_text_QLabel_2).text)
    ExceptedText1=sheet.cell(row=2,column=2).value
    
    test.compare(ExceptedText1, ActulText1, "text is matched")
    snooze(3)
    test.compare(str(waitForObjectExists(names.treatmentScreen_text_QLabel).text), "Left")
    snooze(3)
    setWindowState(waitForObject(names.o_ScreenSwitcher), WindowState.Normal)
    test.breakpoint()
    
    test.imagePresent("image_1")
    test.imagePresent("image_2")
    
    #test.breakpoint()
    
    test.compare(str(waitForObjectExists(names.pulseModeWidget_text_QLabel).text), "Power")
    test.compare(str(waitForObjectExists(names.pulseModeWidget_lbText_QLabel_3).text), "Standard")
    test.imagePresent("image_3")

    # test.breakpoint()
    
    
    mouseClick(waitForObject(names.homeScreen_lbText_QLabel_2), 203, 0, Qt.NoModifier, Qt.LeftButton)
    
