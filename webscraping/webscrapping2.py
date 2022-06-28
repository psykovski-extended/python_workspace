import requests

url = "https://digi4school.at/"
login_data = dict(email='dominik.lovetinsky@htlstp.at', password='')

session = requests.session()
r1 = session.post(url, data=login_data)

for i in range(1, 312):
    url2 = "https://a.hpthek.at/ebook/693/" + str(i) + "/" + str(i) + ".svg"
    to = "D:\\EbookOutput\\page" + str(i) + ".svg"

    r2 = requests.get(url2, allow_redirects=True)
    open(to, "w").write(r2.content)
