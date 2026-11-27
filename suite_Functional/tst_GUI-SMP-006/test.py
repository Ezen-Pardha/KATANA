# -*- coding: utf-8 -*-

import names
from common import *


def verify_system_configuration():
    """
    Verify System Configuration elements, buttons, and left and right widget properties.
    """

    test.compare(str(waitForObjectExists(names.system_Configuration_TabItem).text),
        "System\nConfiguration")

    test.compare(str(waitForObjectExists(names.systemConfigurationWidget_text_QLabel).text),
        "Last Install Setup:")
    test.compare(str(waitForObjectExists(names.systemConfigurationWidget_text_QLabel_2).text),
        "System Serial Number:")

    test.compare(str(waitForObjectExists(names.systemConfigurationWidget_text_QLabel_3).text),
        "MDUF200001")
    test.compare(str(waitForObjectExists(names.systemConfigurationWidget_btResetPasscodeToDefault_WdToolButton).objectName),
        "btResetPasscodeToDefault")

    test.compare(str(waitForObjectExists(names.systemConfigurationWidget_btClearUserPresets_WdToolButton).objectName),
        "btClearUserPresets")

    wd_central = waitForObjectExists(
        names.systemConfigurationWidget_wdCentral_QWidget
    )

    test.compare(str(wd_central.objectName), "wdCentral")
    test.log("wdCentral Object Name: {}".format(wd_central.objectName))

    test.compare(str(waitForObjectExists(names.systemConfigurationWidget_btSetDateTime_WdToolButton).text),
        "Set Date/Time")

    test.compare(str(waitForObjectExists(names.systemConfigurationWidget_btSetDateTime_WdToolButton).objectName),
        "btSetDateTime")
    test.compare(str(waitForObjectExists(names.systemConfigurationWidget_text_QLabel_4).text),
        "Date:")
    test.compare(str(waitForObjectExists(names.systemConfigurationWidget_btDemoModeActive_WdToolButton).objectName),
        "btDemoModeActive")
    test.compare(str(waitForObjectExists(names.systemConfigurationWidget_btDemoModeActive_WdToolButton).text),
        "Demo Mode\nActive")

    test.compare(str(waitForObjectExists(names.systemConfigurationWidget_text_QLabel_5).objectName),
        "text")

    test.compare(str(waitForObjectExists(names.systemConfigurationWidget_text_QLabel_5).text),
        "Time:")

    wd_right = waitForObjectExists(names.systemConfigurationWidget_wdRight_QWidget)
    test.compare(str(wd_right.objectName), "wdRight")
    test.log("wdRight Object Name: {}".format(wd_right.objectName))

    test.compare(str(waitForObjectExists(names.systemConfigurationWidget_btClearLogs_WdToolButton).objectName),
        "btClearLogs")

    test.compare(str(waitForObjectExists(names.systemConfigurationWidget_btClearLogs_WdToolButton).text),
        "Clear Logs")


def main():
    test.log("This Test case Contains the SVV tag GUI-SMP-006")
    select_wired_footswitch()
    settings_to_service()
    serivce_mode_login_passcode()
    verify_system_configuration()
    test.passes("PASS: System Configuration verification completed successfully.")

    
