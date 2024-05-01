import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

def Dominos_bomb(nomer=None):
    with open("User_agent/SeoLik_Список_mobile_user_agent.txt", "r") as user_agent_file:
        user_agents_list = list(user_agent_file)


    #options
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={random.choice(user_agents_list)}")
    #options.add_argument("--headless")

    url = "https://dominos.by/ru/minsk/?utm_source=google&utm_medium=cpc&utm_term=%D0%B4%D0%BE%D0%BC%D0%B8%D0%BD%D0%BE%D1%81&utm_content=608842542231&utm_campaign=Search_Brand_night&gad_source=1&gclid=Cj0KCQjwiMmwBhDmARIsABeQ7xT67Nfs1uhj8MvIaTjpKJnuDVBnQIQyRrzeFKIAyeKD3St9ME1ijqAaArRZEALw_wcB"
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    try:
        driver.implicitly_wait(10)
        vvesti = driver.find_element(By.XPATH, "/html/body/div[1]/div/header/div/div[3]/button").click()
    except Exception as vvesti_VK:
        print("Domino_VK")
    try:
        driver.implicitly_wait(10)
        nomer = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div/div/form/div/div/div/input").send_keys(nomer[1:])
    except Exception as nomer_VK:
        print("Domino_VK")
    try:
        driver.implicitly_wait(10)
        knopka_VK = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div/div/form/div/button").click()
    except Exception as knopka_VK:
        print("domino_VK")

    time.sleep(1)
    driver.quit()

def main():
    Dominos_bomb()

if __name__ == "__main__":
    main()