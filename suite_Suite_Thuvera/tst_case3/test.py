# -*- coding: utf-8 -*-

import names

def main():
    test.log("Thuvera Automation Started")

    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    clickButton(waitForObject(names.wdKeypad_pushButton_0_QPushButton))
    clickButton(waitForObject(names.wdKeypad_pushButton_0_QPushButton))
    clickButton(waitForObject(names.wdKeypad_pushButton_0_QPushButton))
    clickButton(waitForObject(names.wdKeypad_pushButton_0_QPushButton))
    test.imagePresent("Assist_Logo", {}, waitForObjectExists(names.apollo_tbAssistant_QToolButton))
    clickButton(waitForObject(names.sclProfiles_Default_ProfileButton))

    test.breakpoint()
    
    
