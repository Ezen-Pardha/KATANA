# -*- coding: utf-8 -*-

import names


def main():
    startApplication("katana")
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    snooze(1)
    mouseClick(waitForObject(names.frRightButtons_lbIcon_WdIcon_2), 83, 29, Qt.NoModifier, Qt.LeftButton)
    snooze(1)
    mouseClick(waitForObject(names.wdScrollArea_text_QLabel_2), 194, 31, Qt.NoModifier, Qt.LeftButton)
    snooze(1)    
    mouseClick(waitForObject(names.frRightButtons_lbIcon_WdIcon_3), 102, 44, Qt.NoModifier, Qt.LeftButton)
    snooze(1)
    mouseClick(waitForObject(names.keyboardPopup_lbText_QLabel), 122, 19, Qt.NoModifier, Qt.LeftButton)
    snooze(1)
    mouseClick(waitForObject(names.frLeftButtons_lbText_QLabel_8), 98, 5, Qt.NoModifier, Qt.LeftButton)
    snooze(1)
    mouseClick(waitForObject(names.wdScrollArea_text_QLabel_6), 110, 4, Qt.NoModifier, Qt.LeftButton)
    snooze(1)
    mouseClick(waitForObject(names.frLeftButtons_lbText_QLabel_9), 106, 3, Qt.NoModifier, Qt.LeftButton)
    snooze(1)
    mouseClick(waitForObject(names.frLeftButtons_lbIcon_WdIcon_8), 120, 28, Qt.NoModifier, Qt.LeftButton)
