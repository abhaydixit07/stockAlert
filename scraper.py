import requests
from bs4 import BeautifulSoup

def get_stock_price(symbol):
    url = f"https://finance.yahoo.com/quote/{symbol}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find the element containing the stock price
    price_element = soup.find("span", {"data-reactid": "50"})
    if price_element:
        return price_element.text.strip()
    else:
        return "Stock price not found."

# Example usage:
symbol = "AAPL"  # Apple Inc. stock symbol
price = get_stock_price(symbol)
print(f"Current stock price of {symbol}: {price}")
