# -*- coding: utf-8 -*-

import names


def main():
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    mouseClick(waitForObject(names.frLeftButtons_lbText_QLabel), 162, 22, Qt.NoModifier, Qt.LeftButton)
    test.breakpoint()
    mouseClick(waitForObject(names.wdPopup_lbText_QLabel_2), 71, 4, Qt.NoModifier, Qt.LeftButton)
