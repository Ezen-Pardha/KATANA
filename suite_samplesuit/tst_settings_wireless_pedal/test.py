# -*- coding: utf-8 -*-

import names


def main():
    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 39, 82, 483, 101)
    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 40, 90, 484, 109)
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    mouseClick(waitForObject(names.frRightButtons_lbText_QLabel_2), 106, 8, Qt.NoModifier, Qt.LeftButton)
    test.passes("Navigated to Settings screen successfully")
    mouseClick(waitForObject(names.wdScrollArea_text_QLabel_2), 137, 18, Qt.NoModifier, Qt.LeftButton)
    test.passes("Navigated to Wireless pedal screen successfully")
    test.vp("VP1")
    test.passes("verified setting_wireless_footswitch")
    test.vp("VP2")
    test.passes("verified setting_wireless_footswitch")
    test.vp("VP3")
    test.passes("verified continue button")
    clickButton(waitForObject(names.wirelessPedalPairingScreen_pbContinue_QToolButton))

    test.vp("VP1")
    test.passes("verified setting_wireless_footswitch")
    
    test.vp("VP3")
    test.passes("verified continue button")
   
    clickButton(waitForObject(names.wirelessPedalPairingScreen_pbContinue_QToolButton))

    test.vp("VP10")
    test.passes('verified settings button')
    
    mouseClick(waitForObject(names.frRightButtons_lbIcon_WdIcon), 37, 4, Qt.NoModifier, Qt.LeftButton)

    test.vp("VP11")
    test.passes("verified wireless Pedal button")
   
    mouseClick(waitForObject(names.wdScrollArea_text_QLabel_2), 146, 31, Qt.NoModifier, Qt.LeftButton)

    test.vp("VP12")
    test.passes("Verified wireless pedal paird screen")
    snooze(2)

    test.vp("VP13")
    test.passes("click action done on unpair footswitch")
    clickButton(waitForObject(names.wirelessPedalPairingScreen_pbContinue_QToolButton))

    mouseClick(waitForObject(names.wirelessPedalPairingScreen_lbCenterLeftImage_QLabel), 348, 322, Qt.NoModifier, Qt.LeftButton)

