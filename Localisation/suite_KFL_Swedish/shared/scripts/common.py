import openpyxl
import re
import os
import names
import unicodedata

from squish import *

SUITE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)



EXCEL_PATH = os.path.abspath(
    os.path.join(
        SUITE_DIR, "..", "testdata", "Thuvera_Strings.xlsx"
    )
)


LANGUAGE = "English"



def normalize(text):

    if text is None:
        return ""

    text = str(text)
    text = re.sub(
        r"<br\s*/?>",
        " ",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r"<[^>]+>",
        " ",
        text
    )
    text = " ".join(text.split())

    return text.casefold().strip()


def get_text_lines(obj):

    lines = []

    try:

        if not obj.visible:
            return lines

    except:

        pass


    try:

        text = str(obj.text).strip()

        if text:

            text = re.sub(
                r"<br\s*/?>",
                "\n",
                text,
                flags=re.IGNORECASE
            )

            text = re.sub(
                r"<[^>]+>",
                "",
                text
            )

            for line in text.splitlines():

                line = " ".join(
                    line.split()
                ).strip()

                if line:
                    lines.append(line)

    except:

        pass


    try:

        title = str(obj.title).strip()

        if title:

            title = re.sub(
                r"<[^>]+>",
                "",
                title
            )

            title = " ".join(
                title.split()
            ).strip()

            if title:
                lines.append(title)

    except:

        pass



    try:

        for child in object.children(obj):

            lines.extend(
                get_text_lines(child)
            )

    except:

        pass


    return lines


def get_all_text_combinations(obj):

    result = []

    lines = get_text_lines(obj)

    for start in range(len(lines)):

        combined = ""

        for end in range(start, len(lines)):

            if combined:

                combined += " " + lines[end]

            else:

                combined = lines[end]

            result.append(combined)


    return list(set(result))



def load_localized_strings(
        language=LANGUAGE,
        excel_path=EXCEL_PATH):



    workbook = openpyxl.load_workbook(
        excel_path,
        data_only=True
    )


    sheet = workbook.active

    print(
        "Localization Excel Sheet Used: "
        + sheet.title
    )

    headers = []

    for cell in sheet[1]:

        if cell.value is None:

            headers.append("")

        else:

            headers.append(
                str(cell.value).strip()
            )


    try:

        english_column = headers.index(
            "English"
        )

    except ValueError:

        workbook.close()

        raise Exception(
            "English column not found in active sheet: "
            + sheet.title
        )


    try:

        language_column = headers.index(
            language
        )

    except ValueError:

        workbook.close()

        raise Exception(
            "Language '"
            + language
            + "' not found in active sheet: "
            + sheet.title
        )


    strings = []


    for row in sheet.iter_rows(
            min_row=2,
            values_only=True):


        if not row:
            continue


        if len(row) <= max(
                english_column,
                language_column):

            continue


        english = row[english_column]
        localized = row[language_column]


        if english is None or localized is None:
            continue


        english = str(english).strip()
        localized = str(localized).strip()


        if not english or not localized:
            continue



        strings.append({

            "english": english,

            "localized": localized,

            "normalized_english":
                normalize(english),

            "normalized":
                normalize(localized)

        })


    workbook.close()

    return strings




