import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

def ok_bomb(nomer=None):
    with open("User_agent/SeoLik_Список_mobile_user_agent.txt", "r") as user_agent_file:
        user_agents_list = list(user_agent_file)


    #options
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={random.choice(user_agents_list)}")
    #options.add_argument("--headless")

    url = "https://m.ok.ru/"
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    try:
        driver.implicitly_wait(10)
        vvesti = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/div/form/div/div/div[2]/input").click()
    except Exception as vvesti_VK:
        print("OK")

    try:
        driver.implicitly_wait(10)
        vvesti = driver.find_element(By.XPATH, '//*[@id="field_phone"]').click()
    except Exception as vvesti_VK:
        print("OK")


    try:
        driver.implicitly_wait(10)
        nomer = driver.find_element(By.XPATH, '//*[@id="field_phone"]').send_keys(nomer[4:])
    except Exception as nomer_VK:
        print("ok")
    try:
        driver.implicitly_wait(10)
        knopka_VK = driver.find_element(By.XPATH, '//*[@id="reg_phone_button"]').click()
    except Exception as knopka_VK:
        print("ok")

    time.sleep(1)
    driver.quit()

def main():
    ok_bomb()

if __name__ == "__main__":
    main()