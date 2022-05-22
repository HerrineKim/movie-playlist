import requests
from bs4 import BeautifulSoup

url_list = [
    'https://music.bugs.co.kr/musicpd/albumview/18060?wl_ref=list_mab_03_tr',
    'https://music.bugs.co.kr/musicpd/albumview/18174',
    'https://music.bugs.co.kr/musicpd/albumview/18293',
    'https://music.bugs.co.kr/musicpd/albumview/38123'
]

title_list = []
artist_list = []
cnt = 0

for x in range(len(url_list)):
    response = requests.get(url_list[x])

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('p.title')
        artists = soup.select('p.artist')

        for i in range(len(titles)):
            title = titles[i].text.strip().split('\n')[0]
            artist = artists[i].text.strip().split('\n')[0]

            if '[19금]' == title:
                title = titles[i].text.strip().split('\n')[1]

            cnt += 1
            if title in title_list and artist in artist_list:
                continue
            title_list.append(title)
            artist_list.append(artist)
    else:
        print(response.status_code)

print(title_list)
print(artist_list)
print(cnt)
