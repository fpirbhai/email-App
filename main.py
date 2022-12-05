import requests
import send_email



api_key = 'af08a8752fcd4bb0b473429f62029f1f'

url = 'https://newsapi.org/v2/everything?q=tesla&from=2022-11-05&sortBy=publishedAt&apiKey=af08a8752fcd4bb0b473429f62029f1f'


request = requests.get(url,verify=False)
content = request.json()

msg = ''

for index, article in enumerate(content['articles']):
    if article['title'] is not None:
        msg = msg + article['title'] +"\n"+ article['description'] + "\n" + "\n"

msg = msg.encode('utf-8')   

send_email.send_email(msg)

# print(msg)
print('Message Sent')

