# -*- coding: utf-8 -*-

import names




def main():
    
    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 153, 65, 841, 87)
sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 128, 72, 816, 94)
sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 127, 72, 815, 94)

mouseClick(waitForObject(names.wdPopup_lbText_QLabel_5), 99, 5, Qt.NoModifier, Qt.LeftButton)

clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))

# Verify Settings button exists
settingsBtn = waitForObject(names.frRightButtons_lbText_QLabel_2)

# Click Settings button
mouseClick(settingsBtn, 32, 11, Qt.NoModifier, Qt.LeftButton)

# Verify Settings screen opened

waitForObject(names.wdScrollArea_lbText_WdLabel_2)
test.passes("Navigated to Settings screen successfully")


mouseClick(waitForObject(names.wdScrollArea_lbText_WdLabel_2), 87, 93, Qt.NoModifier, Qt.LeftButton)
AddEditpresetBtn = waitForObject(names.frRightButtons_lbText_QLabel_3)
test.passes("Navigated to Add/Edit Physicians screen successfully")
mouseClick(waitForObject(names.frRightButtons_lbText_QLabel_3), 100, 13, Qt.NoModifier, Qt.LeftButton)

clickButton(waitForObject(names.keyboardPopup_t_KeyButton))
clickButton(waitForObject(names.keyboardPopup_e_KeyButton))
clickButton(waitForObject(names.keyboardPopup_s_KeyButton))
clickButton(waitForObject(names.keyboardPopup_t_KeyButton))

mouseClick(waitForObject(names.keyboardPopup_lbIcon_WdIcon), 18, 18, Qt.NoModifier, Qt.LeftButton)
test.log("Physician Created successfully")
mouseClick(waitForObject(names.wdScrollArea_text_QLabel_3), 241, 29, Qt.NoModifier, Qt.LeftButton)
mouseClick(waitForObject(names.frRightButtons_lbText_QLabel_4), 95, 14, Qt.NoModifier, Qt.LeftButton)

clickButton(waitForObject(names.keyboardPopup_btNumbersAlphabet_WdPushButton))
clickButton(waitForObject(names.keyboardPopup_1_KeyButton))
test.log("Physician Edited successfully")

mouseClick(waitForObject(names.keyboardPopup_lbText_QLabel), 185, 13, Qt.NoModifier, Qt.LeftButton)
# mouseClick(waitForObject(names.wdPopup_lbText_QLabel_5), 119, 13, Qt.NoModifier, Qt.LeftButton)
mouseClick(waitForObject(names.frRightButtons_lbText_QLabel_5), 64, 7, Qt.NoModifier, Qt.LeftButton)
mouseClick(waitForObject(names.wdPopup_lbText_QLabel_6), 113, 19, Qt.NoModifier, Qt.LeftButton)
test.log("Physician Deleted successfully")

