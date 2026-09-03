# -*- coding: utf-8 -*-

import names


def main():
    
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    mouseClick(waitForObject(names.frLeftButtons_lbText_QLabel), 161, 0, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon), 28, 28, Qt.NoModifier, Qt.LeftButton)
    snooze(1)
    clickButton(waitForObject(names.numpad_pbBottomLeft_NumpadButton))
    snooze(1)
    clickButton(waitForObject(names.numpad_pbBottomMiddle_NumpadButton))
    snooze(1)
    clickButton(waitForObject(names.numpad_pbBottomRight_NumpadButton))
    snooze(1)
    clickButton(waitForObject(names.numpad_pbMiddleLeft_NumpadButton))
    snooze(1)
    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon_2), 30, 29, Qt.NoModifier, Qt.LeftButton)
    snooze(1)
    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon_2), 30, 29, Qt.NoModifier, Qt.LeftButton)
    snooze(1)
    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon_2), 30, 29, Qt.NoModifier, Qt.LeftButton)
    snooze(1)
    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon_2), 30, 29, Qt.NoModifier, Qt.LeftButton)
    snooze(1)
    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon_2), 30, 29, Qt.NoModifier, Qt.LeftButton)
    detail="User sccussfully logged in"
    test.log("sccussfully logged in", detail)