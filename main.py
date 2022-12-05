import requests


api_key = 'af08a8752fcd4bb0b473429f62029f1f'

url = 'https://newsapi.org/v2/everything?q=tesla&from=2022-11-05&sortBy=publishedAt&apiKey=af08a8752fcd4bb0b473429f62029f1f'


request = requests.get(url,verify=False)
content = request.json()

for index, article in enumerate(content['articles']):
    print(index)
    print(f"Title: {article['title']}")
    print(f"Description: {article['description']}")
    print()


