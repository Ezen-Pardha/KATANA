# -*- coding: utf-8 -*-

import names


def main():
    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 125, 80, 810, 94)
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    mouseClick(waitForObject(names.frRightButtons_lbText_QLabel_2), 61, 21, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.wdScrollArea_text_QLabel_5), 24, 31, Qt.NoModifier, Qt.LeftButton)
    test.vp("system settings")
    clickTab(waitForObject(names.systemSetupScreen_wdTabWidget_WdTabWidget), "Aiming Beam\nDefaults")
    test.vp("aiming beam")
    clickTab(waitForObject(names.systemSetupScreen_wdTabWidget_WdTabWidget), "Emission Tone\nSettings")
    test.vp("emssion tone settings")
    clickTab(waitForObject(names.systemSetupScreen_wdTabWidget_WdTabWidget), "Change\nPasscode")
    clickButton(waitForObject(names.changePasscodeWidget_btBackspace_WdPushButton))
    test.vp("Change passcode")
    clickTab(waitForObject(names.systemSetupScreen_wdTabWidget_WdTabWidget), "Import /\nExport")
    test.vp("imports_exports")
