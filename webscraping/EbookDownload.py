import urllib.request


for i in range(1, 312):
    urllib.request.urlretrieve("https://a.hpthek.at/ebook/693/" + str(i) + "/" + str(i) + ".svg", "D:\\EbookOutput\\page" + str(i) + ".svg")
    """resource = urllib.urlopen("https://a.hpthek.at/ebook/693/" + str(i) + "/" + str(i) + ".svg")
    output = open("D:\\EbookOutput\\page" + str(i) + ".svg", "w")
    output.write(resource.read())
    output.close()"""

