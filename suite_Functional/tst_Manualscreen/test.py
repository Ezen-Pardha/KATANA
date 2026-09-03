# -*- coding: utf-8 -*-

import names


def main():
    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon_3), 100, 19, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    sendEvent("QWheelEvent", waitForObject(names.homeScreen_lbText_QLabel_4), 273, 14, -120, 0, 2)
    mouseClick(waitForObject(names.homeScreen_lbText_QLabel_5), 323, 8, Qt.NoModifier, Qt.LeftButton)
    snooze(3)
    test.vp("VP1")
    snooze(3)
    test.vp("VP2")
    snooze(3)
