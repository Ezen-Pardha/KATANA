import names
from openpyxl import load_workbook


# -----------------------------
# Excel setup
# -----------------------------

excelPath = "/home/ezen/Desktop/Katana All Strings.xlsx"

workbook = load_workbook(
    excelPath,
    data_only=True
)

sheet = workbook["Katana Strings"]


# -----------------------------
# Excel string lookup
# -----------------------------

def getExpectedString(englishString):

    for row in range(2, sheet.max_row + 1):

        excelString = sheet.cell(
            row=row,
            column=2
        ).value

        if excelString is not None:

            if str(excelString).strip() == str(
                englishString
            ).strip():

                return str(
                    excelString
                ).strip()

    test.fail(
        "String not found in Excel: "
        + str(englishString)
    )


# -----------------------------
# UI string verification
# -----------------------------

def verifyLabel(labelObject, englishString):

    expectedString = getExpectedString(
        englishString
    )

    actualString = str(
        waitForObject(labelObject).text
    ).strip()

    test.compare(
        actualString,
        expectedString
    )


# -----------------------------
# Test Steps
# -----------------------------

mouseClick(
    waitForObject(
        names.wdPopup_lbIcon_WdIcon_2
    ),
    27, 29,
    Qt.NoModifier,
    Qt.LeftButton
)

snooze(5)


button = waitForObject(
    names.footswitchPopup_pbWired_WdPushButton
)

test.compare(
    str(button.text).strip(),
    "Wired"
)

test.breakpoint()
snooze(3)


mouseClick(waitForObject(names.homeScreen_lbText_QLabel_2),372, 20, Qt.NoModifier,Qt.LeftButton)

snooze(5)

verifyLabel(
    names.homeScreen_lbText_QLabel_2,
    "Home"
)


mouseClick(
    waitForObject(
        names.pulseModeWidget_lbIcon_WdIcon
    ),
    87, 34,
    Qt.NoModifier,
    Qt.LeftButton
)

snooze(5)

verifyLabel(
    names.pulseModeWidget_lbText_QLabel,
    "Pulse Mode"
)


mouseClick(
    waitForObject(
        names.wdPopup_lbIcon_WdIcon_3
    ),
    82, 18,
    Qt.NoModifier,
    Qt.LeftButton
)

snooze(5)


mouseClick(
    waitForObject(
        names.pulseModeWidget_lbText_QLabel
    ),
    24, 47,
    Qt.NoModifier,
    Qt.LeftButton
)

snooze(5)

verifyLabel(
    names.pulseModeWidget_lbText_QLabel,
    "Pulse Mode"
)


mouseClick(
    waitForObject(
        names.treatmentScreen_lbIcon_WdIcon_2
    ),
    110, 16,
    Qt.NoModifier,
    Qt.LeftButton
)

snooze(5)


mouseClick(
    waitForObject(
        names.treatmentScreen_lbIcon_WdIcon_3
    ),
    155, 41,
    Qt.NoModifier,
    Qt.LeftButton
)

snooze(5)


mouseClick(
    waitForObject(
        names.homeScreen_lbIcon_WdIcon_2
    ),
    277, 55,
    Qt.NoModifier,
    Qt.LeftButton
)

snooze(5)


mouseClick(
    waitForObject(
        names.treatmentScreen_wdBottom_QWidget
    ),
    57, 46,
    Qt.NoModifier,
    Qt.LeftButton
)

snooze(5)


mouseClick(
    waitForObject(
        names.wdRadioButtons_lbText_QLabel
    ),
    35, 60,
    Qt.NoModifier,
    Qt.LeftButton
)

snooze(5)

verifyLabel(
    names.wdRadioButtons_lbText_QLabel,
    "Low"
)


mouseClick(
    waitForObject(
        names.wdRadioButtons_lbText_QLabel_2
    ),
    27, 38,
    Qt.NoModifier,
    Qt.LeftButton
)

snooze(5)

verifyLabel(
    names.wdRadioButtons_lbText_QLabel_2,
    "Medium"
)


mouseClick(
    waitForObject(
        names.wdRadioButtons_lbText_QLabel_2
    ),
    13, 50,
    Qt.NoModifier,
    Qt.LeftButton
)

snooze(5)


mouseClick(
    waitForObject(
        names.wdPopup_lbIcon_WdIcon_4
    ),
    57, 33,
    Qt.NoModifier,
    Qt.LeftButton
)

snooze(5)


mouseClick(
    waitForObject(
        names.pulseModeWidget_lbIcon_WdIcon_2
    ),
    87, 23,
    Qt.NoModifier,
    Qt.LeftButton
)

snooze(5)


mouseClick(
    waitForObject(
        names.wdPopup_lbIcon_WdIcon_3
    ),
    147, 15,
    Qt.NoModifier,
    Qt.LeftButton
)

snooze(1)


mouseClick(
    waitForObject(
        names.pulseModeWidget_lbText_QLabel_2
    ),
    63, 33,
    Qt.NoModifier,
    Qt.LeftButton
)

snooze(5)


clickButton(
    waitForObject(
        names.treatmentScreen_Standby_WdPushButton
    )
)

snooze(5)

verifyLabel(
    names.treatmentScreen_Standby_WdPushButton,
    "Standby"
)


clickButton(
    waitForObject(
        names.treatmentScreen_Ready_WdPushButton
    )
)

snooze(5)

verifyLabel(
    names.treatmentScreen_Ready_WdPushButton,
    "Ready"
)


mouseClick(
    waitForObject(
        names.treatmentScreen_lbIcon_WdIcon_4
    ),
    135, 36,
    Qt.NoModifier,
    Qt.LeftButton
)

snooze(5)


mouseClick(
    waitForObject(
        names.wdPopup_lbText_QLabel_4
    ),
    68, 19,
    Qt.NoModifier,
    Qt.LeftButton
)

snooze(1)


clickButton(
    waitForObject(
        names.treatmentScreen_Standby_WdPushButton
    )
)

snooze(5)


clickButton(
    waitForObject(
        names.treatmentScreen_Ready_WdPushButton
    )
)

snooze(1)


mouseClick(
    waitForObject(
        names.wdTitleBar_wdRightEmptySpace_QWidget
    ),
    104, 16,
    Qt.NoModifier,
    Qt.LeftButton
)

snooze(1)


clickButton(
    waitForObject(
        names.treatmentScreen_Standby_WdPushButton
    )
)

snooze(1)


clickButton(
    waitForObject(
        names.treatmentScreen_Ready_WdPushButton
    )
)

snooze(1)


clickButton(
    waitForObject(
        names.treatmentScreen_emuLeftButton_QToolButton
    )
)

snooze(1)


clickButton(
    waitForObject(
        names.treatmentScreen_emuLeftButton_QToolButton
    )
)

snooze(1)


clickButton(
    waitForObject(
        names.treatmentScreen_emuLeftButton_QToolButton
    )
)

snooze(1)


clickButton(
    waitForObject(
        names.treatmentScreen_emuLeftButton_QToolButton
    )
)

snooze(1)


clickButton(
    waitForObject(
        names.treatmentScreen_emuRightButton_QToolButton
    )
)

snooze(1)


clickButton(
    waitForObject(
        names.treatmentScreen_emuRightButton_QToolButton
    )
)

snooze(1)


clickButton(
    waitForObject(
        names.treatmentScreen_Standby_WdPushButton
    )
)