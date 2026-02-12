from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from src.config import PORTAL_URL, PORTAL_USER, PORTAL_PASS


class PortalLocaliza:

    def __init__(self):
        self.driver = None

    def iniciar_navegador(self):
        options = Options()
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

    def acessar_portal(self):
        self.driver.get(PORTAL_URL)

    def fazer_login(self):
        wait = WebDriverWait(self.driver, 10)

        campo_usuario = wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        campo_senha = self.driver.find_element(By.NAME, "password")

        campo_usuario.send_keys(PORTAL_USER)
        campo_senha.send_keys(PORTAL_PASS)

        botao_login = self.driver.find_element(By.NAME, "login")
        botao_login.click()

    def fechar(self):
        if self.driver:
            self.driver.quit()
