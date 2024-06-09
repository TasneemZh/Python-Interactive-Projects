import os
import requests
from dotenv import load_dotenv
from constants import COMPANY_NAME, NEWS_ENDPOINT

load_dotenv(".env")


def get_news():
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": os.environ.get("NEWS_API_KEY")
    }

    news_resp = requests.get(NEWS_ENDPOINT, params=news_params)
    print(news_resp.url)
    news_resp.raise_for_status()

    news_resp_data = news_resp.json().get("articles")
    return news_resp_data[0:3]
