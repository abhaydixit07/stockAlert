import requests
from twilio.rest import Client

# ----------------------------stock-details-----------------------------------------
customer_name = "Bhawna Dixit"
STOCK = "IDEA"
COMPANY_NAME = "VI(Vodafone Idea)"
API_KEY = "JVN9WTH06T5M2BMN"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": f"{STOCK}.BSE",
    "outputsize": "compact",
    "datatype": "json",
    "apikey": API_KEY,
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()['Time Series (Daily)']
days = [{key: value} for (key, value) in stock_data.items()]
result_day = [days[0], days[1], days[3], days[4]]

keys = []

for i in result_day:
    for j in i:
        keys.append(j)


def extract(list1, key):
    dict1 = {
        "open": list1[key]['1. open'],
        "close": list1[key]['4. close'],
        "high": list1[key]['2. high'],
        "low": list1[key]['3. low'],
    }
    return dict1


result_dict = {keys[0]: extract(result_day[0], keys[0]),
               keys[1]: extract(result_day[1], keys[1])
               }

# ---------------------------------------company-news------------------------------------
news_api_key = "f554669a771249e5a666a56c3e80cc6f"

company_api_parameters = {
    "q": COMPANY_NAME,
    "from": keys[3],
    "to": keys[0],
    "apiKey": news_api_key

}
number_of_news = 3
company_response = requests.get(url="https://newsapi.org/v2/everything", params=company_api_parameters)
if len(company_response.json()["articles"]) < number_of_news:
    number_of_news = len(company_response.json()["articles"])
company_articles = company_response.json()["articles"][0:number_of_news]
company_news = [{"title": i['title'], "brief": i["description"]} for i in company_articles]

# ---------------------------market-news--------------------------------------
market_api_parameters = {
    "country": "in",
    "category": "business",
    "from": keys[3],
    "to": keys[0],
    "apiKey": news_api_key,
    "sortBy": "popularity",

}

market = requests.get(url="https://newsapi.org/v2/top-headlines", params=market_api_parameters)
if len(market.json()["articles"]) < number_of_news:
    number_of_news = len(market.json()["articles"])
market_articles = market.json()["articles"][0:number_of_news]
market_news = [{"title": i['title'], "brief": i["description"]} for i in market_articles]

#-----------------------------------body-------------------------------------------------------
yesterday = keys[0]
day_before_yesterday = keys[1]
yesterday_open=float(result_dict[yesterday]['open'])
day_before_yesterday_close=float(result_dict[day_before_yesterday]['close'])
difference = yesterday_open-day_before_yesterday_close
if difference<0:
    emoji = "🔻"
    inc_dec = "decreased"

else:
    emoji="🔺"
    inc_dec = "increased"
company_news_body = ""
for i in company_news:
    company_news_body = company_news_body+f"•{i['title']}\n"

market_news_body = ""
for i in market_news:
    market_news_body = market_news_body+f"•{i['title']}\n"


percentage = round((abs(difference)/day_before_yesterday_close)*100,3)
message_body=f'''Hi🙏 {customer_name}! Yours today's {STOCK}(Comapany's Name-{COMPANY_NAME}) share details are here:\n
{STOCK} {emoji}{percentage}% {inc_dec} from {day_before_yesterday} closing rate and {yesterday} opening rate.\n
{yesterday} - Open-{result_dict[yesterday]['open']}, Close-{result_dict[yesterday]['close']}, High🔼-{result_dict[yesterday]['high']}, Low🔽-{result_dict[yesterday]['low']}\n
{STOCK} 📜Share News from last four days:-\n
{company_news_body}\n

Indian Stock Market News📰-\n
{market_news_body}
'''
# ------------------------------------sms-service---------------------


# auth_token="54b4fd312061d06d7d91e2397fbdc457"
# account_sid="AC8c897ee9227f9b9c90aa716030c1cb24"

# client = Client(account_sid, auth_token)
# message = client.messages.create(
#         body=message_body,
#         from_='+17622496046',
#         to='+918287467417'
#     )
# print(message.status)
# +12192688076
if percentage>2.5:
    account_sid = 'ACa9592714fc2522185340bdeb7a4a3554'
    auth_token = 'ca27b130dc25b5b43a77ef8513212b59'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message_body,
        from_='+12192688076',
        to='+918076379585',
    )

    print(message.status)
