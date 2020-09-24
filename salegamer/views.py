import time
from django.http import JsonResponse
from bs4 import BeautifulSoup
from selenium import webdriver


def home(request):
    browser = webdriver.Chrome()
    url = ("https://www.epicgames.com/store/en-US/free-games")
    browser.get(url)
    time.sleep(10)
    html_source = browser.page_source
    browser.quit()
    soup = BeautifulSoup(html_source, "html.parser")
    data = {
        "data-testid": "offer-title-info-title",
        "class": "css-tybchz-OfferTitleInfo__title",
        "data-component": "OfferTitleInfo"
    }

    games = []
    for element in soup.find_all("span", data):
        games.append(element.text.strip())
    return JsonResponse({'status': 'success', 'games': games})
