import allure
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def before_scenario(context, driver):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.maximize_window()


def after_scenario(context, driver):
    context.driver.quit()

def after_step(context, step):
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(), name="copie_ecran", attachment_type=allure.attachment_type.PNG)
