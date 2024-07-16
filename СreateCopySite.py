import socket
import socks
import requests
import urllib3
import random
import os
urllib3.disable_warnings()


# Выбор рандомного User Agent
with open('User-Agent.txt', 'r') as f:
    user_agents = f.read().splitlines()
user_agent = random.choice(user_agents)

str(user_agent)
# headers браузера
headers = {
    'accept': '*/*',
    # 'accept-encoding': 'gzip, deflate, br, zstd',
    # 'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    # 'sec-ch-ua-mobile': '?0',
    # # 'Sec-Ch-Ua-Platform:': '"Windows"',
    # 'sec-fetch-dest': 'script',
    # 'sec-fetch-mode': 'cors',
    # 'sec-fetch-site': 'same-origin',
    "User-Agent": user_agent
}

print(headers['User-Agent'])

def СreateCopySite():
    try:
        proxyType = ""
        proxyIP = ""
        proxyPort = 0

        print("Введите тип прокси: \n")
        print("Socks5 - 1\n")
        proxyType = input()

        print(proxyType)

        if proxyType == "1":
            print("Вы выбрали Socks5. Введите IP \n")
            proxyIP = str(input())
            print("Вы выбрали Socks5. Введите Port \n")
            proxyPort = int(input())
        else:
            print("Неверное значение")
            return

        socks.set_default_proxy(socks.SOCKS5, proxyIP, proxyPort)
        socket.socket = socks.socksocket

        print("Прокси вставлены успешно!")

        urlAvito = "https://www.avito.ru/all?q="
        productSelected = input("Введите продукт, который вы ищите на авито\n")

        urlSelected = urlAvito + productSelected

        req = requests.get(urlSelected, headers=headers, verify=False)
        print(req.status_code)

        if req.status_code == 200:
            print("К сайту подключился, скачиваю код страницы")
            
            src = req.text
            
            # Сохраняем HTML-код страницы в файл
            with open("page.html", "w", encoding="utf-8") as file:
                file.write(src)
            print("HTML-код страницы успешно сохранен в файле 'page.html'")
            os.system("python havefile.py")
        else:
            print("Ошибка при загрузке страницы. Код ответа:", req.status_code)
            return
    except Exception as e:
        print("Произошла ошибка:", e)

СreateCopySite()