from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Entrar a la sesión
def login():

    WebDriverWait(driver, 12)\
        .until(EC.element_to_be_clickable(driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[5]/button')))

    username = driver.find_element_by_name('username')
    username.send_keys('galactic_cowboy104')
    time.sleep(3)

    password = driver.find_element_by_name('password')
    password.send_keys('De2a4Verdades')
    time.sleep(3)

    button_login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
    button_login.click()
    print('\nSesión iniciada...')

# Abrir la ventana de seguidores
def open_followers(account_instagram):

    WebDriverWait(driver, 12)\
        .until(EC.element_to_be_clickable(driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')))

    driver.get('https://www.instagram.com/' + account_instagram + '/followers/')

# Scrollear para poder visualizar más seguidores
def scroll_followers(minutes):

    WebDriverWait(driver, 12)\
        .until(EC.element_to_be_clickable(driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[3]/div/button')))

    pop_up_window = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]')
    timeout = time.time() + (60 * minutes)

    while True :

        if time.time() > timeout :
            break

        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', pop_up_window)
        time.sleep(0.1)

# Seguir seguidores
def follow_followers():

    list_followers = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div')

    counter = 0
    flag = 0

    for child in list_followers.find_elements_by_css_selector('li'):

        user_name = child.find_element_by_css_selector('.notranslate').text

        if user_name == 'galactic_cowboy104' :
            continue

        follow_button = child.find_element_by_css_selector('button')

        print('\n----------')
        print(' ' + user_name)

        if follow_button.text == 'Seguir' :

            follow_button.click()
            counter += 1
            print(' Siguiendo...')
            print(' Contador =', counter)
            print('----------')

            flag = 0
            time.sleep(3)

        else :

            print(' Ya lo sigues.')
            print('----------')

        if counter == 0 :
            continue

        if counter == 180 :
            break

        if (counter % 60) == 0 and flag == 0:

            flag = 1
            time.sleep(5400)

            continue

        if (counter % 15) == 0 and flag == 0:

            flag = 1
            time.sleep(180)

# Código principal

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\casa\\OneDrive\\Documentos\\Prácticas Python\\Bot de Instagram\\chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options=options)

time.sleep(6)
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(9)

login()
time.sleep(9)

a = 'davidportilla_'
open_followers(a)
time.sleep(15)

scroll_followers(2)
time.sleep(3)

follow_followers()
time.sleep(3)
