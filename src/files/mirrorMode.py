Re, Gr, Wh, Ye= '\033[1;31m', '\033[1;32m', '\033[1;37m', '\033[1;33m'
import requests

def mirrorModeF():
    respone = requests.get('https://api.ipify.org/')
    Show_IP = respone.text
    print(f"\n{Gr} SHOW INFORMATION YOUR IP")
    print(f"\n{Wh}{Gr} + {Wh} Your IP Adrress : {Gr}{Show_IP}")