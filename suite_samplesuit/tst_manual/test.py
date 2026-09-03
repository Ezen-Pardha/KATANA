# -*- coding: utf-8 -*-

import names


def main():
    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 123, 64, 783, 80)
    snooze(0.3)

    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 133, 63, 793, 79)
    snooze(0.3)

    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    snooze(0.3)

    mouseClick(waitForObject(names.homeScreen_lbIcon_WdIcon_2), 184, 46, Qt.NoModifier, Qt.LeftButton)
    snooze(0.3)

    clickButton(waitForObject(names.treatmentScreen_Error_WdPushButton))
    snooze(0.3)

    doubleClick(waitForObject(names.treatmentScreen_Error_WdPushButton), 218, 75, Qt.NoModifier, Qt.LeftButton)
    snooze(0.3)

    doubleClick(waitForObject(names.wdPulseEnergyPickerWheel_btIncrease_WdPushButton), 61, 81, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.wdPulseEnergyPickerWheel_btIncrease_WdPushButton))
    clickButton(waitForObject(names.wdFrequencyPickerWheel_btIncrease_WdPushButton))

    test.breakpoint()

    clickButton(waitForObject(names.treatmentScreen_Error_WdPushButton))
    snooze(0.3)

    button = waitForObject(names.treatmentScreen_Error_WdPushButton)
    test.compare(button.text, "Error")

    doubleClick(waitForObject(names.treatmentScreen_Error_WdPushButton), 253, 69, Qt.NoModifier, Qt.LeftButton)
    snooze(0.3)

    mouseClick(waitForObject(names.treatmentScreen_lbIcon_WdIcon_3), 55, 34, Qt.NoModifier, Qt.LeftButton)
    snooze(0.3)
    
    mouseClick(waitForObject(names.wdRadioButtons_lbIcon_WdIcon), 33, 66, Qt.NoModifier, Qt.LeftButton)
    snooze(0.3)
   
    mouseClick(waitForObject(names.wdPopup_lbText_QLabel_5), 13, 50, Qt.NoModifier, Qt.LeftButton)
    snooze(0.3)
    

    # label = waitForObject(names.wdPopup_lbText_QLabel_5)
    # test.compare(label.text, "Continuous")

    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon_2), 131, 9, Qt.NoModifier, Qt.LeftButton)
    snooze(0.3)
