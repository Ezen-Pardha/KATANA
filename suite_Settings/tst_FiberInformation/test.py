# -*- coding: utf-8 -*-

import names


def main():
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    test.passes("Wired button is clicked in footswich screen")
    mouseClick(waitForObject(names.frRightButtons_lbIcon_WdIcon), 34, 8, Qt.NoModifier, Qt.LeftButton)
    test.passes("Settings button is clicked in ")
    clickButton(waitForObject(names.wdScrollArea_btDownArrow_WdPushButton))
    mouseClick(waitForObject(names.wdScrollArea_lbText_WdLabel_3), 160, 93, Qt.NoModifier, Qt.LeftButton)
    sendEvent("QWheelEvent", waitForObject(names.fiberInfoScreen_wdTable_QWidget), 534, 461, -120, 0, 2)
    sendEvent("QWheelEvent", waitForObject(names.fiberInfoScreen_wdTable_QWidget), 534, 461, -120, 0, 2)
    sendEvent("QWheelEvent", waitForObject(names.fiberInfoScreen_wdTable_QWidget), 534, 461, -120, 0, 2)
    sendEvent("QWheelEvent", waitForObject(names.fiberInfoScreen_wdTable_QWidget), 534, 461, -120, 0, 2)
