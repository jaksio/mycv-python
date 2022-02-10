from datetime import datetime, timedelta
from random import choice
from cryptography.fernet import Fernet
from os.path import exists
from twilio.rest import Client
import os
import requests
import json


class Stock:
    ''' solution for sending news SMS based on latest trends and using 3 APIs '''

    def __init__(self, stockSymbol="TSLA", companyName="Tesla Inc"):
        ''' initialize class parameters '''
        self.key = Fernet.generate_key()
        self.f = Fernet(self.key)
        self.apiKeys = self.getApiKeys()
        self.stockSymbol = stockSymbol
        self.companyName = companyName
        self.yesterday = (lambda x: (x - timedelta(1)).strftime("%Y-%m-%d"))(datetime.now())
        self.prev_day = (lambda x: (x - timedelta(1)).strftime("%Y-%m-%d"))(
                        datetime.strptime(self.yesterday, "%Y-%m-%d"))
        # self.yesterday_close = (lambda x: data["Time Series (Daily)"][x]["4. close"])
        self.increase = True
        self.difference = self.get_diff()
        self.articles = []


    def getApiKeys(self):
        ''' get Api keys from user '''
        apiKeys = {
            "Alpha": "",
            "News": "",
            "Your Twilio number": "",
            "To who send sms": ""
            }
        if not exists("apikeys.txt"):
            for i in apiKeys.keys():
                apiKeys[i] = input(f"Please enter API key for {i} ")
        
            apiKeys = (self.f).encrypt(bytes(str(apiKeys), "utf-8"))

            with open("apikeys.txt", "w") as myFile:
                myFile.write(str(apiKeys.decode("utf-8")))
            with open("key.txt", "w") as myFile:
                myFile.write(self.key.decode("utf-8"))
        else:
            with open("apikeys.txt", "r") as myFile:
                apiKeys = bytes(myFile.read().encode("utf-8"))
            with open("key.txt", "r") as myFile:
                self.key = myFile.read().encode("utf-8")
                self.f = Fernet(bytes(self.key))
        
        apiKeys = (self.f).decrypt(apiKeys).decode("utf-8")
        apiKeys = apiKeys.replace("\'", "\"")
        return json.loads(apiKeys)


    def get_diff(self):
        ''' gets diference between closes and difference from alpha data '''
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={self.stockSymbol}&apikey={self.apiKeys["Alpha"]}'
        r = requests.get(url)
        data = r.json()
        yesterday_close = data["Time Series (Daily)"][self.yesterday]["4. close"]
        prev_day_close = data["Time Series (Daily)"][self.prev_day]["4. close"]

        difference = (float(yesterday_close) / float(prev_day_close)) * 100
        self.increase = True if difference - 100 >=0 else False
        difference = abs(difference - 100)
        return difference


    def get_news(self):
        ''' returns 3 top news from newsapi '''
        url = f'https://newsapi.org/v2/everything?q={self.companyName}&from={self.prev_day}&to={self.yesterday}&sortBy=publishedAt&apiKey={self.apiKeys["News"]}'
        r = requests.get(url)
        data = r.json()
        return data["articles"][0:3]

    def start_twilio(self):
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        for i in self.articles:
            topic = f"""
            {self.companyName}: 🔺{self.difference}%
            Headline: {i['title']}. 
            Brief: {i['description']}
            """
            message = client.messages.create(
                              body=topic,
                              from_=self.apiKeys["Your Twilio number"],
                              to=self.apiKeys["To who send sms"]
                          )

if __name__ == "__main__":
    stock = Stock()
    # if stock.difference <= 5:  # change to > for right output < is for testing purposes
    stock.articles = stock.get_news()
    stock.start_twilio()


