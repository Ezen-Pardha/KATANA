# -*- coding: utf-8 -*-

import names

def main():
    startApplication("katana")
    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon, 119917), 59, 32, Qt.NoModifier, Qt.LeftButton)
    snooze(3)
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    snooze(3)
    mouseClick(waitForObject(names.homeScreen_lbIcon_WdIcon), 118, 116, Qt.NoModifier, Qt.LeftButton)
    snooze(3)
    clickButton(waitForObject(names.treatmentScreen_Ready_WdPushButton))
    snooze(3)