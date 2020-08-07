from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from pageobjects import locators
from os import sys, path
sys.path.append( path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ) )
from framework.general import *
from datavalues.datavalues import *

def CreateUser(driver):
    insert_text(driver,"By.ID", "username", "nate_web1")
    insert_text(driver, "By.ID", "password", "123&*(@#Asdf")
    insert_text(driver, "By.ID", "verifypassword", "123&*(@#Asdf")

    click(driver, "By.XPATH", "//input[@name='checkall']")

    disableCheckbox(driver, "By.XPATH", "//input[44]") # input

    click(driver, "By.XPATH", "//input[@name='AddUser']")

# Delete Users
def TearDown(driver):
    # Navigate

    click(driver, "By.XPATH", "//ul[@id='mainNav']/li[9]/a/span")

    click(driver, "By.XPATH", "//a[contains(text(),'Users')]")


    # Delete
    click(driver, "By.XPATH", "//a[contains(text(),'nate_web1')]")
    click(driver, "By.XPATH", "//input[@name='deleteuser']")
    click(driver, "By.XPATH", "//input[@name='deleteuser']")

def test_SettingsUsersWebFilesPermissionAdd(driver, url):
    # Log in, activate config
    loginToOrion(driver, url).confirmLoginAndUnlocked()
    activeConfig(driver, url, "svgexmpl.ncd", "OrionLX_AAR_Standard_Test.lua").confirmConfigSet()

    getURL(driver, url, "/Settings/")
    click(driver, "By.XPATH", "//div[3]/ul/li/a")   

    # Create User
    CreateUser(driver);

    # Log out of 'novatech'
    click(driver, "By.XPATH", "//span[contains(.,'Home')]")
    click(driver, "By.XPATH", "//a[contains(text(),'Logout')]")

    # 'Log in as test acct'
    insert_text(driver, "By.XPATH", "//input[@id='username']", "nate_web1")
    insert_text(driver, "By.ID", "password", "123&*(@#Asdf")
    click(driver, "By.XPATH", "//input[@value='Login']")
    click(driver, "By.XPATH", "//a[contains(text(),'Unlock')]")
    insert_text(driver, "By.ID", "password", "123&*(@#Asdf")
    click(driver, "By.XPATH", "//input[@value='Unlock']")

    click(driver, "By.XPATH", "//span[contains(.,'Files')]")

    # Will throw an error, because of permissions
    try:
        uploadFiles(driver, url, ["home_lr.svg"])
    except:
        pass
    # Page stays the same
    assertExpectedConditionTrue(driver, "By.XPATH", "//span[contains(.,'or drag and drop them onto this page to send them to the Orion.')]")
    
    TearDown(driver);