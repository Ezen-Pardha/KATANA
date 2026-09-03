# -*- coding: utf-8 -*-

import names


def main():
    startApplication("katana")
    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon), 109, 32, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    mouseClick(waitForObject(names.frLeftButtons_lbIcon_WdIcon), 120, 10, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon_2), 102, 40, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.numpad_pbMiddleMiddle_NumpadButton))
    clickButton(waitForObject(names.numpad_pbMiddleRight_NumpadButton))
    clickButton(waitForObject(names.numpad_pbTopRight_NumpadButton))
    clickButton(waitForObject(names.numpad_pbTopMiddle_NumpadButton))
    clickButton(waitForObject(names.numpad_pbBottomLeft_NumpadButton))
    clickButton(waitForObject(names.numpad_pbBottomMiddle_NumpadButton))
    clickButton(waitForObject(names.numpad_pbBottomRight_NumpadButton))
    clickButton(waitForObject(names.numpad_pbMiddleLeft_NumpadButton))
    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 123, 382, 997, 403)
