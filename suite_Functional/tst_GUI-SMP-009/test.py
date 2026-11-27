# -*- coding: utf-8 -*-

import names
from common import *


def verify_system_checks_screen():
    """
    Verify Last System Test, USB Read/Write Test,
    System Checks labels and Ethernet Port status.
    """
    test.compare(str(waitForObjectExists(names.stackedWidget_text_QLabel).objectName), 
                 "text")
    test.compare(str(waitForObjectExists(names.stackedWidget_text_QLabel).text), 
                 "Last System Test:")

    test.compare(str(waitForObjectExists(names.stackedWidget_lbText_QLabel).objectName), 
                 "lbText")
    test.compare(str(waitForObjectExists(names.stackedWidget_lbText_QLabel).text), 
                 "USB Read/\nWrite Test")

    test.compare(str(waitForObjectExists(names.systemChecksWidget_text_QLabel).objectName),
                  "text")
    test.compare(str(waitForObjectExists(names.systemChecksWidget_text_QLabel).text), 
                 "Emergency Off")

    test.compare(str(waitForObjectExists(names.systemChecksWidget_text_QLabel_2).objectName),
                  "text")
    test.compare(str(waitForObjectExists(names.systemChecksWidget_text_QLabel_2).text), 
                 "Remote Interlock")

    test.compare(str(waitForObjectExists(names.systemChecksWidget_icon_QLabel).objectName), 
                 "icon")

    test.compare(str(waitForObjectExists(names.systemChecksWidget_text_QLabel_3).objectName), 
                 "text")
    test.compare(str(waitForObjectExists(names.systemChecksWidget_text_QLabel_3).text), 
                 "Window Sense 1")

    test.compare(str(waitForObjectExists(names.systemChecksWidget_text_QLabel_4).objectName), 
                 "text")
    test.compare(str(waitForObjectExists(names.systemChecksWidget_text_QLabel_4).text), 
                 "Window Sense 2")

    test.compare(str(waitForObjectExists(names.systemChecksWidget_text_QLabel_5).objectName),
                  "text")
    test.compare(str(waitForObjectExists(names.systemChecksWidget_text_QLabel_5).text), 
                 "Left Pedal 1")

    test.compare(str(waitForObjectExists(names.systemChecksWidget_text_QLabel_6).objectName), 
                 "text")
    test.compare(str(waitForObjectExists(names.systemChecksWidget_text_QLabel_6).text), 
                 "Left Pedal 2")

    test.compare(str(waitForObjectExists(names.systemChecksWidget_text_QLabel_7).objectName), 
                 "text")
    test.compare(str(waitForObjectExists(names.systemChecksWidget_text_QLabel_7).text), 
                 "Middle Pedal")

    test.compare(str(waitForObjectExists(names.systemChecksWidget_text_QLabel_8).objectName),
                  "text")
    test.compare(str(waitForObjectExists(names.systemChecksWidget_text_QLabel_8).text), 
                 "Wired Pedal")

    test.compare(str(waitForObjectExists(names.systemChecksWidget_text_QLabel_9).objectName),
                  "text")
    test.compare(str(waitForObjectExists(names.systemChecksWidget_text_QLabel_9).text), 
                 "Right Pedal 1")

    test.compare(str(waitForObjectExists(names.systemChecksWidget_text_QLabel_10).objectName), 
                 "text")
    test.compare(str(waitForObjectExists(names.systemChecksWidget_text_QLabel_10).text), 
                 "RFID")

    test.compare(str(waitForObjectExists(names.systemChecksWidget_text_QLabel_11).objectName), 
                 "text")
    test.compare(str(waitForObjectExists(names.systemChecksWidget_text_QLabel_11).text), 
                 "Fiber Sense 1")

    test.compare(str(waitForObjectExists(names.systemChecksWidget_text_QLabel_12).objectName), 
                 "text")
    test.compare(str(waitForObjectExists(names.systemChecksWidget_text_QLabel_12).text), 
                 "Fiber Sense 2")

    test.compare(str(waitForObjectExists(names.frRightButtons_Ethernet_Port_ENABLED_right_WdToolButton).objectName),
                "Ethernet Port ENABLED_right")


def main():
    test.log("This Test case Contains the SVV tag GUI-SMP-009")
    select_wired_footswitch()
    settings_to_service()
    system_checks()
    verify_system_checks_screen()
    test.passes("System Checks screen Verified")

    
