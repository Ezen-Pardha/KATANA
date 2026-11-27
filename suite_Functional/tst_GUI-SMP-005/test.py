# -*- coding: utf-8 -*-

import names
from common import *
def main():
    test.log("This Test case Contains the SVV tag GUI-SMP-005")
    select_wired_footswitch()
    settings_to_service()
    serivce_mode_login_passcode()
    test.compare(str(waitForObjectExists(names.wdTitleBar_text_QLabel_3).text), "Service")
    test.compare(waitForObjectExists(names.wdTitleBar_text_QLabel_3).visible, True)
    test.passes("The program advances into Service Mode")
