# -*- coding: utf-8 -*-

import names
import sys
import os

def main():

    # -------------------------------
    # Check openpyxl
    # -------------------------------
    try:
        from openpyxl import load_workbook
        test.log("openpyxl imported successfully.")
    except Exception as e:
        test.fail("Unable to import openpyxl")
        test.log(str(e))
        return

    # -------------------------------
    # Excel File Path
    # -------------------------------
    excelFile = "/home/ezen/stringssheet.xlsx"

    if not os.path.exists(excelFile):
        test.fail("Excel file not found")
        test.log("Expected Location : " + excelFile)
        return

    test.log("Excel File Found : " + excelFile)

    # -------------------------------
    # Open Workbook
    # -------------------------------
    try:
        wb = load_workbook(excelFile)
        sheet = wb["GUI Strings"]
        test.log("Workbook opened successfully.")
    except Exception as e:
        test.fail("Unable to open workbook")
        test.log(str(e))
        return

    # -------------------------------
    # Read First 5 Strings
    # -------------------------------
    test.log("========== Reading Excel ==========")

    count = 0

    # for row in sheet.iter_rows(min_row=2, values_only=True):
    #
    #     guiID = "" if row[0] is None else str(row[0])
    #     englishText = "" if row[1] is None else str(row[1])
    #
    #     test.log("GUI ID : " + guiID)
    #     test.log("English : " + englishText)
    #
    #     count += 1
    #
    #     if count == 5:
    #         break

    # -------------------------------
    # Recorded Script
    # -------------------------------

    sendEvent("QMoveEvent",waitForObject(names.o_ScreenSwitcher),69, 77, 654, 82)

    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))

    mouseClick(
        waitForObject(names.frLeftButtons_lbIcon_WdIcon),
        124, 25,
        Qt.NoModifier,
        Qt.LeftButton
    )

    mouseClick(waitForObject(names.wdPopup_lbText_QLabel_2),87, 19,Qt.NoModifier,Qt.LeftButton)
    snooze(3)
    btn1 = waitForObject(names.numpad_pbBottomLeft_NumpadButton)
    test.log("Key Pressed: " + str(btn1.text))
    clickButton(btn1)

    snooze(3)

    btn2 = waitForObject(names.numpad_pbBottomMiddle_NumpadButton)
    test.log("Key Pressed: " + str(btn2.text))
    clickButton(btn2)

    snooze(3)

    btn3 = waitForObject(names.numpad_pbBottomRight_NumpadButton)
    test.log("Key Pressed: " + str(btn3.text))
    clickButton(btn3)

    snooze(3)

    btn4 = waitForObject(names.numpad_pbMiddleLeft_NumpadButton)
    test.log("Key Pressed: " + str(btn4.text))
    clickButton(btn4)

    snooze(2)

    clickButton(waitForObject(names.wdPopup_lbText_QLabel_4))

    # -------------------------------
    # Close Workbook
    # -------------------------------
    wb.close()

    #test.log("========== Test Completed ==========")
    
    
    
    
    
    
    