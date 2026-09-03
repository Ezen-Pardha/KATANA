# -*- coding: utf-8 -*-

import names
from openpyxl import load_workbook

def main():
    
    excelpath= "/home/ntc/Desktop/TestData.xlsx"
    workbook = load_workbook(excelpath)
    sheet=workbook["Sheet1"]
    
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    sendEvent("QWheelEvent", waitForObject(names.homeScreen_lbIcon_WdIcon_3), 350, 10, -120, 0, 2)
    sendEvent("QWheelEvent", waitForObject(names.homeScreen_lbIcon_WdIcon_3), 350, 10, -120, 0, 2)
    mouseClick(waitForObject(names.frRightButtons_lbIcon_WdIcon_2), 76, 25, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.wdScrollArea_btDownArrow_WdPushButton))
    mouseClick(waitForObject(names.wdScrollArea_lbText_WdLabel_2), 238, 112, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.wdScrollArea_lbText_WdLabel_3), 225, 101, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.frRightButtons_Save_right_WdToolButton))
    clickButton(waitForObject(names.frLeftButtons_Back_left_WdToolButton))
    mouseClick(waitForObject(names.frLeftButtons_lbIcon_WdIcon_2), 60, 10, Qt.NoModifier, Qt.LeftButton)
    
    ActualText = str(waitForObjectExists(names.wdTitleBar_text_QLabel).text)
    expectedText = sheet.cell(row=2, column=2).value
    test.compare(expectedText, ActualText, "text is matching")
    
    expectedText1 = sheet.cell(row=3, column=2).value
    ActualText1 = str(waitForObjectExists(names.homeScreen_lbPhysician_QLabel).text)
    test.compare(expectedText1, ActualText1, "text is matching") 
    
    expectedText2 = sheet.cell(row=4, column=2).value
    ActualText2 = str(waitForObjectExists(names.homeScreen_lbText_QLabel).text)
    test.compare(expectedText2, ActualText2, "text is matching") 
    
    expectedText3 = sheet.cell(row=5, column=2).value
    ActualText3 = str(waitForObjectExists(names.homeScreen_lbText_QLabel_2).text)
    test.compare(expectedText3, ActualText3, "text is matching")
    
    expectedText4 = sheet.cell(row=6, column=2).value
    ActualText4 = str(waitForObjectExists(names.homeScreen_lbText_QLabel_3).text)
    test.compare(expectedText4, ActualText4, "text is matching")
    
    expectedText5 = sheet.cell(row=7, column=2).value
    ActualText5 = str(waitForObjectExists(names.homeScreen_lbText_QLabel_4).text)
    test.compare(expectedText5, ActualText5, "text is matching")
    
    expectedText6 = sheet.cell(row=8, column=2).value
    ActualText6 = str(waitForObjectExists(names.homeScreen_lbText_QLabel_5).text)
    test.compare(expectedText6, ActualText6, "text is matching")

    test.vp("VP1")
    test.vp("VP2")
    
     
    
    # test.compare(str(waitForObjectExists(names.frRightButtons_lbText_QLabel).text), "Ajustes")
    # test.compare(str(waitForObjectExists(names.frLeftButtons_lbText_QLabel).text), "Cerrar sesi\nón")
    # expectedText8 = sheet.cell(row=10, cloumn=2).value
    # ActualText8 = str(waitForObjectExists(names.frRightButtons_lbText_QLabel).text)
    # test.compare(expectedText8, ActualText8, "text is matching")
    #
    # expectedText7 = sheet.cell(row=9, cloumn=2).value
    # ActualText7 = str(waitForObjectExists(names.frLeftButtons_lbText_QLabel).text)
    # test.compare(expectedText7, ActualText7, "text is matching")
    
    
    
 
    
    
       
      
