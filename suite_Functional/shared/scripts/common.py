# -*- coding: utf-8 -*-
from squish import *

import names
def serivce_mode_login_passcode():
    """
    Navigate to Service Mode Login and entering passcode
    """
    snooze(5)
    clickButton(waitForObject(names.numpad_pbTopLeft_NumpadButton))
    clickButton(waitForObject(names.numpad_pbMiddleLeft_NumpadButton))
    clickButton(waitForObject(names.numpad_pbBottomLeft_NumpadButton))
    clickButton(waitForObject(names.numpad_pbMiddleLeft_NumpadButton))
    clickButton(waitForObject(names.numpad_pbTopLeft_NumpadButton))
    
    
def log_off():
    """
    Navigate to Log off Screen and again Login to the system
    """
    mouseClick(waitForObject(names.frLeftButtons_lbIcon_WdIcon_7))
    mouseClick(waitForObject(names.wdPopup_lbText_QLabel_4))
    snooze(5)
    clickButton(waitForObject(names.numpad_pbBottomLeft_NumpadButton))
    clickButton(waitForObject(names.numpad_pbBottomMiddle_NumpadButton))
    clickButton(waitForObject(names.numpad_pbBottomRight_NumpadButton))
    clickButton(waitForObject(names.numpad_pbMiddleLeft_NumpadButton))
    
def select_wired_footswitch():
    """Select Wired Footswitch during system login."""
    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon))
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))


def navigate_to_lithotripsy_renal_stone():
    """Open Renal Stone under Lithotripsy."""
    mouseClick(waitForObject(names.homeScreen_lbIcon_WdIcon))
    mouseClick(waitForObject(names.wdScrollArea_lbText_WdOutlinedLabel))


def navigate_renal_stone_to_home():
    """Return to Home from Renal Stone."""
    mouseClick(waitForObject(names.treatmentScreen_lbIcon_WdIcon))
    mouseClick(waitForObject(names.frLeftButtons_lbIcon_WdIcon))


def navigate_lithotripsy_to_bladder_stone():
    """Open Bladder Stone under Lithotripsy."""
    mouseClick(waitForObject(names.homeScreen_lbIcon_WdIcon))
    mouseClick(waitForObject(names.wdScrollArea_lbText_WdOutlinedLabel_2))


def navigate_bladder_stone_to_home():
    """Return to Home from Bladder Stone."""
    mouseClick(waitForObject(names.treatmentScreen_lbIcon_WdIcon))
    mouseClick(waitForObject(names.frLeftButtons_lbIcon_WdIcon))


def navigate_lithotripsy_to_ureteral_stone():
    """Open Ureteral Stone under Lithotripsy."""
    mouseClick(waitForObject(names.homeScreen_lbText_QLabel))
    mouseClick(waitForObject(names.wdScrollArea_lbText_WdOutlinedLabel_3))


def navigate_ureteral_stone_to_home():
    """Return to Home from Ureteral Stone."""
    mouseClick(waitForObject(names.treatmentScreen_lbText_QLabel))
    mouseClick(waitForObject(names.frLeftButtons_lbText_QLabel))


def navigate_soft_tissue_to_ablate():
    """Open Ablate/Excise under Soft Tissue."""
    mouseClick(waitForObject(names.homeScreen_lbText_QLabel_2))
    mouseClick(waitForObject(names.wdScrollArea_lbText_WdOutlinedLabel))


def navigate_ablate_to_home():
    """Return to Home from Ablate/Excise."""
    mouseClick(waitForObject(names.treatmentScreen_lbText_QLabel))
    mouseClick(waitForObject(names.frLeftButtons_lbText_QLabel))


def navigate_soft_tissue_to_incise():
    """Open Incise under Soft Tissue."""
    mouseClick(waitForObject(names.homeScreen_lbIcon_WdIcon_2))
    mouseClick(waitForObject(names.wdScrollArea_lbText_WdOutlinedLabel_2))


def navigate_incise_to_home():
    """Return to Home from Incise."""
    mouseClick(waitForObject(names.treatmentScreen_lbText_QLabel))
    mouseClick(waitForObject(names.frLeftButtons_lbText_QLabel))


def navigate_bph_to_enucleation():
    """Open Enucleation under BPH."""
    mouseClick(waitForObject(names.homeScreen_lbIcon_WdIcon_3))
    mouseClick(waitForObject(names.wdScrollArea_lbText_WdOutlinedLabel))


def navigate_enucleation_to_home():
    """Return to Home from Enucleation."""
    mouseClick(waitForObject(names.treatmentScreen_lbIcon_WdIcon))
    mouseClick(waitForObject(names.frLeftButtons_lbIcon_WdIcon))


def navigate_bph_to_vaporization():
    """Open Vaporization under BPH and click its popup label."""
    mouseClick(waitForObject(names.homeScreen_lbIcon_WdIcon_3))
    mouseClick(waitForObject(names.wdScrollArea_lbText_WdOutlinedLabel_2))
    mouseClick(waitForObject(names.wdPopup_lbText_QLabel_2))


def navigate_manual_screen():
    """Open the Manual screen from Home."""
    mouseClick(waitForObject(names.homeScreen_lbText_QLabel_3))


def settings_to_system_test():
    """Open System Test from Settings."""
    mouseClick(waitForObject(names.frRightButtons_lbIcon_WdIcon_3))
    clickButton(waitForObject(names.wdScrollArea_btDownArrow_WdPushButton))
    mouseClick(waitForObject(names.wdScrollArea_text_QLabel))


def settings_to_user_defined_logs():
    """Open User Defined Logs from Settings."""
    mouseClick(waitForObject(names.frRightButtons_lbText_QLabel_2))
    clickButton(waitForObject(names.wdScrollArea_btDownArrow_WdPushButton))
    mouseClick(waitForObject(names.wdScrollArea_text_QLabel_2))


