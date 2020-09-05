from bs4 import BeautifulSoup
import requests
import os
import sys
import json

#https://chanhuiseok.github.io/posts/git-1/#2-github-action%EC%9C%BC%EB%A1%9C-%ED%81%AC%EB%A1%A4%EB%9F%AC-%EC%9E%90%EB%8F%99-%EC%8B%A4%ED%96%89-%EB%B0%8F-push-%ED%95%98%EA%B8%B0

if (os.getenv('GITHUB_REPOSITORY') == 'DevLeti/github_activity'):
    exit(1)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print('start py')
#user_name = os.getenv('GITHUB_ACTOR') #DevLeti
user_name = "DevLeti"
print(user_name)
req = requests.get('https://github.com/'+user_name)
html = req.content
soup = BeautifulSoup(html, 'html.parser')
datas = soup.select(
    '#js-contribution-activity > div:nth-child(3) > div'
)

# date
latest_date = datas[0].find('h3', class_ = 'profile-timeline-month-heading bg-white d-inline-block h6 pr-2 py-1').text.replace('\n','').replace('      ','')
print(latest_date)

# event
latest_event = datas[0].find('span', class_ = 'float-left ws-normal text-left').text
latest_event = latest_event.replace('\n', '').replace('        ', ' ').replace('      ','')[1:]
print(latest_event)
repository = latest_event[latest_event.find('in')+2:latest_event.find('repository')]

# if(int(repository) != 1):
    

latest_json = {'date' : latest_date, 'event' : latest_event}
print(latest_json)
print("crawl completed.")

with open(os.path.join(BASE_DIR, 'activity.json'), 'w+', encoding='utf-8') as json_file:
    json.dump(latest_json, json_file, ensure_ascii = False, indent = '\t')

md_text = requests.get('https://raw.githubusercontent.com/{0}/{1}/master/README.md'.format(user_name, user_name)).text
f = open('main_README.md','w', encoding="UTF8")
f.writelines(md_text)
f.close()

r = open('main_README.md', 'r', encoding ='UTF8')
r_arr = r.readlines()
r.close()

start_failed = False
end_failed = False
for i in range(0, len(r_arr)):
    start = r_arr.index('  <!--START:activity-->\n')
    end = r_arr.index('  <!--END:activity-->\n')
    if(start != -1): #found start point
        if(end != -1): #found end point
            for i in range (start +1, end):
                del r_arr[i]
        else:
            print("end point not found!")
            start_failed = True
            break
    else:    
        print("start point not found!")
        end_failed = True
        break

# Error 발생
if(start_failed):
    raise ValueError('Start Point not found')
elif(end_failed):
    raise ValueError('End Point not found')

r_arr[start] = r_arr[start] + '🌱 Date : {0}, Event : {1}\n'.format(latest_json['date'], latest_json['event'])

r = open('main_README.md', 'w', encoding = 'UTF8')
for line in r_arr:
    r.write(line)
r.close()
print("write completed.")

return 1

# TODO
# ajax 크롤링.
# fakeuseragent 사용해서 header달아서 request.
