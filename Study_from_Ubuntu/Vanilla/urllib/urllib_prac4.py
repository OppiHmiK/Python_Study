import urllib.request as req

if __name__ == "__main__":
    url = "https://www.naver.com/"
    request = req.Request(url)
    source = req.urlopen(request).read()

    print(source)

    with open('response.txt', 'w') as res:
        res.write(str(source))

