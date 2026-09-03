# encoding: UTF-8

from objectmaphelper import *

apollo_MainWindow = {"type": "MainWindow", "unnamed": 1, "visible": 1, "windowTitle": "Apollo"}
apollo_AlarmsListScreen_AlarmsListScreen = {"name": "AlarmsListScreen", "type": "AlarmsListScreen", "visible": 1, "window": apollo_MainWindow}
alarmsListScreen_frmPopup_AlarmNotificationPopup = {"container": apollo_AlarmsListScreen_AlarmsListScreen, "name": "frmPopup", "type": "AlarmNotificationPopup", "visible": 1}
frmPopup_pbAccept_QPushButton = {"container": alarmsListScreen_frmPopup_AlarmNotificationPopup, "name": "pbAccept", "type": "QPushButton", "visible": 1}
apollo_PasswordScreen_PasswordScreen = {"name": "PasswordScreen", "type": "PasswordScreen", "visible": 1, "window": apollo_MainWindow}
passwordScreen_wdKeypad_Keypad = {"container": apollo_PasswordScreen_PasswordScreen, "name": "wdKeypad", "type": "Keypad", "visible": 1}
wdKeypad_pushButton_0_QPushButton = {"container": passwordScreen_wdKeypad_Keypad, "name": "pushButton_0", "type": "QPushButton", "visible": 1}
apollo_sclProfiles_ProfilesScroll = {"name": "sclProfiles", "type": "ProfilesScroll", "visible": 1, "window": apollo_MainWindow}
sclProfiles_Default_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": "Default", "type": "ProfileButton", "unnamed": 1, "visible": 1}
frmPopup_lbTitle_QLabel = {"container": alarmsListScreen_frmPopup_AlarmNotificationPopup, "name": "lbTitle", "type": "QLabel", "visible": 1}
apollo_lbTitle_QLabel = {"name": "lbTitle", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
apollo_frToolbar_QFrame = {"name": "frToolbar", "type": "QFrame", "visible": 1, "window": apollo_MainWindow}
frToolbar_tbAddProfile_QToolButton = {"container": apollo_frToolbar_QFrame, "name": "tbAddProfile", "type": "QToolButton", "visible": 1}
frToolbar_tbEditProfile_QToolButton = {"container": apollo_frToolbar_QFrame, "name": "tbEditProfile", "type": "QToolButton", "visible": 1}
frToolbar_tbDeleteProfile_QToolButton = {"container": apollo_frToolbar_QFrame, "name": "tbDeleteProfile", "type": "QToolButton", "visible": 1}
apollo_tbLogoff_QToolButton = {"name": "tbLogoff", "type": "QToolButton", "visible": 1, "window": apollo_MainWindow}
apollo_lbModeHelp_QLabel = {"name": "lbModeHelp", "type": "QLabel", "visible": 1, "window": apollo_MainWindow}
apollo_tbAssistant_QToolButton = {"name": "tbAssistant", "type": "QToolButton", "visible": 1, "window": apollo_MainWindow}
sclProfiles_test_ProfileButton = {"container": apollo_sclProfiles_ProfilesScroll, "text": "test", "type": "ProfileButton", "unnamed": 1, "visible": 1}
sclProfiles_scrollAreaWidgetContents_QWidget = {"container": apollo_sclProfiles_ProfilesScroll, "name": "scrollAreaWidgetContents", "type": "QWidget", "visible": 1}
apollo_ProfileSelectionScreen_ProfileSelectionScreen = {"name": "ProfileSelectionScreen", "type": "ProfileSelectionScreen", "visible": 1, "window": apollo_MainWindow}
