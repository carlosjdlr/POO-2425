from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
import schedule

# Configura el path del ChromeDriver
CHROME_DRIVER_PATH = 'ruta/a/chromedriver'

# Credenciales y URLs
TEAMS_EMAIL = 'tu_email@ejemplo.com'
TEAMS_PASSWORD = 'tu_contraseña'
TEAMS_CLASS_URL = 'https://teams.microsoft.com/l/clase-url'
ASISTENCIA_URL = 'https://pagina-de-asistencia.com'


# Inicializa el navegador
def iniciar_navegador():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=options)
    return driver


# Ingreso a Microsoft Teams
def ingresar_a_teams(driver):
    driver.get(TEAMS_CLASS_URL)

    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'loginfmt'))
        ).send_keys(TEAMS_EMAIL + Keys.RETURN)

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'passwd'))
        ).send_keys(TEAMS_PASSWORD + Keys.RETURN)

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'idSIButton9'))
        ).click()

        # Espera a que cargue la clase
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'teams-video-button'))
        )
        print("Ingresado a la clase en Teams.")

    except TimeoutException:
        print("Error al ingresar a Teams.")


# Firmar asistencia
def firmar_asistencia(driver):
    driver.execute_script("window.open('');")  # Abrir nueva pestaña
    driver.switch_to.window(driver.window_handles[1])
    driver.get(ASISTENCIA_URL)

    try:
        # Reemplaza los siguientes selectores con los correctos de tu página de asistencia
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'campo-asistencia'))
        ).send_keys('Tu Nombre')

        driver.find_element(By.ID, 'boton-enviar').click()
        print("Asistencia firmada.")

        driver.close()
        driver.switch_to.window(driver.window_handles[0])  # Volver a Teams

    except TimeoutException:
        print("Error al firmar asistencia.")


# Programa la tarea para repetirse cada cierto tiempo
def automatizar_asistencia():
    driver = iniciar_navegador()
    ingresar_a_teams(driver)

    # Firmar asistencia cada 30 minutos
    schedule.every(30).minutes.do(firmar_asistencia, driver=driver)

    try:
        while True:
            schedule.run_pending()
            sleep(10)
    except KeyboardInterrupt:
        driver.quit()
        print("Automatización finalizada.")


if __name__ == '__main__':
    automatizar_asistencia()
