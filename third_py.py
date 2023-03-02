from bs4 import BeautifulSoup
import requests
import json
from pprint import pprint 

def get_file():
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57"}
    link = "https://api.stackexchange.com/2.3/questions?fromdate=1677628800&todate=1677715200&order=desc&sort=activity&tagged=python&site=stackoverflow"

    responce = requests.get(url=link,headers=headers)
    pprint(responce.json())

def read_file(file_path):
    with open(file_path,encoding="UTF-8") as new_file:
        news = json.load(new_file)
        with open("file_add","w",encoding="UTF-8") as file:
            for i in news["items"]:
                for line in i:
                    file.write(f'{i["owner"]["display_name"]} - {i["title"]}\n')
                    break

                



if __name__ == "__main__":
    get_file() # функция которая вытаскивает из API-stackoverflow все вопросы с тегом "python" за 2 дня
    read_file("data.json") # функция которая вначале делает из запроса записывает в текстовой файл имя и вопрос человека.




