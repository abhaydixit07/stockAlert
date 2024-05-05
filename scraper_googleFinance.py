import requests
from bs4 import BeautifulSoup

def get_stock_price(symbol):
    url = f"https://www.google.com/finance/quote/{symbol}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extracting the price
    price = soup.find(class_='YMlKec fxKbKc').text.strip()
    
    return price

if __name__ == "__main__":
    stock_symbol = input("Enter the stock symbol: ")
    stock_price = get_stock_price(stock_symbol)
    print(f"The current price of {stock_symbol} is {stock_price}")
