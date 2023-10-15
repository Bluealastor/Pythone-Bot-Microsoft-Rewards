from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchWindowException
import json
import time

# Dichiarazione globale del driver per renderlo disponibile in tutte le funzioni
driver = None


# Leggi i dati dal file JSON
with open('dati.json') as json_file:
    data = json.load(json_file)

for utente, informazioni in data.items():
    username = informazioni['username']
    password = informazioni['password']



def initialize() -> webdriver:
    print("driver entrato")
    chrome_options = Options()
    driver_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = driver_path
    global driver  # Usiamo 'global' per dichiarare che stiamo utilizzando la variabile globale 'driver'
    driver = webdriver.Chrome(options=chrome_options)
    url = 'https://rewards.bing.com/?new=1'
    driver.get(url)
    time.sleep(5)
    return driver

def userInsert(username):
    print("sto scrivendo username")
    signIn = driver.find_element(By.NAME, "loginfmt")
    signIn.send_keys(username)
    print("inserito")

def clickButtonFirst():
    bottone = driver.find_element(By.ID, "idSIButton9")
    bottone.click()

def passwordInsert(password):
    time.sleep(3)
    print("sto scrivendo Password")
    signIn = driver.find_element(By.NAME, "passwd")
    signIn.send_keys(password)
    print("Password inserito")

def clickButtonFalse():
    time.sleep(2)
    bottone = driver.find_element(By.ID, "idBtn_Back")
    bottone.click()

def openClick(bi_id):
    # Ottieni l'handle della finestra principale
    finestra_principale = driver.current_window_handle
    
    # Clicca sul pulsante per aprire la pagina
    bottone = driver.find_element(By.CSS_SELECTOR, f'[data-bi-id="{bi_id}"]')
    bottone.click()
    time.sleep(3)

def closeWindows():
    finestra_principale = driver.current_window_handle
    finestre_aperte = driver.window_handles
    for finestra in finestre_aperte:
        if finestra != finestra_principale:
            driver.switch_to.window(finestra)
            driver.close()

if __name__ == "__main__":
    print("PRE driver")
    initialize()
    print("driver inizializzato")
    userInsert(username)
    print("inserito username")
    print("clicco sul pulsante")
    clickButtonFirst()
    print("pulsante cliccato")
    print("Inserisco la password")
    passwordInsert(password)
    print("Password inserita")
    clickButtonFirst()
    clickButtonFalse()
    openClick("Gamification_DailySet_ITIT_20231014_Child1")
    openClick("Gamification_DailySet_ITIT_20231014_Child2")
    openClick("Gamification_DailySet_ITIT_20231014_Child3")
    openClick("Gamification_DailySet_ITIT_20231012_Child2")
    closeWindows()
    time.sleep(300)
