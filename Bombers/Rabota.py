import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

def Rabota_bomb(nomer=None):
    with open("User_agent/SeoLik_Список_mobile_user_agent.txt", "r") as user_agent_file:
        user_agents_list = list(user_agent_file)

    #options
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={random.choice(user_agents_list)}")
    #options.add_argument("--headless")

    url = "https://grodno.rabota.ru/"
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    try:
        driver.implicitly_wait(10)
        vvesti = driver.find_element(By.XPATH, '//*[@id="app"]/div[12]/div[3]/div[2]/div[6]/div[1]/header/div[2]/div[3]/div[2]/div/div[2]/button').click()
    except Exception as vvesti_VK:
        print("rabota_VK")
    try:
        driver.implicitly_wait(10)
        nomer = driver.find_element(By.XPATH, '//*[@id="dialog-card-174"]/div[3]/div[2]/div/div/form/div/div/div/div[1]/input').send_keys(nomer)
    except Exception as nomer_VK:
        print("rabota_nomer")
    try:
        driver.implicitly_wait(10)
        knopka_VK = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[8]/div/div/div[3]/div[2]/div/div/form/button").click()
    except Exception as knopka_VK:
        print("rabota_VK")

    time.sleep(1)
    driver.quit()

def main():
    Rabota_bomb()

if __name__ == "__main__":
    main()