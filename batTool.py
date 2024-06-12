import time,os,pygame
from batDefs import options

Re, Gr, Wh, Ye= '\033[1;31m', '\033[1;32m', '\033[1;37m', '\033[1;33m'

def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux
    else:
        _ = os.system('clear')

def execute_option(opt):
    try:       
        if not is_in_options(opt):
            raise ValueError(f'{Re}! Option not found !')
        for option in options:
            if option['num'] == opt:
                if 'func' in option:
                    clear(),option['func']()
                else:
                    print(f'{Re}! No function detected !')

        input(f'\n {Gr}+ Press enter to continue')
        main()
    except ValueError as e:
        print(e), time.sleep(2)
        execute_option(opt)
    except KeyboardInterrupt:
        print(f'\n {Re}! Exit !')
        time.sleep(2), exit()

def is_in_options(num):
    for opt in options:
        if opt['num'] == num:
            return True
    return False

def option():
    print(f"\n {Gr}BatTool - by Kcisti\n"),time.sleep(2)
    for o in range(len(options)):
        print(f" {Wh}{options[o]['num']} {Gr}{options[o]['text']}")

def sound():
    file_audio = 'sound/ad.mp3'
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_audio)
    pygame.mixer.music.play()

def main():
    try:
        clear(),option()
        opt = int(input(f"\n {Gr}Select Option : {Wh}"))
        execute_option(opt)
    except ValueError:
        print(f'\n{Re} !Please input number!')
        time.sleep(2), main()

if __name__ == '__main__':
    try:
        try:
            sound(), main()
        except:
            main()
    except KeyboardInterrupt:
        print(f'\n {Re}!Exit!')
        time.sleep(2), exit()