def settings_to_fiber_information():
    """Open Fiber Information from Settings."""
    mouseClick(waitForObject(names.frRightButtons_lbText_QLabel_2))
    clickButton(waitForObject(names.wdScrollArea_btDownArrow_WdPushButton))
    mouseClick(waitForObject(names.wdScrollArea_lbText_WdLabel))


def settings_to_software_version():
    """Open Software Version from Settings."""
    mouseClick(waitForObject(names.frRightButtons_lbText_QLabel_2))
    clickButton(waitForObject(names.wdScrollArea_btDownArrow_WdPushButton))
    mouseClick(waitForObject(names.wdScrollArea_lbText_WdLabel_2))


def settings_to_service():
    """Open Service from Settings."""
    mouseClick(waitForObject(names.frRightButtons_lbText_QLabel_2))
    clickButton(waitForObject(names.wdScrollArea_btDownArrow_WdPushButton))
    mouseClick(waitForObject(names.wdScrollArea_text_QLabel_3))

def settings_to_languages():
    """Open Languages from Settings."""
    mouseClick(waitForObject(names.frRightButtons_lbText_QLabel_2))
    clickButton(waitForObject(names.wdScrollArea_btDownArrow_WdPushButton))
    clickButton(waitForObject(names.wdScrollArea_item_0_WdButtonGridViewItem))


def settings_to_reset_counters():
    """Open Reset Counters from Settings."""
    mouseClick(waitForObject(names.frRightButtons_lbText_QLabel_2))
    mouseClick(waitForObject(names.wdScrollArea_text_QLabel))


def settings_to_system_setup():
    """Open System Setup from Settings."""
    mouseClick(waitForObject(names.frRightButtons_lbText_QLabel_2))
    mouseClick(waitForObject(names.wdScrollArea_text_QLabel_2))


def settings_to_aiming_beam():
    """Open the Aiming Beam Defaults tab."""
    settings_to_system_setup()
    clickTab(waitForObject(names.systemSetupScreen_wdTabWidget_WdTabWidget),"Aiming Beam\nDefaults",)

def settings_to_emission_tone():
    """Open the Emission Tone Settings tab."""
    settings_to_system_setup()
    clickTab(waitForObject(names.systemSetupScreen_wdTabWidget_WdTabWidget),"Emission Tone\nSettings",)


def settings_to_change_passcode():
    """Open the Change Passcode tab."""
    settings_to_system_setup()
    clickTab(waitForObject(names.systemSetupScreen_wdTabWidget_WdTabWidget),"Change\nPasscode",)


def settings_to_import():
    """Open the Import/Export tab."""
    settings_to_system_setup()
    clickTab(waitForObject(names.systemSetupScreen_wdTabWidget_WdTabWidget),"Import /\nExport",)


def settings_to_treatment_logs():
    """Open Treatment Logs from Settings."""
    mouseClick(waitForObject(names.frRightButtons_lbText_QLabel_2))
    mouseClick(waitForObject(names.wdScrollArea_text_QLabel_4))


def settings_to_wireless_footswitch():
    """Open Wireless Footswitch from Settings."""
    mouseClick(waitForObject(names.frRightButtons_lbText_QLabel_2))
    mouseClick(waitForObject(names.wdScrollArea_lbText_WdLabel_3))


def settings_to_add_physician():
    """Open Add/Edit Physician from Settings."""
    mouseClick(waitForObject(names.frRightButtons_lbIcon_WdIcon_3))
    mouseClick(waitForObject(names.wdScrollArea_lbText_WdLabel_4))


def settings_to_add_preset():
    """Open Add/Edit Preset from Settings."""
    mouseClick(waitForObject(names.frRightButtons_lbIcon_WdIcon_3))
    mouseClick(waitForObject(names.wdScrollArea_lbText_WdLabel_2))


def home_add_preset():
    """Open Add/Edit Preset from Home."""
    mouseClick(waitForObject(names.homeScreen_lbText_QLabel_4))
    
def rfid_configuration():
    """
    Navigate from service Mode to RFID Configuration
    """
    serivce_mode_login_passcode()
    clickTab(waitForObject(names.systemSetupScreen_wdTabWidget_WdTabWidget_2), "RFID\nConfiguration")
    
def system_checks():
    """
    Navigate from Service Mode to System Checks
    """
    serivce_mode_login_passcode()
    clickTab(waitForObject(names.systemSetupScreen_wdTabWidget_WdTabWidget_2), "System\nChecks")
  
def software_update():
    """
    Navigate from Service Mode to Software Update
    """ 
    serivce_mode_login_passcode() 
    clickTab(waitForObject(names.systemSetupScreen_wdTabWidget_WdTabWidget_2), "Software\nUpdate")
  
def firmware_updates():
    """
    Navigate from Service Mode to FirmWare Update
    """
    settings_to_service()
    serivce_mode_login_passcode()
    clickButton(waitForObject(names.systemSetupScreen_WdPushButton))
    clickTab(waitForObject(names.systemSetupScreen_wdTabWidget_WdTabWidget_2), "Firmware\nUpdate")    
  
def system_event_log():
    """
    Navigate from Service Mode to System Event Log
    """
    settings_to_service()
    serivce_mode_login_passcode()
    clickTab(waitForObject(names.systemSetupScreen_wdTabWidget_WdTabWidget_2), "System Event\nLog")

def touch_screen():
    """
    Navigate from Service Mode to Touch Screen
    """
    settings_to_service()
    serivce_mode_login_passcode()
    clickTab(waitForObject(names.systemSetupScreen_wdTabWidget_WdTabWidget_2), "Touch\nScreen")
    
  
  
  
  
    
    
    

