from bs4 import BeautifulSoup
import requests
import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print('start py')
user_name = os.getenv('GITHUB_ACTOR')
print(user_name)
# req = requests.get('https://github.com/'+user_name)
# soup = BeautifulSoup()