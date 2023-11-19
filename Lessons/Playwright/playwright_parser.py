import json
from playwright.sync_api import sync_playwright

data_parse = []
indx = 0

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Запускає браузер Chromium browser = p.chromium.launch(headless=False)
    page = browser.new_page()  # Відкриває нову сторінку
    page.goto('https://quotes.toscrape.com/login')

    page.fill("input[id='username']", 'admin')
    page.fill("input[id='password']", 'admin')

    page.click('.btn.btn-primary')
    page.wait_for_load_state('load')
    if "Logout" in page.content():
        # page.goto("https://quotes.toscrape.com")
        while True:
            quotes = page.query_selector_all('.quote')
            for q in quotes:
                indx += 1
                dict_values = {"id" : indx,
                               "author" : q.query_selector('.author').inner_text(),
                               "quote" : q.query_selector('.text').text_content(),
                                "tags" : [tag.text_content() for tag in q.query_selector_all('.tags a.tag')]}
                # print(text, author, tags)
                data_parse.append(dict_values)
            next_link = page.query_selector('.next a')
            if next_link:
                next_link.click()
                page.wait_for_load_state('load')
            else:
                break

    browser.close()

with open("data_parse.json", 'w', encoding='utf-8') as fd:
    json.dump(data_parse, fd, ensure_ascii = False, indent = 4)