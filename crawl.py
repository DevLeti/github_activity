from bs4 import BeautifulSoup
import requests
import os
import sys
import json

#https://chanhuiseok.github.io/posts/git-1/#2-github-action%EC%9C%BC%EB%A1%9C-%ED%81%AC%EB%A1%A4%EB%9F%AC-%EC%9E%90%EB%8F%99-%EC%8B%A4%ED%96%89-%EB%B0%8F-push-%ED%95%98%EA%B8%B0

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print('start py')
# user_name = os.getenv('GITHUB_ACTOR') #DevLeti
user_name = "DevLeti"
print(user_name)
req = requests.get('https://github.com/'+user_name)
html = req.content
soup = BeautifulSoup(html, 'html.parser')
datas = soup.select(
    '#js-contribution-activity > div:nth-child(3) > div'
)

latest_event = datas[0].find('span', class_ = 'float-left ws-normal text-left').text
latest_event = latest_event.replace('\n', '').replace('        ', ' ').replace('      ','')[1:]
print(latest_event)

input = {latest_event}
with open(os.path.join(BASE_DIR, 'event.json'), 'w+', encoding='utf-8') as json_file:
    json.dump(input, json_file, ensure_ascii = False, indent = '\t')

#print(datas[0])
#print(datas[0].find('span', class_ = 'float-left ws-normal text-left').text)
# type(datas[0]) == bs4.element.Tag
