from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pageobjects import locators
from os import sys, path
sys.path.append( path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ) )
from framework.general import *
from datavalues.datavalues import *

# Control 1
def CreateControlUser1(driver):
    insert_text(driver,"By.ID", "username", "nate_control1")
    insert_text(driver, "By.ID", "password", "123$Asdfnovatech!")
    insert_text(driver, "By.ID", "verifypassword", "123$Asdfnovatech!")

    click(driver, "By.XPATH", "//input[@name='checkall']")

    if global_vars.platform_version == "lxm" or global_vars.platform_version == "mx":
        # LXM shifts everything on the table down one
        disableCheckbox(driver, "By.XPATH", "//input[14]") #2
        disableCheckbox(driver, "By.XPATH", "//input[15]") #3
        disableCheckbox(driver, "By.XPATH", "//input[16]") #4 
        disableCheckbox(driver, "By.XPATH", "//input[17]") #5
    else:
        disableCheckbox(driver, "By.XPATH", "//input[15]") #2
        disableCheckbox(driver, "By.XPATH", "//input[16]") #3
        disableCheckbox(driver, "By.XPATH", "//input[17]") #4 
        disableCheckbox(driver, "By.XPATH", "//input[18]") #5

    click(driver, "By.XPATH", "//input[@name='AddUser']")


def TestAccount1(driver):
    # Logging in:
    insert_text(driver, "By.XPATH", "//input[@id='username']", "nate_control1")
    insert_text(driver, "By.ID", "password", "123$Asdfnovatech!")
    click(driver, "By.XPATH", "//input[@value='Login']")
    click(driver, "By.XPATH", "//a[contains(text(),'Unlock')]")
    insert_text(driver, "By.ID", "password", "123$Asdfnovatech!")
    click(driver, "By.XPATH", "//input[@value='Unlock']")
    click(driver, "By.XPATH", "//a[contains(text(),'home_lr.svg')]")

    # ASSERTS Recloser 1 (Working):
    click(driver, "By.ID", "rect5131"); 
    if global_vars.platform_version == "lxplus":
        click(driver, "By.ID", "rect12699")
    else:
        click(driver, "By.ID", "rect12685"); 

    assertExpectedConditionTrue(driver, "By.XPATH", "//p[contains(.,'Control Feeder1 Recloser')]")
    assertExpectedConditionFalse(driver, "By.XPATH", "//span[contains(.,'Insufficient permissions.')]") 

    click(driver, "By.XPATH", "//button[contains(.,'Cancel')]");

    # ASSERTS Breaker 1 (Working):
    click_action_chains(driver, "By.ID", "tspan14345", "BREAKER CONTROL")
    assertExpectedConditionTrue(driver, "By.XPATH", "//p[contains(.,'Control Feeder1 Breaker')]")
    assertExpectedConditionFalse(driver, "By.XPATH", "//span[contains(.,'Insufficient permissions.')]")

    click(driver, "By.XPATH", "//button[contains(.,'Cancel')]");

    driver.execute_script("window.history.go(-1)") # back one

    # ASSERTS Recloser 2: 
    click(driver, "By.ID", "rect2417");
    if global_vars.platform_version == "lxplus":
        click(driver, "By.ID", "rect12699")
    else:
        click(driver, "By.ID", "rect12685");

    assertExpectedConditionTrue(driver, "By.XPATH", "//span[contains(.,'Insufficient permissions.')]")
    assertExpectedConditionFalse(driver, "By.XPATH", "//p[contains(.,'Control Feeder2 Breaker')]")
    click(driver, "By.XPATH", "//button[contains(.,'Ok')]");

    # ASSERTS Breaker 2:
    click_action_chains(driver, "By.ID", "tspan14345", "BREAKER CONTROL")
    assertExpectedConditionTrue(driver, "By.XPATH", "//span[contains(.,'Insufficient permissions.')]") 
    assertExpectedConditionFalse(driver, "By.XPATH", "//p[contains(.,'Control Feeder2 Breaker')]")
    click(driver, "By.XPATH", "//button[contains(.,'Ok')]");

    driver.execute_script("window.history.go(-1)") # back one


    # ASSERTS Recloser 3:
    click(driver, "By.ID", "rect2467"); 
    if global_vars.platform_version == "lxplus":
        click(driver, "By.ID", "rect12699")
    else:
        click(driver, "By.ID", "rect12685");

    assertExpectedConditionTrue(driver, "By.XPATH", "//span[contains(.,'Insufficient permissions.')]")
    assertExpectedConditionFalse(driver, "By.XPATH", "//p[contains(.,'Control Feeder3 Breaker')]")
    click(driver, "By.XPATH", "//button[contains(.,'Ok')]");

    # ASSERTS Breaker 3:
    click_action_chains(driver, "By.ID", "tspan14345", "BREAKER CONTROL")
    assertExpectedConditionTrue(driver, "By.XPATH", "//span[contains(.,'Insufficient permissions.')]") 
    assertExpectedConditionFalse(driver, "By.XPATH", "//p[contains(.,'Control Feeder3 Breaker')]")
    click(driver, "By.XPATH", "//button[contains(.,'Ok')]");


    driver.execute_script("window.history.go(-1)") # back one


    # ASSERTS Recloser 4:
    click(driver, "By.ID", "rect2517") 
    if global_vars.platform_version == "lxplus":
        click(driver, "By.ID", "rect12699")
    else:
        click(driver, "By.ID", "rect12685");

    assertExpectedConditionTrue(driver, "By.XPATH", "//span[contains(.,'Insufficient permissions.')]")
    assertExpectedConditionFalse(driver, "By.XPATH", "//p[contains(.,'Control Feeder4 Breaker')]")
    click(driver, "By.XPATH", "//button[contains(.,'Ok')]");

    # ASSERTS Breaker 4:
    click_action_chains(driver, "By.ID", "tspan14345", "BREAKER CONTROL") 
    assertExpectedConditionTrue(driver, "By.XPATH", "//span[contains(.,'Insufficient permissions.')]")
    assertExpectedConditionFalse(driver, "By.XPATH", "//p[contains(.,'Control Feeder4 Breaker')]")
    click(driver, "By.XPATH", "//button[contains(.,'Ok')]");


    click(driver, "By.XPATH", "//span[contains(.,'Home')]");


