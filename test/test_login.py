from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page.login_page import loginPage
from utils.logger import logger
import pytest 

@pytest.mark.smoke
def test_login_validation(driver):
    login_Page = loginPage(driver)
    login_Page.login("standard_user","secret_sauce")
    assert"/inventory.html" in driver.current_url, "No se redirigió al inventario"
        
    logger.info("Sesion iniciada correctamente")


def test_login_invalid_password(driver):
    login_Page = loginPage(driver)

    login_Page.login("standard_user","123456")

    error  = login_Page.get_error_message()

    assert "Epic sadface: Username and password do not match any user in this service" in error
    #assert error == "Hola"