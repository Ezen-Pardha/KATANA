import names
from openpyxl import load_workbook


excelPath = "/home/ezen/Desktop/Katana All Strings.xlsx"

workbook = load_workbook(
    excelPath,
    data_only=True
)

sheet = workbook["Katana Strings"]


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


def main():

    # Your Squish actions here
    
    mouseClick(waitForObject(names.wdPopup_lbText_QLabel_5), 55, 8, Qt.NoModifier, Qt.LeftButton)
   
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    snooze(1)
    mouseClick(waitForObject(names.homeScreen_lbText_QLabel_2), 203, 0, Qt.NoModifier, Qt.LeftButton)
    snooze(5)

    

    # test.ocrTextPresent(
    #     getExpectedString("remaining"),
    #     {
    #         "tesseract": {
    #             "psm": 6
    #         }
    #     }
    # )
    
    # test.compare(str(waitForObjectExists(names.wdTitleBar_text_QLabel_3).text), "Manual")
    # test.compare(str(waitForObjectExists(names.treatmentScreen_text_QLabel_2).text), "Left Pedal")
    # test.compare(str(waitForObjectExists(names.treatmentScreen_text_QLabel_3).text), "Right Pedal")
    test.compare(
    str(waitForObjectExists(names.wdTitleBar_text_QLabel_3).text),
    getExpectedString("manual")
)

# test.compare(
#     str(waitForObjectExists(names.treatmentScreen_text_QLabel_2).text),
#     getExpectedString("leftPedal")
# )
#
# test.compare(
#     str(waitForObjectExists(names.treatmentScreen_text_QLabel_3).text),
#     getExpectedString("rightPedal")
#     )
#
#

