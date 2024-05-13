from requests_html import HTMLSession
from time import sleep
from selenium import webdriver


def stock_coolmod(url: str):
    session = HTMLSession()

    while True:

        product_page = session.get(url)
        print(product_page)
        found = product_page.html.find("#productBuyButtons")

        if len(found) > 0:
            driver = webdriver.Firefox()
            driver.get(url)
            print("durmiendo 5 segundos")
            sleep(5)
            driver.find_element(
                "#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
            driver.find_elements_by_css_selector(
                "svg.svg-inline--fa:nth-child(4) > path:nth-child(1)").click()
            print("HAY STOCK!")
            break
        else:
            print("POR AHORA NADA")
            sleep(30)


def main():
    stock_coolmod(
        "https://www.coolmod.com/powercolor-amd-radeon-rx-7900-xt-hell-hound-oc-20gb-gddr6/")


if __name__ == "__main__":
    main()