def verify_strings(
        objects,
        screen_name,
        excel_strings,
        expected_english_strings):


    runtime_candidates = []

    for obj in objects:

        runtime_candidates.extend(
            get_all_text_combinations(obj)
        )



    runtime_candidates = list(
        set(runtime_candidates)
    )

    normalized_runtime = []

    for text in runtime_candidates:

        normalized = normalize(text)

        if normalized:

            normalized_runtime.append(
                (normalized, text)
            )


    pass_count = 0
    fail_count = 0



    for expected_english in expected_english_strings:

        excel_item = None
        
        for item in excel_strings:

            if (
                item["normalized_english"]
                ==
                normalize(expected_english)
            ):

                excel_item = item

                break


        if excel_item is None:

            message = (
                "English string not found in Excel -> "
                + expected_english
            )

            print("FAIL: " + message)

            test.fail(message)

            fail_count += 1

            continue


        expected_localized = (
            excel_item["localized"]
        )

        expected_normalized = (
            excel_item["normalized"]
        )


        matched = False
        untranslated = False


      
        for actual_normalized, actual_text in normalized_runtime:

            if "XXXX" in str(expected_localized):
        
                if match_profile_placeholder(
                    actual_text,
                    expected_localized
                ):
                    matched = True
        
                    test.log(
                        "PASS: Dynamic placeholder matched -> "
                        + repr(actual_text)
                    )
                    break
        
            else:
        
                if actual_normalized == expected_normalized:
                    matched = True
                    break
        
                elif (
                    len(expected_normalized) >= 4
                    and expected_normalized in actual_normalized
                ):
                    matched = True
                    break
        
            if actual_normalized == excel_item["normalized_english"]:
                untranslated = True


  

            if actual_normalized == expected_normalized:

                matched = True

                break



            elif (
                len(expected_normalized) >= 4
                and
                expected_normalized
                in actual_normalized
            ):

                matched = True

                break


            if (
                actual_normalized
                ==
                excel_item["normalized_english"]
            ):

                untranslated = True


        if matched:

            print(
                "PASS: "
                + expected_english
                + " -> "
                + expected_localized
            )

            test.passes(
                expected_english
                + " -> "
                + expected_localized
            )

            pass_count += 1

        elif untranslated:

            message = (
                "UNTRANSLATED: "
                + expected_english
                + " is displayed instead of "
                + expected_localized
            )

            print("FAIL: " + message)

            test.fail(message)

            fail_count += 1


        else:

            message = (
                "Expected "
                + expected_english
                + " -> "
                + expected_localized
                + " but localized string was not found on "
                + screen_name
            )

            print("FAIL: " + message)

            test.fail(message)

            fail_count += 1

    print(
        screen_name
        + " Localization Result: PASS = "
        + str(pass_count)
        + ", FAIL = "
        + str(fail_count)
    )


    if fail_count == 0 and pass_count > 0:

        test.passes(
            screen_name
            + " LOCALIZATION VALIDATION PASSED"
        )

    else:

        test.fail(
            screen_name
            + " LOCALIZATION VALIDATION FAILED"
        )

def validate_localization(
        objects,
        screen_name,
        expected_strings,
        language=LANGUAGE,
        excel_path=EXCEL_PATH):

    excel_strings = load_localized_strings(
        language=LANGUAGE,
        excel_path=excel_path
    )

    verify_strings(
        objects=objects,
        screen_name=screen_name,
        excel_strings=excel_strings,
        expected_english_strings=expected_strings
    )
    
    
def enterpin():
    """Login to the application by accepting the popup and entering PIN 0000."""
    for i in range(4):
            clickButton(waitForObject(names.wdKeypad_pushButton_0_QPushButton, 20000))
    
    test.passes("PASS: PIN 0000 entered")
    
def open_default_profile_presets():
    """Select Default Profile and open Presets."""
 
    try:
        clickButton(waitForObject(
            names.sclProfiles_Default_ProfileButton, 20000))
        test.passes("PASS: Default Profile selected")
 
        clickButton(waitForObject(
            names.apollo_btPresets_QPushButton, 20000))
        test.passes("PASS: Presets screen opened")
 
    except Exception as error:
        test.fail("FAIL: Open Default Profile Presets - {}".format(error))
        raise
  
    
def open_default_profile_treatment_logs():
    """Select Default Profile and open Treatment Logs."""
 
    try:
        clickButton(waitForObject(
            names.sclProfiles_Default_ProfileButton, 20000))
        test.passes("PASS: Default Profile selected")
 
        clickButton(waitForObject(
            names.apollo_btTreatmentLogs_QPushButton, 20000))
        test.passes("PASS: Treatment Logs screen opened")
 
    except Exception as error:
        test.fail("FAIL: Open Default Profile Treatment Logs - {}".format(error))
        raise
    
 
def open_default_profile_settings():
    """Select Default Profile and open Settings."""
 
    try:
        clickButton(waitForObject(
            names.sclProfiles_Default_ProfileButton, 20000))
        test.passes("PASS: Default Profile selected")
 
        clickButton(waitForObject(
            names.apollo_btSettings_QPushButton, 20000))
        test.passes("PASS: Settings screen opened")
 
    except Exception as error:
        test.fail("FAIL: Open Default Profile Settings - {}".format(error))
        raise    
    
    
def get_text_lines(obj):
    lines = []

    try:
        if not obj.visible:
            return lines
    except:
        pass

    try:
        text = str(obj.text).strip()
        if text:
            lines.append(text)
    except:
        pass

    # READ PLACEHOLDER TEXT
    try:
        placeholder = str(obj.placeholderText).strip()
        if placeholder:
            lines.append(placeholder)
    except:
        pass

    try:
        title = str(obj.title).strip()
        if title:
            lines.append(title)
    except:
        pass

    try:
        for child in object.children(obj):
            lines.extend(get_text_lines(child))
    except:
        pass

    return lines



