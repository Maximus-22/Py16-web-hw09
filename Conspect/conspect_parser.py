import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

# # знайти перший тег <p> на сторінці
# first_paragraph = soup.find("p")
# print(first_paragraph)
# # знайти всі теги <p> на сторінці
# all_paragraphs = soup.find_all("p")
# print(all_paragraphs)
# # отримати текст першого тега <p> на сторінці
# first_paragraph_text = first_paragraph.get_text()
# print(first_paragraph_text.strip())  # 'Login'
# # отримати значення атрибута "href" першого тегу <a> на сторінці
# first_link = soup.find("a")
# first_link_href = first_link["href"]
# print(first_link_href)  # '/'

# # Щоб отримати всі дочірні елементи першого тегу <body> на сторінці, використовуємо атрибут [children].
# body_children = list(first_paragraph.children)
# print(body_children)

# # знайти перший тег <a> всередині першого тегу <div> на сторінці
# first_div = soup.find("div")
# first_div_link = first_div.find("a")
# print(first_div_link)

# # Щоб отримати батьківський елемент першого тегу <p> на сторінці, ми можемо використовувати властивість [parent]
# first_paragraph_parent = first_paragraph.parent
# print(first_paragraph_parent)

# # Також можна використовувати методи [find_parent] і [find_parents] для пошуку батьківських елементів
# container = soup.find("div", attrs={"class": "quote"}).find_parent("div", class_="col-md-8")
# print(container)

# Метод [select] дозволяє шукати елементи на основі CSS-селекторів. Він приймає рядок із CSS-селектором і повертає всі
# елементи, що відповідають цьому селектору

# Знайдемо всі теги <p> на сторінці
p = soup.select("p")
print(p)

# Знайдемо всі елементи з класом ["text"]
text = soup.select(".text")
print(text)

# Знайдемо всі елементи з ідентифікатором ["header"]. Ідентифікатор - це спеціальний атрибут тегу id.
header = soup.select("#header")
print(header)

# Комбіновані селектори шукають елементи, що відповідають кільком умовам. 
# Наприклад, знайдемо всі елементи <a> всередині тегу <div> з класом ["container"]
a = soup.select("div.container a")
print(a)

# Можна шукати елементи за значенням атрибутів. Знайдемо всі елементи, у яких атрибут <href> починається з ["https://"]
href = soup.select("[href^='https://']")
print(href)

# Знайдемо всі елементи, у яких атрибут <class> містить слово ["text"]
ctext = soup.select("[class*='text']")
print(ctext)