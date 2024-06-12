#file10 not exist - is exitrrMODE
#file11 not exist - is helprrMODE
from src.files.file12 import main as intproMODEF
from src.files.file13 import main as mirrorMODEF
from src.files.file14 import main as userssMODEF
from src.files.file15 import main as numberMODEF
from src.files.file16 import main as instasMODEF
from src.files.file17 import main as maskinMODEF
from src.files.file18 import main as dossnnMODEF
from src.files.file19 import main as encrypMODEF
from src.files.file20 import main as downloMODEF
from src.files.file21 import main as dandenMODEF
from src.files.file22 import main as wificrMODEF

import os
Re, Gr, Wh, Ye= '\033[1;31m', '\033[1;32m', '\033[1;37m', '\033[1;33m'

def is_option(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

    return wrapper

# FUNCTIONS FOR MENU
@is_option
def helprrMODE():
    print(f'\n{Gr} HELP FOR BEGINNERS\n')
    for opt in options:
        print(f' {Wh}[{opt["num"]}]{Gr} {opt["help"]}')

@is_option#12
def intproMODE():intproMODEF()

@is_option#13
def mirrorMODE():mirrorMODEF()

@is_option#14
def userssMODE():userssMODEF()

@is_option#15
def numberMODE():numberMODEF()

@is_option#16
def instasMODE():instasMODEF()

@is_option#17
def maskinMODE():maskinMODEF()

@is_option#18
def dossnnMODE():dossnnMODEF()

@is_option#19
def encrypMODE():encrypMODEF()

@is_option#20
def downloMODE():downloMODEF()

@is_option#21
def dandenMODE():dandenMODEF()

@is_option#22
def wificrMODE():wificrMODEF()


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
        'func': helprrMODE
    },
    {
        'num': 12,
        'text': 'Internet Protocol Tracker',
        'help' : 'IP Tracker',
        'func': intproMODE
    },
    {
        'num': 13,
        'text': 'Your Internet Protocol',
        'help' : 'Show your IP',
        'func': mirrorMODE

    },
    {
        'num': 14,
        'text': 'Username Social Finder',
        'help' : 'Username Finder',
        'func': userssMODE
    },
    {
        'num': 15,
        'text': 'Phone Numbers Tracker',
        'help' : 'Phone Numbers Tracker',
        'func': numberMODE
    },
    {
        'num': 16,
        'text': 'Instagram Info & Scraping',
        'help' : 'Download IG Data',
        'func': instasMODE
    },
    {
        'num': 17,
        'text': 'Masking Phishing URL',
        'help' : 'Mask URL',
        'func': maskinMODE
    },
    {
        'num': 18,
        'text': 'Doss Attack x200 Packs',
        'help' : 'Doss Attack',
        'func': dossnnMODE
    },
    {
        'num': 19,
        'text': 'Encrypted Chat Room',
        'help' : 'Encrypted Chat Room',
        'func': encrypMODE
    },
    {
        'num': 20,
        'text': 'Download Youtube Video',
        'help' : 'Download Youtube Video',
        'func': downloMODE
    },
    {
        'num': 21,
        'text': 'Encode or Decode MSG',
        'help' : 'Encode or Decode Messages',
        'func': dandenMODE
    },
    {
        'num': 22,
        'text': 'Wifi Bruteforce passkey',
        'help' : 'Wifi Bruteforce attack',
        'func': wificrMODE
    },
]