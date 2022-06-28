import requests

site_url = 'https://digi4school.at/'

s = requests.Session()
s.get(site_url)
s.post(site_url, data={'email': 'dominik.lovetinsky@htlstp.at', 'password': ''})

for i in range(1, 312):
    url = "https://a.hpthek.at/ebook/693/" + str(i) + "/" + str(i) + ".svg"
    to = "D:\\EbookOutput\\page" + str(i) + ".html"

    with open(to, 'w') as svg:
        f = s.get(url).content
        svg.write(str(f))
