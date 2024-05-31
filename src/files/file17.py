Re, Gr, Wh, Ye= '\033[1;31m', '\033[1;32m', '\033[1;37m', '\033[1;33m'
from requests.utils import quote as urlEncode
from json import loads
from requests import get
def main():
    class Doppelgang:
        def __init__(self,url,maskingDomain="google.com",keyword="login"):
            self.url = url
            self.maskingDomain = maskingDomain
            self.keyword = keyword
            self.shorturl = None
        def shorten(self):
            encodedUrl = urlEncode(self.url)
            res = get(f"https://is.gd/create.php?format=json&url={encodedUrl}").text
            json = loads(res)
            try:
                self.shorturl = json["shorturl"]
            except:
                self.shorturl = self.url
            return self.shorturl
        def mask(self):
            maskedURL = self.shorturl.replace("https://",f"https://{self.maskingDomain}-{self.keyword}@")
            return maskedURL
    url = input(f"\n{Wh} Enter the url to be masked: {Gr}")
    mask = input(f"{Wh} Enter a masking domain: {Gr}")
    keyword = input(f"{Wh} Type a kewword [no whiteSP]: {Gr}")
    target = Doppelgang(url,mask,keyword)
    target.shorten()
    print(f"{Wh} Output url: {Gr}",target.mask())