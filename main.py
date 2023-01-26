from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--start-maximized')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://automated.pythonanywhere.com/")
time.sleep(2)

def clean_text(text):
  """extract only the temperature from text"""
  output = str(text.split(": ")[1])
  return output

def grabber():
  myElement = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  myText = clean_text(myElement.text)
  return myText

def file_maker():
  i = 0 
  while i < 3:
    currentText = grabber() 
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d.%H-%M-%S") #dt_string can be our filename
    f = open(dt_string + ".txt", "a")
    f.write(currentText)
    f.close()
    i += 1
    time.sleep(2)
    print("i = " + str(i) + " and I have waited")

file_maker()
