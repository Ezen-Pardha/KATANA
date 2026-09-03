# -*- coding: utf-8 -*-

import user

def main():
    clickButton(waitForObject(user.footswitchPopup_pbWired_WdPushButton))
    mouseClick(waitForObject(user.homeScreen_wdBottom_QWidget), 134, 120, Qt.NoModifier, Qt.LeftButton)
    setWindowState(waitForObject(user.o_ScreenSwitcher), WindowState.Minimize)
    
    expectedEnergy = ["0.15", "0.2", "0.3", "0.4", "0.5"]

    for energyValue in expectedEnergy:

        clickButton(waitForObject(user.wdPulseEnergyPickerWheel_btIncrease_WdPushButton))
        snooze(2)

    # Verify Frequency
        frequencyWheel = waitForObject(user.pulseModeWidget_wdFrequencyPickerWheel_WdPickerWheel)
        test.log("Frequency = {}".format(frequencyWheel.displayValue))
        test.compare(frequencyWheel.displayValue, "20")

    # Verify Energy
        energyWheel = waitForObject(user.pulseModeWidget_wdPulseEnergyPickerWheel_WdPickerWheel)
        test.log("Energy = {}".format(energyWheel.displayValue))
        test.compare(energyWheel.displayValue, energyValue)
       
        expectedPower = float(energyValue) * float(str(frequencyWheel.displayValue))
        if expectedPower.is_integer():
            expectedPower = str(int(expectedPower))
        else:
            expectedPower = str(expectedPower)

            averagePower = waitForObjectExists(user.pulseModeWidget_wdAveragePowerValue_WdUnitLabel)

            test.compare(str(averagePower.text), expectedPower)

    # Verify Average Power
        averagePower = waitForObjectExists(user.pulseModeWidget_wdAveragePowerValue_WdUnitLabel)
        test.log("Average Power = {}".format(averagePower.text))
        test.compare(str(averagePower.text), expectedPower)
        test.log("Average Power = {} * {} = {}".format(energyWheel.displayValue,frequencyWheel.displayValue,expectedPower))
        snooze(2)

    expectedEnergy = ["0.4", "0.3", "0.2","0.15"]

    for energyValue in expectedEnergy:

        clickButton(waitForObject(user.wdPulseEnergyPickerWheel_btDecrease_WdPushButton))
        snooze(2)

    # Verify Frequency
        frequencyWheel = waitForObject(user.pulseModeWidget_wdFrequencyPickerWheel_WdPickerWheel)
        test.compare(frequencyWheel.displayValue, "20")

    # Verify Energy
        energyWheel = waitForObject(user.pulseModeWidget_wdPulseEnergyPickerWheel_WdPickerWheel)
        test.compare(energyWheel.displayValue, energyValue)

    # Calculate Expected Average Power
        expectedPower = float(energyValue) * float(str(frequencyWheel.displayValue))
        if expectedPower.is_integer():
            expectedPower = str(int(expectedPower))
        else:
            expectedPower = str(expectedPower)

            averagePower = waitForObjectExists(user.pulseModeWidget_wdAveragePowerValue_WdUnitLabel)

            test.compare(str(averagePower.text), expectedPower)
    # Verify Average Power
        averagePower = waitForObjectExists(user.pulseModeWidget_wdAveragePowerValue_WdUnitLabel)
        test.log("Average Power = {}".format(averagePower.text))
        test.compare(str(averagePower.text), expectedPower)
        test.log("Average Power = {} * {} = {}".format(energyWheel.displayValue,frequencyWheel.displayValue,expectedPower))
        snooze(2)        

    snooze(2) 
    
    
