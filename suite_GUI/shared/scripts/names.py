# encoding: UTF-8

from objectmaphelper import *

o_ScreenSwitcher = {"type": "ScreenSwitcher", "unnamed": 1, "visible": 1}
homeScreen_HomeScreen = {"name": "HomeScreen", "type": "HomeScreen", "visible": 1, "window": o_ScreenSwitcher}
homeScreen_WdPopup_FiberVerificationPopup = {"container": homeScreen_HomeScreen, "name": "WdPopup", "type": "FiberVerificationPopup", "visible": 1}
wdPopup_lbText_QLabel = {"container": homeScreen_WdPopup_FiberVerificationPopup, "name": "lbText", "type": "QLabel", "visible": 1}
homeScreen_FootswitchPopup_FootswitchPopup = {"container": homeScreen_HomeScreen, "name": "FootswitchPopup", "type": "FootswitchPopup", "visible": 1}
footswitchPopup_pbWired_WdPushButton = {"container": homeScreen_FootswitchPopup_FootswitchPopup, "name": "pbWired", "type": "WdPushButton", "visible": 1}
wdPopup_lbIcon_WdIcon = {"container": homeScreen_WdPopup_FiberVerificationPopup, "name": "lbIcon", "type": "WdIcon", "visible": 1}
homeScreen_btManual_WdToolButton = {"container": homeScreen_HomeScreen, "name": "btManual", "type": "WdToolButton", "visible": 1}
homeScreen_lbIcon_WdIcon = {"container": homeScreen_HomeScreen, "name": "lbIcon", "occurrence": 3, "type": "WdIcon", "visible": 1}
homeScreen_lbIcon_WdIcon_2 = {"container": homeScreen_HomeScreen, "name": "lbIcon", "occurrence": 4, "type": "WdIcon", "visible": 1}
homeScreen_lbIcon_WdIcon_3 = {"container": homeScreen_HomeScreen, "name": "lbIcon", "occurrence": 5, "type": "WdIcon", "visible": 1}
