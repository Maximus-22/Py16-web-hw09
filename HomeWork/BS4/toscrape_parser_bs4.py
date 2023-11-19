import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime


BASE_URL = "http://quotes.toscrape.com"
QUOTES = []
AUTHORS = []
DATA_QUOTES = "quotes.json"
DATA_AUTHORS = "authors.json"


def get_page_content(url):
    response = requests.get(url)
    content = BeautifulSoup(response.content, 'html.parser')
    return content


def get_quotes(content):
    quote_data = []
    quotes = content.find_all('div', class_='quote')
    for q in quotes:
        quote = q.find('span', class_='text').get_text(strip = True)
        author = q.find('small', class_='author').get_text(strip = True)
        tags_elements = q.find('div', class_='tags').find_all('a', class_='tag')
        tags = [tag.get_text(strip = True) for tag in tags_elements]
        quote_data.append({"quote" : quote, "author" : author, "tags" : tags})
    return quote_data


def get_authors(content):
    authors_data = []
    authors = content.find_all('div', class_='quote')
    for author in authors:
        author_link = author.find('a')['href']
        author_url = BASE_URL + author_link  
        response = requests.get(author_url)
        if response.status_code == 200:
            # Отримуємо HTML-контент сторінки автора
            author_page_content = response.text
            author_soup = BeautifulSoup(author_page_content, 'html.parser')
            fullname = author_soup.find('h3', class_='author-title').get_text(strip = True)
            born_date = author_soup.find('span', class_='author-born-date').get_text()
            # born_date_object = datetime.strptime(born_date, '%B %d, %Y')
            born_location = author_soup.find('span', class_='author-born-location').get_text(strip = True)
            description = author_soup.find("div", class_='author-description').get_text(strip = True)
            authors_data.append({"fullname" : fullname, "born_date" : born_date,
                                 "born_location" : born_location, "description" : description})
    return authors_data


def save_to_json(data, filename):
    with open(filename, "w", encoding = "UTF-8") as fd:
        json.dump(data, fd, ensure_ascii = False, indent = 4)


def unique_authors_data(authors):
    # Перетворення кожного словника на кортеж й створення множини 
    unique_author_tuples = {tuple(author.items()) for author in authors}
    # Перетворення назад до списку словників
    unique_authors = [dict(author_tuple) for author_tuple in unique_author_tuples]
    return unique_authors


def main():
    # Обробка першої сторiнки
    page_content = get_page_content(BASE_URL)

    while True:
        QUOTES.extend(get_quotes(page_content))
        AUTHORS.extend(get_authors(page_content))

        # Перевiрка iснування посилання на наступну сторiнку
        next_page_link = page_content.find('li', class_='next')
        if next_page_link is None:
            break
        
        # Якщо посилання iснує, додаємо його сiгнатуру до базового лiнку
        next_page_url = BASE_URL + next_page_link.find('a')['href']
        page_content = get_page_content(next_page_url)

    
    save_to_json(QUOTES, DATA_QUOTES)
    save_to_json(unique_authors_data(AUTHORS), DATA_AUTHORS)


if __name__ == "__main__":
    main()
