import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
from constants import STOCK, STOCK_ENDPOINT

load_dotenv(".env")


def get_stock_diff():
    today_date = datetime.now()
    curr_month = today_date.month
    curr_year = today_date.year
    print(f"month: {curr_month} - year: {curr_year}")

    stock_params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": STOCK,
        "interval": "60min",
        "month": f"{curr_year}-{curr_month}",
        "apikey": os.environ.get("STOCK_API_KEY")
    }

    print(os.environ.get("STOCK_API_KEY"))

    stock_resp = requests.get(STOCK_ENDPOINT, params=stock_params)
    print(stock_resp.url)
    stock_resp.raise_for_status()

    stock_resp_data = stock_resp.json().get("Time Series (60min)")
    if not stock_resp_data:
        info_message = stock_resp.json().get("Information", "No data available")
        raise Exception(info_message)

    stock_resp_keys = list(stock_resp.json()["Time Series (60min)"].keys())
    stock_day_1_key = stock_resp_keys[0]
    stock_day_1 = float(stock_resp_data[stock_day_1_key]["4. close"])
    format_string = "%Y-%m-%d %H:%M:%S"
    stock_day_2_key = str(datetime.strptime(stock_day_1_key, format_string) - timedelta(days=1))
    stock_day_2 = float(stock_resp_data[stock_day_2_key]["4. close"])

    print(f"stock_day_1_key: {stock_day_1_key} - stock_day_2_key: {stock_day_2_key}")
    print(stock_day_1)
    print(stock_day_2)
    stock_percent = abs(stock_day_1 - stock_day_2) / stock_day_2 * 100

    if stock_day_1 > stock_day_2:
        is_diff_higher = True
    else:
        is_diff_higher = False

    return {"stock_percent": round(stock_percent, 2), "is_diff_higher": is_diff_higher}
