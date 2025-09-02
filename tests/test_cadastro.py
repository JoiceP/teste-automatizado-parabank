import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver          
    driver.quit()
    

@pytest.mark.parametrize ("usuario, senha, confirmar",[
                          ("teste2", "senha2025", "senha2025"),
                           ("teste3", "senha", "errado")
                            ])

def test_cadastro_valido(driver, usuario, senha, confirmar):    
    driver.get("https://parabank.parasoft.com/parabank/register.htm")
    time.sleep(5)

    driver.find_element (By.ID, "customer.firstName" ).send_keys ("Teste") 
    driver.find_element (By.ID, "customer.lastName").send_keys ("Da Silva")
    driver.find_element (By.ID, "customer.address.street").send_keys ("Minha Rua")
    driver.find_element (By.ID,"customer.address.city").send_keys ("BH")
    driver.find_element (By.ID, "customer.address.state").send_keys ("Minas Gerais")
    driver.find_element (By.ID, "customer.address.zipCode").send_keys ("12345-000")
    driver.find_element (By.ID, "customer.phoneNumber").send_keys ("012-12832193912")
    driver.find_element (By.ID, "customer.ssn").send_keys ("123")
    time.sleep(2)
    driver.find_element(By.ID, "customer.username").send_keys(usuario) #ALTERAR AQUI CASO FOR FAZER UM NOVO CADASTRO
    driver.find_element (By.ID, "customer.password").send_keys (senha)
    driver.find_element (By.ID, "repeatedPassword").send_keys (confirmar)


    driver.find_element (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[13]/td[2]/input').click()
    time.sleep(5)


#pytest -v test_cadastro.py