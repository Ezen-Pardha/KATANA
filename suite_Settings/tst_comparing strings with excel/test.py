# -*- coding: utf-8 -*-

import names
from openpyxl import load_workbook

def main():

    excelFile = "/home/ezen/Desktop/stringsheet.xlsx"

    workbook = load_workbook(excelFile)
    sheet = workbook["Sheet1"]

    # Read expected button text from Excel
    expectedText = sheet.cell(row=2, column=2).value

    # Get actual button text from the application
    button = waitForObject(names.footswitchPopup_pbWired_WdPushButton)
    actualText = button.text
    test.passes("Wired Button String is verified with excel data")
    # Compare button text
    test.compare(actualText, expectedText)

    # Continue only if the text matches
    clickButton(button)

    sendEvent("QWheelEvent", waitForObject(names.homeScreen_lbIcon_WdIcon_3),
              220, 89, -120, 0, 2)
    sendEvent("QWheelEvent", waitForObject(names.homeScreen_lbIcon_WdIcon_3),
              220, 89, -120, 0, 2)

    
    expectedText1=sheet.cell(row=4,column=3).value
    
    titleBar = waitForObject(names.homeScreen_wdTitleBar_WdTitleBar)
    # Find QLabel inside WdTitleBar
    titleLabel = waitForObject({
    "container": names.homeScreen_wdTitleBar_WdTitleBar,
    "name": "text",
    "type": "QLabel",
    "visible": 1
           })


    actualText1 = titleLabel.text
    
    test.compare(actualText1, expectedText1)
    test.passes("Home title String is verified with excel data")
    # Get actual button text from the application
    

    mouseClick(waitForObject(names.frLeftButtons_lbIcon_WdIcon),
               158, 7, Qt.NoModifier, Qt.LeftButton)

    mouseClick(waitForObject(names.wdPopup_lbText_QLabel),
               68, 1, Qt.NoModifier, Qt.LeftButton)
    snooze(1)
    #  clickButton(waitForObject(names.numpad_pbBottomLeft_NumpadButton))
    btn1 = waitForObject(names.numpad_pbBottomLeft_NumpadButton)
    test.log("Button 1 text: " + str(btn1.text))
    clickButton(btn1)
    snooze(1)
    btn2 = waitForObject(names.numpad_pbBottomMiddle_NumpadButton)   
    test.log("Button 2 text: " + str(btn2.text))
    clickButton(btn2)
    # clickButton(waitForObject(names.numpad_pbBottomMiddle_NumpadButton))
    snooze(1)
    #clickButton(waitForObject(names.numpad_pbBottomRight_NumpadButton))
    btn3 = waitForObject(names.numpad_pbBottomRight_NumpadButton)
    test.log("Button 3 text: " + str(btn3.text))
    clickButton(btn3)
    snooze(1)
    #clickButton(waitForObject(names.numpad_pbMiddleLeft_NumpadButton))
    btn4 = waitForObject(names.numpad_pbMiddleLeft_NumpadButton)
    test.log("Button 4 text: " + str(btn4.text))
    clickButton(btn4)
    snooze(1)
    clickButton(waitForObject(names.wdPopup_btAccept_WdToolButton))
    snooze(1)
    clickButton(waitForObject(names.wdPopup_btAccept_WdToolButton))
    snooze(1)
    clickButton(waitForObject(names.wdPopup_btAccept_WdToolButton))
    snooze(1)
    clickButton(waitForObject(names.wdPopup_btAccept_WdToolButton))
    snooze(1)
    clickButton(waitForObject(names.wdPopup_btAccept_WdToolButton))
    snooze(1)
    workbook.close()
