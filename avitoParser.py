import os
import time

def StartParsing():
    print("Файл сайта есть, запускаю парсер")
    os.system("python havefile.py")

while True:
    print("Добро пожаловать в парсер авито. Введите цифру для выбора опции: \n")
    print("Спарсить существующий сайт - 1\n")
    print("Создать новый файл сайта - 2\n")
    
    answerMainMenu = int(input())

    page_path = os.path.abspath("page.html")
    print(page_path)

    if answerMainMenu == 1:
        if os.path.isfile(page_path):
            StartParsing()
        else:
            print("Файл page.html не найден \n")
            time.sleep(5)


    elif answerMainMenu == 2:
        os.system("python СreateCopySite.py")
    else:
        print("Некорректный выбор, попробуйте снова.")



# if os.path.isfile("page.html"):
#     print("Файл сайта есть, запускаю парсер")
#     os.system("python havefile.py")
# else:
#     urlSelected = input("Введите ссылку на поиск авито\n")

#     req = requests.get(urlSelected, headers=headers, verify=False)
#     print(req.status_code)

#     if req.status_code == 200:
#         print("К сайту подключился, скачиваю код страницы")
        
#         src = req.text
        
#         # Сохраняем HTML-код страницы в файл
#         with open("page.html", "w", encoding="utf-8") as file:
#             file.write(src)
#         print("HTML-код страницы успешно сохранен в файле 'page.html'")
#         os.system("python havefile.py")
#     else:
#         print("Ошибка при загрузке страницы. Код ответа:", req.status_code)