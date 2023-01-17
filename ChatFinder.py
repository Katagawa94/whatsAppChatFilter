import sys

keys = sys.argv[1:]
counter = 0

def checkMsg():
    for key in keys:
        if key in msg:
            return True
    return False

with open('chat.txt',encoding='utf-8') as chat:
    hits = open('ergebnis.txt','w',encoding='utf-8')
    msg=''
    for line in chat:
        if line[0].isnumeric():
            if msg and checkMsg():
                hits.write(f'{msg} \n')
                counter += 1
            msg=''
        msg += line
    
    if msg and checkMsg():
        hits.write(f'{msg} \n')

print(f'\n DONE - {counter} HITS')