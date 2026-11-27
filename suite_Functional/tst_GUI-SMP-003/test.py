# -*- coding: utf-8 -*-

import names
from common import *
def main():
    test.log("This Test case contains SVV tag GUI-SMP-003")
    select_wired_footswitch()
    settings_to_service()
    snooze(5)
    clickButton(waitForObject(names.numpad_pbTopLeft_NumpadButton))
    clickButton(waitForObject(names.numpad_pbMiddleLeft_NumpadButton))
    clickButton(waitForObject(names.numpad_pbBottomLeft_NumpadButton))
    clickButton(waitForObject(names.numpad_pbMiddleLeft_NumpadButton))
    test.compare(str(waitForObjectExists(names.inputFrame_passcodeInput_QLineEdit).displayText), "****")
    clickButton(waitForObject(names.numpad_pbTopLeft_NumpadButton))
    test.log("Only four hidden characters are visible. Upon entering the 5th character, the Service Mode page becomes visible.")
    test.passes("Only four hidden characters are visible, and upon entering the 5th character, the Service Mode page becomes visible.")