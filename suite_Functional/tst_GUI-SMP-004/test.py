# -*- coding: utf-8 -*-

import names
from common import *
def main():
    test.log("This TC contains SVV tag GUI-SMP-004")
    select_wired_footswitch()
    settings_to_service()
    snooze(5)
    clickButton(waitForObject(names.numpad_pbTopLeft_NumpadButton))
    clickButton(waitForObject(names.numpad_pbMiddleLeft_NumpadButton))
    clickButton(waitForObject(names.numpad_pbBottomLeft_NumpadButton))
    clickButton(waitForObject(names.numpad_pbMiddleLeft_NumpadButton))
    clickButton(waitForObject(names.numpad_pbBottomMiddle_NumpadButton))
    test.compare(str(waitForObjectExists(names.frCenterButtons_lbMessage_QLabel).text), "Incorrect passcode entered")
    test.passes("The program reports incorrect passcode message and doesn’t advance into Service Mode")
