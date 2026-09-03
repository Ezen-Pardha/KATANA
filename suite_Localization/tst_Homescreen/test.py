# -*- coding: utf-8 -*-

import names

# from openpyxl import load_workbook

def main():
    
    snooze(5)
    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon_2), 107, 28, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
   
    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon_2), 78, 35, Qt.NoModifier, Qt.LeftButton)
    snooze(5)
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    snooze(2)
    sendEvent("QCloseEvent", waitForObject(names.o_ScreenSwitcher))
   

    test.compare(str(waitForObjectExists(names.wdTitleBar_text_QLabel).text), "Home")
    
    expectedText = sheet.cell(row=9, column=2).value
    
    
    text1 = str(waitForObjectExists(names.wdTitleBar_text_QLabel).text)
    # test.compare(expectedText, text1, "text compared")

    test.verify(expectedText, text1, "text compared")
    mouseClick(waitForObject(names.homeScreen_lbText_QLabel), 376, 33, Qt.NoModifier, Qt.LeftButton)
    
    mouseClick(waitForObject(names.frLeftButtons_lbIcon_WdIcon), 145, 17, Qt.NoModifier, Qt.LeftButton)
    test.compare(str(waitForObjectExists(names.homeScreen_lbText_QLabel).text), "My Presets")
    
    mouseClick(waitForObject(names.homeScreen_lbText_QLabel_2), 109, 4, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.treatmentScreen_lbIcon_WdIcon), 112, 14, Qt.NoModifier, Qt.LeftButton)

    test.compare(str(waitForObjectExists(names.homeScreen_lbText_QLabel_2).text), "Manual")
    
    mouseClick(waitForObject(names.homeScreen_lbText_QLabel_3), 243, 14, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frLeftButtons_lbIcon_WdIcon_2), 142, 16, Qt.NoModifier, Qt.LeftButton)

    test.compare(str(waitForObjectExists(names.homeScreen_lbText_QLabel_3).text), "Lithotripsy")
    mouseClick(waitForObject(names.homeScreen_lbText_QLabel_4), 265, 21, Qt.NoModifier, Qt.LeftButton)
   

    mouseClick(waitForObject(names.frLeftButtons_lbIcon_WdIcon_2), 134, 19, Qt.NoModifier, Qt.LeftButton)
    test.compare(str(waitForObjectExists(names.homeScreen_lbText_QLabel_4).text), "Soft Tissue")
    
    mouseClick(waitForObject(names.homeScreen_lbIcon_WdIcon), 143, 70, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frLeftButtons_lbIcon_WdIcon_2), 158, 18, Qt.NoModifier, Qt.LeftButton)

    test.compare(str(waitForObjectExists(names.homeScreen_lbText_QLabel_5).text), "BPH")
    
    mouseClick(waitForObject(names.frLeftButtons_lbIcon_WdIcon_3), 94, 14, Qt.NoModifier, Qt.LeftButton)

    
    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon), 103, 5, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frRightButtons_lbIcon_WdIcon), 34, 17, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frLeftButtons_lbIcon_WdIcon_4), 83, 15, Qt.NoModifier, Qt.LeftButton)
    
    test.ocrTextPresent("Home", { "tesseract": { "psm": 6 } })
    test.passes("Home screen verified successfully")
    


    
    
