import asyncio
import datetime
import re
from pyppeteer import launch
from pymongo import MongoClient

async def main():
    client = MongoClient('45.11.24.111', username='mongo-root', password='passw0rd', authSource='admin')
    print(client)
    db = client.news
    data = db.data
    browser = await launch({'args': ['--no-sandbox', '--disable-setuid-sandbox', '--disable-infobars',  '--ignore-certifcate-errors-spki-list', '--user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"']})
    page = await browser.newPage()
    await page.setViewport({
        'width': 1200,
        'height': 800
    })
    await page.goto('https://novostivolgograda.ru/', {'waitUntil': 'domcontentloaded'})
    newsLinks = []
    titles = []
    texts = []
    dates = []
    elements = await page.querySelectorAll('.right-block .item')
    path = await page.evaluate('(element) => element.getAttribute("href")', await page.querySelector('.left-block'))
    newslink = "https://novostivolgograda.ru" + path
    newsLinks.append(newslink)
    titles.append(await page.evaluate('(element) => element.textContent', await page.querySelector('.left-block .title-text')))
    for el in elements:
        path = await page.evaluate('(element) => element.getAttribute("href")', el)
        newslink = "https://novostivolgograda.ru" + path
        newsLinks.append(newslink)
        titles.append(await page.evaluate('(element) => element.textContent', await el.querySelector('.title-text')))
    elements = await page.querySelectorAll('#other-matters-chosen .item')
    for el in elements:
        path = await page.evaluate('(element) => element.getAttribute("href")', el)
        newslink = "https://novostivolgograda.ru" + path
        newsLinks.append(newslink)
        titles.append(await page.evaluate('(element) => element.textContent', await el.querySelector('.title-text')))
    elements = await page.querySelectorAll('.mat-card-small')
    for el in elements:
        path = await page.evaluate('(element) => element.getAttribute("href")', el)
        newslink = "https://novostivolgograda.ru" + path
        newsLinks.append(newslink)
        titles.append(await page.evaluate('(element) => element.textContent', await el.querySelector('.title')))
    for el in newsLinks:
        await page.goto(el, {'waitUntil': 'domcontentloaded', 'timeout': 300000})
        elements = await page.querySelectorAll('.cm-par-medium')
        text = ""
        for elem in elements:
            text = text + await page.evaluate('(element) => element.textContent', elem)
        texts.append(text)
        date = re.search(r'[\d]*-[\d]*-[\d]+', el)
        dates.append(date.group())
        print(el)
        print(text)
    await browser.close()
    for i in range(0, len(titles)):
        data.update({u'newsDate': dates[i], u'newsName': titles[i], u'newsLink': newsLinks[i], u'newsText': texts[i]}, { u'$setOnInsert': { u'newsDate': dates[i], u'newsName': titles[i], u'newsLink': newsLinks[i], u'newsText': texts[i], u'forAnalysis': True } }, **{ 'upsert': True })

def run():
    asyncio.get_event_loop().run_until_complete(main())
    print('парсинг закончин')