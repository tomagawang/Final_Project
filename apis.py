import json
import urllib.request
import pprint
import requests
from api2 import rapid_api

def get_insult():
    '''get insult quote from an api online'''
    url = 'https://evilinsult.com/generate_insult.php?lang=en&type=json'
    # print(url)
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint.pprint(response_data)
    quote = response_data['insult']
    return quote

def get_math(number):
    '''get a math trivia answer from numbersapi'''
    url = f'http://numbersapi.com/{number}/trivia?json'
    # print(url)
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint.pprint(response_data)
    text = response_data['text']
    text = text.split()
    text = " ".join(text[1:])
    return text

def get_love(name1, name2):
    '''An API that calculates the love compatibility score based on two names'''
    url = "https://love-calculator.p.rapidapi.com/getPercentage"
    querystring = {"sname":{name1},"fname":{name2}}
    headers = {
	"X-RapidAPI-Host": "love-calculator.p.rapidapi.com",
	"X-RapidAPI-Key": rapid_api
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()['percentage']

def main():
    print(get_insult())
    print(get_math(40))
    print(get_love('Nick','Julie'))
if __name__ == "__main__":
    main()