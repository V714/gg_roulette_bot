# GG Roulette Bot by V7
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import argparse
import getpass
import sys

PATH='chromedriver'

def make_parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--loops', type=int, help='Number of loops in roulette. Default: 10', default=10)
    parser.add_argument('--sex', default="both", help="Type female or male. Default: both")
    parser.add_argument('--login', help="Login, number, email I guess or sth.")
    parser.add_argument('--passw', help='Password')
    args = parser.parse_args()

    if not args.login:
        print("Press enter your login by --login LOGIN")
        quit()
    elif not args.passw:
        print("Press enter your password by --passw 'PASS'")
        quit()
    return args

def logging_gg(login,passw,driver):
    driver.get("https://www.ggapp.com/")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "pum-close"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign In"))).click()

    print("Waiting for login form.")
    time.sleep(2)

    loginframe = driver.find_element_by_name("login-iframe")
    print("Login form detected.")
    driver.switch_to_frame(loginframe)

    driver.find_element_by_id("login_input").send_keys(login)
    print("Entering login.")
    driver.find_element_by_id("password").send_keys(passw)
    print("Entering pass.")
    driver.find_element_by_name("doAction").click()
    print("Logging in.")
    driver.switch_to_default_content()


def roulette_settings(sex,driver):
    if not sex == 'both':
        driver.get("https://www.ggapp.com/#roulette")
        print("Entering roulette.")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-search-options'))).click()
        print("Into options")
        if sex == 'female':
            try:
                WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[4]/div[2]/div/div[2]/div/div[1]/div/ul/li[1]/label/img"))).click()
            except:
                WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[4]/div[2]/div/div[3]/div/div[1]/div/ul/li[1]/label/img"))).click()
            print("Females only selected.")
        elif sex == 'male':
            try:
                WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[4]/div[2]/div/div[2]/div/div[1]/div/ul/li[2]/label/img"))).click()
            except:
                WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[4]/div[2]/div/div[3]/div/div[1]/div/ul/li[2]/label/img"))).click()
            print("Males only selected.")

def roulette(roulette_loops,driver,sex):
    loops = 0
    cnt = 0
    web.get("https://www.ggapp.com/#roulette")
    loops = loops + 1
    WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.CLASS_NAME, "wide"))).click()
    print(loops, ' loop.')

    #roulette start
    for _ in range(roulette_loops-1):
        #Keep drawing
        try: 
            WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.CLASS_NAME, "white"))).click()
            loops = loops + 1
            print(loops, ' loop.')
        #if could not find anyone
        except: 
            cnt = cnt + 1
            print("Could not find anyone. Re: ", cnt)
            WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.CLASS_NAME, "wide"))).click()
            loops = loops + 1
    #wait to finish drawing and quit
    try:
        verWait(driver, 25).until(EC.element_to_be_clickable((By.CLASS_NAME, "white"))).click()
        web.quit()
    except:
        WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.CLASS_NAME, "wide"))).click()
        web.quit()  
        
    return loops, cnt       



if __name__ == '__main__':

    args = make_parse_args(sys.argv[1:])
    web = webdriver.Safari()
    logging_gg(args.login,args.passw,web)
    print("GG loaded.")
    roulette_settings(args.sex,web)

    time.sleep(1)
    
    loops, cnt = roulette(args.loops,web,args.sex)

    print('Roulette finished. ', loops, ' loops and ', cnt, ' drawing failed.')
