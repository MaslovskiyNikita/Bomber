import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

def A1_bomb(nomer=None):
    with open("User_agent/SeoLik_Список_mobile_user_agent.txt", "r") as user_agent_file:
        user_agents_list = list(user_agent_file)


    #options
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={random.choice(user_agents_list)}")
    #options.add_argument("--headless")

    url = "https://asmp.a1.by/asmp/LoginMasterServlet?service=Portal&cookie=skip&level=20&userRequestURL=https%3A%2F%2Fwww.a1.by%2Fru%2Fc%2Fshop%3Futm_source%3Dgoogle%26utm_medium%3Dcpc%26utm_campaign%3DBY_a1_B2C_AO_24Jan-NoEnd_PerfMax%26utm_content%3DPerfMax_conv_con_dev_sea_banner%26gad_source%3D1%26gclid%3DCj0KCQjwiMmwBhDmARIsABeQ7xSImXZFtN2flBCKbql_GkXyuYhqBh8C11ztf1V91DNpCkIoz8mzJfgaAlIQEALw_wcB%26fromSSO%3Dtrue"
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    try:
        driver.implicitly_wait(10)
        nomer = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/div/section/form/div[2]/div[2]/div/input").send_keys(nomer[4:])
    except Exception as nomer_VK:
        print("nomer_A1")
    try:
        driver.implicitly_wait(10)
        knopka_VK = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div/div/section/form/div[2]/div[3]/div[1]/div/a/span[2]").click()
    except Exception as knopka_VK:
        print("knopka_A1")

    time.sleep(1)
    driver.quit()
def main():
    A1_bomb()

if __name__ == "__main__":
    main()