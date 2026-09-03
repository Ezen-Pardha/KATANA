# -*- coding: utf-8 -*-

import names


def main():
    test.compare(str(waitForObjectExists(names.frmPopup_lbTitle_QLabel).text), "Device Configuration Error")
    clickButton(waitForObject(names.frmPopup_pbAccept_QPushButton))
    clickButton(waitForObject(names.wdKeypad_pushButton_0_QPushButton))
    clickButton(waitForObject(names.wdKeypad_pushButton_0_QPushButton))
    clickButton(waitForObject(names.wdKeypad_pushButton_0_QPushButton))
    clickButton(waitForObject(names.wdKeypad_pushButton_0_QPushButton))
    test.vp("Profiles_Screen")
    sendEvent("QShowEvent", waitForObject(names.apollo_lbTitle_QLabel))
    sendEvent("QShowEvent", waitForObject(names.frToolbar_tbAddProfile_QToolButton))
    sendEvent("QShowEvent", waitForObject(names.frToolbar_tbEditProfile_QToolButton))
    sendEvent("QShowEvent", waitForObject(names.frToolbar_tbDeleteProfile_QToolButton))
    sendEvent("QShowEvent", waitForObject(names.apollo_frToolbar_QFrame))
    sendEvent("QShowEvent", waitForObject(names.apollo_tbLogoff_QToolButton))
    sendEvent("QShowEvent", waitForObject(names.apollo_lbModeHelp_QLabel))
    sendEvent("QShowEvent", waitForObject(names.apollo_tbAssistant_QToolButton))
    sendEvent("QShowEvent", waitForObject(names.sclProfiles_Default_ProfileButton))
    sendEvent("QShowEvent", waitForObject(names.sclProfiles_test_ProfileButton))
    sendEvent("QShowEvent", waitForObject(names.sclProfiles_scrollAreaWidgetContents_QWidget))
    sendEvent("QShowEvent", waitForObject(names.apollo_sclProfiles_ProfilesScroll))
    sendEvent("QShowEvent", waitForObject(names.apollo_sclProfiles_ProfilesScroll))
    sendEvent("QShowEvent", waitForObject(names.apollo_ProfileSelectionScreen_ProfileSelectionScreen))

