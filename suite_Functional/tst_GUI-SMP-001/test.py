# -*- coding: utf-8 -*-

import names
from common import *
def main():
    test.log("This TC contains the SVV tag GUI-SMP-001")
    select_wired_footswitch()
    settings_to_service()
    test.compare(waitForObjectExists(names.loginScreen_mainFrame_QFrame).visible, True)
    test.compare(str(waitForObjectExists(names.loginScreen_mainFrame_QFrame).objectName), "mainFrame")
    test.passes("PASS: Service Mode login screen is displayed and verified successfully.")
