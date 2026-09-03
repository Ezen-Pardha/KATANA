# -*- coding: utf-8 -*-

import names

from openpyxl import load_workbook

def main():
    excelpath = "/home/ezen/Desktop/stringsheet.xlsx"
    workbook = load_workbook(excelpath)
    sheet = workbook["Sheet7"]
    
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    mouseClick(waitForObject(names.frRightButtons_lbIcon_WdIcon), 132, 39, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.wdScrollArea_btDownArrow_WdPushButton))
    mouseClick(waitForObject(names.wdScrollArea_text_QLabel_3), 214, 14, Qt.NoModifier, Qt.LeftButton)
    
    expectedText1 = sheet.cell(row=2, column=2).value
    ActualText1 = str(waitForObjectExists(names.wdTitleBar_text_QLabel_3).text)           
    test.compare(expectedText1, ActualText1)      
    
    expectedText2 = sheet.cell(row=3, column=2).value
    ActualText2 = str(waitForObjectExists(names.softwareVersionScreen_text_QLabel).text)           
    test.compare(expectedText2, ActualText2)  
    
    expectedText3 = sheet.cell(row=4, column=2).value
    ActualText3 = str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_2).text)           
    test.compare(expectedText3, ActualText3)  
    
    expectedText4 = sheet.cell(row=5, column=2).value
    ActualText4 = str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_3).text)           
    test.compare(expectedText4, ActualText4)  
    
    expectedText5 = str(sheet.cell(row=6, column=2).value)
    ActualText5 = str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_4).text)           
    test.compare(expectedText5, ActualText5)
     
    expectedText6 = sheet.cell(row=7, column=2).value
    ActualText6 = str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_5).text)           
    test.compare(expectedText6, ActualText6)
    
    
    expectedText7 = str(sheet.cell(row=8, column=2).value)
    ActualText7 = str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_6).text)           
    test.compare(expectedText7, ActualText7)
    
    # test.compare(str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_7).text), "Controller FPGA:")
    # test.compare(str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_8).text), "1.2")
    # test.compare(str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_9).text), "Laser Module MCU:")
    # test.compare(str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_10).text), "58.2.1")
    # test.compare(str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_11).text), "Laser Module FPGA:")
    # test.compare(str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_12).text), "8.20.1")
    #
    # test.compare(str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_13).text), "Factory Procedures:")
    # test.compare(str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_14).text), "1")
    # test.compare(str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_15).text), "Safety Board MCU:")
    # test.compare(str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_16).text), "1.3")
    # test.compare(str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_17).text), "Safety Board FPGA:")
    # test.compare(str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_18).text), "1.3")
    # test.compare(str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_19).text), "Optical Board MCU:")
    # test.compare(str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_20).text), "1.6")
    # test.compare(str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_21).text), "Optical Board FPGA:")
    # test.compare(str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_22).text), "1.5")
    #
    
    expectedText8 = str(sheet.cell(row=9, column=2).value)
    ActualText8 = str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_7).text)           
    test.compare(expectedText8, ActualText8)
    
    expectedText9 = str(sheet.cell(row=10, column=2).value)
    ActualText9 = str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_8).text)           
    test.compare(expectedText9, ActualText9)
    
    expectedText10 = str(sheet.cell(row=11, column=2).value)
    ActualText10 = str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_9).text)           
    test.compare(expectedText10, ActualText10)
    
    expectedText11 = str(sheet.cell(row=11, column=2).value)
    ActualText11 = str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_10).text)           
    test.compare(expectedText11, ActualText11)
    
    expectedText12 = str(sheet.cell(row=11, column=2).value)
    ActualText12 = str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_11).text)           
    test.compare(expectedText12, ActualText12)
    
    expectedText13 = str(sheet.cell(row=11, column=2).value)
    ActualText13 = str(waitForObjectExists(names.softwareVersionScreen_text_QLabel_12).text)           
    test.compare(expectedText13, ActualText13) 
    
    
    
    