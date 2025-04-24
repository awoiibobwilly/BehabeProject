#from behave import Given, When, Then
from sys import executable

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('launch google chrome browser')
def launch_browser(context):
    #context.driver=webdriver.Chrome(executable_path="K:\RA_APP03_2025\APP03_BDD\Drivers\chromedriver-win64\chromedriver.exe")
    context.driver = webdriver.Chrome()


@when('open refactory academy homepage')
def open_homepage(context):
    context.driver.get("https://refactory.academy/")


@then('verify that the refactory logo is on the page')
def verify_logo(context):
    status=context.driver.find_element(By.XPATH, "//div[@class='logo']//img[@alt='logo']").is_displayed()
    assert status is True


@then('close the browser')
def close_browser(context):
    context.driver.close()