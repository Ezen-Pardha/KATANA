# -*- coding: utf-8 -*-

import names


def main():
    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 76, 67, 797, 84)
    snooze(0.3)
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    snooze(0.3)
    mouseClick(waitForObject(names.homeScreen_lbIcon_WdIcon), 257, 7, Qt.NoModifier, Qt.LeftButton)
    snooze(0.3)
    mouseClick(waitForObject(names.wdScrollArea_lbText_WdOutlinedLabel), 97, 40, Qt.NoModifier, Qt.LeftButton)
    snooze(0.3)
    doubleClick(waitForObject(names.wdPulseEnergyPickerWheel_btIncrease_WdPushButton), 48, 95, Qt.NoModifier, Qt.LeftButton)
    snooze(0.3)
    clickButton(waitForObject(names.wdPulseEnergyPickerWheel_btIncrease_WdPushButton))
    snooze(0.3)
    mouseClick(waitForObject(names.treatmentScreen_lbText_QLabel), 152, 19, Qt.NoModifier, Qt.LeftButton)
    snooze(0.3)
    mouseClick(waitForObject(names.savePresetScreen_lbText_QLabel), 162, 31, Qt.NoModifier, Qt.LeftButton)
    snooze(0.3) 
    type(waitForObject(names.keyboardPopup_wdEdit_WdLineEdit), "150")
    snooze(0.3)
    mouseClick(waitForObject(names.keyboardPopup_lbIcon_WdIcon), 97, 33, Qt.NoModifier, Qt.LeftButton)
    snooze(0.3)
    mouseClick(waitForObject(names.frRightButtons_wdBottom_QWidget), 140, 47, Qt.NoModifier, Qt.LeftButton)
    snooze(0.3) 
    mouseClick(waitForObject(names.treatmentScreen_lbText_QLabel_2), 143, 11, Qt.NoModifier, Qt.LeftButton)
    snooze(0.3)
    
