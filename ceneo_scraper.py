import os
import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

product_code = input("Provide product code: ")
page = 1
next = True

headers = {
    'Host': 'www.ceneo.pl',
    'Cookie': 'sv3=1.0_92827a71-3ccc-11f1-9d4a-23a2f55d0ccf; urdsc=1; userCeneo=ID=97b58e09-d095-4f62-9f69-4c43f8221b32; __RequestVerificationToken=KlWE9lqorZjXMC1mqJT6vONRS9Gu98Pdyc0oXnc4ORNV0HfGBSI9ncdHkAZs53vb_fgJKej-1Vnc2fMjmW8AABiCD_cc54Wiqb9E6QaULFo1; ai_user=IGZbp|2026-04-20T15:21:15.694Z; __utmf=b005f137479d61dcd846fea07a2e7c2c_Dsgqi6QMc9CtX7buqOpcIw%3D%3D; ai_session=RQyRJ|1776698476207.1|1776698476207.1; appType=%7B%22Value%22%3A1%7D; cProdCompare_v2=; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%2C%22expiryDate%22%3A%222027-04-20T15%3A21%3A16.870Z%22%7D; __rtbh.aid=%7B%22eventType%22%3A%22aid%22%2C%22id%22%3A%2292827a71-3ccc-11f1-9d4a-23a2f55d0ccf%22%2C%22expiryDate%22%3A%222027-04-20T15%3A21%3A16.870Z%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22rZJkksAfsJOGjWsiJqLt%22%2C%22expiryDate%22%3A%222027-04-20T15%3A21%3A16.871Z%22%7D; browserBlStatus=0; ga4_ga=GA1.2.92827a71-3ccc-11f1-9d4a-23a2f55d0ccf; _gcl_au=1.1.12079675.1776698478; consentcookie=eyJBZ3JlZUFsbCI6dHJ1ZSwiQ29uc2VudHMiOlsxLDMsNCwyXSwiVENTdHJpbmciOiJDUWk5ajBBUWk5ajBBR3lBQkJQTENiRXNBUF9nQUFBQUFCNVlLTHREN0Q3ZExXRmd3SHhuWUtzUU1JMWY4ZUNBWW9RQUJBYUJBU0FCU0FLUUlJUUdra0FRSkFTZ0JBQUNBQUlBS0NSQklRQU1BQUNBQ0VBQVFJQUFJUUFFQUFDUUFRZ0tBQUFFaUFBUUFBQVlBQUFpQ0lBQUFRQUlnRUlFRUJFQW1RaEFBQUlBRUZBQWpBQUVJQUFBQUFBQUFBQUFBd0FBQUFBQ0FBSUFBQUFBZ0NBQUFJQUFBQUFBQUVBQVFCZ0lFQUFBQUFFQUFBQUFBQUFBQVFBQUFCQUFBQUFJS0xnQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUJZS0FEQUFFRkZ3a0FHQUFJS0xob0FNQUFRVVhFUUFZQUFnb3VLZ0F3QUJCUmNaQUJnQUNDaTQ2QURBQUVGRnlFQUdBQUlLTGtvQU1BQVFVWEtRQVlBQWdvdVdnQXdBQkJSY0EuSUtMdEQ3RDdkTFdGZ3dIeG5ZS3NRTUkxZjhlQ0FZb1FBQkFhQkFTQUJTQUtRSUlRR2trQVFKQVNnQkFBQ0FBSUFLQ1JCSVFBTUFBQ0FDRUFBUUlBQUlRQUVBQUNRQVFnS0FBQUVpQUFRQUFBWUFBQWlDSUFBQVFBSWdFSUVFQkVBbVFoQUFBSUFFRkFBakFBRUlBQUFBQUFBQUFBQUF3QUFBQUFDQUFJQUFBQUFnQ0FBQUlBQUFBQUFBRUFBUUJnSUVBQUFBQUVBQUFBQUFBQUFBUUFBQUJBQUFBQUlBIiwiVmVyc2lvbiI6InYzIn0=; FPID=FPID2.2.UTJGlMBV58l7nhBB75LipGnno1eaURI4HFNqX2QhG5E%3D; FPLC=zx36HcmP5cQbImiV62WFEi%2B6TKa9ueizBaAZhRIHWI8jAk2x08cEkETcCv38tMtqLS%2FBBxIWy24Lj%2FXE5bPw%2BP7XL2ixfEfvJXjInScdY3Oy4OE%3D; ga4_ga_K2N2M0CBQ6=GS2.2.s1776698476$o1$g0$t1776698504$j33$l0$h1386369129',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'
}
all_opinions = []
while next:
    url = f"https://www.ceneo.pl/{product_code}/opinie-{page}"
    print(url)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        page_dom = BeautifulSoup(response.text, 'html.parser')
        print(type(page_dom))
        product_name = page_dom.find("h1", {'class': 'product-top__product-info__name'}).get_text()
        if page == 1:
            product_name = page_dom.select_one("h1.product-top__product-info__name").get_text()
        opinions = page_dom.select("div.js_product-review:not(.user-post--highlight)")
        print(type(opinions))
        print(len(opinions))
        opinions = [r for r in page_dom.find_all("div", {"class": "js_product-review"}) if "user-post--highlight" not in r.get('class', [ ])]
        for opinion in opinions:
            single_opinion = {
                'opinion_id': opinion['data-entry-id'],
                'author': opinion.select_one('span.user-post__author-name').get_text().strip(),
                'recommendation': opinion.select_one('span.user-post__author-recomendation > em').get_text().strip() if opinion.select_one('span.user-post__author-recomendation > em') else None,
                'score': opinion.select_one('span.user-post__score-count').get_text().strip(),
                'content': opinion.select_one('div.user-post__text').get_text().strip() if opinion.select_one('div.user-post__text') else None,
                'pros': [p.get_text() for p in opinion.select('div.review-feature__item--positive')] if [p.get_text() for p in opinion.select('div.review-feature__item--positive')] else None,
                'cons': [c.get_text() for c in opinion.select('div.review-feature__item--negative')] if [c.get_text() for c in opinion.select('div.review-feature__item--negative')] else None,
                'like': opinion.select_one('button.vote-yes > span').get_text().strip(),
                'dislike': opinion.select_one('	button.vote-no > span').get_text().strip() if opinion.select_one('	button.vote-no > span') else None,
                'publish_date': opinion.select_one('span.user-post__published > time:nth-child(1)[datetime]')['datetime'].strip() if opinion.select_one('span.user-post__published > time:nth-child(1)[datetime]') else None,
                'purchase_date': opinion.select_one('span.user-post__published > time:nth-child(2)[datetime]')['datetime'].strip() if opinion.select_one('span.user-post__published > time:nth-child(2)[datetime]') else None,
            }
            all_opinions.append(single_opinion)
        next = True if page_dom.select_one('button.pagination__next') else False
    if next: page += 1
if not os.path.exists("./opinions"):
    os.mkdir("./opinions")
with open(f"./opinions/{product_code}.json", "w", encoding="UTF-8") as jf:
    json.dump(all_opinions, jf, indent=4, ensure_ascii=False)