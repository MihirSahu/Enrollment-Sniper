#!/usr/bin/env python3

# Import modules
import time
import requests
from tkinter import *
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Selenium driver instance
driver = webdriver.Chrome()

# Functions
def startBrowser():
    url = 'https://accessuh.uh.edu/login.php'
    driver.get(url)

def getSourceCode():
    return driver.page_source

def logIn():
    username = ""
    password = ""
    startBrowser()
    username_input = driver.find_element_by_name('username').send_keys(username)
    password_input = driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_class_name('waves-button-input').click()

def bypassDuo():
    '''
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//button[@tabindex='2']")))
    for x in driver.find_elements_by_xpath("//button[@type='submit']"):
        print(x)
    '''
    time.sleep(5)
    soup = BeautifulSoup(getSourceCode(), 'lxml')


# Main
logIn()
bypassDuo()
