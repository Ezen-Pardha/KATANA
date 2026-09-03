# -*- coding: utf-8 -*-

import names


def main():
    startApplication("katana")
    snooze(2)
    mouseClick(waitForObject(name='FiberVerificationOK'), 153, 26, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    mouseClick(waitForObject(names.homeScreen_lbIcon_WdIcon), 502, 47, Qt.NoModifier, Qt.LeftButton)
    setWindowState(waitForObject(names.o_ScreenSwitcher), WindowState.Minimize)
