import json
import urllib.request
import pprint

def get_quote():
    url = f'https://evilinsult.com/generate_insult.php?lang=en&type=json'
    # print(url)
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint.pprint(response_data)
    quote = response_data['insult']
    return quote

def main():
    print(get_quote())

if __name__ == "__main__":
    main()