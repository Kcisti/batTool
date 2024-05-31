Re, Gr, Wh, Ye= '\033[1;31m', '\033[1;32m', '\033[1;37m', '\033[1;33m'
import requests, instaloader
from bs4 import BeautifulSoup

def main():
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