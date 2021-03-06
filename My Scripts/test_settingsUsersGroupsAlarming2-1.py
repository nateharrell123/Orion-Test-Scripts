from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from pageobjects import locators
from os import sys, path
sys.path.append( path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ) )
from framework.general import *
from datavalues.datavalues import *

# Alarm2
def CreateAlarmUser2(driver):
    insert_text(driver,"By.ID", "username", "nate_alarming2")
    insert_text(driver, "By.ID", "password", "123$Asdfnovatech!")
    insert_text(driver, "By.ID", "verifypassword", "123$Asdfnovatech!")

    click(driver, "By.XPATH", "//input[@name='checkall']")

    disableCheckbox(driver, "By.XPATH", "//input[8]")
    disableCheckbox(driver, "By.XPATH", "//input[10]")
    disableCheckbox(driver, "By.XPATH", "//input[11]")
    disableCheckbox(driver, "By.XPATH", "//input[12]")

    click(driver, "By.XPATH", "//input[@name='AddUser']")




def ForcePoints(driver):
   # (driver, row, forceValue, forceValueType=None, commStatus=None, timeForced=None, choice=None):
    forceInputValue(driver, 1, 1, None, None, 20) # 1
    forceInputValue(driver, 2, 1, None, None, 20) # 10
    forceInputValue(driver, 12, 1, None, None, 20) # 2
    forceInputValue(driver, 23, 1, None, None, 20) # 3
    forceInputValue(driver, 30, 1, None, None, 20) # 4

    click(driver, "By.XPATH", "//a[@id='datavalues_table_next']")
    for i in range(1,6):
        forceInputValue(driver, i, 1, None, None, 20) # 5-10


def Assertions(driver):
    assertExpectedConditionTrue(driver, "By.XPATH", "//table[@id='alarmsInfoTable']/tbody/tr[3][@style='color: darkorange;']/td[4]")
    assertExpectedConditionTrue(driver, "By.XPATH", "//table[@id='alarmsInfoTable']/tbody/tr[8][@style='color: darkorange;']/td[4]") 


def TestAccount2(driver):
    click(driver, "By.XPATH", "//a[contains(text(),'Logout')]")
    insert_text(driver, "By.XPATH", "//input[@id='username']", "nate_alarming2")
    insert_text(driver, "By.ID", "password", "123$Asdfnovatech!")

    click(driver, "By.XPATH", "//input[@value='Login']")
    click(driver, "By.XPATH", "//span[contains(.,'Alarms')]")

    click(driver, "By.XPATH", "//a[contains(text(),'Click here to unlock these options.')]")
    insert_text(driver, "By.ID", "password", "123$Asdfnovatech!")
    click(driver, "By.XPATH", "//input[@value='Unlock']")


def Organize(driver):
    if global_vars.platform_version == "io":
        print("about to click")
        click(driver, "By.XPATH", "(//input[@id='update'])[2]")
    else:
        click(driver, "By.XPATH", "//input[@id='selectAll']")
        click(driver, "By.XPATH", "//input[@id='AckSelectedAlarms']")
        click(driver, "By.XPATH", "//th[contains(.,'Point Name')]")
        click(driver, "By.XPATH", "//th[contains(.,'Point Name')]")

# Delete Users
def TearDown(driver):
    # Navigate
    click(driver, "By.XPATH", "//ul[@id='mainNav']/li[9]/a/span")

    insert_text(driver, "By.XPATH", "//input[@id='password']", "novatech")
    click(driver, "By.XPATH", "//input[@value='Unlock']")

    click(driver, "By.XPATH", "//a[contains(text(),'Users')]")


    click(driver, "By.XPATH", "//a[contains(text(),'nate_alarming2')]")
    click(driver, "By.XPATH", "//input[@name='deleteuser']")
    click(driver, "By.XPATH", "//input[@name='deleteuser']")


def CleanSlate(driver):
    if global_vars.platform_version == "io":
        click(driver, "By.XPATH", "//span[contains(.,'Alarms')]")
        click(driver, "By.XPATH", "(//input[@id='update'])[2]")
    else:
        click(driver, "By.XPATH", "//span[contains(.,'Alarms')]")
        click(driver, "By.XPATH", "//input[@id='selectAll']")
        click(driver, "By.XPATH", "//input[@id='AckSelectedAlarms']")
    # maybe add more version checks here


def test_settingsUsersGroupsAlarmingGroups2(driver, url):
    # Log in, activate config
    loginToOrion(driver, url).confirmLoginAndUnlocked()
    activeConfig(driver, url, "OrionLX_AAR_Standard_Test.ncd", "OrionLX_AAR_Standard_Test.lua").confirmConfigSet()

    CleanSlate(driver)


    # To settings
    getURL(driver, url, "/Settings/")
    click(driver, "By.XPATH", "//div[3]/ul/li/a")    

    # Create Alarm Users
    CreateAlarmUser2(driver)


    # Logic Inputs
    click(driver, "By.XPATH", "//ul[@id='mainNav']/li[2]/a/span")
    if global_vars.platform_version == "io":
        click(driver, "By.XPATH", "//a[contains(@href, '/Points/Port/124/Inputs')]")
    else:
        click(driver, "By.XPATH", "(//a[contains(text(),'inputs')])[22]")


    clearInputOverride(driver)

    # Search 'alarm'
    insert_text(driver, "By.XPATH", "//input[@id='searchTerm']", "alarm")
    click(driver, "By.XPATH", "//button[@id='searchPoints']")

    #Force points
    ForcePoints(driver)

    # Logic Inputs
    click(driver, "By.XPATH", "//ul[@id='mainNav']/li[2]/a/span")
    click(driver, "By.XPATH", "(//a[contains(text(),'inputs')])[22]")

    # Testing one of the accounts
    TestAccount2(driver)

    # Format table
    Organize(driver)
    Assertions(driver)

    click(driver, "By.XPATH", "//a[contains(text(),'Logout')]")
    insert_text(driver, "By.XPATH", "//input[@id='username']", "novatech")
    insert_text(driver, "By.XPATH", "//input[@id='password']", "novatech")

    click(driver, "By.XPATH", "//input[@value='Login']")

    TearDown(driver)