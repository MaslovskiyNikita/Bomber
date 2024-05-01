import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

def Zabava_bomb(nomer=None):
    with open("User_agent/SeoLik_Список_mobile_user_agent.txt", "r") as user_agent_file:
        user_agents_list = list(user_agent_file)


    #options
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={random.choice(user_agents_list)}")
    #options.add_argument("--headless")

    url = "https://zabava.by/restaurant/pitstseriya"
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    try:
        driver.implicitly_wait(10)
        vvesti = driver.find_element(By.XPATH, "/html/body/div/header/div[2]/div[5]/a").click()
    except Exception as vvesti_VK:
        print("Zabava_VK")
    try:
        driver.implicitly_wait(10)
        nomer = driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(nomer[4:])
    except Exception as nomer_VK:
        print("Zabava_VK")
    try:
        driver.implicitly_wait(10)
        knopka_VK = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/form/button").click()
    except Exception as knopka_VK:
        print("Zabava_VK")

    time.sleep(1)
    driver.quit()

def main():
    Zabava_bomb()

if __name__ == "__main__":
    main()