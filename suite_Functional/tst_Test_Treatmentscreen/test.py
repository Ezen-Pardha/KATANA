# -*- coding: utf-8 -*-

import names


def main():
    snooze(3)

    mouseClick(waitForObject(names.wdPopup_lbText_QLabel_2), 95, 7, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.footswitchPopup_pbWired_WdPushButton))
    snooze(3)
    mouseClick(waitForObject(names.homeScreen_lbText_QLabel_2), 317, 33, Qt.NoModifier, Qt.LeftButton)
    snooze(3)
    clickButton(waitForObject(names.wdPulseEnergyPickerWheel_btIncrease_WdPushButton, 84448))
    snooze(3)
   
#---------------------------------Working one-------------------    
    # Expected values after each click
    expectedEnergy = [ "0.2", "0.3","0.4","0.5","0.6"]
    expectedAveragePower = ["4", "6","8","10","12"]   # Update these values as per your application
    expectedFrequecy=["20", "20", "20", "20", "20"]
    for energyValue, avgPowerValue, freqValue in zip(expectedEnergy, expectedAveragePower,expectedFrequecy):
        snooze(2)
        clickButton(waitForObject(names.wdPulseEnergyPickerWheel_btIncrease_WdPushButton))
        snooze(2)
    
    # Verify Frequency
        frequencyWheel = waitForObject(names.pulseModeWidget_wdFrequencyPickerWheel_WdPickerWheel)
        test.log("Frequency = {}".format(frequencyWheel.displayValue))
        test.compare(frequencyWheel.displayValue, freqValue)
        snooze(2)
    # Verify Energy
        energyWheel = waitForObject(names.pulseModeWidget_wdPulseEnergyPickerWheel_WdPickerWheel)
        test.log("Energy = {}".format(energyWheel.displayValue))
        test.compare(energyWheel.displayValue, energyValue)
        snooze(2)
    # Verify Average Power
        averagePower = waitForObjectExists(names.pulseModeWidget_wdAveragePowerValue_WdUnitLabel)
        test.log("Average Power = {}".format(averagePower.text))
        test.compare(str(averagePower.text), avgPowerValue)
        snooze(2)
    
    expectedEnergy1 = ["0.5", "0.4","0.3","0.2"]
    expectedAveragePower1 = ["10","8","6","4"]   # Update these values as per your application
    expectedFrequecy1=["20", "20", "20", "20", "20"]    
    
    for energyValue1, avgPowerValue1, freqValue1 in zip(expectedEnergy1, expectedAveragePower1,expectedFrequecy1):
        snooze(5)    
        clickButton(waitForObject(names.wdPulseEnergyPickerWheel_btDecrease_WdPushButton))
    
    # Verify Frequency
        frequencyWheel1 = waitForObject(names.pulseModeWidget_wdFrequencyPickerWheel_WdPickerWheel)
        test.log("Frequency = {}".format(frequencyWheel1.displayValue))
        test.compare(frequencyWheel1.displayValue, freqValue1)
        snooze(2)
    # Verify Energy
        energyWheel1 = waitForObject(names.pulseModeWidget_wdPulseEnergyPickerWheel_WdPickerWheel)
        test.log("Energy = {}".format(energyWheel.displayValue))
        test.compare(energyWheel1.displayValue, energyValue1)
        snooze(2)
    # Verify Average Power
        averagePower1 = waitForObjectExists(names.pulseModeWidget_wdAveragePowerValue_WdUnitLabel)
        test.log("Average Power = {}".format(averagePower1.text))
        test.compare(str(averagePower1.text), avgPowerValue1)
        snooze(2)
    
    
    

