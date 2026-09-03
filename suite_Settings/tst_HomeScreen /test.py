# -*- coding: utf-8 -*-

import names
from openpyxl import load_workbook

def main():
    
    excelFile = "/home/ezen/Desktop/stringsheet.xlsx"

    workbook = load_workbook(excelFile)
    sheet = workbook["Sheet2"]
    
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))

    expectedText = sheet.cell(row=2, column=2).value

    test.compare(str(waitForObjectExists(names.wdTitleBar_text_QLabel_2).text), "Home")
    
    text1 = str(waitForObjectExists(names.wdTitleBar_text_QLabel_2).text)
         
    test.compare(expectedText, text1, "text compared")
           
    test.breakpoint()
    
    
    
    # ocr1 = test.ocrTextPresent("Home")
    # print(ocr1)
    # test.compare(expectedText, ocr1, "text compared")
    
    # Get the button object
    button = waitForObject(
    names.homeScreen_btMyPresets_WdToolButton)

     # Read actual button text
    actualText = button.text 

# Compare button text with Excel
    test.compare(
    str(actualText).strip(),
    str(expectedText).strip()  
             )
    test.passes("My Presets button String is compared with Excel data its matching") 
    mouseClick(waitForObject(names.homeScreen_lbIcon_WdIcon_2), 457, 84, Qt.NoModifier, Qt.LeftButton)   
    mouseClick(waitForObject(names.frLeftButtons_lbIcon_WdIcon_2), 163, 34, Qt.NoModifier, Qt.LeftButton)
    expectedText1 = sheet.cell(row=3, column=2).value

    # Get the button object
    button1 = waitForObject(
    names.homeScreen_btManual_WdToolButton) 

     # Read actual button text
    actualText1 = button1.text 

# Compare button text with Excel
    test.compare(
    str(actualText1).strip(),
    str(expectedText1).strip() 
             )
    test.passes("Manual button String is compared with Excel data its matching")
    mouseClick(waitForObject(names.homeScreen_lbIcon_WdIcon), 131, 113, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.treatmentScreen_lbIcon_WdIcon), 133, 37, Qt.NoModifier, Qt.LeftButton)
    expectedText2 = sheet.cell(row=4, column=2).value

    # Get the button object
    button2 = waitForObject(
    names.homeScreen_btLithotripsy_WdToolButton
                           )
    
     # Read actual button text
    actualText2 = button2.text 

# Compare button text with Excel
    test.compare(
    str(actualText2).strip(),
    str(expectedText2).strip() 
                )
    test.passes("Lithotripsy button String is compared with Excel data its matching")            
    mouseClick(waitForObject(names.homeScreen_lbIcon_WdIcon_4), 347, 51, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frLeftButtons_lbText_QLabel_2), 111, 34, Qt.NoModifier, Qt.LeftButton) 
    expectedText3 = sheet.cell(row=5, column=2).value

    # Get the button object
    button3 = waitForObject(
    names.homeScreen_btSoftTissue_WdToolButton 
                           ) 
    
     # Read actual button text
    actualText3 = button3.text 

# Compare button text with Excel
    test.compare(
    str(actualText3).strip(),
    str(expectedText3).strip() 
                ) 
    test.passes("SoftTissue button String is compared with Excel data its matching")
    mouseClick(waitForObject(names.homeScreen_lbText_QLabel), 64, 6, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frLeftButtons_lbIcon_WdIcon_3), 109, 25, Qt.NoModifier, Qt.LeftButton)
    expectedText4 = sheet.cell(row=6, column=2).value

    # Get the button object
    button4 = waitForObject(
    names.homeScreen_btBph_WdToolButton  
                           ) 
    
     # Read actual button text
    actualText4 = button4.text   

# Compare button text with Excel
    test.compare(
    str(actualText4).strip(), 
    str(expectedText4).strip() 
                ) 
    test.passes("BPH button String is compared with Excel data its matching")
    mouseClick(waitForObject(names.homeScreen_lbIcon_WdIcon_3), 20, 55, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frLeftButtons_lbText_QLabel_2), 118, 7, Qt.NoModifier, Qt.LeftButton)
    expectedText5 = sheet.cell(row=7, column=2).value

    # Get the button object
    button5 = waitForObject(
    names.frRightButtons_Settings_right_WdToolButton 
                           ) 
    
     # Read actual button text
    actualText5 = button5.text 
   
# Compare button text with Excel
    test.compare(
    str(actualText5).strip(), 
    str(expectedText5).strip() 
                ) 
    test.passes("Settings button String is compared with Excel data its matching")
    mouseClick(waitForObject(names.frRightButtons_lbIcon_WdIcon), 54, 26, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frLeftButtons_lbText_QLabel_3), 76, 7, Qt.NoModifier, Qt.LeftButton)  
    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 318, 98, 743, 115)
    expectedText6 = sheet.cell(row=8, column=2).value

    # Get the button object
    button6 = waitForObject(
    names.frLeftButtons_Log_off_left_WdToolButton 
                           ) 
    
     # Read actual button text
    actualText6 = button6.text 

# Compare button text with Excel
    test.compare(
    str(actualText6).strip(),  
    str(expectedText6).strip() 
                ) 
    test.passes("Logoff button String is compared with Excel data its matching")
