Re, Gr, Wh, Ye= '\033[1;31m', '\033[1;32m', '\033[1;37m', '\033[1;33m'
def dANDenModeF():
    e = {'a':' 0001','b':' 0010','c':' 0100','d':' 1000',
     'e':' 0002','f':' 0020','g':' 0200','h':' 2000',
     'i':' 0003','l':' 0030','m':' 0300','n':' 3000',
     'o':' 0004','p':' 0040','q':' 0400','r':' 4000',
     's':' 0005','t':' 0050','u':' 0500','v':' 5000',
     'z':' 0006','k':' 0666','w':' 0600','x':' 6000',
     'y':' 0060','j':' 6600'}
    d ={'0001':'a','0010':'b','0100':'c','1000':'d',
        '0002':'e','0020':'f','0200':'g','2000':'h',
        '0003':'i','0030':'l','0300':'m','3000':'n',
        '0004':'o','0040':'p','0400':'q','4000':'r',
        '0005':'s','0050':'t','0500':'u','5000':'v',
        '0006':'z','0666':'k','0600':'w','6000':'x',
        '0060':'y','6600':'j'}
    inp = input(f"\n{Wh} encode or decode: {Gr}")
    inp = inp.lower()
    print(f'\n{Gr} info: recommended to use [space? space] to divide words')
    msg = input(f"\n{Wh} target msg for {inp}: {Gr}")
    msg = msg.lower()
    if inp == 'encode':
        encodeMsg = ''
        for c in range(len(msg)):
            try:
                encodeMsg = encodeMsg + e[msg[c]]
            except:
                encodeMsg = encodeMsg + msg[c]
        print(f'{Wh} Encoded msg: {Gr}{encodeMsg}')
    elif inp == 'decode':
        msg = msg.split()
        decodeMsg = ''
        for c in range(len(msg)):
            try:
                decodeMsg = decodeMsg + d[msg[c]]
            except:
                decodeMsg = decodeMsg + '?'
        print(f' {Wh}Decoded msg: {Gr}{decodeMsg}')