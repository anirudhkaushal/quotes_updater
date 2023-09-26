import requests
from pprint import pprint

def get_random_quote():

    request_url = 'https://api.quotable.io/quotes/random'

    quote = requests.get(request_url).json()

    # pprint(quote)
    # print(quote[0]["content"])
    # print(quote[0]["author"])

    with open('README.md', 'w') as readme_file:
        readme_file.write(f'# Latest quote \n\nQuote: {quote[0]["content"]} \n\nBy: {quote[0]["author"]}')

if __name__ == "__main__":
    get_random_quote()
