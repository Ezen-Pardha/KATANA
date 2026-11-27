# -*- coding: utf-8 -*-

import names
from common import *

def verify_rfid_configuration():
    """
    Verify RFID Configuration labels, object names, and update button.
    """
    test.compare(str(waitForObjectExists(names.frBody_text_QLabel).objectName),
        "text")
    test.compare(str(waitForObjectExists(names.frBody_text_QLabel).text),
        "RFID Read Power")

    test.compare(str(waitForObjectExists(names.rfidConfigurationWidget_text_QLabel).objectName),
        "text")
    test.compare(str(waitForObjectExists(names.rfidConfigurationWidget_text_QLabel).text),
        "RFID Region")

    test.compare(str(waitForObjectExists(names.frBody_text_QLabel_2).objectName),
        "text")
    test.compare(str(waitForObjectExists(names.frBody_text_QLabel_2).text),
        "RFID Write Power")

    test.compare(str(waitForObjectExists(names.rfidConfigurationWidget_text_QLabel_2).objectName),
        "text")
    test.compare(str(waitForObjectExists(names.rfidConfigurationWidget_text_QLabel_2).text),
        "Fiber Idle Timeout")

    test.compare(str(waitForObjectExists(names.rfidConfigurationWidget_text_QLabel_3).objectName),
        "text")
    test.compare(str(waitForObjectExists(names.rfidConfigurationWidget_text_QLabel_3).text),
        "Fiber Startup Timeout")
    test.compare(str(waitForObjectExists(names.frRightButtons_lbText_QLabel_4).text),
        "Update RFID Config")
    test.compare(str(waitForObjectExists(names.frRightButtons_lbText_QLabel_4).objectName),
        "lbText")

def main():
    test.log("This Test case Contains the SVV tag GUI-SMP-005")
    select_wired_footswitch()
    settings_to_service()
    rfid_configuration()
    verify_rfid_configuration()
    test.log("PASS: RFID Configuration elements verified successfully.")
    test.passes("RFID configuration options are verified")
    
