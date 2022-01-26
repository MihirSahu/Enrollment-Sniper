#!/usr/bin/env python3

# FIND EVERYTHING HERE
# https://www.selenium.dev/

# Import modules
import time
import requests
from tkinter import *
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# Selenium instance
driver = webdriver.Chrome()

# Global Variables
username = ""
password = ""
term = ""
class_name = ""
class_number = ""

# Functions
def main():
    logIn()
    bypassDuo()
    navigateToEnroll()
    searchForClass()

def startBrowser():
    url = 'https://accessuh.uh.edu/login.php'
    driver.get(url)

def getSourceCode():
    return driver.page_source

def logIn():
    startBrowser()
    username_input = driver.find_element_by_name('username').send_keys(username)
    password_input = driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_class_name('waves-button-input').click()

def bypassDuo():
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "duo_iframe")))
    driver.switch_to.frame(driver.find_element(By.ID, "duo_iframe"))
    driver.find_element_by_css_selector("button[tabindex='2']").click()

def navigateToEnroll():
    time.sleep(5)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='myUH Self Service']")))
    driver.find_element_by_css_selector("img[alt='myUH Self Service'").click()
    # Switch selenium active tab
    original_window = driver.current_window_handle
    WebDriverWait(driver, 30).until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    # Click on Student Center
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "win0groupletPTNUI_LAND_REC_GROUPLET$3")))
    driver.find_element_by_id('win0groupletPTNUI_LAND_REC_GROUPLET$3').click()
    # Click on Search
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "ptifrmtgtframe")))
    driver.switch_to.frame(driver.find_element(By.ID, "ptifrmtgtframe"))
    driver.find_element_by_css_selector("a[name='DERIVED_SSS_SCR_SSS_LINK_ANCHOR1']").click()

def searchForClass():
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "win0divCLASS_SRCH_WRK2_STRM$35$")))
    # Select term
    Select(driver.find_element(By.CSS_SELECTOR, "select[name='CLASS_SRCH_WRK2_STRM$35$']")).select_by_visible_text(term)
    time.sleep(2)
    # Select subject
    Select(driver.find_element(By.CSS_SELECTOR, "select[name='SSR_CLSRCH_WRK_SUBJECT_SRCH$1']")).select_by_value(class_name)
    time.sleep(2)
    # Enter class number
    driver.find_element(By.CSS_SELECTOR, "input[name='SSR_CLSRCH_WRK_CATALOG_NBR$2']").send_keys(class_number)
    time.sleep(2)
    # Search
    driver.find_element(By.CSS_SELECTOR, "input[name='CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH']").send_keys(Keys.ENTER)

main()
