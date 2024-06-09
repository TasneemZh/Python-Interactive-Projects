from stocks import get_stock_diff
from news import get_news
from sms import send_sms_message

stock = get_stock_diff()
if stock["stock_percent"] >= 5:
    [send_sms_message(article, stock["stock_percent"], stock["is_diff_higher"]) for article in get_news()]
