# -*- coding: utf-8 -*-

import names


def main():
    mouseClick(waitForObject(names.wdPopup_lbIcon_WdIcon_2), 66, 26, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    test.compare(str(waitForObjectExists(names.wdTitleBar_text_QLabel).text), "Home")
    
    test.compare(str(waitForObjectExists(names.homeScreen_lbText_QLabel).text), "My Presets")
    
    test.compare(str(waitForObjectExists(names.homeScreen_lbText_QLabel_4).text), "Manual")
    
    test.compare(str(waitForObjectExists(names.homeScreen_lbText_QLabel_2).text), "Lithotripsy")
    
    test.compare(str(waitForObjectExists(names.homeScreen_lbText_QLabel_3).text), "Soft Tissue")
    
    test.compare(str(waitForObjectExists(names.homeScreen_lbText_QLabel_5).text), "BPH")
    
    test.compare(str(waitForObjectExists(names.frLeftButtons_lbText_QLabel).text), "Log off")
    
    test.compare(str(waitForObjectExists(names.frRightButtons_lbText_QLabel).text), "Settings")
