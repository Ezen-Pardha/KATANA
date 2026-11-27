# -*- coding: utf-8 -*-

import names
from common import *
def verify_settings_screen():
    """Verify that the Settings screen is displayed and visible.
    """
    settings_screen = waitForObjectExists(names.wdTitleBar_text_QLabel_2)

    if str(settings_screen.text) == "Settings" and settings_screen.visible == True:
        test.log("PASS: Settings screen is visible")
    else:
        test.fail("FAIL: Settings screen is not visible or title does not match")
        
        
def main():
    test.log("This Test case Contains the SVV tag GUI-SMP-002")
    select_wired_footswitch()
    settings_to_service()
    serivce_mode_login_passcode()
    mouseClick(waitForObject(names.frLeftButtons_lbIcon_WdIcon_8), 46, 37, Qt.NoModifier, Qt.LeftButton)
    verify_settings_screen()
    test.passes("PASS: GUI-SMP-002 - Settings screen navigation and visibility verified successfully.")
