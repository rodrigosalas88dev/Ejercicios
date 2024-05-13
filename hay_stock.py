from requests_html import HTMLSession
from time import sleep


def stock_coolmod(url: str):
    session = HTMLSession()

    while True:

        r = session.get(url)
        print(r)
        buy_zone = r.html.find("#productBuyButtons")
        if len(buy_zone) > 0:
            print("HAY STOCK!")
            break
        else:
            print("POR AHORA NADA")
            sleep(30)


def main():
    stock_coolmod("https://www.coolmod.com/inno3d-geforce-rtx-4090-ichill-black-24gb-gddr6x/")


if __name__ == "__main__":
    main()
