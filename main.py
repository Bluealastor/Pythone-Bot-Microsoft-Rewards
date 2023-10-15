
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Specifica il percorso al driver del browser (es. Chrome)
driver_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

# Crea un'istanza di ChromeOptions e specifica il percorso del driver
chrome_options = Options()
chrome_options.binary_location = driver_path

# Crea un'istanza del driver di Chrome con le opzioni
driver = webdriver.Chrome(options=chrome_options)

# Specifica l'URL del sito web che vuoi aprire
url = 'https://rewards.bing.com/?new=1'

# Apri il sito web
driver.get(url)

# # Trova l'elemento per classe e fai clic su di esso
# element = driver.find_element_by_class_name("ds-card-sec ng-scope")
# element.click()

# Chiudi il browser dopo qualche tempo (ad esempio, 10 secondi)
import time
time.sleep(100)  # Attendi per 10 secondi
driver.quit()