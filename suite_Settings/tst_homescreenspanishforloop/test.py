# -*- coding: utf-8 -*-
 
import names

from openpyxl import load_workbook
 
 
# --------------------------------------------------

# Excel File

# --------------------------------------------------

EXCEL_FILE = "/home/ezen/Desktop/Katana All Strings.xlsx"

SHEET_NAME = "Katana Strings"
 
 
# --------------------------------------------------

# Load Spanish strings for Home Screen (HM)

# --------------------------------------------------

def loadSpanishStrings():
 
    wb = load_workbook(EXCEL_FILE)

    sheet = wb[SHEET_NAME]
 
    spanishStrings = []
 
    for row in sheet.iter_rows(min_row=2, values_only=True):
 
        module = row[0]

        english = row[1]

        spanish = row[2]
 
        if module == "HM" and spanish:

            spanishStrings.append(str(spanish).strip())
 
    test.log("Loaded Home Screen Spanish Strings : " + str(len(spanishStrings)))
 
    return spanishStrings
 
 
# --------------------------------------------------

# Read Home Screen Text

# --------------------------------------------------

def verifyTexts(obj, expectedTexts):
 
    try:
 
        if obj.inherits("QLabel"):
 
            txt = str(obj.text).strip()
 
            if txt != "":
 
                test.log("Detected : " + txt)
 
                if txt in expectedTexts:

                    test.passes("Verified : " + txt)

                else:

                    test.fail("Not Found In Excel : " + txt)
 
    except:

        pass
 
    try:
 
        for child in object.children(obj):

            verifyTexts(child, expectedTexts)
 
    except:

        pass
 
 
# --------------------------------------------------

# Main

# --------------------------------------------------

def main():
 
    # -----------------------------

    # Load Excel

    # -----------------------------

    expectedSpanish = loadSpanishStrings()
 
    # -----------------------------

    # Change Language to Spanish

    # -----------------------------

    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
 
    mouseClick(waitForObject(names.frRightButtons_lbText_QLabel_2),

               122, 8, Qt.NoModifier, Qt.LeftButton)
 
    clickButton(waitForObject(names.wdScrollArea_btDownArrow_WdPushButton))
 
    mouseClick(waitForObject(names.wdScrollArea_text_QLabel_6),

               227, 40, Qt.NoModifier, Qt.LeftButton)
 
    mouseClick(waitForObject(names.wdScrollArea_text_QLabel_7),

               305, 11, Qt.NoModifier, Qt.LeftButton)
 
    mouseClick(waitForObject(names.frRightButtons_lbIcon_WdIcon_4),

               34, 21, Qt.NoModifier, Qt.LeftButton)
 
    mouseClick(waitForObject(names.frLeftButtons_lbText_QLabel_4),

               156, 16, Qt.NoModifier, Qt.LeftButton)
 
    mouseClick(waitForObject(names.frLeftButtons_lbText_QLabel_2),

               156, 16, Qt.NoModifier, Qt.LeftButton)
 
    mouseClick(waitForObject(names.frLeftButtons_lbIcon_WdIcon),

               130, 25, Qt.NoModifier, Qt.LeftButton)
 
    snooze(3)
 
    # -----------------------------

    # Login

    # -----------------------------

    mouseClick(waitForObject(names.wdPopup_lbText_QLabel_2),

               77, 32, Qt.NoModifier, Qt.LeftButton)
 
    snooze(5)
 
    clickButton(waitForObject(names.numpad_pbBottomLeft_NumpadButton))

    clickButton(waitForObject(names.numpad_pbBottomMiddle_NumpadButton))

    clickButton(waitForObject(names.numpad_pbBottomRight_NumpadButton))

    btn4 = waitForObject(names.numpad_pbMiddleLeft_NumpadButton)

    test.log("Key Pressed: " + str(btn4.text))

    clickButton(btn4)
 
    snooze(1)
 
    clickButton(waitForObject(names.wdPopup_lbText_QLabel_4))
 
    snooze(5)
 
    mouseClick(waitForObject(names.wdPopup_lbText_QLabel_5),

               168, 13, Qt.NoModifier, Qt.LeftButton)
 
    snooze(8)
 
    # -----------------------------

    # Read Home Screen

    # -----------------------------
 
    test.vp("VP1")
 
    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon_6), 84, 41, Qt.NoModifier, Qt.LeftButton)

    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon_6), 84, 41, Qt.NoModifier, Qt.LeftButton)

    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon_6), 84, 41, Qt.NoModifier, Qt.LeftButton)

 
    

    home = waitForObject(names.homeScreen_HomeScreen)

    test.log("====================================")

    test.log("Reading Home Screen Spanish Strings")

    test.log("====================================")
 
    verifyTexts(home, expectedSpanish)
 
 
    
 
    test.log("Verification Completed")

 