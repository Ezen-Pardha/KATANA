# -*- coding: utf-8 -*-

import names


def main():
    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 360, 146, 837, 164)
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    mouseClick(waitForObject(names.frRightButtons_lbIcon_WdIcon), 65, 31, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.wdScrollArea_btDownArrow_WdPushButton))
    mouseClick(waitForObject(names.wdScrollArea_text_QLabel_2), 153, 29, Qt.NoModifier, Qt.LeftButton)
    test.vp("VP1")
