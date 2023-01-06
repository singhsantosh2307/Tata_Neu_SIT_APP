from appium import webdriver
from os import path
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
import time


APPIUM = 'https://dev-in-mua-0.headspin.io:7024/v0/0eac5bd7e0b64ccfa9d7044dc07522c1/wd/hub'

CAPS = {
    "deviceName": "iPhone 13",
    "udid": "00008110-001C059C22E9801E",
    "automationName": "xcuitest",
    "platformVersion": "15.3",
    "platformName": "ios",
    "bundleId" : "com.tatadigital.tcp.dev",
    "headspin:capture.video": True
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

#Locators

notNowBtn = (MobileBy.ACCESSIBILITY_ID,'Not Now')
flightsBtn = (MobileBy.ACCESSIBILITY_ID, 'Flights')
cancelBtn = (MobileBy.ACCESSIBILITY_ID, 'crossWhite')
flyTo = (MobileBy.XPATH,"//div[text()='Fly to']")
selectFirstDestn = (MobileBy.XPATH,"(//button[@id='list-item'])[1]")
goToBooking = (MobileBy.XPATH,"//img[@alt='select']")
selectFlight = (MobileBy.XPATH, "(//div[@class='b2c-standard-price fsa-price-block-width'])[1]")
continueBtn = (MobileBy.XPATH,"//button[@class='continue-btn']")
saveBtn = (MobileBy.XPATH, "(//button[text()='Save'])[1]")
continuePassenger = (MobileBy.XPATH, "//button[@class='pi-continue-btn']")
yesBtn = (MobileBy.XPATH, "//button[@class='nsspm-yes-btn']")
makeThePayment = (MobileBy.XPATH, "//span[text()='Make the payment']")

#Code

def swipeDown():
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(268, 600)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(235, 436)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

def switch_to_web_context(window_title= None, window_index=None ):
        """
        switching to Web Context
        """
        print("starting context switching")

        for _ in range(5):
            if len(driver.contexts) != 1:
                context_list = driver.contexts
                # print(context_list)
                break
            time.sleep(1)
        else:
            raise Exception("Webview not available for context switching")
        driver.switch_to.context(context_list[-1])
        print("Current Context : ",driver.current_context)
        print(driver.title)    

try:
    wait = WebDriverWait(driver, 15)
    print("App Launched")
    time.sleep(2)
    wait.until(EC.presence_of_element_located(notNowBtn)).click()
    wait.until(EC.presence_of_element_located(notNowBtn)).click()
    try:
        wait.until(EC.presence_of_element_located(cancelBtn)).click()
    except:
        pass
    print("Not Now Clicked")

    try:
        swipeDown()
        time.sleep(2)
        wait.until(EC.presence_of_element_located(flightsBtn)).click()
    except:    
        swipeDown()
        time.sleep(2)
        wait.until(EC.presence_of_element_located(flightsBtn)).click()
    print("Swipe Down")
    print("Flight Tab Click")
    time.sleep(10)
    switch_to_web_context()
    time.sleep(2)
    wait.until(EC.presence_of_element_located(flyTo)).click()
    wait.until(EC.presence_of_element_located(selectFirstDestn)).click()
    wait.until(EC.presence_of_element_located(goToBooking)).click()
    print("Flight Booking Proceed")
    time.sleep(2)
    swipeDown()
    wait.until(EC.presence_of_element_located(selectFlight)).click()
    wait.until(EC.presence_of_element_located(continueBtn)).click()
    time.sleep(2)
    wait.until(EC.presence_of_element_located(saveBtn)).click()
    time.sleep(2)
    swipeDown()
    wait.until(EC.presence_of_element_located(saveBtn)).click()
    print("Passenger Details Saved")
    time.sleep(2)
    wait.until(EC.presence_of_element_located(continuePassenger)).click()
    wait.until(EC.presence_of_element_located(continuePassenger)).click()
    time.sleep(2)
    wait.until(EC.presence_of_element_located(continuePassenger)).click()
    time.sleep(2)
    wait.until(EC.presence_of_element_located(yesBtn)).click()
    print("Seat Selection Done")
    time.sleep(2)
    wait.until(EC.presence_of_element_located(makeThePayment))
    print("User Reach Payment Page")
    time.sleep(2)
finally:
    driver.quit()
    