# Delete Users
def TearDown(driver):
    # Navigate
    click(driver, "By.XPATH", "//ul[@id='mainNav']/li[9]/a/span")

    click(driver, "By.XPATH", "//a[contains(text(),'Users')]")


    # Delete
    click(driver, "By.XPATH", "//a[contains(text(),'nate_control1')]")
    click(driver, "By.XPATH", "//input[@name='deleteuser']")
    click(driver, "By.XPATH", "//input[@name='deleteuser']")


def test_settingsUsersGroupsControl1(driver, url):
    # Log in, activate config
    loginToOrion(driver, url).confirmLoginAndUnlocked()
    activeConfig(driver, url, "svgexmpl.ncd", "svgexmpl.bas").confirmConfigSet()

    # To settings
    getURL(driver, url, "/Settings/")
    click(driver, "By.XPATH", "//div[3]/ul/li/a")   

    # Create Control Users
    CreateControlUser1(driver);
    getURL(driver, url, "/Settings/")

    # WebUI -> home_lr -> save -> home
    click(driver, "By.XPATH", "//a[contains(text(),'WebUI')]")
    click(driver, "By.XPATH", "//span[@id='Save']/span/button")

    webUIFiles(driver, url, ["home_lr.svg"]).confirmSVGFilesActivated()

    click(driver, "By.XPATH", "//span[contains(.,'Home')]")
    click(driver, "By.XPATH", "//a[contains(text(),'Logout')]")

    TestAccount1(driver);

    click(driver, "By.XPATH", "//a[contains(text(),'Logout')]")


    assertURL(driver, "/Home", 4)
    assertExpectedConditionTrue(driver, "By.XPATH", "//input[@id='username']", None, 4)

    loginToOrion(driver, url).confirmLoginAndUnlocked()



    TearDown(driver);