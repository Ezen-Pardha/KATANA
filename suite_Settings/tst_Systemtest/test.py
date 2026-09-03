# -*- coding: utf-8 -*-

import names


def main():
    snooze(2)
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    snooze(2)
    test.vp("Home Screen")
    test.passes("Home screen successfully verified.")
    mouseClick(waitForObject(names.frRightButtons_lbIcon_WdIcon), 165, 25, Qt.NoModifier, Qt.LeftButton)
    test.vp("Settings Screen")
    snooze(2)
    test.passes("Settings screen successfully verified.")
    clickButton(waitForObject(names.wdScrollArea_btDownArrow_WdPushButton))
    snooze(2)
    test.vp("Second Screen")
    test.passes("second screen successfully verified")
    mouseClick(waitForObject(names.wdScrollArea_lbText_WdLabel_2), 307, 85, Qt.NoModifier, Qt.LeftButton)
    test.vp("SystemTest")
    test.passes("Screen lable names are verified")
    
   
     
    
