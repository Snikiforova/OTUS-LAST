import time


def test_buy_order(buy_page):
    buy_page.open()
    time.sleep(1)
    buy_page.add_to_cart()
    time.sleep(1)
