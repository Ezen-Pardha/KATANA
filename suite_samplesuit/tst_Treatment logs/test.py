# -*- coding: utf-8 -*-

import names


def main():
    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 36, 39, 659, 57)
    sendEvent("QMoveEvent", waitForObject(names.o_ScreenSwitcher), 43, 43, 666, 61)
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))

    test.vp("VP5")
    test.passes("Nagavted to setting screen")

    mouseClick(waitForObject(names.frRightButtons_lbText_QLabel_2), 109, 5, Qt.NoModifier, Qt.LeftButton)

    test.vp("VP6")
    test.passes("click action done on treatment logs button")

    mouseClick(waitForObject(names.wdScrollArea_text_QLabel_4), 157, 34, Qt.NoModifier, Qt.LeftButton)
    test.vp("VP1")
    test.passes("verified treatment logs screen 1")
    scrollTo(waitForObject(names.tvLog_QScrollBar), 5)
    test.vp("VP2")
    test.passes("verified treatment logs screen 2")
    
    test.vp("VP8")
    test.passes("nagavited to exports logs screen")

  
    mouseClick(waitForObject(names.frRightButtons_lbIcon_WdIcon_3), 238, 46, Qt.NoModifier, Qt.LeftButton)
    
    test.vp("VP3")
    test.passes("displayed pop up 1")
    
    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon_5), 145, 11, Qt.NoModifier, Qt.LeftButton)
    test.vp("VP4")
    test.passes("displayed pop up 2")
    
    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon_6), 125, 25, Qt.NoModifier, Qt.LeftButton)
    
