from selenium.webdriver.common.by import By
import time
import pytest

@pytest.mark.parametrize(("nome", "senha"),[
    ("teste2", "senha2025"),
    ("errado","senhaerrada")
])

def test_login_valido(driver, nome, senha):
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    driver.find_element (By.NAME, "username").send_keys (nome)
    driver.find_element (By.NAME, "password").send_keys (senha)
    time.sleep(2)
    driver.find_element (By.XPATH, '//*[@id="loginPanel"]/form/div[3]/input').click()
    time.sleep(3)



#pytest -v tests/test_login.py

    