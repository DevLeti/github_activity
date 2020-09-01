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
    '#js-contribution-activity > div.contribution-activity-listing.float-left.col-12.col-lg-10 > div'
)

print(datas[0])
# type(datas[0]) == bs4.element.Tag