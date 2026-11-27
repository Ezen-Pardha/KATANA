# -*- coding: utf-8 -*-

import names
from common import *

def verify_system_software_update():
    """
    Verify System Software Update labels and displayed version information.
    """

    test.compare(str(waitForObjectExists(names.systemSoftwareUpdateWidget_text_QLabel).objectName),
        "text")
    test.compare(str(waitForObjectExists(names.systemSoftwareUpdateWidget_text_QLabel).text),
        "Application:")

    test.compare(str(waitForObjectExists(names.systemSoftwareUpdateWidget_text_QLabel_2).objectName),
        "text")
    test.compare(str(waitForObjectExists(names.systemSoftwareUpdateWidget_text_QLabel_2).text),
        "1.1.0")

    test.compare(str(waitForObjectExists(names.systemSoftwareUpdateWidget_text_QLabel_3).objectName),
        "text")
    test.compare(str(waitForObjectExists(names.systemSoftwareUpdateWidget_text_QLabel_3).text),
        "Kernel:")

    test.compare(str(waitForObjectExists(names.systemSoftwareUpdateWidget_text_QLabel_4).objectName),
        "text")
    test.compare(str(waitForObjectExists(names.systemSoftwareUpdateWidget_text_QLabel_4).text),
        "Device<br>tree:")

    test.compare(str(waitForObjectExists(names.systemSoftwareUpdateWidget_text_QLabel_5).objectName),
        "text")
    test.compare(str(waitForObjectExists(names.systemSoftwareUpdateWidget_text_QLabel_5).text),
        "unknown")

    test.compare(str(waitForObjectExists(names.systemSoftwareUpdateWidget_text_QLabel_6).objectName),
        "text")
    test.compare(str(waitForObjectExists(names.systemSoftwareUpdateWidget_text_QLabel_6).text),
        "unknown")

    test.compare(str(waitForObjectExists(names.systemSoftwareUpdateWidget_text_QLabel_7).objectName),
        "text")
    test.compare(str(waitForObjectExists(names.systemSoftwareUpdateWidget_text_QLabel_7).text),
        "01.0B.02.05-20.18.08.06-BL12.12.13.0")
    test.compare(str(waitForObjectExists(names.systemSoftwareUpdateWidget_text_QLabel_8).objectName),
        "text")
    test.compare(str(waitForObjectExists(names.systemSoftwareUpdateWidget_text_QLabel_8).text),
        "Factory<br>Procedures:")

    test.compare(str(waitForObjectExists(names.systemSoftwareUpdateWidget_text_QLabel_9).objectName),
        "text")
    test.compare(str(waitForObjectExists(names.systemSoftwareUpdateWidget_text_QLabel_9).text),
        "1")

def main():
   test.log("This Test case Contains the SVV tag GUI-SMP-008")
   select_wired_footswitch()
   settings_to_service()
   software_update()
   verify_system_software_update()
   test.log("PASS: System Software Update elements verified successfully.")
   test.passes("Software Update screen Is verified")

