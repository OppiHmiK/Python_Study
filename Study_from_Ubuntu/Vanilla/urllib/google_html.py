import urllib.request as req

url = "http://www.google.co.kr/"
g_html = req.urlopen(url).read()

with open("google_html.txt", "wb") as data:

    data.write(g_html)
