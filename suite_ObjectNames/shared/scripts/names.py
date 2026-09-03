# encoding: UTF-8

from objectmaphelper import *

o_ScreenSwitcher = {"type": "ScreenSwitcher", "unnamed": 1, "visible": 1}
homeScreen_HomeScreen = {"name": "HomeScreen", "type": "HomeScreen", "visible": 1, "window": o_ScreenSwitcher}
homeScreen_WdPopup_FiberVerificationPopup = {"container": homeScreen_HomeScreen, "name": "WdPopup", "type": "FiberVerificationPopup", "visible": 1}
wdPopup_lbIcon_WdIcon = {"container": homeScreen_WdPopup_FiberVerificationPopup, "name": "FiberVerificationOK", "type": "WdIcon", "visible": 1}
homeScreen_FootswitchPopup_FootswitchPopup = {"container": homeScreen_HomeScreen, "name": "FootswitchPopup", "type": "FootswitchPopup", "visible": 1}
footswitchPopup_pbWired_WdPushButton = {"container": homeScreen_FootswitchPopup_FootswitchPopup, "name": "pbWired", "type": "WdPushButton", "visible": 1}
homeScreen_lbIcon_WdIcon = {"container": homeScreen_HomeScreen, "name": "lbIcon", "type": "WdIcon", "visible": 1}
