from src.files.mirrorMode import mirrorModeF
from src.files.dossNNMode import dossNNModeF
from src.files.encrypMode import encrypModeF

from src.files.intProTracker import intProModeF
from src.files.phoneTracker import numberModeF
from src.files.userOsint import userSSModeF
from src.files.instaData import instaSModeF
from src.files.urlMaskin import maskinModeF
from src.files.youtubeDl import downloModeF
from src.files.cryptoGraph import dANDenModeF

Re, Gr, Wh, Ye= '\033[1;31m', '\033[1;32m', '\033[1;37m', '\033[1;33m'


def is_option(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

    return wrapper

# FUNCTIONS FOR MENU
@is_option
def help():
    print(f'\n{Gr} HELP FOR BEGINNERS\n')
    for opt in options:
        print(f' {Wh}[{opt["num"]}]{Gr} {opt["help"]}')

@is_option
def IntProMode():
    intProModeF()

@is_option
def numberMode():
    numberModeF()

@is_option
def userSSMode():
    userSSModeF()

@is_option
def mirrorMode():
    mirrorModeF()

@is_option
def instaSMode():
    instaSModeF()

@is_option
def maskinMode():
    maskinModeF()

@is_option
def dossNNMode():
    dossNNModeF()

@is_option
def encrypMode():
    encrypModeF()

@is_option
def downloMode():
    downloModeF()

@is_option
def dANDenMode():
    dANDenModeF()


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
        'func': IntProMode
    },
    {
        'num': 13,
        'text': 'Your Internet Protocol',
        'help' : 'Show your IP',
        'func': mirrorMode

    },
    {
        'num': 14,
        'text': 'Username Social Finder',
        'help' : 'Username Finder',
        'func': userSSMode
    },
    {
        'num': 15,
        'text': 'Phone Numbers Tracker',
        'help' : 'Phone Numbers Tracker',
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
        'text': 'Doss Attack x200 Packs',
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
    {
        'num': 21,
        'text': 'Encode or Decode MSG',
        'help' : 'Encode or Decode Messages',
        'func': dANDenMode
    },
]