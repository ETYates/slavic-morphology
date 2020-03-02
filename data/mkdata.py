import json
import os

def main(): 
    f = open('rusm.json', 'r')
    data = json.load(f)
    src_train = open('src-train.txt', 'w')
    tgt_train = open('tgt-train.txt', 'w')
    src_val = open('src-val.txt', 'w')
    tgt_val = open('tgt-val.txt', 'w')

    for n in range(len(data)):
        print(data[n].lower())
        lpf = data[n].split()
        if len(lpf) == 3:
            a, b, c = data[n].split()
            if n % 10 == 0:
                src_val.write(a.lower() + ' ' + b + '\n')
                tgt_val.write(c + '\n')
            else:
                src_train.write(a.lower() + ' ' + b + '\n')
                tgt_train.write(c + '\n')

main()
