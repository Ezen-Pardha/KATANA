# -*- coding: utf-8 -*-

import names
from common import *

def verify_critical_system_configuration():
    """
    Verify critical System Configuration warning messages and confirmation popups.
    """

    mouseClick(waitForObject(names.systemConfigurationWidget_lbText_QLabel))

    test.compare(str(waitForObjectExists(
            names.wdCentral_div_style_line_height_130_This_setting_must_only_be_changed_as_in_structed_by_an_official_SERVICE_BULLETIN_Confirm_changes_are_performed_EXACTLY_as_instructed_Uncorrectly_entered_values_can_expose_users_to_increased_risk_div_QLabel
        ).text),
        "<div style=\"line-height:130%\">This setting must only be changed as in-structed by an official SERVICE BULLETIN. Confirm changes are performed EXACTLY as instructed. Uncorrectly entered values can expose users to increased risk.</div>"
    )

    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon_4))

    mouseClick(waitForObject(names.systemConfigurationWidget_lbText_QLabel_2))

    test.compare(str(waitForObjectExists(
            names.wdCentral_div_style_line_height_130_This_setting_must_only_be_changed_as_in_structed_by_an_official_SERVICE_BULLETIN_Confirm_changes_are_performed_EXACTLY_as_instructed_Uncorrectly_entered_values_can_expose_users_to_increased_risk_div_QLabel
        ).text),
        "<div style=\"line-height:130%\">This setting must only be changed as in-structed by an official SERVICE BULLETIN. Confirm changes are performed EXACTLY as instructed. Uncorrectly entered values can expose users to increased risk.</div>"
    )

    test.compare(str(waitForObjectExists(names.wdPopup_text_QLabel_2).text),
        "Change Critical System Configuration")

    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon_4))


def main():
    test.log("This Test case Contains the SVV tag GUI-GUI-SRV-007")
    select_wired_footswitch()
    settings_to_service()
    serivce_mode_login_passcode()
    verify_critical_system_configuration()
    test.log("PASS: Critical System Configuration warning and confirmation popups verified successfully.")

