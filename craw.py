from bs4 import BeautifulSoup
import requests
import html
import shutil
import json

images = {}

images["data"] = []

for num_of_page in range(1,10):
    url = 'https://factsandchicks.com/page/%d'%(num_of_page)
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')   
    for img in soup.find('div', {"id": "content"}).findAll('img'):
        src = img.get('src')
        alt = img.get('alt').replace('\nsource','')
        if alt != 'Hey, this post may contain adult content, so we’ve hidden it from public view.\nLearn more.':
            images["data"].append({"url": src, "description": alt.encode('ascii', 'ignore').decode('UTF-8')})

with open('data.json', 'w', encoding='utf-8') as outfile:
    json.dump(images, outfile)
# for key,img in enumerate(images):
#     print(img[0])
    # r = requests.get(img[0], stream=True)
    # if r.status_code == 200:
    #     path = 'images/%d.jpg'%(key)
    #     with open(path, 'wb') as f:
    #         r.raw.decode_content = True
    #         shutil.copyfileobj(r.raw, f)   