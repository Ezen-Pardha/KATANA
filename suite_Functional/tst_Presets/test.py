# -*- coding: utf-8 -*-

import names

def main():
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    mouseClick(waitForObject(names.homeScreen_lbIcon_WdIcon_2), 289, 114, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frRightButtons_lbText_QLabel_2), 198, 29, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.frRightButtons_lbIcon_WdIcon), 101, 25, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.keyboardPopup_wdEdit_WdLineEdit), "<CapsLock>")
    type(waitForObject(names.keyboardPopup_wdEdit_WdLineEdit), "O")
    type(waitForObject(names.keyboardPopup_wdEdit_WdLineEdit), "<CapsLock>")
    type(waitForObject(names.keyboardPopup_wdEdit_WdLineEdit), "ne ")
    type(waitForObject(names.keyboardPopup_wdEdit_WdLineEdit), "<CapsLock>")
    type(waitForObject(names.keyboardPopup_wdEdit_WdLineEdit), "P")
    type(waitForObject(names.keyboardPopup_wdEdit_WdLineEdit), "<CapsLock>")
    type(waitForObject(names.keyboardPopup_wdEdit_WdLineEdit), "hysician")
    mouseClick(waitForObject(names.keyboardPopup_lbText_QLabel), 82, 15, Qt.NoModifier, Qt.LeftButton)
    snooze(5)
    mouseClick(waitForObject(names.frLeftButtons_lbIcon_WdIcon), 73, 45, Qt.NoModifier, Qt.LeftButton)
    snooze(5)
    #test.ocrTextPresent("One Physician")
    test.vp("Physician Name")
    #test.breakpoint()
    
