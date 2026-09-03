# encoding: UTF-8

from objectmaphelper import *

o_ScreenSwitcher = {"type": "ScreenSwitcher", "unnamed": 1, "visible": 1}
homeScreen_HomeScreen = {"name": "HomeScreen", "type": "HomeScreen", "visible": 1, "window": o_ScreenSwitcher}
homeScreen_WdPopup_FiberVerificationPopup = {"container": homeScreen_HomeScreen, "name": "WdPopup", "type": "FiberVerificationPopup", "visible": 1}
wdPopup_lbIcon_WdIcon = {"container": homeScreen_WdPopup_FiberVerificationPopup, "name": "lbIcon", "type": "WdIcon", "visible": 1}
homeScreen_FootswitchPopup_FootswitchPopup = {"container": homeScreen_HomeScreen, "name": "FootswitchPopup", "type": "FootswitchPopup", "visible": 1}
footswitchPopup_pbWired_WdPushButton = {"container": homeScreen_FootswitchPopup_FootswitchPopup, "name": "pbWired", "type": "WdPushButton", "visible": 1}
homeScreen_wdToolBar_WdToolBar = {"container": homeScreen_HomeScreen, "name": "wdToolBar", "type": "WdToolBar", "visible": 1}
wdToolBar_frLeftButtons_QFrame = {"container": homeScreen_wdToolBar_WdToolBar, "name": "frLeftButtons", "type": "QFrame", "visible": 1}
frLeftButtons_lbIcon_WdIcon = {"container": wdToolBar_frLeftButtons_QFrame, "name": "lbIcon", "type": "WdIcon", "visible": 1}
wdPopup_LogoffPopup = {"name": "WdPopup", "type": "LogoffPopup", "visible": 1, "window": o_ScreenSwitcher}
wdPopup_lbIcon_WdIcon_2 = {"container": wdPopup_LogoffPopup, "name": "lbIcon", "occurrence": 2, "type": "WdIcon", "visible": 1}
loginScreen_LoginScreen = {"name": "LoginScreen", "type": "LoginScreen", "visible": 1, "window": o_ScreenSwitcher}
loginScreen_mainFrame_QFrame = {"container": loginScreen_LoginScreen, "name": "mainFrame", "type": "QFrame", "visible": 1}
mainFrame_gbPasscode_QGroupBox = {"container": loginScreen_mainFrame_QFrame, "name": "gbPasscode", "type": "QGroupBox", "visible": 1}
gbPasscode_inputFrame_PasscodeInputWidget = {"container": mainFrame_gbPasscode_QGroupBox, "name": "inputFrame", "type": "PasscodeInputWidget", "visible": 1}
inputFrame_numpad_Numpad = {"container": gbPasscode_inputFrame_PasscodeInputWidget, "name": "numpad", "type": "Numpad", "visible": 1}
numpad_pbMiddleMiddle_NumpadButton = {"container": inputFrame_numpad_Numpad, "name": "pbMiddleMiddle", "type": "NumpadButton", "visible": 1}
numpad_pbMiddleRight_NumpadButton = {"container": inputFrame_numpad_Numpad, "name": "pbMiddleRight", "type": "NumpadButton", "visible": 1}
numpad_pbTopRight_NumpadButton = {"container": inputFrame_numpad_Numpad, "name": "pbTopRight", "type": "NumpadButton", "visible": 1}
numpad_pbTopMiddle_NumpadButton = {"container": inputFrame_numpad_Numpad, "name": "pbTopMiddle", "type": "NumpadButton", "visible": 1}
numpad_pbBottomLeft_NumpadButton = {"container": inputFrame_numpad_Numpad, "name": "pbBottomLeft", "type": "NumpadButton", "visible": 1}
numpad_pbBottomMiddle_NumpadButton = {"container": inputFrame_numpad_Numpad, "name": "pbBottomMiddle", "type": "NumpadButton", "visible": 1}
numpad_pbBottomRight_NumpadButton = {"container": inputFrame_numpad_Numpad, "name": "pbBottomRight", "type": "NumpadButton", "visible": 1}
numpad_pbMiddleLeft_NumpadButton = {"container": inputFrame_numpad_Numpad, "name": "pbMiddleLeft", "type": "NumpadButton", "visible": 1}
wdPopup_lbText_QLabel = {"container": homeScreen_WdPopup_FiberVerificationPopup, "name": "lbText", "type": "QLabel", "visible": 1}
