import urllib.request as req

if __name__ == "__main__":
    url = "https://www.naver.com/"
    request = req.Request(url)
    source = req.urlopen(request).read()

    with open("repsponse_basic.html", "wb") as res_b:
        res_b.write(source)