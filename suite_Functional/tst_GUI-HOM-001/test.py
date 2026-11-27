# -*- coding: utf-8 -*-

import names
from common import *


def verify_navigation_screen(object_name, expected_text, screen_name):
    """
    Verify whether the expected screen is displayed.
    """

    try:
        actual_text = str(waitForObjectExists(object_name).text)
        if actual_text == expected_text:
            test.log("PASS: {} screen was present".format(screen_name))
        else:
            test.fail(
                "FAIL: {} screen was not present. Expected: '{}', Actual: '{}'".format(
                    screen_name, expected_text, actual_text
                )
            )
            raise Exception("{} screen verification failed".format(screen_name))

    except Exception as e:
        if str(e) == "{} screen verification failed".format(screen_name):
            raise

        test.fail("FAIL: {} screen was not present. Error: {}".format(
            screen_name, str(e)
        ))
        raise

def verify_complete_navigation():
    """
    Navigate through all application screens, verify their presence, and perform numpad selection.
    """
    mouseClick(waitForObject(names.homeScreen_lbIcon_WdIcon_2))
    verify_navigation_screen(names.factoryPresetSelectionScreen_text_QLabel,"Soft Tissue","Soft Tissue")
    clickButton(waitForObject(names.frLeftButtons_Back_left_WdToolButton))
    mouseClick(waitForObject(names.homeScreen_lbText_QLabel))
    verify_navigation_screen(names.factoryPresetSelectionScreen_text_QLabel,"Lithotripsy","Lithotripsy")
    mouseClick(waitForObject(names.frLeftButtons_lbIcon_WdIcon))
    mouseClick(waitForObject(names.homeScreen_lbIcon_WdIcon_3))
    verify_navigation_screen(names.factoryPresetSelectionScreen_text_QLabel,"BPH","BPH")
    mouseClick(waitForObject(names.frLeftButtons_lbIcon_WdIcon))
    mouseClick(waitForObject(names.homeScreen_lbText_QLabel_4))
    verify_navigation_screen(names.individualPresetScreen_text_QLabel,"My Presets","My Presets")
    mouseClick(waitForObject(names.frLeftButtons_lbText_QLabel_4))
    mouseClick(waitForObject(names.homeScreen_lbText_QLabel_3))
    verify_navigation_screen(names.wdTitleBar_text_QLabel,"Manual","Manual")
    mouseClick(waitForObject(names.treatmentScreen_lbText_QLabel))
    mouseClick(waitForObject(names.frLeftButtons_lbText_QLabel_5))
    verify_navigation_screen(names.wdPopup_text_QLabel,"Log off","Log off")
    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon_3))
    clickButton(waitForObject(names.numpad_pbBottomLeft_NumpadButton))
    clickButton(waitForObject(names.numpad_pbBottomMiddle_NumpadButton))
    clickButton(waitForObject(names.numpad_pbBottomRight_NumpadButton))
    clickButton(waitForObject(names.numpad_pbMiddleLeft_NumpadButton))

def main():
    test.log("This TC contains the SVV tgs from GUI-HOM-001 to GUI-HOM-008")
    select_wired_footswitch()
    verify_complete_navigation()
    test.passes("PASS: GUI-HOM-001 to GUI-HOM-008 - All navigation screens were verified successfully.")

