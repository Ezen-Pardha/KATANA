# -*- coding: utf-8 -*-

import names

from openpyxl import load_workbook

def main():
    
    excelFile = "/home/ezen/Desktop/stringsheet.xlsx"
    workbook = load_workbook(excelFile)
    sheet = workbook["Sheet4"]
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    snooze(2)
    mouseClick(waitForObject(names.frRightButtons_lbIcon_WdIcon), 50, 7, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.wdScrollArea_lbText_WdLabel_7), 279, 101, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.wdScrollArea_text_QLabel_9), 312, 39, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frRightButtons_lbIcon_WdIcon_2), 122, 12, Qt.NoModifier, Qt.LeftButton)
    sendEvent("QWheelEvent", waitForObject(names.presetPedalScreen_Standard_PulseModeButton), 85, 108, -120, 0, 2)
    sendEvent("QWheelEvent", waitForObject(names.presetPedalScreen_PresetSquareModeWidget), 992, 558, -120, 0, 2)
    mouseClick(waitForObject(names.frRightButtons_lbIcon_WdIcon_3), 154, 10, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frRightButtons_lbIcon_WdIcon_3), 154, 10, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.summaryPresetScreen_lbText_QLabel), 289, 49, Qt.NoModifier, Qt.LeftButton)
    snooze(2)
    # clickButton(waitForObject(names.keyboardPopup_t_KeyButton))
    # clickButton(waitForObject(names.keyboardPopup_e_KeyButton))
    # clickButton(waitForObject(names.keyboardPopup_s_KeyButton))
    # clickButton(waitForObject(names.keyboardPopup_t_KeyButton))
    # clickButton(waitForObject(names.keyboardPopup_KeyButton_2))
    # clickButton(waitForObject(names.keyboardPopup_p_KeyButton))
    # clickButton(waitForObject(names.keyboardPopup_r_KeyButton))
    # clickButton(waitForObject(names.keyboardPopup_e_KeyButton))
    # clickButton(waitForObject(names.keyboardPopup_s_KeyButton))
    # clickButton(waitForObject(names.keyboardPopup_e_KeyButton))
    # clickButton(waitForObject(names.keyboardPopup_t_KeyButton))
    # clickButton(waitForObject(names.keyboardPopup_KeyButton_2))
    # clickButton(waitForObject(names.keyboardPopup_f_KeyButton))
    # clickButton(waitForObject(names.keyboardPopup_o_KeyButton))
    # clickButton(waitForObject(names.keyboardPopup_u_KeyButton))
    # clickButton(waitForObject(names.keyboardPopup_r_KeyButton))

    mouseClick(waitForObject(names.keyboardPopup_wdEdit_WdLineEdit), 104, 48, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.keyboardPopup_wdEdit_WdLineEdit), "test preset 2")
    mouseClick(waitForObject(names.keyboardPopup_lbIcon_WdIcon), 57, 18, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frRightButtons_lbIcon_WdIcon_4), 186, 1, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.wdCentral_lbText_QLabel), 129, 33, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.wdPopup_lbText_QLabel_4), 92, 24, Qt.NoModifier, Qt.LeftButton)
    snooze(5)
    clickButton(waitForObject(names.wdScrollArea_btDownArrow_WdPushButton_2))
    snooze(5)
    clickButton(waitForObject(names.wdScrollArea_btDownArrow_WdPushButton_2))
    snooze(5)
    clickButton(waitForObject(names.wdScrollArea_btDownArrow_WdPushButton_2))
    snooze(5)
    test.ocrTextPresent("test preset", { "occurrence": 2 }) 
    test.passes("Preset added successfully")
    
    
    
    
    
