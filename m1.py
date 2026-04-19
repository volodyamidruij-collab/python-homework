import requests
from bs4 import BeautifulSoup

BASE_URL = "http://books.toscrape.com/"


def get_titles():
    url = BASE_URL
    titles = []

    while url:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.h3.a["title"]
            titles.append(title)

        # перевірка на наступну сторінку
        next_btn = soup.find("li", class_="next")
        if next_btn:
            url = BASE_URL + next_btn.a["href"]
        else:
            url = None

    return titles


if __name__ == "__main__":
    titles = get_titles()

    for t in titles:
        print(t)