def match_profile_placeholder(actual_text, expected_text):

    def clean_text(text):
        text = unicodedata.normalize("NFKC", str(text))

        text = text.casefold()

        text = text.translate(str.maketrans({
            "„": '"',
            "”": '"',
            "“": '"',
            "‟": '"',
            "’": "'",
            "‘": "'"
        }))

        text = re.sub(r"<br\s*/?>", " ", text, flags=re.IGNORECASE)
        text = re.sub(r"\s+", " ", text).strip()

        return text

    actual = clean_text(actual_text)
    expected = clean_text(expected_text)

    if "xxxx" not in expected:
        return actual == expected

    pattern = re.escape(expected)

    pattern = pattern.replace(
        re.escape("xxxx"),
        r".+?"
    )

    return re.fullmatch(pattern, actual) is not None


def validate_aiming_beam_label():
 
    from openpyxl import load_workbook
 
    english_text = "AIMING BEAM"
 
    workbook = load_workbook(
        EXCEL_PATH,
        read_only=True,
        data_only=True
    )
 
    try:
        sheet = workbook["GUI Strings"]
 
        language_column = None
 
        for column in range(1, sheet.max_column + 1):
 
            language_name = sheet.cell(row=1, column=column).value
 
            if (
                language_name
                and str(language_name).strip().casefold()
                == LANGUAGE.strip().casefold()
            ):
                language_column = column
                break
 
        if language_column is None:
            test.fail(
                "Language '{}' not found in Excel.".format(LANGUAGE)
            )
            return
 
        expected_text = None
 
        for row in range(2, sheet.max_row + 1):
 
            english_value = sheet.cell(row=row, column=1).value
 
            if (
                english_value
                and str(english_value).strip().casefold()
                == english_text.casefold()
            ):
                expected_text = sheet.cell(
                    row=row,
                    column=language_column
                ).value
                break
 
        if expected_text is None or not str(expected_text).strip():
            test.fail(
                "'{}' translation not found in Excel for language '{}'.".format(
                    english_text,
                    LANGUAGE
                )
            )
            return
 
        expected_text = str(expected_text).strip()
 
    finally:
        workbook.close()
 
    aiming_beam_label = waitForObject({
        "name": "lbAimingBeam",
        "type": "QLabel"
    })
 
    actual_text = str(aiming_beam_label.text).strip()
 
    if normalize(actual_text) == normalize(expected_text):
 
        test.passes(
            english_text + " -> " + expected_text
        )
 
    else:
 
        test.fail(
            "FAIL: "
            + english_text
            + " -> "
            + expected_text
            + " | Actual UI text: "
            + actual_text
        )
        
        
def validate_assistant_label():

    from openpyxl import load_workbook

    english_text = "Assistant"

    workbook = load_workbook(
        EXCEL_PATH,
        read_only=True,
        data_only=True
    )

    try:
        sheet = workbook["GUI Strings"]

        language_column = None

        for column in range(1, sheet.max_column + 1):
            language_name = sheet.cell(row=1, column=column).value

            if (
                language_name
                and str(language_name).strip().casefold()
                == LANGUAGE.strip().casefold()
            ):
                language_column = column
                break

        if language_column is None:
            test.fail(
                "Language '{}' not found in Excel.".format(LANGUAGE)
            )
            return

        expected_text = None

        for row in range(2, sheet.max_row + 1):
            english_value = sheet.cell(row=row, column=1).value

            if (
                english_value
                and str(english_value).strip().casefold()
                == english_text.casefold()
            ):
                expected_text = sheet.cell(
                    row=row,
                    column=language_column
                ).value
                break

        if expected_text is None or not str(expected_text).strip():
            test.fail(
                "'{}' translation not found in Excel for language '{}'.".format(
                    english_text,
                    LANGUAGE
                )
            )
            return

        expected_text = str(expected_text).strip()

    finally:
        workbook.close()

    assistant_button = waitForObject(
        names.apollo_tbAssistant_QToolButton
    )

    actual_text = str(
        assistant_button.property("localizationText")
    ).strip()

    if normalize(actual_text) == normalize(expected_text):

        test.passes(
            english_text + " -> " + expected_text
        )

    else:

        test.fail(
            "FAIL: "
            + english_text
            + " -> "
            + expected_text
            + " | Actual UI text: "
            + actual_text
        )
        
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
