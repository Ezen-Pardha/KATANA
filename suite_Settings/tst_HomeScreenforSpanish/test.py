# -*- coding: utf-8 -*-

import names
from openpyxl import load_workbook

def main():
    
    excelpath= "/home/ezen/Desktop/stringsheet.xlsx"
    workbook = load_workbook(excelpath)
    sheet=workbook["Sheet6"]
    
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    sendEvent("QWheelEvent", waitForObject(names.homeScreen_lbIcon_WdIcon_3), 350, 10, -120, 0, 2)
    sendEvent("QWheelEvent", waitForObject(names.homeScreen_lbIcon_WdIcon_3), 350, 10, -120, 0, 2)

    mouseClick(waitForObject(names.frRightButtons_lbIcon_WdIcon), 80, 14, Qt.NoModifier, Qt.LeftButton)

    sendEvent("QWheelEvent", waitForObject(names.wdScrollArea_btDownArrow_WdPushButton), 55, 79, -120, 0, 2)
    sendEvent("QWheelEvent", waitForObject(names.wdScrollArea_btDownArrow_WdPushButton), 55, 79, -120, 0, 2)
    sendEvent("QWheelEvent", waitForObject(names.wdScrollArea_btDownArrow_WdPushButton), 55, 79, -120, 0, 2)
    clickButton(waitForObject(names.wdScrollArea_btDownArrow_WdPushButton))
    mouseClick(waitForObject(names.wdScrollArea_lbText_WdLabel_9), 131, 106, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.wdScrollArea_text_QLabel_10), 190, 40, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frRightButtons_lbIcon_WdIcon_7), 21, 8, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frLeftButtons_lbIcon_WdIcon_14), 162, 16, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frLeftButtons_lbIcon_WdIcon_7), 171, 16, Qt.NoModifier, Qt.LeftButton)
 
    # test.compare(str(waitForObjectExists(names.wdTitleBar_text_QLabel_2).text), "Inicio")
    # test.compare(str(waitForObjectExists(names.homeScreen_lbText_QLabel_3).text), "Mis preajustes")
    # test.compare(str(waitForObjectExists(names.homeScreen_lbText_QLabel_5).text), "Manual")
    # test.compare(str(waitForObjectExists(names.homeScreen_lbText_QLabel_2).text), "Litotricia")
    # test.compare(str(waitForObjectExists(names.homeScreen_lbText_QLabel).text), "Tejido blando")
    # test.compare(str(waitForObjectExists(names.homeScreen_lbText_QLabel_4).text), "HPB")
    #
    # test.breakpoint()
    ActualText = str(waitForObjectExists(names.wdTitleBar_text_QLabel_2).text)
    expectedText = sheet.cell(row=2, column=2).value
    test.compare(expectedText, ActualText, "text is matching")
    
    expectedText1 = sheet.cell(row=3, column=2).value
    ActualText1 = str(waitForObjectExists(names.homeScreen_lbText_QLabel_3).text)
    test.compare(expectedText1, ActualText1, "text is matching") 
    
    expectedText2 = sheet.cell(row=4, column=2).value
    ActualText2 = str(waitForObjectExists(names.homeScreen_lbText_QLabel_5).text)
    test.compare(expectedText2, ActualText2, "text is matching") 
    
    expectedText3 = sheet.cell(row=5, column=2).value
    ActualText3 = str(waitForObjectExists(names.homeScreen_lbText_QLabel_2).text)
    test.compare(expectedText3, ActualText3, "text is matching")
    
    expectedText4 = sheet.cell(row=6, column=2).value
    ActualText4 = str(waitForObjectExists(names.homeScreen_lbText_QLabel).text)
    test.compare(expectedText4, ActualText4, "text is matching")
    
    expectedText5 = sheet.cell(row=7, column=2).value
    ActualText5 = str(waitForObjectExists(names.homeScreen_lbText_QLabel_4).text)
    test.compare(expectedText5, ActualText5, "text is matching")
    
    # expectedText6 = sheet.cell(row=8, column=2).value
    # ActualText6 = str(waitForObjectExists(names.frLeftButtons_lbText_QLabel).text)
    # test.compare(expectedText6, ActualText6, "text is matching")

    test.compare(str(waitForObjectExists(names.frLeftButtons_lbText_QLabel).text), "Cerrar sesi\nón")
    test.vp("VP2")
    
    
  

 
     
    
    
 
    
    
       
      
