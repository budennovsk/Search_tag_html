from dataclasses import dataclass

from bs4 import BeautifulSoup
import requests

URL = "https://jetlend.ru/"
response = requests.get(URL)

if response.status_code != 200:
    raise Exception('Ошибка подключения')

soup = BeautifulSoup(response.content, "lxml")


def search() -> tuple:
    """ Функция поиска тегов и тегов с атрибутами на HTML"""
    count_tag = 0
    count_tag_only_attr = 0
    for tag in soup.find_all():
        if tag.attrs:
            count_tag_only_attr += 1
        count_tag += 1
    return count_tag, count_tag_only_attr


if __name__ == "__main__":
    try:
        result = search()
        print(f'HTML-тегов всего на странице {result[0]}')
        print(f'Атрибутов в тегах всего на странице {result[1]}')
    except Exception as e:
        print('Ошибка')

# Решение ниже автора https://github.com/vavilovnv сохранил себе так как понравилось!
TARGET_URL = 'https://jetlend.ru/'


@dataclass
class Result:
    tags: int
    attrs: int


def count_tags_and_attrs() -> Result | None:
    response = requests.get(TARGET_URL)
    if response.status_code != 200:
        return None
    # need to install the dependency: pip install lxml
    bs = BeautifulSoup(response.text, features='lxml')
    return Result(len(bs()), sum([1 for tag in bs() if tag.attrs]))


def main():
    result = count_tags_and_attrs()
    if result:
        print(f'HTML-тегов в коде страницы {TARGET_URL} - {result.tags}.')
        print(f'Среди них с атрибутами: {result.attrs}.')


if __name__ == "__main__":
    main()
