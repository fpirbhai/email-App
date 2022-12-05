import requests
import send_email

topic = 'Deloitte'

api_key = 'af08a8752fcd4bb0b473429f62029f1f'

url = f"https://newsapi.org/v2/everything?q={topic}&from=2022-11-05&sortBy=publishedAt&apiKey=af08a8752fcd4bb0b473429f62029f1f&language=en"


request = requests.get(url,verify=False)
content = request.json()

msg = ''

for index, article in enumerate(content['articles'][:20]):

    if article['title'] is not None:
        msg = msg + article['title'] +"\n"+ article['description'] + "\n" + article['url']+ 2*"\n"

msg = msg.encode('utf-8')   

msg = f'Subject: Today {topic} News\n'.encode('utf-8') + msg

send_email.send_email(msg)

# print(msg)
print('Message Sent')

