# -*- coding: utf-8 -*-

import names


def main():
    mouseClick(waitForObject(names.wdPopup_lbText_QLabel), 56, 1, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    mouseClick(waitForObject(names.frLeftButtons_lbIcon_WdIcon), 155, 28, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon_2), 64, 30, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.numpad_pbBottomLeft_NumpadButton))
    test.breakpoint()
    clickButton(waitForObject(names.numpad_pbBottomMiddle_NumpadButton))
    clickButton(waitForObject(names.numpad_pbBottomRight_NumpadButton))
    clickButton(waitForObject(names.numpad_pbMiddleLeft_NumpadButton))
    