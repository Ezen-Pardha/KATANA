# -*- coding: utf-8 -*-

import names


def main():
    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon), 74, 23, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    test.imagePresent("image")
    test.passes("My presets Button is verified successfully")
    test.vp("VP1")
    test.passes("Manual Button is verified successfully")
    test.vp("VP2")
    test.passes("Lithotripsy Button is verified successfully")
    test.vp("VP3")
    test.passes("Soft Tissue Button is verified successfully")
    test.vp("VP4")
    test.passes("BPH Button is verified successfully")