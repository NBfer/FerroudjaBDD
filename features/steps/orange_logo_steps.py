from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@when('j\'ouvre l\'application Orange')
def OuvrirOrange(context):
    global wait
    wait = WebDriverWait(context.driver, 10)
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print("j\'ouvre l\'application Orange")

@then('le Logo s\'affiche sur la page d\'acceuil')
def ValiderAffichageLogo(context):
    wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@id='appp']//img)[1]")))
    #logo = wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@id='app']//img)[1]")))
    #status = context.driver.find_element(By.XPATH, "(//div[@id='app']//img)[1]").is_displayed()
    # status = logo.is_displayed()
    # assert status is True
    print("le Logo s\'affiche sur la page d\'acceuil")



